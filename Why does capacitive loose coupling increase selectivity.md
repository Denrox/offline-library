# Why does capacitive loose coupling increase selectivity?

*Tags: equipment-design, antenna-tuner, crystal-radio · score 6*

## Question

There are multiple ways to couple antennas. It is said that an antenna is capacitive loose coupled if a small capacitor is used between the antenna and the parallel resonant circuit (like **C2** in the image below). Such a loose coupling will increase the selectivity of the following parallel resonant circuit. That means the bandwidth of the parallel resonant circuit will be smaller. Therefore frequency parts of the signal which are farther away from the resonant frequency of the parallel resonant circuit will be "filtered out".

I understand, that a smaller capacitor means a looser coupling. The smaller the capacitor, the less energy will be transferred to the resonant circuit (therefore it is "loose" rather than "tight" coupled), due to an increasing capacitive reactance.

My question is: How can the increase of selectivity physically explained? It seems as if the capacitor suddenly acts like a bandpass. But why is that?

I googled a lot, but unfortunately everything I found just says "it is like that" or "do it like that" but not why this phenomenon is observed.

## Answer (score 2, by ESP32)

I think if we were able to use perfect components, it would not matter. However, your antenna is not a perfect component. Is has many losses which result in a resistor R in its replacement diagram, in serial to C2. Now you can consider your antenna system as one resonant circuit consisting of: L/C of the wire, C2, L1, C1 and R.

Looking at the circuit this way helps me to understand why a looser coupling of the lossy C2/R component helps to increase the all over Q of the circuit. Because the smaller C2 gets, the more the high Q of C1, L1 comes into position.

We should keep in mind that having a small C2 will help to get a higher Q, which is desirable for active antennas (receiving antennas). On the other hand loose coupling will reduce the efficiency, if C2 does not match the L/C of the antenna.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16372/why-does-capacitive-loose-coupling-increase-selectivity, by dudekowsky, ESP32. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
