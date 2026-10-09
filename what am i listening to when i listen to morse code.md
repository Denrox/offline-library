# what am i listening to when i listen to morse code?

*Tags: cw · score 3*

## Question

morse code signals are only carrier waves, right? so a transceiver transmits a 14 MHz wave, unmodulated, or nothing at all. but i can't hear 14 mhz.

i know my radio plays a 700 Hz "side tone" when i transmit (i think) but when i listen to others, the tone can change, so i don't think the tone is being generated locally.

so what am i hearing when i am listening to morse code?

## Accepted answer (score 3, by Phil Frost - W8II)

A CW receiver works by first tuning an oscillator to the dial frequency, minus the difference frequency. This is called the local oscillator or "LO". The LO is then mixed with the LO. The difference frequency is usually the same as the sidetone frequency, so the sidetone you hear when transmitting is at the same pitch as a properly tuned signal being received. It's typically between 400 and 700 Hz, and in most modern radios is configurable.

This mixing, with the appropriate filtering, has the effect of "shifting down" the RF in frequency, so for example a carrier at 14,000,000 Hz makes a tone at 700 Hz, and a carrier at 14,000,100 Hz makes a tone at 800 Hz.

This is identical in operation to USB, the only difference being CW mode usually has a narrower filter, and applies a fixed offset (in this example, 700 Hz) to the LO. This is why you can also hear CW transmissions in Morse code in USB mode, if you tune 700 Hz below them.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17679/what-am-i-listening-to-when-i-listen-to-morse-code, by SRoberts, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
