# What's the pinout for "Kenwood" 2.5mm TRS/3.5 mm TRS connector?

*Tags: connectors, kenwood · score 25*

## Question

I've seen many Chinese HTs (Baofeng, Puxing, Wouxun, QuanSheng etc.) using the so-called "Kenwood connector", which has a 2.5 mm TRS connector and a 3.5 mm TRS connector. It looks something like this:

I've seen it used for serial ports, speakers, microphones, PTT devices and similar.

My question is: What's the exact pinout of this connector?

## Accepted answer (score 23, by captcha)

This is the one I use for my Baofeng UV-5R.

## Answer (score 17, by W8AWT)

Here is a Diagram from page 11 of The (Chinese) Radio Documentation Project's Baofeng UV-5R Manual PDF:

## Answer (score 5, by wpns)

FWIW: The Baofeng UV-5R HT supplies 3.3V through 100(*) ohms on the tip of the 3.5mm connector, not 5V as documented above. Also, the PTT is pulled up thru 10K to 3.3V, and the MIC+ connection line also has a more complex (constant current source?) pullup to 3.3V. [This is nice, as the PTT line can directly connect to a Raspberry Pi GPIO pin!]

There's a (wrong in several places, but you can get the idea of the general functions) schematic at http://static2.rigreference.com/manuals/baofeng/baofeng-uv5r-circuit-diagram.pdf

(*) Correction! The schematic says it's a 100 ohm pullup, one radio measured 10K and the other measured 100K, so it's anyone's guess what a particular radio might have installed. I'm going to mark this pin as "Not Useful".

Further study shows a DC bias of about half the battery voltage across the speaker due to the external speaker being connected to only half of the bridged output amplifier, so you might want to use a DC blocking capacitor.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1891/what-s-the-pinout-for-kenwood-2-5mm-trs-3-5-mm-trs-connector, by AndrejaKo, captcha, W8AWT, wpns. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
