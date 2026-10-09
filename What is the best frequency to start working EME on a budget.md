# What is the best frequency to start working EME on a budget?

*Tags: antenna, frequency, eme · score 5*

## Question

Well, the title says it all: I want to start making EME contacts with the lowest possible budget, and I doubt between 2m, 70cm and 23cm. Since I cannot afford those expensive power amplifiers for these frequencies, I decided to go for a big yagi array instead (increase the gain of the antenna in order to get an equivalent EIRP compared to the PA). I have a lot of experience in antennae design and simulation software, so this won't be an issue.

These are the options I have:

**2m:** I have a 50W TX, and could afford a cheap 100W VHF amplifier such as this one. For the antennae, I would build an array of four 6-element yagis. Each yagi should have a gain of around 9,7dBi, so the whole array should provide around 15,5dBi.

**70cm:** My rig is able to provide 35W at this frequency. However, I did not find any affordable amplifier for this frequency. For the antenna, I could use some four yagi array, that would provide an overall gain of around 16dBi.

**23cm:** Due to the smaller wavelength, I could try some 6 or even 9 yagi array. They would be around 12 element arrays and provide a global gain of 18,5dBi. Nevertheless, my rig (ICOM IC-7100) does not work at this frequency, so I would need some kind of upconverter. I did not find any cheap solution that works at the desired power outputs (around 50/100W).

This analysis suggests me that I should go for the 2m option. Moreover, path loss is smaller at 2m than at 70cm or 23cm. However, all of the beginner/small EME station work on either 70cm or 23cm. Moreover, I fear choosing a frequency that is not being used too much, and making few contacts because of this.

Any advice or recommendation will be appreciated.

BTW: for working EME, is there any noticeable difference between building an array of 2x2 or of 4x1 yagi antennae?

73 de EA4HFV!

## Accepted answer (score 8, by Marcus Müller)

You're generally right, the free space path loss formula incorporates wavelength quadratically, so it would seem wise use the lowest available frequency.

Since you're bouncing off an object, you get a loss that is quadratically proportional to both frequency, and distance, on each direction, where the reflected power can only be as much as reached the object, so overall, you get a fourth power (radar equation).

However, what it does forgo to account for is the fact that if you keep the dimensions of your antenna fixed, the gain of said antenna grows quadratically.

So, overall, the loss on your earth-moon-earth path, including your antenna, is proportional to the fourth power of distance, and quadratic to the frequency, if you say "the best antenna I can have on any frequency can never be larger than this and that", and that is pretty realistic.

That is, given you can still build a high-gain antenna under these constraints. This becomes impossible as soon as antenna dimensions become significantly smaller than wavelength.

Sooooo: you can guy a used / thrown out 1 m satellite dish, and work 0.7 m on it, giving you some hm, say, 10 to 12 dB of gain. Can't do that with 2m, dish is simply too small, can't really make much use of it, because you can't even realistically build a feed.

The very nice thing about dishes is that they usually don't exhibit much of a gain in directions you don't want, which is nearly more important than having gain in the direction you're interested in, since you'd be working in bands where other people have fun, too. What counts at the receiver is not signal power, but signal power in relation to noise plus interference power.

Then, go for a low-rate digital mode. FT8, JT65B.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17152/what-is-the-best-frequency-to-start-working-eme-on-a-budget, by user3141592, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
