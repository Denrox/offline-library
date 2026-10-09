# Can Yaesu FT-65 be charged from a 12 VDC automotive accessory outlet?

*Tags: ht, mobile, yaesu, equipment-protection · score 3*

## Question

I recently purchased a Yaesu FT-65 handheld radio and quickly discovered it had no 12 VDC power port like other handheld radios I've seen. The charging cradle uses a 12 VDC wall wart for power, and the radio sits in the cradle to charge, there's no power input port on the radio itself. At least I couldn't find one. I went looking for a cable to plug the charging cradle into an automotive accessory power outlet, AKA cigarette lighter, from the manufacturer and found none. The manual makes no mention of this as an option. I contacted Yaesu using their website and didn't get a response, not yet anyway. This leads me to think that I should not attempt to make a cable to connect the charger base to an automotive accessory port, at least not without some voltage regulation.

Just how sensitive is the Yaesu FT-65 charging cradle to voltage variation from the 12 volts specified? It's typical for Amateur radio gear to be able to take in a fairly wide range, such as the 11.5 to 15 volts seen from a healthy automotive battery that's under load and while charging. I'd like to be able to charge the radio while traveling from an automotive accessory port but not damage anything while doing so.

Anyone know what voltage range the Yaesu FT-65 charging cradle will safely take? Is there a third party adapter for this that will regulate the voltage from an automotive accessory outlet to a "clean" 12 volts?

## Answer (score 2, by Zeiss Ikon)

The battery inside the radio is almost certainly a lithium-ion type (one to three cells, most likely one or two), which requires the device to manage its charge (for safety, as well as for battery cycle life purposes). That means that not only is there most likely some regulation in the charging cradle (even if the cable from the wall wart is DC -- and it might well be 12VAC), but the radio itself is managing the charge going to the actual battery.

All that to say that if the wall wart is marked with output of 12.0 V DC, it should be fine to make up a cable with the correct polarity to connect to your vehicle 12V outlet.

There are also various "universal" power supplies that run on 12V outlet power and produce (more or less) regulated output at various user selectable voltages -- and generally also include an assortment of connectors. You'll usually find these at auto parts stores, in my experience (I've bought them at Radio Shack, but that's been a while). Select the correct voltage, match the polarity (should show on either the cradle or wall wart), plug and go.

From comments, "Looking at the bottom of the cradle it lists the input as simply 12 VDC @ 1 A, and output as 8.4 VDC @ 800 mA." First, that output voltage strongly implies a 2-cell battery. Second, the voltage difference from input to output says there's almost certainly a regulator in the cradle.

Now the question becomes whether the cradle can handle an input variation of 10-ish V during start up to peaks of 14.6V, depending how your vehicle handles voltage regulation. If the components are particularly lightweight (as they might be if the wall wart is itself regulated), it's possible it may drop out during a start (not a big deal, generally, when powering a battery device), or burn out a component on a peak of 14.6V (more likely to occur if the device is drawing near maximum to charge a deeply discharged battery).

One possible way to deal with Yaesu's intransigence on what you can plug the cradle into would be to purchase a small inverter to run on your vehicle's 12V outlet, to give 120VAC to power the cradle's wall wart. For the low draw you need, these can be had for around $20 at parts stores, and might well be the easy way out for this situation.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16194/can-yaesu-ft-65-be-charged-from-a-12-vdc-automotive-accessory-outlet, by MacGuffin, Zeiss Ikon. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
