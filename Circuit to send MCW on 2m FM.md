# Circuit to send MCW on 2m FM

*Tags: cw, vhf · score 6*

## Question

I regularly practice Morse with a friend on 2m NFM by holding our tone generators, which we also use for personal practice, close to the microphone. We send text by CW, read it back, and discuss how we are doing and how can improve our "fists". However we have to turn the volume up on the tone generator so loud it is annoying to others in the house.

We would like to build a circuit that allows us to inject the tone directly into the microphone lead, and use earphones to listen to both CW and voice. I have seen circuits for this but they all include a tone generator, we would like to keep that separate.

Please has anyone advice on how to go about this, the design parameters to work to, and what pitfalls there might be?

## Answer (score 4, by Kevin Reid AG6YO)

Broadly speaking, this is the same kind of problem as connecting it to a computer's sound output for digital-mode operation. The exact circuit you will need **depends on the specific characteristics of the microphone input of your model of transmitter**, but it will likely need these characteristics:


**Attenuation**: your tone generator's output is meant to supply power to a speaker or headphones, whereas a microphone input expects a very small signal collected from sound waves (unless the type of microphone used has a built-in amplifier). This is exactly the same as in RF: connecting a transmitter's output to a receiver's input is likely to destroy the receiver unless you attenuate.


**Impedance matching**: likely not a serious issue in itself since you are not trying to transfer power efficiently, but the impedance of the connected devices will affect the design of the attenuator.


**Isolation**: If your tone generator is battery-powered, this is not necessary. If it is powered by an AC adaptor or USB or some such, you will want to make sure you're not creating a ground loop with your transmitter; this usually takes the form of capacitors in series with the input and/or output lines. This may also be needed if the transmitter supplies DC bias power to the microphone (I don't know if this is common for amateur radio microphones, but some kinds of audio systems do this).

If you want advice on a specific circuit to build, you'll need to provide more information in your question:

- Specifications of transmitter microphone input (microphone type, impedance); may be found in the manual.
- Signal level of tone generator output.
- Impedance of tone generator output.
- Power source of tone generator.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2081/circuit-to-send-mcw-on-2m-fm, by Harry Weston, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
