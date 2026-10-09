# How do I notify and publish information on experimental modes?

*Tags: united-states, legal, modes, fcc · score 9*

## Question

I'm considering tinkering with a new mode. Of course I'll stick to experimental channels and low power for now, but as people notice my transmissions they won't immediately understand what is being transmitted.

How do I disseminate information that shows others how to receive and read my transmissions so as to avoid the appearance of encrypted or secret transmissions?

Do I have to disseminate that information before I start my testing, or can I do the testing, finalize the design, then publish? What I'm worried about here is that as the mode evolves and changes, keeping already published information up to date is time consuming, and I'd rather publish a little overview, do the work until it's complete, then publish the final details.

## Accepted answer (score 9, by oh7lzb)

Back, before the Internet, the documents were published in magazines, conference papers and such – well after the protocols were designed and initial tests were done.

In some cases CWID (transmitting callsign using CW every now and then) has been used to make sure the transmissions are well identified even if the actual data is a bit hard to decode.

Nowadays, I think, people usually just experiment quite freely and publish when they have something ready.

If you're really worried, you can always do testing transmissions with a dummy load, keeping the radiated power so low that it cannot be considered a licensed transmission at all. After all, you can generally transmit on any frequency, any power, as long as you don't radiate that energy. If you're tinkering with a new mode, it might actually be easiest to do it using a **simulated predictably noisy multipath software environment** without initially involving real radios at all!

Publication method ideas:

- **Set up a blog or wiki site**, let people know roughly which frequencies you're using, your callsign, and some general information about the mode.
- **Open Source** is the hip thing to do nowadays. Consider pushing your development code on Github or some other similar code repository - that's what I do myself. Your current code serves as pretty definite documentation as it is. As an added bonus you get an off-site backup of your code, and it might even attract other developers to help out.

## Answer (score 4, by Jmons)

I've been doing some experimentation as well and met the same issue. The way I've been dealing with it is to use a CW tag before and after the mode (as well as sometimes alongside my data mode). In it I put my callsign, and a tiny url (as its morse)

e.g. if my experiment data was at google.com, i nip to tinyurl and get a tinyurl: http://tinyurl.com/2tx, so I would transmit:

```
[CALLSIGN]    EXPERIMENT SEE - HTTP TINYURL COM 2TX    [CALLSIGN]

```

and hopefully people understand that without the punctiaton. The page itself is generally a blog page containing information on what I'm doing - not necessarily anywhere you can download a file to decode or instructions, but importantly I put a contact form or a way of getting in touch if I'm causing interference.

I currently pre-code the audio files that I transmit, and can overlay that morse alongside the data blob so it goes out like a margin notes.

The rules (in the UK) say you can't transmit secret codes, and the essence of my work not being public isn't that I'm being secret, just that I'm not ready to publish the source (thats arguably an interpretation). In practice it wouldn't take long for someone to analyse and decode the message as mine are all PSK based of underlying data.

Software testing with generated noise etc is good, but doesn't always let you test reality. I probably do 99% of my tests with just audio connections between overplayed with static etc, which lets me tinker without having to make real radio connections between people.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/996/how-do-i-notify-and-publish-information-on-experimental-modes, by Adam Davis, oh7lzb, Jmons. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
