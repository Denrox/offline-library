# What are the electrical differences between smaller and larger coaxial cables?

*Tags: coaxial-cable · score 7*

## Question

How do different sized coaxial cables, such as RG-58 and RG-8, compare in terms of electrical properties such as loss? Do different cable types have different losses at different frequencies?

From test pool question: T9B10

## Accepted answer (score 2, by Dan KD2EE)

There are three basic electrical characteristics: characteristic impedance, loss per unit distance, and velocity factor.

Most amateur radio rigs and antennas expect to see a characteristic impedance of 50 ohms. There is coaxial cable with difference impedances, such as 75 ohms. Attempting to use a 75 ohm coaxial cable with a rig expecting to see 50 ohms of impedance will result in a portion of your transmitted signal being reflected back into the radio (or amplifier). This raises your SWR and will either cause your radio to decrease (fold back) its power (if it's a newer rig), or can cause your final amplifier to heat up faster than it should and can burn it out. (Don't get confused - characteristic impedance is measured in ohms, but it isn't measured with a multimeter. This has nothing to do with resistive power loss, it has to do with the ratio between voltage and current of a wave on that cable.)

Loss per unit distance is the big one. Generally speaking, the larger the cable, the lower the loss - but it also depends on frequency. Higher frequencies typically result in higher loss. This is usually given in decibles per hundred feet, and a value of $3dB/100ft$ means that if you use 100 ft of that coax at that frequency, you'll lose half of your power. If you need to get the loss of a particular cable, or compare two cables, you should get a chart or table from the manufacturer. This table lists some common types of coax at a variety of frequencies.

Velocity factor isn't something you'll need often. It tells you how fast a wave will propagate along that cable - which you can use if you want to build a phased array, for example. This is where you have two (or more) antennas spaced a certain distance apart, and also delay the signal going to some of the antennas so that they constructively interfere with each other in the direction of the array. It allows you to create a much tighter beam, at the cost of needing more space and supplies.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/765/what-are-the-electrical-differences-between-smaller-and-larger-coaxial-cables, by JC Hulce, Dan KD2EE. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
