# Stub impedance matching

*Tags: impedance, transmission-line · score 4*

## Question

What is the process of stub impedance matching and what are the elements included in the calculations relevant to it?

## Answer (score 3, by Phil Frost - W8II)

"Stubs" are sections of transmission line which are usually less than a half-wavelength long and either shorted or open on one end.

The two connections on the other end look like two terminals on a lumped impedance which can be either an inductor or a capacitor, depending on the length of the stub.

For a short-circuited stub, the impedance is:

$$ j Z_0 \tan\left({2\pi\over\lambda}l\right) $$

where:

- $j$ is the imaginary unit,
- $Z_0$ is the characteristic impedance of the transmission line,
- $\lambda$ is the wavelength, and
- $l$ is the length of the line (in the same units as the wavelength).

An open-circuited stub is the same but negative:

$$ -j Z_0 \tan\left({2\pi\over\lambda}l\right) $$

It is thus possible to construct a stub which has the same effect as any reactive component at a particular frequency. A distinct advantage is that stubs are in some cases more easily fabricated than capacitors or inductors, for example at microwave frequencies where transmission lines are easily fabricated on PCBs.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/4885/stub-impedance-matching, by Max, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
