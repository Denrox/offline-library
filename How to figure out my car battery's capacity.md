# How to figure out my car battery's capacity?

*Tags: mobile, power-supply, battery, portable · score 3*

## Question

I was participating in an emergency radio training and I was asked how long I could operate.

I'm using an old car battery, which was sometimes not capable of starting the car in winter, which is why I have it. It has a nominal capacity of 45Ah.

Is there a good way to find out its real remaining capacity except draining it by a known current and measuring time?

## Accepted answer (score 5, by Gil)

There are many ways to do this. My favorite and I would assume you have these items in your shack. Most inverters have an automatic low-voltage disconnect feature. It makes a beeping sound and stops putting out 110AC when the battery voltage drops below 11 volts or so. You have probably encountered this feature while using your inverter. You connect a load to the inverter (light bulbs work great) and an electric clock (I start at 12:00) to determine how long it runs. When the inverter quits the clock will tell you how long it ran. If you have a 24 hour electric clock it would would be perfect for this however a 12 hour will work just as good. A 60 watt light bulb makes my inverter draw about 5 amps from the battery. Using your favorite math formula from OHM: Watts = Volts * Amps. 60 watts = 12 volts * 5 Amps. 5 Amps = 60 Watts / 12 Volts to be sure, check the current and voltage with your meter(s).

## Answer (score 2, by natevw - AF7TB)

Is there a good way to find out [a battery's] real remaining capacity except draining it by a known current and measuring time?

While I'm curious to this myself and would love to see other answers, my guess is that applying a known load and seeing how it responds is the most reliable way.

In fact a "battery load tester" is a fairly common tool used by auto mechanics when evaluating the health of a battery. You may be able to borrow a simple one from an auto parts store. It's essentially just a dummy load and meter and you'll still have to extrapolate from the voltage under load to an estimate of health/capacity.

Your parts store or auto mechanic may also have a fancier "battery analyzer" or "intelligent battery tester" that does an actual discharge test for you and can display a report when it's done.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18529/how-to-figure-out-my-car-battery-s-capacity, by Thomas W., Gil, natevw - AF7TB. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
