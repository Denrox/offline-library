# Globar resistor repair or alternative(s)?

*Tags: receiver, repair, components · score 3*

## Question

I am restoring a Hallicrafters S-120 receiver and when trying to unsolder the wires, from the electrolytic capacitor, I noticed that one of the terminals of the Globar resistor (880-100 Ohm / 023-00327) was loose. Common soldering practices to resolder the lead were unsuccessful. Question: is there a way to fix the Globar resistor? Any ideas (including alternatives) will be greatly appreciated. Thank you.

May, 09 added picture (click image to expand)

@W5VO As explained before, I opted for the "2 resistors + switch" but instead of a switch, I will be using a simple circuit to circumvent the flaw mentioned in the last paragraph of your proposed solution. The 12VDC will be derived, from a point after the power-on switch, by means of a rectifier, resistor, and electrolytic capacitor, Thanks for your support.

Acknowledgment: http://www.bowdenshobbycircuits.info/page2.htm#delay.gif

## Accepted answer (score 4, by W5VO)

This is an Inrush Current Limiter (ICL). You can still get them today, but they look quite a bit different. See Digikey for a wide range of parts. Typically, these are used for reducing the inrush current of main power supply capacitors instead of filament protection, so they're optimized a bit differently. https://www.digikey.com/en/products/filter/inrush-current-limiters-icl/151

What you would need to know to design this circuit is how much current it normally draws, the starting resistance, and the ending resistance. There's a bit of experimentation I think you would want to do in order to make sure the circuit is working right.

Taking a look at an example higher starting resistance ICL part here, you could put 3-4x 220Ω ICL parts in series to get your starting resistance. When they get up to temperature, their resistance drops to 2-5Ω, which is much lower than your ending resistance of 100Ω. To compensate, plan on putting a large power resistor in the 80-100Ω range in series with this mess.

They come in different current ratings and sizes, so I'd say get a few options to play around with. Neither the starting resistance or the final resistance are going to be *that* critical.

I would hate to have a manual inrush switch - I know I would forget to switch it from "Run" to "Start" at the end.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18437/globar-resistor-repair-or-alternative-s, by essential555, W5VO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
