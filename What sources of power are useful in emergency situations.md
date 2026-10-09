# What sources of power are useful in emergency situations?

*Tags: emergency, power-supply, dc-power · score 10*

## Question

Situations that call for emergency operating usually have some hams working in field conditions.

Relying on the mains grid could be problematic. A lead-acid battery would probably be heavy to lug around should the operator need to relocate in a hurry. The same could be argued for a generator.

Under emergency conditions, what kind(s) of source(s) of power would be available and useful to an amateur radio operator?

## Answer (score 4, by Ron J. KD2EQS)

The most convenient power source would in fact be the lead-acid battery. However, not carried by hand, but in a vehicle. This provides an easy source of recharging power (just start the car), mobility to quickly relocate (driving), and the lead acid battery does have enough amperage to power most field radios (100 W+). As a lighter alternative, a Lithium battery pack may be a QRP solution, but the weight would be almost comparable to a lead acid for greater power levels. As a heavier alternative, a portable (gasoline) generator along with sufficient fuel may be plausible if many hands are available to carry equipment.

## Answer (score 3, by guitarpicva)

This is sort of an "it depends" question, and you noted that yourself in your text I believe. It will take some Q & A with yourself to come to a conclusion.

First: What is the "field" situation.

a. A literal field?

b. The side of the road?

c. A shelter in place situation with no grid mains?

d. Pure mobile/portable on the move?

Second: Based on "First", one decides what is then appropriate, and whether the situation may be fluid and require "oozing" from one situation to another.

a. A literal field: Photo-voltaic panel(s) with integrated charge controller to an appropriate battery. AGM batteries offer the capacity of a lead acid with less weight and less maintenance and less chance of losing your battery due to a tip over where you might lose the fluid. They also don't emit gasses like wet lead acid (more important for c.).

b. The side of the road: A mobile set-up with a PV charging backup is ideal, because you can run the engine if you really need to, but can choose to recharge the vehicle battery with the PV. Not ideal because the vehicle battery is not deep cycle, and you run the risk of stranding yourself until you get enough sun to let her crank again. Having a second battery, and a deep cycle one either installed with vehicle charging or carried with PV charging is a good move.

c. A shelter in place situation: This allows you to plan this all out in advance. A generator is a perfect companion to the deep cycle battery(ies) and the PV charging. Fuel-sipping, quiet, 2kW Honda generators can run for 8 hours or more on a gallon of gasoline, particularly with a low overall load.

d. Pure mobile/portable: Pretty much b. above, but if constantly changing position, mobile operation within the vehicle and it's battery makes the most sense, just so long as fuel is abundant, thus your "solution" is carrying fuel, vs. carrying batteries, PV's, etc.

This is truly one of those never-ending answers, and I guess there isn't really any sort of truly lightweight power to be had. Battery technologies improve in size, weight and capacity regularly.

If I were to be forced to choose only one technology, it would be PV and AGM (or Lithium Ion) deep cycle batteries. None of the answers are terribly convenient, but as long as you have sunshine, you can use the radio.

Third: Operating requirements/types.

a. Repeater ops that can be done with hand-helds or low power mobiles?

b. Simplex ops with HF?

These are the two major methodologies that Hams have used for decades. Using the least power to accomplish the "mission" is your task in this discussion.

Repeater ops make it easy as they are typically very low power, and if you are using ONE repeater, then the antenna is as (or more) important than the power source (and a gain antenna sort of IS a power source).

Simplex HF ops are more challenging, but one can usually move more information further, per hop, thus using potentially less power. The best of the QRP capable HF mobile/portable rigs like the Yaesus are incredibly flexible when coupled with the right software and perhaps a simple Signalink.

While this consideration doesn't speak directly to a power source, I think it certainly colors the decision making process. You could work all day and half the night with one AGM battery in repeater ops. It might require two or three for HF ops.

## Answer (score 3, by MicroservicesOnDDD)

When they installed solar on my house, I lamented how Hurricane Sandy came, and yet all of the people having solar on their house could not use it because of the anti-islanding law(s) which say that your solar system, which usually pumps its excess power into the grid, must not do so when the grid is down, to prevent from electrocuting electric company personnel working on the lines.

I lamented how all of that solar power was on their roofs, and yet they couldn't use it. The guy installing my solar system actually listened to me, and found another way!

I have an SMA inverter (Sunny Boy, I think), and this particular model of SMA inverter comes with (or allows) an outlet that attaches directly to the inverter, and from which you can extract power if the grid is down -- potentially running your refrigerator long enough to preserve your food, and of course it should deliver enough power to run many ham setups. And to charge one or more lead-acid batteries -- I bought the biggest marine battery I could find.

The key to this setup is that, when the grid is down, the inverter does not supply AC power to the house, and therefore does not violate the anti-islanding law that protects electrician linemen. But the inverter **does** still supply power directly to the two outlets directly attached to the box. An extension cord allows you to bring it to what needs it. I will try to bring more specific information back later about which specific Sunny Boy I have, and what the attachment is, because I spent some time on the SMA America site to try to find the outlet attachment and couldn't find it.

EDIT: I just had an opportunity to use the outlet. When the grid is down and I'm extracting power through the special attached outlets, it displays a message "P: nnnnW SPS-mode active" where nnnnW is how many watts is being delivered. I was using a heat gun with lots of settings to extract power, slowly increasing the wattage until it finally choked. In the storm, because of cloudiness, the power that I was able to extract ranged from about 1,000W all the way down to about 200W (dark like twilight). When you draw more power than can be delivered, the inverter cycles on and off (on for short times) and the inverter keeps turning back on to try to deliver what you're asking of it. I did not get the opportunity to test it under full sun. We have 20 panels. Inverter (utility interactive 1-phase) is Sunny Boy Model "SB5.0-1SP-US-40" mfd. 9-2016.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/891/what-sources-of-power-are-useful-in-emergency-situations, by VU2NHW, Ron J. KD2EQS, guitarpicva, MicroservicesOnDDD. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
