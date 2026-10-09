# Antenna tuning while receiving

*Tags: transceiver, antenna-tuner, equipment-operation · score 8*

## Question

I've built AA5TB's antenna coupler for a 5W 20m transceiver.

Tuning was kind of difficult because my transceiver has buttons for sending a dot and a dash, but no tuning mode, so I couldn't have the transmitter on permanently to tune easily. I had to tweak it a bit to make it do this. I also have a 7.017MHz calibrated transmitter. Would it be okay to put the transceiver in receive mode, on 14.034MHz, hold that calibrated transmitter close to the antenna, and tune until the signal is the loudest (or, until the LED doesn't light / the voltage measured over D2 is in its minimum)? So in other words: can I tune the antenna when not transmitting?

## Accepted answer (score 3, by Phil Frost - W8II)

You can tune by receiving, generally. When your antenna is tuned, then SWR losses are minimized. By reciprocity this minimizes receive losses also, so you can just listen to noise and tune for maximum received noise level. In fact, with more complicated tuners that have more adjustments, this is usually the first step so that you can be in the right ballpark and avoid subjecting your transmitter to a really horrible match.

Your proposed method of coupling another transmitter to this particular tuner has a couple of problems, though. Firstly, this device doesn't really measure SWR, but instead is an impedance bridge which determines if the antenna impedance is 50 ohms. See the [explanation of how the circuit works](Adapting%20an%20antenna%20coupler.md) in another question, and it should be obvious how this won't work without the transmitter.

Additionally, if you put your calibrated transmitter "very close" to the antenna, then it will be coupling to the antenna in the near field, which has significantly different characteristics than the far field, which is what you care about for radio communication.

Lastly, tuning is frequency dependent, so a 7.017MHz transmitter isn't of much help for tuning 14.034MHz. You could probably find a way to make your transmitter generate a 2nd harmonic and filter that out, and then you'd have 14.034MHz.

I have a much simpler idea: try increasing C1. If you increase it enough, it will be able to power D2 through the period between the dashes. You can also try increasing R4, which will make the LED less bright, but discharge C1 more slowly. To get an idea of the values you need, consider the time constant of R4 and C1, which you want to be on the order of the spacing between the dashes, which is around 60ms for 20 WPM. So:

$$ 1\:\mathrm k \Omega \cdot C_1 = 60\:\mathrm{ms} \\ C_1 \approx 60 \:\mu \mathrm F $$

The disadvantage of this modification is that the LED indicator will be less responsive to your adjustments.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2400/antenna-tuning-while-receiving, by Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
