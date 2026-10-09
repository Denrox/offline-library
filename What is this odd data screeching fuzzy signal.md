# What is this odd data/screeching/fuzzy signal?

*Tags: receiver, rfi, signal-identification · score 3*

## Question

I was listening to a commercial FM radio station on 100.9 MHz, and this intermittent weird sound kept coming through it.

**Here is a recording of it**. The audio starts at about 15 seconds.

It sounded like some data signal or screeching and beeping interrupted my listening experience, it did so periodically. It sounds like if you accidentally call a fax machine and you get that buzzing and screeching sound.

It was powerful enough to take out the station; I don't know if it was coming from the station itself, or if it was interference from another source. I had problems before with Internet signals getting through.

No other stations that I get have this problem.

I have a single-wire loop antenna that I have to twist to get clearer reception, and a Kenwood digital tuner.

Another observation is that the day was cloudy. I had no problem with reception other than static.

Is there anything I can do to prevent this?

## Accepted answer (score 2, by Rowan Hawkins)

Welcome the land of QRM also known as man made noise.

I realize this came from the headphone jack, so it recorded as stereo. its really a mono signal, both channels have the same wave form. because you used a lossy compression it would be may make it harder to try and decode it. (not that I'm that good mind you)

It kind of sounds like a problem we had here with a paging company. They were putting out 50Kw and as the transmitter unkeyed, the transmitter frequency would drift down from 465mhz down to into the VHF ham band. You would only hear it if you were within about a mile of the transmission site, The repeater didn't hear it because it used a PL for interference reduction.

Here is how you go about tracking it down... First confirm you can hear it on more than one receiver and in more that one place. This means that the thing you hear is real (for other people's verification). Then you can either go the Foxhunt route yourself, or contact the Radio Station on 100.9 and hopefully they can convince someone to do so. If you can prove that the interference is over a chunk of their listening audience, and affects say, their advertising then getting them to act on it is easier.

If you look at the audio as a wave form, you can see that the noise starts earlier than 15 seconds and runs until about 23, starts just before 30, and runs to 38. so its 9-10 seconds with a 5-7 second gap between transmissions. The encoding is likely some sort of audio FSK.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/11645/what-is-this-odd-data-screeching-fuzzy-signal, by Ben Madison KO4UXC, Rowan Hawkins. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
