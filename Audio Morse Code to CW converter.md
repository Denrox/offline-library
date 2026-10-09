# Audio Morse Code to CW converter?

*Tags: cw, transmitter · score 3*

## Question

What kind of circuit can be constructed and/or could be used to convert audio containing Morse Code sounds (say from an old practice tape, or from computer generated audio) into key, switch or relay closures that can be connected to a generic simple CW transmitter's key input terminals to transmit that code?

## Answer (score 5, by AndrejaKo)

First, I'd start by separating the idea into smaller logical parts. I'd have an audio input section, a detection section that would test to see if we actually have a Morse code tone and a section that would trigger the output device.

In the input section, I'd place some sort of galvanic isolation that would separate the input jack from the part connected to the transmitter. A small audio transformer could be useful here. Also series capacitors for AC coupling would be a good idea.

In the detection part, I'd use a dual operational amplifier as the main device. I'd use one op-amp as a band-pass filter that would only select frequency range used on the tape and another wired as a comparator. There's a calculator for bandpass filters here. I'm not sure what level would be good for the comparator, so I'd experiment here or maybe even use two fixed resistors and a potentiometer to set sensitivity level.

The output from the comparator would go into the section that would drive the relay. Here's a tutorial on how to connect a MOSFET as a switch. The relay would then key the transmitter. For the diodes, I'd use Schottky type

Here's a rough sketch of the circuit:  
Ucc would whatever voltage is available and can trigger a relay. Op-amp probably wouldn't matter too much, but it would need to work at the voltage used for relay. Some tweaking will probably be needed in case relay noise upsets the op-amps. Also tweaking the gain of the OP1 circuit might be helpful, depending on the input signal level.

A program like Audacity can be used to get the frequency of the Morse code tones for band-pass filter design. One more consideration is the relay used. It should be rated for large number of switches, so perhaps a reed relay could be used here.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1602/audio-morse-code-to-cw-converter, by hotpaw2, AndrejaKo. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
