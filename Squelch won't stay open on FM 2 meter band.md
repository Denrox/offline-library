# Squelch won't stay open on FM 2 meter band

*Tags: antenna, baofeng, 2m-band, squelch · score 3*

## Question

I am currently using a Baofeng BF-F9V2+ radio. I have found that when listening, my squelch won't stay open, despite getting a good clean signal. I am using a homemade vertical dipole antenna for 2-meter band. Compared to the rubber duck, it gets excellent reception signal, except for this unreliable squelch problem.

I have also found that when I turn the squelch off, I get a continuous signal, so I do not believe that it is a problem with my antenna.

Are there variables that could cause something like this other than an issue with the radio?

Thanks, Addison

## Answer (score 3, by hobbs - KC2G)

I can think of two possible issues, but both of them are "something to do with the radio".

The first is that something in the signal you're listening to is tweaking the [Baofeng squelch tail eliminator](How%20does%20the%20baofeng%20radio%20eliminate%20squelch%20tail.md). The answer to that question describes menu options that can stop a radio from *transmitting* the STE tones, but my understanding is that there is no way at all to stop the receiver from muting when it *hears* the tones. If the signal you're listening to contains content at those frequencies, your radio might decide to drop squelch intermittently.

The second possibility is the well-known susceptibility of Baofeng front-ends to overload, prompted by your mention of an external antenna. Working against this is the fact that you say everything is fine with squelch disabled, but it's still possible that some other strong signal is interfering with the squelch tracking, without causing audible distortion. If your reception gets *better* with the stock rubber-duck antenna fitted, then overload is a likely culprit.

## Answer (score 3, by melinydre)

My personal experience: Baofeng UV-5R, works fine with stock rubber ducky antenna. Made a simple quarter-wave dipole antenna, connected to my radio with about 10 feet of cable. It transmitted much better than stock antenna. However, there was a problem with reception. The radio would receive the first transmission, and but would not re-open the squelch until I pressed the [EXIT] key. If I didn't press the [EXIT] key the radio remained silent, no matter the squelch setting, whether 0 through 9. When I pressed the [EXIT] key I immediately began receiving the contact's transmission.

I concluded that the radio was too near the antenna. I connected a 25-foot cable between the radio and the quarter-wave dipole antenna, and transmission and reception worked normally.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16068/squelch-won-t-stay-open-on-fm-2-meter-band, by Addison Ballif, hobbs - KC2G, melinydre. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
