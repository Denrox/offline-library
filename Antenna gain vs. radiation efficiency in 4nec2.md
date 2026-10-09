# Antenna gain vs. radiation efficiency in 4nec2

*Tags: antenna-theory, hf, antenna-modeling · score 3*

## Question

I'm trying to evaluate HF antennas for low angle performance to pick from a list of designs that will fit in my limited space. I'm using 4nec2 to simulate them and compare the patterns.

When your simulated antenna has a low radiation efficiency, is the reported gain compared to an isotropic radiator with perfect radiation efficiency, or one with a radiation efficiency the same as your simulated antenna?

Here's an example to clarify because I'm not sure I'm using the right terminology. I'm comparing two antennas:


Antenna 1 reports 6dBi at 0 degrees azimuth and 10 degrees elevation, and it has a radiation efficiency of 80%.


Antenna 2 reports 6dBi at 0 degreez azimuth and 10 degrees elevation, but it has a **radiation efficiency of only 40%**.

Assuming everything else like ground and feed systems are the same, is the model telling me that the effective radiated power in that specific direction will be the same for both antennas, or will antenna 2 radiate half as much power in that direction because of the lower radiation efficiency?

## Accepted answer (score 3, by rclocher3)

4nec2 takes the radiation efficiency into account when it calculates the gain. You can see this for yourself by modeling an antenna made of copper and then writing down the gain, and then changing the antenna model to use a lossier material such as iron. So 6 dBi is 6 dBi no matter what the radiation efficiency of the antenna may be. To answer your question, both antennas would radiate the same amount of power in that specific direction. But there is no such thing as a free lunch, so the lower efficiency of the lossier antenna surely shows up in the antenna pattern in the form of lower gain in other directions, even if the peak gain of 6 dBi is the same as the peak gain of the other antenna.

## Answer (score 2, by Richard Fry)

Recall that:


Antenna system **gain** (efficiency) *includes* system r-f losses. If any exists, then a proportional amount of applied power from the transmitter is dissipated as heat in the lossy elements of that antenna system.


The shape of the radiated envelope (relative fields) of that antenna system remains the same for all *non-zero* losses, but for other things equal, its radiated power is reduced.

For an example using 4nec2 with a NEC4.2 engine, the far-field study shown below illustrates that the E/E(max) relative fields of a vertical monopole remain the same for the two different configurations of a lossy ground plane connection to the earth, but **not** their gains (efficiencies).

The blue trace there shows the pattern directivity if that system had zero losses, and in this configuration, antenna system radiation efficiency is 100%.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5848/antenna-gain-vs-radiation-efficiency-in-4nec2, by hamateur_sandwich, rclocher3, Richard Fry. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
