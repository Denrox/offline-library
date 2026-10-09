# What is the expected microphone input voltage level of a handheld transceiver?

*Tags: diy, ht, microphone, audio-interface · score 10*

## Question

Ok, so I'm looking to inject some computer generated CW into a little handheld rig by wiring direct into the mic input line. What sort of voltage is expected on this input, are we talking uV, mV or even Volts?

## Accepted answer (score 4, by WPrecht)

In general you are talking volts. But it's different for each make of radio and even different models of the same brand. You might want to start researching here, the link contains a vast amount of information about microphone pinouts and links to even more information. I know you mentioned you are hacking what's probably a cheap Chinese HT, but this source will give you some idea.

Next, connecting the computer directly to the radio, without some form of isolation is a Bad Idea (tm). It's doable for short tests, but you'll introduce noise and the possibility of ground loops, etc. They make cheap audio transformers for just such a purpose, plus they are useful for my next point.

PC speakers and mics are generally very low impedance, like 4 or 8 Ohms. Radio mikes are all over the place on impedance, but frequently 600 Ohms. So you'll need a transformer to match that anyways, once you determine the impedance of the microphone, you can select the right value.

## Answer (score 4, by Adam Davis)

A very simple adaptor can be built as follows:

You can increase R1 to lower the signal level at the microphone output, or decrease R1 to raise the signal level. While some use potentiometers to make adjustments easier, I've found they are a frustrating source of noise and failure in such circuits, and suggest that, if used, they should be used only to find an appropriate level, then measured and replaced with a fixed resister. C1 can be between 1uF and 4.7uF for audio level signals, but if you're trying to pass very high frequency signals you might stay on the lower end of that.

While C1 will help reduce ground loop problems, you may still experience them, particularly if the radio is located far from the computer, or attached to a different power source than the computer. The use of an audio isolation transformer can be helpful with this.

Impedance matching isn't necessary since the microphone impedance is significantly larger than the speaker output, and we're not trying to transfer significant power. The only worry one might consider is whether the speaker output will be damaged with a high impedance. My experience with most PC sound cards suggests that there's nothing to worry about, but you can place a low value resister in parallel with this circuit on the speaker output if it concerns you.

The values as suggested will probably provide more volume than needed. This only drops about 30dB, whereas I'd expect a 40dB drop is needed for a speaker output to microphone input. However, this is intentional, and allows further volume control to occur on the computer. Again, increase R1 by doubling it each time if you find this too "loud". A 1Mohm resistor in R1 would give about a 40dB drop.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1593/what-is-the-expected-microphone-input-voltage-level-of-a-handheld-transceiver, by WPrecht, Adam Davis. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
