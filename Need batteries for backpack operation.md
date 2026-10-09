# Need batteries for backpack operation

*Tags: transceiver, mobile, dc-power, portable · score 4*

## Question

I am building an HF backpack rig using an Icom IC-706MkIIG with a Opek HVT-400B antenna. The specifications on the radio say 20 A draw at high power, so what size and type batteries would be suitable for a backpack operation?

## Answer (score 6, by hjf)

I used LiFePO4 (read: Lithium Iron Phosphate) for my dad's FT-891. The big advantages of LiFePo4 are:

- Very power dense, almost as much as Li-Ion, IIRC twice as much Wh/kg than Lead-acid
- Extremely safe: they don't short circuit themselves to flames, like Li-Ion does
- Flat voltage discharge characteristics: their nominal voltage is 3.2V and they stay at 3.2V until they suddenly start dropping.
- Handles overcharging much better than Li-Ion: will not be damaged or catch fire from overchariging.

Disadvantages are:

- Rarer than Li-Ion.
- Current limited by chemistry

A series of 4 3.2V give you a convenient 12.8V. You actually need to charge to 3.65V per cell, 14.6V total. But don't worry, after you remove the battery from the charger, the voltage will drop to 12.8V.

The current limit is irrelevant for 100W operation since you will be pulling 20A max. I got cells for 30A discharge current and put two in parallel. Works just fine.

I bought mine from Aliexpress from a chinese supplier that makes them into nice rectangular shapes. Very easy to make a pack.

I used 8 3.2 10Ah batteries, connected as 4S2P, that is, two parallel packs of 4 battery series. From the same seller you need to also buy a BMS, which is a charge controller that will keep them balanced.

In our experience, the battery lasts a very respectable 2-4 hours of 100W SSB ragchewing. My dad goes mobile on weekends and his pack lasts him for the weekend. Unlike the car battery, the voltage stays constant. Often my dad has to start the engine to recharge the battery after half an hour of operation. The LiFePO4 stays rock solid at 12.8V, and unlike the car battery, the voltage does NOT drop when you PTT.

I can provide links to the Ali seller I got them from, if you want. But if you're in the USA I suppose there are US sellers available. Don't be fooled by the high prices of other LiFePO4 packs you'll see. Those are giant batteries for use with solar systems at home (they're safe enough that they will not set your house on fire).

## Answer (score 3)

Sealed lead acid batteries are heavy. I would not recommend them. lithium phosphate or lipo are lighter, but can be hazardous. in case of physical damage to the battery they can burst into flames or even explode. Lithium Iron Phosphate batteries are also light weight and are much safer.

Bioenno is a well known battery vendor that has a wide selection of batteries and have several designed for HAM radio operators that even come with Anderson Power Pole connectors.

Like most good backpacking gear they can be expensive.

you also might want to look at a portable solar panel to supplement the battery. the solar panel will not provide enough current to run the radio during transmit, but it can extend the battery especially if you are just receiving.

I also agree with rclocher3, the radio and antenna you have listed are not the best for backpacking. there are lighter radio and more effective antennas. I admit I like ICOM and I have been waiting for the ICOM 705 to become available in the USA. I also like end fed half wave antennas. They are multiband and only require a single wire and matching transformer.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16506/need-batteries-for-backpack-operation, by Steven Donnell KG5GRI, hjf. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
