# Does using a computer SMPS to supply a transceiver bleed hum into the signal?

*Tags: power-supply · score 3*

## Question

A dedicated/custom power-supply for an HF rig may, on occasion, be unavailable. The internet lists any number of articles on the subject of modifying a computer power-supply.

E.g.

- http://www.wikihow.com/Convert-a-Computer-ATX-Power-Supply-to-a-Lab-Power-Supply
- http://www.instructables.com/id/Convert-an-ATX-Power-Supply-Into-a-Regular-DC-Powe/

Apparently using a computer SMPS to power a transceiver bleeds hum into the signal. Is there any truth to this? Does using a computer SMPS to supply a transceiver bleed hum into the signal?

## Accepted answer (score 2, by Adam Davis)

The power supply usually recommended is an ATX computer power supply, which has minimum specifications for ripple and regulation.

The minimum standard indicates that:

- The 12V supply must be within +/- 5% (11.40V to 12.60V)
- The ripple in the 10Hz to 20MHz band must be less than 120mV

This is fine for computing requirements, but terrible for radio and analog use. Note that the specification doesn't care about ripple above 20MHz, and at that point you've only got the basic bare minimum protections the FCC requires Part B computing equipment to follow. This can account for a significant amount of noise.

While you can use a PC power supply as a radio supply, the supply may not provide clean enough power to satisfy your personal signal requirements.

Note, however, that this will vary from supply to supply, and from radio to radio. Radios with very good power supply noise rejection (such as mobile radios designed for vehicle power supplies) may be able to provide good signals with a poor power supply. Similarly you may find that a particular PC power supply is very clean with low ripple.

Due to the noise inherent with switching power supplies, though, many hams insist on transformer style power supplies with linear regulation and would balk at any switch mode power supply.

If you are concerned about signal quality, choose good power supplies, or quantify the noise your supply generates with a spectrum analyzer. You may also be able to add additional filtering on the output of the power supply to mitigate those issues, but that usually costs more than the savings you had from starting with a cheap PC power supply in the first place.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/294/does-using-a-computer-smps-to-supply-a-transceiver-bleed-hum-into-the-signal, by VU2NHW, Adam Davis. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
