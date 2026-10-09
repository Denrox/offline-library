# How do I determine which HT antenna is better based on their very similar catalogue descriptions?

*Tags: antenna, ht · score 3*

## Question

I'm considering getting an after-market antenna for my new 2 m/70 cm HT and am trying to decide which of the two antennas I should get. My primary reason for considering an alternative antenna is improved RX/TX performance.

Both antennas in their specifications on the manufacturers web-site say following:

Maximum power: 10 W, gain 2.15 dBi, 1/4 wave on 2m, 1/2 wave on 70 cm, both have appropriate connector and impedance, both have specified SWR as less or equal to 1:1.5.

The only difference between them is that one antenna is 19 cm long and the other antenna is 36 cm long.

After doing some research on the internet, I've noticed that a large number of HT antennas have extremely similar technical specifications, with only difference being the antenna length. I've also read very vague and general descriptions saying that longer HT antenna==better HT antenna.

So how do I determine which antenna is better based on provided information?

By the way, I want to keep the question as general as possible, so I didn't mention models until now, but they are Diamond SRH-701S and Diamond SRH-536.

## Accepted answer (score 6, by Phil Frost - W8II)

Catalog descriptions are bogus. What they are describing are characteristics of monopole antennas in general, not either *specific* model.

Clearly, they can't both be 1/4 wave antennas at the same frequency but also be different lengths. A 1/4 wave at 145 MHz is about 49 cm. Neither one is a 1/4 wave antenna,. What they probably are is *electrically* a 1/4 wave, made electrically longer than they physically are with a loading coil. The more loading, the shorter the antenna, and everything else being equal, the less efficient the radiator.

They also both quote gain as 2.15 dBi. This is the theoretical gain of a half-wave dipole in free space. An ideal quarter-wave monopole is equivalent to a dipole, and has the same gain. It doesn't sound like they made any actual measurement of either antenna's gain. These antennas have *significant* deviation from the ideal models: they have loading coils, they are over (lossy) Earth, and they lack a ground plane that's anything close to ideal.

Absent accurate specifications from the manufacturer or vendor, it's true of all antennas that longer is better, up to the point that the antenna is self-resonant. To make it shorter requires the addition of reactive components that don't contribute to radiation and must necessarily introduce additional loss if constructed of real materials.

## Answer (score 5, by Ron J. KD2EQS)

All other things being equal, a longer HT whip will outperform a shorter whip. The shorter length is *probably* because of a larger loading coil, which *could* result in loss.

The gain numbers from most antenna manufacturers should be taken with a grain of salt. They use wild assumptions when calculating it. In most cases HT whips are so cheap, one could buy both (or several) and simply try them all out to find the best performance for the given band/frequency/repeater.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1909/how-do-i-determine-which-ht-antenna-is-better-based-on-their-very-similar-cata, by AndrejaKo, Phil Frost - W8II, Ron J. KD2EQS. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
