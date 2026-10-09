# Impedance miss-match short vs long section?

*Tags: antenna-theory, impedance-matching · score 3*

## Question

Let's say there is a 50 Ohm transmission line coming from a transmitter, suddenly the transmission line is spliced into a 300 Ohm line. From what I've learned a partial reflection occurs at this point. After a few feet of the 300 Ohm line it turns back into 50 Ohm. I think there is another partial reflection here?

What difference does it make whether the miss-matched section is a few inches, versus a few feet, versus several wavelengths long? Example: At 200 MHz at 50 Ohm, 1 piece of 300 Ohm line that is 5cm in length, does that even have any effect? If yes, is it negligible compared to the same but with a 200cm piece of miss-matched line? It's a lot to ask sorry. I'm trying to understand the mechanics behind these reflections.

## Accepted answer (score 6, by tomnexus)

Hams usually send just one frequency down a transmission line (as opposed to say high speed data like HDMI). So it's much simpler to analyse *impedance* down the line, than look at the reflections. Trying to add up the effect of multiple reflections is very complicated in the time domain.

The Smith chart is the best way to do it intuitively.

In your example, if the 300 ohm section is a half wave long, or n half waves, then at that frequency the impedance remains 50 ohms. Or if you like, the two equal and opposite reflections cancel out.

If the 300 ohm section is a quarter wave long (or 1/4 + n/2), the 50 ohms is transformed into 1800 ohms.

5 cm is about $\lambda/30$ at 200 MHz, this is 1/7 of a quarter wave, so the effect will be small. In reflection thinking, the 50-to-300 reflection and the 300-to-50 reflection are nearly at the same time, and of course have opposite sign, so they almost cancel.

In the limit, as you know from basic experience, a very short length of mismatch, like a cable joint or cheap connector, has a very small effect.

For playing with the Smith chart, I recommend this site: https://www.will-kelsey.com/smith_chart/

Here is a Smith Chart showing your exact question. Amazing.

Draw the chart for the 300 ohm line with the 50 ohm load on one end. Mark the 50 ohm point, then simply follow a constant-VSWR circle around the centre (using a compass), until you reach the desired electrical angle (pi * 5 cm / 150 cm). This is the impedance at the end of the 300 ohm line.

52.2 + j 61.9 Ohms

Or about a 3:1 VSWR. So not that insignificant.

## Answer (score 2)

There is no short answer. The Smith chart is the best tool to find out what happens. Start from from the back (the load).

https://www.qsl.net/w2aew/youtube/Basics_of_Smith_Charts_W2AEW_2018.pdf

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20106/impedance-miss-match-short-vs-long-section, by AllYourBaseAreBelongToUs, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
