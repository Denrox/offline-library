# How can I construct a practical loop antenna for 2m band?

*Tags: antenna, fox-hunt, direction-finding · score 7*

## Question

How can I construct a practical loop antenna for 2m band to use in a fox hunt? Is it even possible to construct a hand-held antenna for the 2m and 70 cm bands? I tried to calculate the dimensions using a few online tools and formula, and the dimensions seemed impractical to hold and walk around.

Can this antenna be miniaturized in any way? I have a Yamaha receiver that can receive AM band (few thousand kHz) and it is really small - less than 15cm across.

## Answer (score 5, by Kuerno)

Here is my dumbed-down experience.

If you are looking at T-hunts. I have always made sniffer loops about 1/10th or less then actual wavelength. Many times we would add a trimmer-cap across the antenna feed point but most the time would not. Even before I was a serious ham I did this quite successfully on the CB band for "Skunk Hunts" where we would all put a few bucks in the winner's pot.

What I did find is the "null" on the gain was much more precise then the strong side. I would use the back mounted vertical on my vehicle and do a "doughnut" in a vacant parking lot to take a heading. I would either mentally (if I knew the area well) or on paper (pre-internet) maps from the front of pone books, draw a line for the heading. Then I would move to the side a couple blocks and quickly do it again, sometimes a few times.

Once I could triangulate the approximate area I s could move in and with an antenna switch I could switch between my back mounted vertical and the small loop maybe 9 or 10 inches in diameter mounted on a 2 or 3 foot wooden stick or "wand". The 'Null' (which IIRC was the feed point forward) was sharp as a tack and working with the RF-Gain on the receive radio I could confidently move in for the kill even when the transmitter was "hidden".

Now AM broadcast? That will be a different monster. The middle of the band will be 300 meters wavelength and a tenth would still be nearly 10 feet in diameter. Not something you will be able to easily mount on a piece of PVC pipe and hang out the sun-roof of your car!

You could do as others have suggested and look and the true magnetic loops and maybe "Multi-turn-Mag-loops". Also most cheap AM receivers with loop sticks are also VERY directional. Sometimes it can be tricky picking which is "front" and "back" but they are directional. There are also various after market "ferrite coil" antennas for the AM band usually marketed to improve reception but I am sure you could use it to 'DF' AM broadcast band transmitters as well. You might ask some real old-timers but I think I heard the idea for C.Crane ferrite coil may have come from coils used in WW2 by the military aircraft to home in on a target city. That may be ham radio urban-myth but I have heard similar claims since I first became a ham in the mid 80s.

## Answer (score 5, by Phil Frost - W8II)

There are two kinds of "loop antennas". There are resonant loops, which are loops where the length of the loop is long enough to be resonant. These can be considered folded dipoles, which have been folded into a loop.

A quite distinct antenna is the small loop. These antennas have a perimeter that is electrically small, meaning less than one-tenth of the wavelength.

The two are quite different. The small loop has nulls in two directions perpendicular to the plane of the loop. The resonant loop has nulls in two directions on the plane of the loop. The small loop has a highly inductive impedance. The resonant loop has a purely resistive impedance.

Anyhow, small loops are frequently used for direction finding at HF because they are small and easy to construct. They are quite inefficient antennas, but it's easy to make low-noise amplifiers at HF which can make up for the low efficiency and poor impedance match.

The *electrically* small loop can be made *physically* smaller in three ways:

1. Make more turns of wire. A small loop with two turns encircling area $A$ is equivalent to a larger loop with one turn encircling area $2A$.
2. Increase the permittivity of the space encircled by the loop. For example, by winding the loop around a ferrite material.
3. Just make it smaller. Decreasing the area encircled by the loop reduces the antenna's efficiency and sensitivity, but provided the signal is still above the noise floor, this isn't a problem. The small loop wasn't very efficient or sensitive to begin, anyway.

An example of an antenna that does both of these things, and most likely the type of antenna employed by your AM receiver, is a loopstick antenna. These consist of very many turns around a high-permittivity ferrite rod. In doing so, they make the antenna appear electrically much bigger than it is physically.

However, I doubt you will meet success with either of these techniques at 2m. Adding more turns increases the DC resistance, and thus loss of an already not very sensitive antenna. Low noise amplifiers to overcome this are easy at low frequencies, but not at 2m. Also, ferrite materials are lossier with increasing frequency.

On the other hand, you may not need to employ such techniques. An electrically small antenna at 2m is only $2\mathrm{m}/10 = 20\mathrm{cm}$ *or less*. It's already pretty small.

## Answer (score 2, by NoGy)

If a simple magnetic loop antenna is what you want, you should have a look at

http://www.m0ukd.com/Magnetic_Loop/

The loop he constructed is about 10cm in diameter (which is approx. 4 inches) which is not that much to carry around.

For 70cm you might want to go for a small Yagi design since it provides you with some additional gain. For a 4-Element yagi the boom would be about 35cm (<14inch) long. A good design will give you around 7.5 dBd gain and a F/B ratio of around 13dB. For more information about that please visit

http://www.qsl.net/dk7zb/70cm/70cm-kurz.htm

With regard to the shortwave antenna you mentioned: These are normally wound around a ferrite core in order to increase the inductivity while keeping the antenna itself very small. Please note that most of these cores will not be suited for use in the UHF/VHF bands.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/559/how-can-i-construct-a-practical-loop-antenna-for-2m-band, by KF5RRR, Kuerno, Phil Frost - W8II, NoGy. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
