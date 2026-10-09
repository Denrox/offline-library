# What is the impedance of an end-fed half-wave antenna?

*Tags: antenna-theory, impedance, end-fed-antenna · score 15*

## Question

It is my understanding that the feed-point impedance ($Z_a$) of an end-fed half-wave antenna is dependent on at least the following factors:

- $L_a$: The length of the radiating element of the antenna.
- $D_a$: The diameter of the radiating element of the antenna.
- Environment surrounding the antenna.

It it also my understanding that such an antenna is not actually resonant (Meaning the impedance is purely resistive) when $L_a = 0.5\lambda$, but rather something a tad smaller. A common number I've seen thrown around is ~$0.41\lambda$, but different sources seem to have slightly different values.

My general question is, assuming the antenna is radiating in free-space, what is the theoretical mathematical relationship between $L_a$, $D_a$, and $Z_a$?

More specifically, I'd like to know how to calculate two things:

- For a given $D_a$, what value of $L_a$ (when $L_a \le 0.5\lambda)$ would give me a real (purely resistive) $Z_a$ in free-space?
- For a given $L_a$ and $D_a$ (or when those variables are constrained so that $Z_a$ is always real), what is the exact value of $Z_a$ in free-space?

Bonus points for elaborating on how these values are related in practical, non-free-space environments.

I have seen many confusing estimations for $Z_a$, ranging between 1800Ω and 5000Ω, which is a huge range. I want to better understand what factors are involved and how to mathematically calculate the value under ideal circumstances.

## Accepted answer (score 12, by Phil Frost - W8II)

It's very difficult to predict the impedance of an end-fed wire, other than to say it's high. Usually it's determined empirically.

You are looking for a theoretical formulation. Consider, the feedpoint is a voltage source which makes a difference in electric potential between to things. The end of the dipole, and...what?

Maybe you could imagine the feedpoint connected to a theoretical shell of infinite radius, similar to how self-capacitance is calculated? I'd guess the result depends strongly on the geometry of the wire, but generally the thicker the wire, the lower the impedance. I don't know of what practical value this model would be since any real antenna has at least a feedline and a ground/aircraft/spacetraft nearby which would be more significant.

You can also calculate the impedance of an [off-center fed](How%20does%20moving%20a%20feedpoint%20off-center%20in%20a%20dipole%20affect%20the%20resonant%20frequency%20and%20resistive%20load.md) dipole, very close to the end. You'll notice the limit of that function as the feedpoint approaches the end is infinity. This is of course an approximation assuming the dipole is relatively thin, and that the capacitance to the other half of the dipole is the most relevant factor.

So if there isn't another half of the dipole, what is the relevant factor? In practice it's going to be the ground, and the feedline. Neither is amenable to a simple expression. Simulation of your particular installation is your best bet.

We can make some generalizations though:

An end-fed dipole is resonant (or not) just like a more ordinary center-fed dipole. The feedpoint (in the middle, near the end, or somewhere between) is transparent to the resonance of the wire.

An exactly half-wave dipole isn't resonant in the sense that its feedpoint impedance has a reactive component. Theoretically, (73 + j42.5)Ω.

When the dipole is too short, its reactance will be capacitive. When it's too long, inductive. Since the exactly half-wave dipole has a slightly inductive reactance, shortening it can eliminate the reactance. The exact amount of shortening depends on the thickness of the wire. 0.41λ sounds like a reasonable estimate.

The feedpoint impedances repeat with every wavelength of length. That is, in terms of feedpoint impedance, 0.5λ, 1.5λ, 2.5λ, ... dipoles all look the same.

As the dipole becomes thicker, its bandwidth increases. That means for an equal change in length, the impedance of a thicker dipole will change less than a thinner dipole.

Since the impedance must repeat with every wavelength, this also means that the highest impedance (for example, at the ends of a half-wave dipole) is lower with a thicker wire.

Finally, a practical point: since the impedance at the end of a dipole is very high, the common-mode impedance looks relatively low. Successfully making an end-fed dipole then depends on very effective choking (a very high common-mode impedance), which is difficult to realize in practice. If the choking isn't very effective (meaning, the common mode impedance isn't much higher than the differential mode), then making the choking more effective will increase the impedance seen by the transmitter.

