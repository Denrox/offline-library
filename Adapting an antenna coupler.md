# Adapting an antenna coupler

*Tags: transceiver, electronics, antenna-tuner, 20m-band · score 5*

## Question

I've built AA5TB's antenna coupler:

I left out C2 because I didn't understand why I would need it - why would I? It works fine without.

Unfortunately, when I started tuning for a 5W 20m transceiver, the LED was on all the time. I then measured with a multimeter the AC voltage over the LED, and tuned to its minimum, about 3.2V~. The maximum was about 4.2V~. I was thinking of changing R4 and/or R5 so that these extremes are a bit lower. Is that the right way to do this? I'm worried, because I'd say the resistance of the whole R4-R5-D2 circuit should be about 51 Ohm, like the other resistors. Or would adding C2 resolve this issue?

## Accepted answer (score 1, by Phil Frost - W8II)

C2 removes the AC component across the LED, and prevents the LED from being on when the antenna is matched to 50 ohms. You say the circuit works anyway -- probably at QRP levels it's not bright enough to see. I bet if you try it in a dark room, or with a higher power transmitter, you will see it.

Anyway, consider how this circuit works. Here's a simplified version which makes the antenna impedance more explicit, and lacks any sort of visible indicator:

This is a Wheatstone bridge. V1 is your transmitter, and the antenna is the resistor of unknown value ($R_{ant}$).

Think of it this way: $R_1$ and $R_3$ form a voltage divider, and $R_2$ and $R_{ant}$ form another.

D1, C1, and R5 make a peak detector. If $R_{ant} < R_3$, then on the positive cycle of V1, the voltage at A is greater than the voltage at B, and C1 charges through D1 to the peak difference.

If $R_{ant} > R_3$, then on the negative cycle of V1, the voltage at B is more negative than at A, and again C1 charges through D1.

But if $R_{ant} = R_3$ (50Ω, our target impedance), then there is no voltage between A and B, and so D1 can never be forward biased, and so C1 can have no voltage across it, except for a small AC component via R5. The time constant of C1 and R5 make a filter with a cutoff frequency of

$$ f_c = \frac{1}{2\pi R C} = \frac{1}{2 \pi (10\:\mathrm k\Omega) (10\:\mathrm{nF})} \approx 1600\:\mathrm{kHz} $$

This is so low far below the frequency of V1 that we can consider the AC component of the voltage across C1 to be zero. Instead, it appears across R5.

So now, look back to your circuit with the LED. It is connected across R5, which has some RF voltage across it all the time. When C1 is charged because the antenna isn't 50Ω then there is additionally some DC component, and it's really this DC component that we are interested in. Remember, a capacitor looks like a low impedance at higher frequencies, so by adding C2, you are effectively shunting any RF current around the LED, so that the LED sees only the DC component.

An alternate solution to this problem is to connect the LED across C1, like this:

For that matter, why bother with two diodes when you already have one? An LED doesn't make a great RF rectifier, but I bet it works well enough at HF in this application. In fact, with one less diode drop of voltage I bet it's even more sensitive. We don't really need the capacitor since an LED flickering at 14 MHz looks just the same:

Adjust the value of R4 to get the right LED brightness for your transmitter power.

One might ask why AA5TB's design is the way it is, and I'm guessing it's because that's how someone else did it, and the design was just copied with minor modifications. R4 and R5 together used to be a potentiometer. The arrangement of connected the LED to ground instead of point B (thus requiring C2) is probably because the LED used to be a meter. If you have a meter with a metal casing, and you are building this in a metal box, it may be easier to connect the meter to ground than to isolate it from the enclosure. With an LED you have no such restrictions.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2399/adapting-an-antenna-coupler, by Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
