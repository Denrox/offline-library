# In software circularly polarization of antennas

*Tags: antenna, software-defined-radio, polarization · score 3*

## Question

I have an RSPduo which has true diversity capability. Now my question is whether or not I can use this diversity feature to select the optimal amplitude and phase contribution of the horizontal and vertical elements from a cross yagi.

So instead of delaying one of the radiators with a 90° phase coax line I just hook both radiators up to the SDRduo, one to each leg and then use the software phase and amplitude regulation to create a "circularly" polarized antenna.

Is this feasible and does it provide any advantages over the hardware implementation?

Often sat reception antennas can be switched between horizontal and circular polarization to optimise the noise on low-elevation passes. Here is a journal describing such a switcher. https://www.amsat.org/amsat/articles/i8cvs/Part_1_AMSATJournal_MarApr07_I8CVS_Polarization-1.pdf

Thank you for your insight. 73 de HB9HIH

## Answer (score 3, by Marcus Müller)

So instead of delaying one of the radiators with a 90° phase coax line I just hook both radiators up to the SDRduo, one to each leg and then use the software phase and amplitude regulation to create a "circularly" polarized antenna.

Sure, that works, if the two channels are phase-coherent.

Is this feasible and does it provide any advantages over the hardware implementation?

yes, it's done, and the advantage is that you can adjust things to your heart's delight – including correcting for e.g. elliptic polarization due to propagation effects.

I don't agree with Ryuji there, rarely enough that that happens: The 3 dB "penalty" isn't one; you get to sum up both orthogonal antenna's output powers, whether you do it in hard- or in software.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/23323/in-software-circularly-polarization-of-antennas, by Phönix 64, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
