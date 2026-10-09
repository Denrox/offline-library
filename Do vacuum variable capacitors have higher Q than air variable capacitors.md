# Do vacuum variable capacitors have higher Q than air variable capacitors?

*Tags: antenna-tuner, electronics · score 5*

## Question

Do vacuum variable capacitors have higher Q than air variable capacitors?

They are not commonly seen in tuners or crystal sets.

But they are mentioned as superior to air variables for resonating magnetic loop antennas opposite the feed point -- because of the plate voltages involved in bringing a magnetic loop antenna to resonance.

Do vacuum variable have any Q advantage in lower voltage applications?

## Accepted answer (score 5, by WPrecht)

Q isn't related to the voltage. A simple definition of Q could be the ratio of the total energy in a system to the energy lost per cycle. So the biggest factor in Q is the loss in the dielectric.

In general, vacuum variable capacitors (VVC) have a higher Q than air variable capacitors (AVC) but there is some overlap. A common range for VVCs is a Q of 5000 to 10000, for AVC, a Q of 5000 is near the top end.

Vacuum would qualify as a better dielectric than air, but another reason to prefer VVC would be stability and endurance. The VVCs are sealed in a glass or ceramic vessel and therefore less sensitive to temperature changes and immune to other environmental changes such as humidity, dust, insects, children, dog fur, etc.

When considering the Q of a tuned circuit, Q = frequency / bandwidth where the frequency is the resonant frequency of the tank and the bandwidth is the frequency difference between the 3 dB points. As shown (Wikipedia):

As to why VVC are not commonly seen in crystal radios, it could be because crystal radios are generally inexpensive radios. Vacuum variables are considerably more expensive than the usual air variables. Although there are some highly sought after air variables that could set you back >100USD used due to some of their features and the fact they haven't been produced in some time.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1152/do-vacuum-variable-capacitors-have-higher-q-than-air-variable-capacitors, by Paul, WPrecht. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
