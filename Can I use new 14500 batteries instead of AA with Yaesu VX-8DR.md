# Can I use new 14500 batteries instead of AA with Yaesu VX-8DR?

*Tags: yaesu, battery · score 7*

## Question

In addition to the proprietary battery, that came with my radio, I also purchased the part allowing usage of three AA-batteries. That was about 10 years ago, before the appearance (and wide availability) of the 14500 standard.

Simply replacing AAs with 14500s *seems* crazy -- instead of the 4.5V provided by three sequential AAs, the three 14500s in sequence will measure 10.8V!..

However, according to the manual, the DC-plug must be used with voltage ranging from 7.5V to 12V, so, maybe, the device really can handle the much higher voltage fine -- and the reason the manufacturer didn't provide room for more batteries is simply that they wanted the unit to remain *small*?

*Update*: got the following reply from Yaesu tech-support:

It is not recommended to use Lithium-Ion AA in the FBA-39 only use Alkaline, the internal resistance is too high inside consumer Lithium-Ion batteries.

What does "internal resistance" mean? Did they understand my question, or just reacted with a pre-canned reply to anything mentioning "Lithium"?

*Update*: according to the service manual, supply voltages are:

- Nominal:  7.4 V DC (Negative Ground)
- Operating:  4-14 V DC (Negative Ground, EXT DC jack)
- Operating with Charging:  11-14 V DC (Negative Ground, EXT DC jack)

## Answer (score 5, by rclocher3)

The email from Yaesu's tech support was probably talking about non-rechargeable 1.5 V lithium (not lithium-ion) AA batteries, rather than rechargeable lithium-ion batteries with a nominal voltage of 3.6–3.8 V. (Apparently at least one company makes rechargeable lithium-ion AA batteries with an output voltage of 1.5 V that charge from a USB cable plugged into the side. I would guess that these batteries are really 3.6 V lithium-ion batteries that include a voltage regulator inside the AA-sized package to reduce the output voltage to 1.5 V. I don't think that tech support was talking about this type of battery.)

All batteries have an internal resistance, which reduces the terminal voltage (and therefore also the delivered power) when a high current flows through the battery. The internal resistance limits the current that can be delivered by a battery pack. The internal resistance of different battery types is a specification that designers of battery-powered devices need to plan around, but that ordinary consumers can ignore.

The VX-8DR could have been designed to use power from the internal battery pack in the same way as external power, or the power from the battery could go through a separate circuit with a different voltage regulator. Ideally the voltage and current expectations of the internal battery pack would be clearly laid out in the specifications, but to save space in the manual the specifications probably only state the battery types that were known to work at the time the radio was designed, so the specifications probably are no help. The only way to find out for sure, besides testing the radio the hard way, would be to look at the radio's schematic and the specification sheets of various ICs that are used. The radio's schematic can probably be found in the radio's service manual.

EDIT: I downloaded the service manual, and the block diagram shows that the current from the internal battery pack doesn't pass through a voltage regulator like the current from the DC jack. There is no exact schematic with every part in the radio, just the block diagram, which does show that the final amplifier is a 2SK2476 MOSFET made by Toshiba. The 2SK2476's data sheet says that it can be driven with a drain-source voltage as high as 20 V. I would think that the final amplifier is driven by battery voltage directly, but I've never experimented with MOSFET amplifier circuits, so I'm not sure about that.

There's also an NJU7231F30 voltage regulator that converts the battery voltage to 3 V. That part is rated for a maximum of 18 V input.

I would think that applying 10.8 V to the battery terminals instead of 4.5 V wouldn't hurt anything in receive mode. However I'd think that you'd run the risk that a higher battery voltage would drive the 2SK2476 final to produce too much power, overheat, and cook itself. Unfortunately I have no way of judging how likely that outcome might be. If you had test equipment, you could connect a variable-voltage power supply to the battery terminals, transmit momentarily, and measure the output power. Then you could gradually raise the input voltage and see what happens to the output power; if the output power went higher than the specified maximum, then I'd say you'd run a high risk of damaging the device. If the output power stays about the same, then you your plan of substituting the 14500 series lithium-ion batteries for the AAs that the radio expects might work.

## Answer (score 3, by David Hoelzer)

This would very much depend on how the device is wired internally. Is it possible that this will work? Yes. Is it possible that you can destroy your device? Yes. The current that can be delivered by those 14500s is significantly higher than you will get out of three AAs. You would need to carefully examine how the device is wired, if (and where) current limiting circuitry is present, what voltage regulation is present, etc.

Update:

I've looked over the service manual that you linked. Yes, if you don't want to buy the correct replacement battery for $30-40, you could create your own using 14500s. You should be mindful that building your on Lion battery pack is *very, very risky*, especially if you are thinking that you will solder leads to one or both of the batteries. Under no circumstances should you apply heat to these cells, ever.

Given what I perceive to be substantial risk, especially since you weren't sure how to figure out if these could be used based on the service manual (this isn't a criticism, so please don't hear it that way), I'm not inclined to offer any additional assistance that might lead to you blowing up one of the cells. :)

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20312/can-i-use-new-14500-batteries-instead-of-aa-with-yaesu-vx-8dr, by Mikhail T., rclocher3, David Hoelzer. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
