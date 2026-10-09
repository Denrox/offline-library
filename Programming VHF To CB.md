# Programming VHF To CB

*Tags: vhf, citizens-band, radio-programming · score 3*

## Question

New to this particular site on StackExchange and new to amateur radio period so bear with me:

I'm looking into buying a VHF radio for work related purposes. More specifically the Icom IC-2300H.

I've been wondering if it was possible to program a VHF radio to run on CB radio frequencies?

I've done some searching but didn't find anything on the topic, but I may not be using the correct keywords.

I'm not familiar with the various radio frequencies and types.

I'm not looking to specifically use this radio for the purpose of cb, but just the possibility of.

## Accepted answer (score 3, by Kevin Reid AG6YO)

CB or its close relatives fall into the HF frequency range (covering somewhere around 26 to 28 MHz, depending on country), so anything that accurately calls itself a VHF radio will not transmit (and most likely will not receive) CB.

In general, what you do to answer this kind of question is find the radio's *specifications* — either on the web site or in the user's manual which will often be available as a PDF — and look for the transmit and receive frequency ranges. You can see that this radio's lowest receive frequency is 136 MHz, somewhat below the low end of the 2-meter amateur band. Therefore it cannot receive or transmit on CB frequencies.

(Another issue is whether it supports the relevant modulation, or *mode* — which in this case is also a problem, because this radio supports only FM whereas CB is conventionally AM and sometimes SSB.)

You also cannot use this radio “for work related purposes” unless you are intending to receive only and not transmit. This is because it will only transmit on the amateur bands, where any use for which you receive compensation is prohibited. Outside the amateur bands, all other frequencies you might legitimately use in the US (I see your location from your profile) require “certified” (formerly “type accepted”) equipment, which in practice means equipment that transmits on that band or frequency *only*.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6679/programming-vhf-to-cb, by Jesse Elser, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
