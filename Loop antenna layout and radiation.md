# Loop antenna layout and radiation?

*Tags: antenna-construction, hf, propagation, wire-antenna, loop-antenna · score 5*

## Question

I've got, for the near term, limited resources to put up an HF antenna at my home. One of the options I can manage without excessive cost is a loop, which would enclose the house. I need to transmit on 80m, and likely up to 20m (I understand loops are very tolerant of shorter wavelengths). It wouldn't be as high as I'd like, so would probably perform more like an NVIS, with poor horizontal radiation (given I live in a draw, that's not entirely a bad thing, as less of my energy will go into the ground where it rises).

The only thing is, the space I have pretty much requires the loop to enclose the house, if I'm to avoid entanglements in the dense pine/hardwood mix that covers more than half the lot. How will the steel roof (about 5x20 meters) affect the radiation of an 80m loop (probably hexagonal), mounted close to roof height (roundly 3 meters above ground)?

I'm not certain of the grounding status of the roof panels; it was applied by a "handyman" who seems to do no better work than is expected of him (that is, if you don't know it's wrong, he won't do it right), before I lived in the house.

Here's the property aerial view; the bright white roof with two extensions is mine. The property line follows the fence parallel with the driveway, the near edge of the line of trees next to the plowed field North of the house, and loops into the heavily treed area S and SSE (mix of pines and hardwoods, tangled branches, difficult to run wire into).

As requested in chat, here are photos of the trees that have reasonably open space nearby -- as noted, a mix of pines and hardwoods.

## Accepted answer (score 6, by Brian K1LI)

Summary: substantial advantage can be realized for every meter increase in the height of the loop. Other parameters, including the metal roof, are much weaker factors in performance.

I simulated a 3.8MHz 1-$\lambda$ hexagonal loop (no wire loss) mounted 3-m above medium-conductivity ground, surrounding a 5m x 20m grid of wires as shown here:

Because the loop is so close to the ground (in wavelengths), the 0.2-dBi maximum radiation occurs at the zenith.

dropping to -3-dBi at 45$^\circ$ elevation angle. The gain increases less than 0.25-dB when the wire grid is removed, a small change as expected from the low currents reported in the grid wires.

SWR calculations show that the "roof" does have a meaningful effect on the loop's characteristics:

Feeding the loop at the mid-point of a side parallel to the long edge of the "roof" gives somewhat better SWR than feeding the mid-point of one of the "angled" sides, so the loop must indeed be exciting meaningful current in the grid wires. It's possible that the slight gain decrease with the wire grid is due to ground losses, which would couple into the loop, lowering the Q and the efficiency of the antenna. Conversely, feeding at a corner of the loop has minimal impact on the SWR curve, regardless of the presence of the wire grid. The antenna's feedpoint impedance varies considerably as the band is changed; a wide-range antenna matching network will probably be required.

Raising the loop just 1 meter increases the gain at the zenith by 2dB. Another meter increase adds another 1.5dB. The gain at 45$^\circ$ elevation increases at about half the rate of the gain at the zenith.

At the request of another SE member, here are 3D plots that show how the pattern evolves as the frequency is successively doubled:

7.15MHz - maximum gain ~0dBi, impedance 152.6 - J 423.1 ohms

14.2MHz - maximum gain 5dBi, impedance 439.3 - J 1106 ohms

## Answer (score 2, by Aleksander Alekseev - R2AUK)

The space I have pretty much requires the loop to enclose the house [...] How will the steel roof (about 5x20 meters) affect the radiation of an 80m loop?

Although such antenna may work, personally I wouldn't expect it to have an overwhelming performance. From what I know a loop antenna radiates perpendicularly to the plane of the antenna which means it will radiate 50% of the energy to the ground and 50% - to zenith. Thus on 80m only short distance communication will be possible. Also I hope you are aware that a multiband loop antenna requires a tuner (you didn't mention whether you have one).

If you have a tuner my advice would be to give up 80m (who needs 80m anyway? :D) and build a 40m vertically polarized vertically oriented delta loop. Unlike horizontally polarized delta, vertically polarized delta has to be placed only ~2m above the ground to be suitable for long-distance communication.

I've tried such an antenna not a long time ago, here is a scheme:

It works on HF bands from 80m to 10m, although it's not very efficient on 80m. I used a 10m fiberglass fishing rod as a mast which costs ~45$ on eBay. As I understood you have trees near your house thus probably you don't need a mast.

(Note: For 80m double the length of the loop, the distance from the ground and the mast height.)

Another option that doesn't require a tuner is to build a trap dipole. I've built such a dipole for 20, 40, 80m bands once. The antenna turned out to have total length 27.5m. It also worked on 10/12/15/17/30m bands with SWR about 2. It's enough to place the balun about 6-7 meters above the ground, although for better performance on 80m it's better to place it higher.

Hope this will help. Good luck and 73!

## Answer (score 2, by Phil Frost - W8II)

As other answers have established, the presence of the roof doesn't affect the loop pattern too much. However, the proximity to ground does make the antenna quite inefficient, and radiation is mostly upward.

Moreover, I suspect the noise performance of such an antenna will be especially poor. A loop antenna around the house will make a very effective inductive pickup for every noise source inside the house.

So let me propose an alternative design: a mobile antenna on the roof. It would be easy to install and cheap, probably more so than the loop.

The metal roof will make an excellent ground plane, and a vertical can take advantage of that. The roof need not be grounded in any particular way to be effective as an antenna: it merely needs to be conductive.

If the antenna is grounded, the antenna can only reduce your risk of lightning related fire and structural damage. Lightning rods are installed on fire-prone buildings (like barns) so the bulk of the surge current travels through the lightning rod, ground rod, and conductor between. The result is some warm copper. Without a lighting rod the current may go through wood, bales of straw, or other flammable and not very conductive materials, the result is fire.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/13289/loop-antenna-layout-and-radiation, by Zeiss Ikon, Brian K1LI, Aleksander Alekseev - R2AUK, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
