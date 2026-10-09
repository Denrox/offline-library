# Will I harm batteries by only trickle charging them, or connecting them to a power supply?

*Tags: diy, battery · score 3*

## Question

I have some 12V, 12Ah Enercell batteries from RadioShack, RS part number 2301219. As far as I can tell these are AGM SLA batteries.

I picked up this 3-stage charger from Harbor Freight and as far as I can tell it's charging the batteries (which were probably on the shelf for years and not touched).

The goal is to build a portable 12V (and hopefully 36Ah) battery box. I've wired the batteries in parallel:

The batteries need 14.5-14.9V (max 3.6A) for "normal charging" and 13.6-13.8V (max 1.8A) for "trickle charging". The packaging says not to use automotive or marine chargers. So for single batteries, the only thing I've found has been something like this charger from PowerStream.

Will I harm these batteries by only charging them on a trickle charger? If I hook these up to my 15A MFJ power supply for a short period of time, would that hurt these batteries?

## Accepted answer (score 2, by Vince Mulhollon)

You're not getting answers for multiple reasons.

1) Batteries are a science but its surrounded by marketing and astrological tradition (concrete floors, blah blah)

2) If something bad happens they are destroyed or blow up the house or start a fire and no one wants to get involved in that mess. I guess I'm just crazy.

3) You're using stuff from mainland China, not exactly legendary for reliability. So the charger you have is spec'd by its manual which I downloaded and read, to output never higher than 13.2 volts to float... and from http://www.powerstream.com/SLA.htm its impossible to outgas explosive hydrogen unless the voltage at room temp (it varies with temp) is around 14.5 volts, so all good there, and most SLA recombinators won't vent until about C/3 charge rate and your Chinese charger theoretically only outputs 0.75 amp so its safe on any battery larger than about 3 amphours and you're at 36. So you've got a factor of safety of more than a volt and over ten times the capacity, so IF it works to it's written specs, THEN you're totally safe. At 3/4 amp rate, and 36 theoretical aH capacity, thats going to take more than two days to charge a completely dead battery, but it'll get there eventually.

The most effective way to kill a SLA is over volt it causing plate corrosion, and cheap 1970s car chargers don't voltage limit because flooded cell batteries from 1970 can have distilled water added when they outgas (unlike a SLA). So the battery mfgr covers all bases by saying "don't use a car charger" But per the specs your modern trickle charger even worst case should be very safe if you compare it to typical SLA battery mfgr specs.

With no current limiting directly wiring the MFJ supply would just try to supply like 100 amps and blow a fuse if the battery is low. If it doesn't blow a fuse and you do draw 15 amps (which it won't, for reasons beyond this discussion) then thats about C/2 charge rate and the recombinators in SLAs are usually rated to handle C/3 (optimistically) so you'll pop the vent and leak some acid and get to buy new batteries, which is annoying. In summary, no, don't wire it directly to a power supply without some kind of circuitry in between, like a charger or charge controller type gadget.

The powerstream charger looks awesome and would make a great charger.

In other news "which were probably on the shelf for years and not touched" lead acid cells die by abuse (not a problem here) cycles (not a problem) or old age (oh oh thats a problem). You only get "less than a decade" starting the instant acid hits lead back in the factory. Just saying if it sat on the shelf for five years already, they don't really have that long to live anymore. So on one hand if they die "soon" it's probably not your fault, and on the other hand if you do something bad to them they were going to the recycler soon enough anyway so you've not got much to lose.

Anyway 73, best of luck, de N9NFB K

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/3627/will-i-harm-batteries-by-only-trickle-charging-them-or-connecting-them-to-a-po, by nvahalik, Vince Mulhollon. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
