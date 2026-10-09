# Bonding ground rods for lighting protection

*Tags: grounding, lightning · score 3*

## Question

I am installing 2 antenna masts on one end of my house. The utility ground is on the far end of the house, and was buried under the asphalt driveway.

Working with my electrician, he suggests 2 ground rods by the 2 masts and 2 ground rods at the entry point for the coax to the house. the rods in the 2 groups will be spaced at least 8' apart.

The antennas will be ~60' from the house and the utility ground and the 2 new grounds by the house will be ~80' apart.

Because of the distance, and being under the driveway, bonding the 2 sets of grounding rods together will be difficult. It would end up being approx 200' of wire to get around the house and then digging a trench in the driveway to find the ground rod, and then fixing the driveway.

What are the consequences of not bonding the new rods with the existing ground rod? Is there something else I can do to mitigate the issues?

## Accepted answer (score 6, by hobbs - KC2G)

Consequence 1: it's not up to code. A contractor shouldn't do it that way, and if you do it yourself, it might make it difficult for you to sell your house (if you don't take everything down beforehand), or make it difficult for you to recover from insurance if anything *happens* to your house. Worst case, your house burns down from a lightning strike and you end up with no house, no shack, and no money.

Consequence 2: ground potential rise. When there's a lightning strike nearby, the potential of "ground" at two points a few hundred feet apart can differ briefly by hundreds or thousands of volts. If your ground rods are bonded the way that they should be, the current that equalizes that voltage difference will mostly flow through the bonding conductors. If they aren't, then it will flow through any *other* path it can find, i.e. from the tower ground to your coax, from the coax to the chassis of your radio, from the chassis of the radio to the power supply ground, and from there to your utility grounding rod. This is bad because it goes through your radio, but it's also bad because it goes through your house, and you don't *want* it to go through your house.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/22194/bonding-ground-rods-for-lighting-protection, by mbond, hobbs - KC2G. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
