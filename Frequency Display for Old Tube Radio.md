# Frequency Display for Old Tube Radio

*Tags: receiver, diy, vacuum-tubes, superheterodyne, modification · score 4*

## Question

I have a Hallicrafters S-120 1960s vintage vacuum tube receiver (an "All American Five" superhet with solid state rectifier replacing one of the "five" tubes). It works well, doesn't have excessive internal noise, and seems very sensitive (with the regenerating IF used for "exalted carrier" on AM, and as a BFO for CW and SSB).

I've considered using this as a secondary receiver, for some version of "split" operation.

The problem with that is that, while the tuning is plenty precise (with the Bandspread control allowing several turns of a secondary tuning knob to cover a few hundred kilohertz), the tuning indicator needle is significantly off the actual tuned frequency (correctable) and doesn't move at all when using the Bandspread. I had the idea to connect a digital frequency display, which would allow me to see exactly where I'm tuned. I have such a display on hand, built from a kit.

The only place I see to get current tuned frequency from a superhet receiver is to tap into the local oscillator. Am I correct in thinking this will give a frequency 455 KHz *below* the actual tuned frequency?

## Accepted answer (score 5, by Kevin Reid AG6YO)

Yes, attaching a general-purpose frequency counter to the local oscillator of a superheterodyne radio will result in displaying a frequency with an **offset** either above or below (depending on the design of the radio) the nominal frequency of the signal being received.

In order to account for this, apply the reverse offset numerically, between the frequency counter and its digit display.

This may or may not be practical with the counter module you already have.

- A frequency counter intended for the purpose should have a programmable offset.
- If it is microcontroller-based and has open source firmware then you could reprogram it (this may or may not require special programming hardware and software).
- If it is based on discrete logic, then the circuit could be modified to include an adder/subtractor and the offset programmed using wiring or switches.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/14944/frequency-display-for-old-tube-radio, by Zeiss Ikon, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
