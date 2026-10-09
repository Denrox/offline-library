# Can I have the Hytera PD785G turned on in the charger?

*Tags: safety, battery-charging, hytera · score 3*

## Question

I have a Hytera PD785G. Typically, I charge it overnight, then take it out and use it.

Since this is currently my only radio station, I'd like to misuse it as a stationary device. Most of the time, I'm just listening and waiting for calls. For making a call, I'd then take it out of the charger.

I have looked up the User Guide, which says (emphasis mine)

Charging the Battery

Caution:

● **Make sure the radio is powered off before charging.** Read the Safety Information Booklet in advance to get necessary safety information.

● To achieve optimal battery performance, please charge the battery for at least 5 hours before initial use.

Please use the charger specified by the Company to charge the battery. Charging Diagram is listed below.

This lets me assume, I cannot simply put it into the charger. Is there some acessoire that would let me use it in a more stationary way?

## Answer (score 5, by Marcus Müller)

Never owned a similar device, but judging from the product pictures:

Indeed, the charging logic for the battery is not inside the handset, but the charging cradle, and hence, that would quite likely be confused should you transmit while charging, as that looks like a sudden drop in battery voltage.

So, the other option is what Hytera sells as "Battery Eliminator", which has the shape and handset contacts that a battery has, but is actually nothing but a step-down voltage converter giving you something in the range of 7.4 V, plus probably just a resistor to emulate the temperature sensor of the battery pack.

If it's that easy, you can either buy the Hytera battery eliminator, and attach the cigarrette lighter plug to a 12V supply, or you can zurechtbastel something that just happens to have contacts in the right places:

Check the number of contacts on the device side of the battery.

- 2 only: simplest case, you just need to connect a 7.4 V power supply to these (watch polarity)
- 3 or 4: there's a sensor to measure the battery temperature built in to the battery pack, and your handheld *might* check that to make sure the battery isn't overheating.

In that case: you need to emulate that sensor:

Verify which pins are the positive and negative contact with a multimeter.

Measure whether there's a voltage between the other two (4 contacts), or between the third and the negative contact. If that's the case, it's a thermocouple. If no reasonable voltage is found:

put the battery in the fridge, measure the resistance between the two contacts that aren't + and -. Let it warm up (sun, heating, body warmth!), and compare. If it drastically changes, yep, there's a thermistor attached here, and you might need to emulate that so that the handset doesn't think the battery is overheating.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16780/can-i-have-the-hytera-pd785g-turned-on-in-the-charger, by Thomas W., Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
