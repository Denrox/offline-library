# Super-low-tech VHF low-pass filter construction?

*Tags: rfi, filter · score 7*

## Question

Related to this question: [Is it legal to broadcast an FM radio signal with a Raspberry Pi Zero?](Is%20it%20legal%20to%20broadcast%20an%20FM%20radio%20signal%20with%20a%20Raspberry%20Pi%20Zero.md)

Is it possible to build a super-low-tech low-pass filter for VHF harmonic suppression without a PCB or any other non-trivial-to-find components? (e.g. nothing surface-mount or tiny) Would a bunch of coax-stub (or twisted pair) reflective notch filters work? Hookup wire wound around a pencil inductors? etc.

## Answer (score 2, by Hamsterdave)

If you've got an RTL-SDR or similar broadband VHF SDR, you could construct a wideband noise generator and use it as a sort of poor man's VNA to tune the notch on a set of coaxial stubs. A dozen or so meters of high quality coax, RG-213, 9913F, or even better, hardline, could be used to build a set of stubs that would suppress harmonics fairly well. A pair of them properly connected should be able to suppress 2nd order harmonics by something close to 30dB. 3rd order is trickier, and requires carefully designed "T" type stubs that have reactance compensation included to avoid attenuating the primary frequency as well. It is not a trivial process, but the required materials are the same.

The same SDR/Noise Generator combination could potentially be used to tune a typical multipole LC filter, but that will not be at all trivial. You'll need a good L/C meter, and ideally an oscilloscope and a good clean variable signal generator to get the same attenuation as the coaxial stubs, and the components cannot be scrounged typically. You'll need low loss NP0 capacitors in very precise values and inductors wound carefully to avoid stray capacitance and thermal variation as well.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7279/super-low-tech-vhf-low-pass-filter-construction, by hotpaw2, Hamsterdave. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
