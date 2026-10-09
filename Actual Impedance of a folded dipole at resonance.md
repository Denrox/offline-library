# Actual Impedance of a folded dipole at resonance

*Tags: antenna-theory, antenna-system, balun · score 4*

## Question

I am using a Folded Dipole which I bought when I first got my General License. It was advertised as an all band antenna. My results with it were less than the claims made by the makers to say the least. At a height of about 40 feet above local ground level and a manufactured length of 90 feet I could not make many contacts on any band. I began to believe that what the ad meant when it described the antenna as "Quiet" was actually deaf.

I was given a Yaesu FT-1000 by a member of my radio club after a field day during which I logged for him whenever he was operating. I read the manual even though that is supposed to be some sort of violation of some sacred rule and found out that it had an internal antenna tuner. The manual and other sources said the internal tuner would bring any SWR up to 3:1 down to 1.5:1 or better.

Since much of what I read about the Terminated Folded Dipole called them by such uncomplimentary names as "Bird foot warmers" and my experience with mine had been so unrewarding I thought I would give the tuner in the FT-1000 a try at making the beastie perform more effectively. I did some reading and took it as gospel that the impedance of a folded dipole without the 600 Ohm resister and the 12:1 balun would be 300 Ohms at resonance. I then ran the usual formula for Resonance and got ~5.464 MHz for my 90 foot long folded dipole. I knew that wouldn't be exactly right because the antenna is not strung at quite >45 feet but I thought it might be close enough to try the FT-1000 internal tuner on. The tuner would not match the antenna anywhere I tried it. I concluded that the SWR had to be greater than 3:1 and thus beyond the tuners limit. I figured I could get the antenna to an actual 50 Ohm load with 300 Ohm window line down to a 6:1 balun. Suddenly the tuner likes the antenna from 160 Meters to 6 meters because the indicators said the the tuner was getting a match.

As it is know there is ~25 feet of Times Microwave Systems LMR-400, 1:6 balun, ~30 feet 300 Ohm window line, feed point of 90 foot long folded dipole.

Here is the heart of my question. Does it seem at all likely to those of you with more theoretical acumen that the tuner is getting a match through that wide a range of Wavelengths?

If I take my club's AEA HF Analyzer and hook it up to the 6:1 balun will it show me what the tuner is actually seeing? Would their be any benefit to using the more recently designed RigExpert AA-200 instead?

What is the proper technique to measure the impedance of an antenna with a balanced feed line using an analyzer with in imbalanced input?

I would be grateful for any help that anyone cares to offer.

-- Tom Horne W3TDH

## Answer (score 5, by Phil Frost - W8II)

Since you say "Terminated Folded Dipole" and mention a resistor, it sounds like you are talking about a T2FD. This is a significantly different antenna from a vanilla folded dipole, which does not have a resistor.

A T2FD can indeed provide a flat-ish impedance over a wide band, however this comes at the expense of efficiency. A significant fraction of the power is absorbed in the resistor.

The feedpoint impedance of a T2FD is usually around 300 ohms, so a 6:1 balun is indeed a good choice if you intend to operate this antenna with a radio designed for a 50 ohm load, such as the FT-1000. An antenna analyzer would indeed be useful to get a more precise answer.

Unfortunately, none of this will address the inefficiency inherent to the design of the antenna. In a receive application the inefficiency may not be too much of a problem since both signal and noise are attenuated. But in a transmitting application, an inefficient antenna wastes transmitter power.

Height above ground is also a factor. If you want long-distance communication, a dipole of any sort should be at least a half-wavelength above ground. Any lower than this and most of the radiation tends to go straight up rather than towards the horizon, and you lose significant power in the resistance of the soil. At 40 feet, 20 meters should work, but as frequency decreases you'll find your antenna limited to local contacts.

I would suggest building a simple 20 meter wire dipole at least as a point of reference. It's cheap and performs very well at 40 feet above ground. It only works for one band, but it will at least give you an idea of what's possible with a good antenna before you explore other designs.

## Answer (score 3, by Richard Fry)

Below for further discussion is a NEC4.2 study for the folded dipole antenna description provided in earlier posts in this thread.

Of course its input SWR and radiation patterns vary with frequency. The patterns at the two ends of the HF amateur bands and the input SWR across that spectrum are shown in the study.

The NEC wire model showed no segment or geometry errors at runtime.

. *Added 16 Nov:* To partially address the comments of W3TDH, below are the NEC4.2-calulated R and j values at the feedpoint terminals of that folded dipole, across the 3-30 MHz band.

The SWR match to R300 j0 ohms is best at/near 5 MHz, where it has a value of about 1.08:1.

I'll limit this edit to add this graphic, only, as I have not kept up to date on the test equipment and procedures commonly used by amateur radio operators to measure impedance these days.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15628/actual-impedance-of-a-folded-dipole-at-resonance, by Tom Horne W3TDH, Phil Frost - W8II, Richard Fry. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
