# How to tune an FM transmitter to a specific frequency?

*Tags: legal, frequency, fm, transmitter · score 8*

## Question

I am planning to organise a simple fox hunt, a family event. This includes building a transmitter. I am currently considering the following schematics:

- https://maker.pro/education/diy-fm-transmitter
- http://www.buildcircuit.com/simple-steps-for-making-fm-transmitter/

Both target the 88-110 MHZ band, but that range of frequencies requires licensing. I live in Ireland and according to the local rules the following bands seem to be available:

- 26.957 – 27.283 MHz (no further requirements)
- 40.660 – 40.700 MHz (no further requirements)
- 49.82 – 49.98 MHz, 10 mW ERP, no other requirements
- 169.4 - 169.475 MHz, 500 mW ERP, Duty cycle < 10% Max 50 kHz channel spacing
- 433.050 – 434.790 MHz, 10 mW ERP, Duty Cycle ≤ 10 %

This is how I understand the document https://www.comreg.ie/media/dlm_uploads/2015/12/ComReg0271R9.pdf

Now, from the list above 169 MHz range seems to be the closest to 110 MHz. My plan is to first build the transmitter within the 88-110 MHz range, verify using common radio receiver that it works and then tune up to 169 MHz.

I assume that if I play with the coil inductor (add or remove turns) and/or capacitor the shift from 110 to 169 MHZ will be possible. I found a surprisingly affordable frequency counter on Amazon and hope it will help me to validate the frequency (so that I do not skip to 200 MHz). https://www.amazon.co.uk/gp/product/B01B3ZCP3U/

Would that work? Is this how tuning is normally done?

EDIT: The desired communication distance is up to 100-200 meters from the fox box in a park (within line of sight).

## Accepted answer (score 4, by Glenn W9IQ)

I will assume you will get the legal issues sorted so I will address the circuit itself.

If you look at the second circuit you referenced, you will find L1 and VC1 in parallel. These form a tuned circuit that sets the output frequency of the transmitter (ignore the polarity symbol on VC1, it is a remnant of the circuit editor on this site):

The formula for the resonant frequency of this circuit is:

$$Frequency=\frac{1}{2\pi\sqrt{LC}} \tag 1$$

where Frequency is in Hertz, L is the inductance in Henries and C is the capacitance in Farads.

In your case you may find it helpful to solve equation 1 for LC:

$$LC=\left(\frac{1}{Frequency*2\pi}\right)^2 \tag 2$$

where resonance is achieved by any combination of inductance and capacitance where their product equals the right side of equation 2.

So with L1 = 0.1 $\mu$H, VC1 would need to be set to about 26 pF to hit the middle of the FM band (98 MHz).

If you wish to adjust the output frequency to ~170 MHz, VC1 would need to be set to approximately 9 pF according to equation 1. But the recommended capacitor for VC1 probably will not go that low so select a different variable capacitor that can be adjusted to this value; or place a 10 pF capacitor in series with VC1; or use a 10 pF fixed capacitor instead of VC1 and simply stretch or compress the windings of L1 a bit to adjust the frequency. Your frequency counter will make this a straight forward process.

As the capacitor value gets quite small, the circuit may not behave as expected due to stray capacitance. You can overcome this by reducing the inductance value. For example, 4 turns of wire wound on a 0.25 inch form and spaced out to make a coil that is about 0.5 inches long will form an inductance of ~0.04 $\mu$H. A 22 pF capacitor in parallel with this will get you into the 170 MHz range.

The circuit will be sensitive to the presence of your hand or any metal tools. You can make the inductor adjustment with a small wooden stick to avoid this problem. A stiff piece of plastic (e.g from a plastic milk jug) can serve as a poor man's adjustment tool for the variable capacitor.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10017/how-to-tune-an-fm-transmitter-to-a-specific-frequency, by Alexander Churanov, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
