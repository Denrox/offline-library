# When is it relevant to consider a trace as a RF transmission line

*Tags: impedance-matching, transmission-line · score 3*

## Question

I'm building a simple Greinacher based RF Power meter for the PMR band i.e 446MHz. I intend it to work as a confirmation device and not something really acurate.

The circuit is quite simple:  The led is for visual control if the system works well.

I have obtained the Following routing (without the LED):

From left to right: I have the input SMA, with a transmission line adapted to 50Ohms. Which goes into the C1 capacitor, then in the diodes, and then in the C3 capacitor.

Is it relevant to consider the trace between C1 and D1 and between D1 and C3 as transmission lines? They are short L < 4mm, for a wavelength of around 70cm. For the moment I have used the embedded calculator in kicad to find the dimensions of the transmission line used :

## Accepted answer (score 5, by Phil Frost - W8II)

The general rule of thumb is anything more than 1/10th the wavelength should be considered a transmission line. At 446 MHz, that's 67 mm.

Your circuit is much smaller than that, so there's not much point in worrying about the trace impedance.

Furthermore, everything right of the rectifier is DC. So moving the diode to be as close to possible to the RF connector will be a further improvement.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18546/when-is-it-relevant-to-consider-a-trace-as-a-rf-transmission-line, by Wireless Learning, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
