# Is a connecting computer sound output equivalent to connecting a "dynamic" mic?

*Tags: audio-interface, microphone · score 3*

## Question

I bought a Kenwood audio breakout cable having only the kenwood connector (3.5mm and 2.5mm-in-one) on one end and up to me to add connectors on the other side.

It came with a nice diagram for how to wire it up, but also said that a 1µF capacitor should be added in series with the microphone if it's a dynamic mic.

Which microphones are "dynamic", needing this capacitor?

What happens with non-dynamic mics if I add the capacitor?

My plan is to add two 3.5mm connectors to connect to a computer (specifically this USB audio card) and trigger tx with VOX, so a USB sound card is what I'm most interested in how to properly set up.

## Answer (score 6, by Phil Frost - W8II)

A dynamic microphone is basically a speaker in reverse. A diaphragm moves a magnet in proximity to a coil, varying the magnetic flux though the coil and inducing a current in it. You can in fact use a speaker as a dynamic microphone, though the sound quality is quite colored.

A condenser microphone is a capacitor. (In some places and times, "condenser" is synonymous with "capacitor".) One plate is fixed, and the other is the diaphragm. The capacitor is biased with a constant charge. As the diaphragm moves the distance between the plates changes, and thus the capacitance charges. Since the charge is constant, the voltage varies.

Condensers require a source of power to bias the capacitor, and in practice they must also include a buffer to convert the high condenser output impedance to something appropriately low for a long cable. It often takes the form of a simple FET integrated with the microphone capsule. Rather than running another pair of wires just to power the microphone, it's common to use the same wires to deliver power by employing a bias tee:

This circuitry would be inside the radio so a microphone can simply be plugged in without additional components. The capacitor serves to block DC while allowing AC (the audio signal) to pass. In this way the circuitry inside the radio can bias the audio signal to whatever voltage is required by the design, independently of the bias voltage to power the microphone.

By adding another series capacitor to the left of V1 you're blocking the bias voltage from reaching the microphone. In the case of a dynamic microphone this is important, since the coil of a dynamic microphone looks like a short to DC. As such your microphone would become a heater, then a smoke machine, then a paperweight.

However, this would also block the bias voltage necessary to run a condenser microphone.

To determine what kind of microphone you have, it's best to just read the manual.

A USB sound card isn't a microphone at all. The sound card output may already include a series capacitor, but I wouldn't count on it. Since the sound card doesn't need a bias voltage to power it, I would include a series capacitor to be sure, similar to a dynamic microphone. You may also find the sound card output is much too loud, so adding a voltage divider to attenuate the sound card output may be necessary.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/11772/is-a-connecting-computer-sound-output-equivalent-to-connecting-a-dynamic-mic, by Thomas, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