## Answer (score 5, by abcd567)

1.

**Wikipedia: Monopole Antenna**

The monopole always has another set of conductors to which the second wire from source is connected.

This second coundutor may be earth, or a metal object commonly known as "ground plane". The ground plane turns the monopole into a virtual dipole with length each limb of virtual dipole equal to length of monopole. Thus the half wave monopole's virtual dipole is a full wave dipole.

The impedance of monopole is half of its virtual dipole's impedance. For example a quarterwave monopole with ground planehas impedance of 36 ohms, which is half of 75 ohms, the impedance of its virtual dipole, the halfwave dipole.

2.

**Wikipedia: Dipole Antenna**

The impedance of a dipole varies very sharply when its length is fullwave. The equivalen monopole is half of its length, so monopole's impedance varies very sharply when its length is halfwave. The best way is to use simulation software to determine impedance (R and X). A plot of R & X vs length by sweep can give the point where you can get desired values.

3.

If you want to use formula to determine impedance, please see this book: **ANTENNA THEORY - ANALYSIS AND DESIGN By Constantine A. Balanis** Chapter 8: Integral Equations, Moment Method, and Self and Mutual Impedances

## Answer (score 4, by K9AXN)

Model the 1/2 wave center fed antenna using the wire size, altitude, and all location attributes to determine the center fed impedance.

divide 600 by the 73 ohms or whatever you calculate the center fed impedance to be then multiply the answer by 600 --- you're home.

Example: $600/73 = 8.22 \times 600 = 4900$ ohms.

This is the original and correct quarter wave transform using 600 ohms to represent the surge impedance of a single wire. Earlier I edited the 600 ohm value to 380 ohms in error because some of the CAD antenna design tools apparently used approximately 380 ohms.

Using repeatable measurements, the Surge impedance of a single wire verifies that the impedance of a wire unmolested by external sources will be approximately 600 ohms and will vary less with wire diameter than previously thought.

The measurement can be done at the feed point of an open wire and verified with termination value.

The equation used to determine the surge impedance of a single wire is

$$ Z = 138 \log\left(\frac{4L}{d}\right) $$

where $L$ is the length of the wire and $d$ is the diameter of the wire — same units; In space.

INFORMATION ADDED FOR CLARITY:

The following url represents a circuit that can be used to measure the surge impedance and velocity factor of a single wire or transmission line. It is a variable voltage divider, adjustable from 50 to 1050 ohms.

http://www.k9axn.com/attachments/Finished_3_jpg_final.jpg

The following url represents the measurement of the surge impedance and velocity factor of a 54 foot length of #14 wire.

http://k9axn.com/attachments/Single_wire_4.AVI

Important to note: The two timing lines from the rise to 115ns represent an approximately 4 volt @ .007A wave entering the wire. The wave will have reached the end of the wire at mid point, then return during the second half where you see the voltage rise to 8 volts and current cease.

The rise and fall times are a result of instrument limitations. Surge current behaves as purely resistive, much like the impedance of space. It is used to calculate the radiation resistance of an antenna and is largely unaffected by proximity to the ground.

END OF INFORMATION ADDED FOR CLARITY

The above Image represents the measurement of the Surge impedance and velocity factor of a single wire. It can be used to measure the Surge impedance and velocity factor in coax, twin lead or any antenna wire.

The surge impedance of a single conductor or transmission line is essentially composed of two primary notions, the impedance of space 377 ohms and the energy used to accelerate electrons. Be mindful that the electrons in a 1 KW 14MHz transmission line or antenna will remain within approximately 1/10,000 of an inch from where they started. This can be visualized using a Newton's cradle.

With that information it becomes clear that the opinions regarding end fed antennas are wanting: The impedance at the feed point is not infinite and is easily calculated. The reflected waves/current that flow within an antenna when reaching an end are wholly reflected.

The next edit will consist of a cycle by cycle narrative of the measurements and events as the antenna is spooled up.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7081/what-is-the-impedance-of-an-end-fed-half-wave-antenna, by Robert Quattlebaum, Phil Frost - W8II, abcd567, K9AXN. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
