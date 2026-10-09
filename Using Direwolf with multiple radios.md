# Using Direwolf with multiple radios?

*Tags: packet, direwolf, ax.25 · score 7*

## Question

I'd like to play around with ax.25 connections. It seems that if I have more than one radio (operating on different frequencies) that I would want to have multiple ax.25 interfaces. Direwolf creates a /tmp/kisstnc symlink to the KISS pty device, and this path is hardcoded. This means you can only run a single instance of Direwolf providing a KISS pty interface...and since kissattach seems to only work with character devices, this would seem to limit a system to a single ax.25 interface when using direwolf.

If I want to run multiple direwolf-controlled ax.25 interfaces, what are my options? Am I thinking about this the wrong way? Is there a way to attach an ax.25 interface to Direwolf's KISS network port rather than using the pty device?

## Accepted answer (score 8, by larsks)

I've put together something that is conceptually similar to @user3486184's comment, but without actually using chroot. I'm taking advantage of SystemD to manage both direwolf and the subsequent kissattach command necessary to activate an ax.25 interface.

I created the following Systemd template unit and installed it into /etc/systemd/system/direwolf@.service.

```
[Unit]
Description=Direwolf %I soundcard modem

[Service]
Type=simple

PrivateTmp=true
ExecStart=/usr/bin/direwolf -t 0 -p -c /etc/direwolf/%i.conf -q h -q d

# Relocate /tmp/kisstnc symlink to /run/direwolf/<instance name>.
ExecStartPost=/bin/timeout 10 /bin/sh -c 'while ! test -c /tmp/kisstnc; do sleep 1; done; cp -a /tmp/kisstnc /run/direwolf/%i'

# Clean up symlink on exit.
ExecStopPost=/bin/rm -f /run/direwolf/%i

[Install]
WantedBy=multi-user.target

```

A "template unit" allows you to start multiple distinct instances of a service using the same unit file. To start a template unit, you run systemctl unitname@instancename, and the value of instancename is available to you in the unit as %i. So with the example above, I could run:

```
systemctl start direwolf@uhf

```

Or:

```
systemctl start direwolf@vhf

```

Etc. This will start up Direwolf pointing at a configuration named after the instance; in other words, given the latter example, this would run:

```
/usr/bin/direwolf -t 0 -p -c /etc/direwolf/vhf.conf -q h -q d

```

The unit makes use of the PrivateTmp directive, which when set means that each service gets its own /tmp directory that is not shared with anything else. This allows each Direwolf instance to create it's own /tmp/kisstnc symlink.

An ExecStartPost runs after Direwolf has started. It waits for the /tmp/kisstnc link to show up, and then it copies that into /run/direwolf/<instancename>. If I run both of the above systemctl start ... commands, I would end up with /run/direwolf/uhf and /run/direwolf/vhf.

I've created a companion kisstnc@.service unit that looks like this:

```
[Unit]
Requires=direwolf@%i.service
After=direwolf@%i.service

[Service]
Type=simple
ExecStart=/usr/sbin/kissattach /run/direwolf/%i %i

[Install]
WantedBy=multi-user.target

```

With this in place, I can simply run systemctl start kisstnc@uhf and then:

- Systemd will start the direwolf@uhf service, because the kisstnc@uhf service Requires it to run first.
- The direwolf@uhf unit creates the /run/direwolf/uhf symlink
- The kisstnc@uhf unit runs the appropriate kissattach command

For this to work, your /etc/ax25/axports file must have port names that match the instance names you're using in the above commands. For example, something like:

```
uhf     TEST-0      0   128 2   Direwolf@radio0
vhf     TEST-1      0   128 2   Direwolf@radio1

```

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/11785/using-direwolf-with-multiple-radios, by larsks. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
