# How to tell if a vacuum tube has gone bad?

*Tags: electronics, transmitter, am, vacuum-tubes · score 4*

## Question

Because it was $5 on my local classifieds, and I have a bit of a weakness for old junk, I bought myself a Heathkit HW-30 "Two-er". I've been going through the alignment procedure in the manual and have been pleasantly surprised at how well everything is working so far. **I have not replaced any components, including tubes. Only adjusted trimmer capacitors and inductors as directed.** The receiver works very well; no issues there. However, the transmitter seems to have tome trouble.

For those not familiar with the Two-er, it is an all-vacuum-tube, 2M, AM transceiver. The transmit section consists of a 8 MHz oscillator, followed by a doubler, two triplers (to get up to 144 MHz), and then a final amplifier. Having gone through the alignment procedure, the frequency multipliers seem to be working okay because I get ~144 MHz at the output on my frequency counter. But the output power is far below where the manual says I should expect it.

Here is the schematic of the oscillator+multipliers+final. I've gone through and checked the noted voltages on transmit (as specified by the manual). All are good, except the grid voltages are consistently higher than what it calls for here. For example, pin 7 on V5A has a voltage of only -15 V on transmit, instead of -30V. Only pin 7 on V4B has the specified voltage of -4V.

Does this mean the tubes have gone bad? Could the tube still work to multiply the frequency without providing the necessary drive to the final?

Since V4 and V5 are the same, I was tried swapping them. No change in performance.

## Answer (score 5, by Ryuji AB1WX)

I am definitely a transistor/integrated circuit generation and not as old as the tube guys. But your description fits the common problem with aged tubes: cathode depletion.

Cathode depletion can occur when the materials on the cathode and the heater "spend up" over time, or their surfaces could have been chemically deteriorated to render them ineffective in emitting electrons. When this happens, fewer electrons (the negatively charged particles) reach the grid, and the grid potential moves positive-wise.

Other mechanisms, such as increased grid leakage and gas contamination, can be possible.

With these problems, the tube will have slow warm-up time, less gain, greater plate resistance, less output power, and more distortion. You still get enough harmonics to multiply frequency, but not as much power will come out.

If the problem is caused by a long unused period, it might be momentary; leave the heater on for a while. Some people apply slightly higher heater voltage if it is safe for rejuvenation purposes.

I would say test with a fresh tube is the best way to go.

##### Addendum

The oscillation is achieved in V5A by using the screen grid as the "anode" of the bottom half of the pentode. Then, the first frequency tripler is at the top of the same pentode, using screen as the input, and use the real plate as the anode. Then V5B triples again and V4A doubles.

##### Common problem with dirty FT243 crystals

This video just popped up on my Youtube recommendation:

https://www.youtube.com/shorts/JoZ6q-axvzQ

It shows how the oscillator takes a long time to stabilize the frequency (sounds like very long chirps) while still producing the full power. The crystal was cleaned, and the oscillator then started and stabilized quickly.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/23363/how-to-tell-if-a-vacuum-tube-has-gone-bad, by byl, Ryuji AB1WX. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
