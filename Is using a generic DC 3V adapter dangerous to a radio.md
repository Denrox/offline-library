# Is using a generic DC 3V adapter dangerous to a radio?

*Tags: power-supply · score 3*

## Question

I have the mini Eton radio and it has a DC 3V port but I haven't been able to find the official plug. Is using a generic one safe? How do i know if I found the correct AC adapter? It goes through 2 AAA's in two days! So I definitely want an alternative power source but safety comes first.

## Answer (score 3, by rclocher3)

A new generic AC adapter that says 3 VDC with the correct plug and the correct polarity should be safe. Almost all 3 VDC adapters will have the correct polarity; if the polarity were wrong, then the radio probably just wouldn't work. The trickiest part about finding an AC adapter is usually getting the correct plug, because there is no standard plug for 3 VDC. Hopefully a local electronics store could help you find the correct AC adapter, if you bring the radio in.

## Answer (score 3, by Dick_Extra Class HAM)

The 3-volt plug that works with the Eton Mini portable reciever is the Philmore # 204. Its stated dimensions are 1.3mm I.D. and 3.5mm O.D. It works!

## Answer (score 2, by user3486184)

It looks as if the Eton Mini needs a 3 volt center-positive power supply. It's probably 3.8 mm OD, 1.4 mm ID barrel connector, but that's just a guess based on the half-inch depth specification of the radio:

Since it lasts you two days on two AAA batteries (probably 1000 mAh) you can probably get by with a minimum 0.1 A (100 mA) power supply. A little more would put you on the safe side, and 1000 mAh / 1 Ah would be overkill but sure to work.

Any generic power supply with the right connector, voltage, polarity and amperage will work. (Power supplies with higher amp ratings will also work, but beware of power supplies with higher volt ratings.) The adapter plug's connector outer shield will need to touch the metal on the inside edge of the socket connector on the radio, and the adapter's inner connector will need to make contact with the pin inside the socket's connector on the radio. Barrel connector sockets can accommodate plugs of slightly different/incorrect sizes in a pinch.

Anything that advertises itself as compatible should work fine - there's nothing fancy about the power supply.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6631/is-using-a-generic-dc-3v-adapter-dangerous-to-a-radio, by verve, rclocher3, Dick_Extra Class HAM, user3486184. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
