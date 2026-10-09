# receiving AM radio station on UHF frequency

*Tags: uhf · score 9*

## Question

I'm studying for my Technician license, and listening in to HF, VHF and UHF bands just to get a feel for how to work with frequencies, squelch, antennas, etc. Had something happen today that I couldn't explain. I was doing a scan through the 70cm band, running from 400MHz to 480MHz, and at 450.040 I picked up a local AM radio station. I checked the radio station website and they only broadcast on 1520 KHz. How did I receive that signal on such a different frequency? I wasn't even working with a very powerful antenna, just a Baofeng UV5R. My first thought was that perhaps the local signal was just so powerful it overcame my radio reception. But if that's the case, why did it happen just on that one frequency? I was scanning other frequencies through the day and didn't have it happen on any other frequency. I also checked to see if we had any nearby repeaters at that frequency but we don't; nearest frequency for a regional repeater is 444.9750. Thanks.

## Answer (score 4, by Edwin van Mierlo)

at 450.040 I picked up a local AM radio station

I am sure you picked up a transmission

just a Baofeng UV5R

But not with that radio, or at least not AM

You either:

- Picked up a signal which is indeed AM, but then it would not be very distorted as the radio you are using only has FM (de)modulation.

or:

- Picked up something else.

If the audio received was not distorted (so then it must be FM), and clearly the same 'program' as the said AM station on 1520 KHz. Then it is very likely this is a "studio to transmitter link/feed" that you picked up. (as detailed in the comments already)

**But to give you the official answer:**

You are **not** picking up an **AM** transmission originally on **1520 KHz**, on **450.040 MHz** with an **Baofeng UV5R** radio. *That would be quite impossible*

:-)

## Answer (score 2, by Ricky)

I was trying to research some info and I came across your thread.

My guess is they took the audio output from the 1520 kHz tuner and fed it in the input of a 450.040 MHz transmitter. That's why it can be heard in the UHF region. In this way, FM or AM or frequency doesn't matter, because its only an audio feed from an 1520 kHz tuner. You could have listen to a 1520 kHz tuner and a 450.040 MHz tuner at the same time. There should be a delay between the two tuners, I would guess.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6538/receiving-am-radio-station-on-uhf-frequency, by K. Kerby, Edwin van Mierlo, Ricky. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
