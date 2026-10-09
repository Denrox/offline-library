# Find the right COM to setup Winlink

*Tags: packet, linux · score 3*

## Question

I managed to successfully install Winlink on my Ubuntu operating system but it is not completely functional yet. I don't know which COM my computer is set up to use, and there are a lot of them available.

That's my question though, how to quickly find the right COM without going through each and every one individually. Thank you very much, and I look forward to hearing from you.

## Accepted answer (score 1, by Duston)

If you're running under WINE, you can make the port whatever you want. You need to know the Linux device name (like /dev/ttys0 or /dev/ttyUSB or whatever) the TNC is plugged into on the computer. Then all you do is set up a symlink in ~/.wine/dosdevices that "connects" the two. If you look in that directory, you can see the default devices already set up. If you don't know how to set up a symlink, look for help on the ln command.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/14535/find-the-right-com-to-setup-winlink, by BJsgoodlife, Duston. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
