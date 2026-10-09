# Double power-handling ability of RF amplifier output transformer

*Tags: rf-power, electronics, equipment-design, amplifier · score 7*

## Question

I want to base the output network for a 500W push-pull HF amplifier on "A 250W Broadband Linear Amplifier" described in Chapter 17 of the 2014 ARRL *Handbook*. I need advice on whether and/or how the 1:4 impedance step-up transmission line transformer should be modified to handle twice the originally intended power.

The long-form article included on the companion DVD shares the rationale for the transformer:

The advantage of the transmission line type of RF transformer is that it does not have the leakage reactance that plagues the tube-and-sleeve type of transformer used on many solid-state amplifiers.

Simulation documents the significance of this statement: even with compensation, the gain falls off with increasing frequency when the coupling factor of a conventional transformer is reduced from the ideal value of k=1.

T3, the output transformer for this 250W PA, comprises two (2) separate ferrite-loaded 25$\Omega$ transmission lines whose inputs are paralleled on the low-Z side and connected in series on the high-Z side:

The transformer calls for miniature coax such as p/n D260-4118-0000 wound on Fair-Rite 2861010002 binocular cores. How can I determine, *a priori*, whether this transformer can handle a 500W output level? If it can't handle 500W, how do I determine what changes I need to make to the coax and ferrite components?

Is calculating power dissipation as simple as noting the resistance component of the impedance from the data sheet and multiplying that by the square of the product of the current and the number of turns? How do I convert that into temperature rise for the core?

## Answer (score 3, by Brian K1LI)

Details on 25$\Omega$ coax are not easy to find. In addition to the coax called out in the Handbook design, Communication Concepts sells UT-141C-25. Sadly, CCI does not publish datasheets for many of the products they sell, but I was able to find a datasheet for UT-141C-25 at Microstock Inc. With 0.1dB/ft loss at *500* MHz, the cable is rated to handle 470W, so it should dissipate about 5W running 500W at 30MHz and below.

The cable diameter is 3.6mm, so three turns require a core with a 7.9mm opening. Fair-Rite 2661801902 appears suitable, but with X$_L$=10$\Omega$ at 10MHz, three turns on two cores end-to-end would produce only 2.8$\mu$H of inductance and X$_L$=32$\Omega$ of reactance at 1.8MHz, short of the 50$\Omega$ needed.

The next larger core is Fair-Rite 2661665702, which delivers X$_L$=35$\Omega$ at 10MHz with a single core. Three turns will produce 5$\mu$H of inductance and X$_L$=57$\Omega$ at 1.8MHz, adequate for this design.

Care must be taken when winding the coax. Since the minimum bend radius is 4.8mm, winding the coax tightly against the shoulder of the core could damage the coax.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/14567/double-power-handling-ability-of-rf-amplifier-output-transformer, by Brian K1LI. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
