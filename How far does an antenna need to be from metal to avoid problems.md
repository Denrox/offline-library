# How far does an antenna need to be from metal to avoid problems?

*Tags: antenna, antenna-theory · score 9*

## Question

Living in an apartment, I'm struggling to get good antennas set up, especially for HF. Worse yet, I'm not allowed external antennas (but am willing to try something low profile on the balcony), my apartment is built with stucco (with the "chicken wire" embedded in it), and my window frames are all aluminum. I have a balcony, but it's got a low (3') wall made of stucco inside and out (2 layers of mesh!) topped with a metal railing.

I tried a dual-hamstick dipole for 20M, but was placing it only 24" over the balcony floor, and this is below the edge of the wall. Tuning it was basically impossible, though I eventually could get 2:1 at one frequency. The balcony is about 4 feet deep and 10 feet long, and there is another floor above mine (so no roof access, and there's poured concrete above).

So how far away does metal have a significant impact on my antennas? I'm assuming it's design- and frequency-dependent, but I'm looking for resources that can help me figure out approximate clearances that are needed. Mostly I'd like to work at 20M, 10M, and 2M. (My balcony is way too small to think about 40M and lower.)

## Accepted answer (score 3, by Phil Frost - W8II)

It sounds like any antenna you can build in this situation is going to be a compromise.

Distances are going to be relative to wavelength, so an HF antenna will be more difficult than VHF or UHF. For the antenna to be really in the clear, two wavelengths is a good rule of thumb. You can probably get as close as a quarter wavelength and still make things work with some adjustments to the tuning.

You can use the metal parts of your structure as part of the antenna, if that makes things easier. For example, I bet a 2m whip on the corner of the balcony could work well enough, with the metal railing being the ground "plane". It's far from ideal of course.

HF is going to be tricky, no way around it.

## Answer (score 3, by W4QA)

The region around the antenna where metallic objects will have the most impact is within the "near field". This distance is directly proportional to wavelength, and varies depending on if the antenna is electrically short or long. The energy reflections in the near field will have a direct impact on the source, impacting the impedance seen and the loss experienced.

There is a good description of Near Field vs. Far Field here: https://en.wikipedia.org/wiki/Near_and_far_field

## Answer (score 2, by Louis Seaman)

Reflection from a grounded surface can cause an issue; but who knows if the chicken wire is grounded and how good a ground it is? The more probable cause of your high VSWR is common-mode current finding it's way back to your radio on your coax shield unless you've put choke on the coax near the antenna feed-point. To address your desire to work 2M, that is easily done with a J-Pole antenna that you can build out of some old 300 Ohm twin lead, or any number of plans online; here's one: J-Pole Example 1 J-Pole Example 2

A J-Pole is a 1/4 wave (λ) parallel transmission line, shorted on on end, with the other end feeding a 1/2λ radiating element, with the transmission line (coax) feeding the 1/4λ wave transmission line at the 50 Ohm point; so the overall antenna is 3/4 of a wave length, with only the 1/2λ element at the top, radiating, and allowing the bottom of the U part of the antenna, to be grounded if desired. You do want to form a choke out of your coax as near to your feed-point as possible, without letting the coil touch the parallel transmission line.

For 10M, and 20M if you dare, you can build this balcony antenna out of PVC and coax. Basically, everything left of the coax choke hangs outside your balcony, and the coax choke, along with some creativity, keeps the antenna vertical and stable on your balcony (that part of the design is up to you). The design uses 1/2" PVC outside the balcony for weight savings, and 3/4" PVC for strength and counterbalancing, inside the balcony. If you're ambitious, you can use threaded fittings here and there so you can take it apart and keep your better half happy when you're not using it.

The formula (2952/frequency in MHz) for stripping your coax cover in inches and separating your braid from your center conductor, will get you close to your desired frequency. To tune the antenna, you must have the coax choke in place, otherwise your coax will carry common-mode current as it acts as a second counterpoise. You will want to set your radio to its lowest power output, and go through the band you designed the antenna for and find the frequency where your VSWR is lowest; if that frequency where the VSWR is lowest, is above your desired "center" frequency, then trim a couple of inches off the center conductor radiator, and the braid counterpoise, and repeat until the VSWR is lowest at your "center" frequency. If your VSWR is lowest below your desired frequency, woops, trash that formula, and pull out the coax and strip back more of the coax cover, and separate more shield and center conductor (this is the reason why you want a foot or so of the center conductor radiator, and shield counterpoise, hanging beyond the 1/2" pipe). Repeat test until satisfactory.  Notes on design: Normally a 90 degree counterpoise would give you a 37 Ohm feed-point impedance, but not when you only have 1 counterpoise, it will be closer to 46Ω, and if the PVC droops under its own weight, it may actually get to 50Ω; and for what it's worth, your signal will be favoring the counterpoise, away from the building. And orientation of the coax center conductor can point to the sky or the ground or anywhere in-between to get the best VSWR or best receive of another station.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/3518/how-far-does-an-antenna-need-to-be-from-metal-to-avoid-problems, by David KF4MDV, Phil Frost - W8II, W4QA, Louis Seaman. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
