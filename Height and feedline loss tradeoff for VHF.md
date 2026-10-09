# Height and feedline loss tradeoff for VHF

*Tags: antenna, coaxial-cable, vhf, transmission-line · score 4*

## Question

Currently my 2m antenna is about 3m above the ground inside, my HF antenna is connected to 30m (2db loss) coax and is about 12m up. Since the loss for 2m is a lot more when traveling down such a long piece of coax will moving my 2m antenna to the same mast as the HF antenna be worth the gain in height?

## Accepted answer (score 3, by BenSwayne)

I'm not a feed line guru, but I'm not sure your question as its worded now has an academicly "correct" answer anyway as it's a matter of owner preference and local conditions.

You should clarify what you want from your VHF setup. If you can already effectively work all your local repeaters and are not concerned with simplex coverage, then maybe it won't be worth relocating your VHF antenna for you.

If you are concerned about simplex coverage for emergency use when repeaters could be down, then the height improvement may be worth any potential feed line loss to you.

If your living conditions or significant other require you to move the antenna for space/placement reasons, the top of the tower may be nice and out of the way.

You will need to weigh these benefits and costs against your desired performance.

Of course if you are running inexpensive feed line with your VHF antenna *indoors*, moving it outside with good quality feed line may not cost you anything more than you are already losing with the antenna indoors! So its just a matter of cash and time to mount it right.

**EDIT After comments:** Taking into account your clarification in the comments above, I would say getting the antenna outdoors and replacing the "car kit" feed line with quality low loss feed line will likely give you an all around better setup. ARRL seems to recommend Belden 9913 or LMR-400. "For base stations in particular, always buy the lowest-loss coax you can afford." - from that same ARRL page.

I've seen more than a few people put a VHF vertical above the apex of a dipole on a tower. But hopefully someone more knowledgeable than I can advise on a recommended minimum separation distance. If you can keep the vertical a few feet above the dipole that will help reduce any interaction between them.

Whatever separation distance you can achieve, I'd be pretty confident your setup will improve getting your antenna outside with better feedline.

## Answer (score 2, by KD5QLN)

Some possible solutions would be:

1.

Get better feedline, like LMR400

2.

Get an LNA, this is a special amplifier that sits between your antenna and feedline and is powered by a supply at the other end of the feedline.

3.

Transverter. A transverter will take for instance a 10m signal and convert it to 6m and vice-versa. You see these a lot in the GHz spectrum, as installing waveguide or LMR1200 is not practical.

## Answer (score 2, by Phil Frost - W8II)

Usually, higher is better, assuming you are using coax that isn't exceptionally lossy. At VHF, this will be something other than the cheapest coax you can buy.

Unfortunately, that's the most accurate answer you can get here, because the benefit of additional height depends on a lot of things about your environment that we don't know. Are there buildings in the way? Trees? What are ground conditions like around your location? What's the height of the other antenna?

The best height will be the one where coax loss + path loss are at a minimum. Calculating the coax loss is easy: read the datasheet. Calculating path loss not feasible, but you can measure it.

Put your antenna on a piece of coax long enough to reach to your highest height considered. Mount the antenna down low. Go far away. Make a test transmission. Measure the received signal strength. Now move the antenna up higher and repeat. Now you know what you stand to gain by putting the antenna higher. Compare that to what you will lose, calculated from the coax specifications, and you will know if higher is better.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1332/height-and-feedline-loss-tradeoff-for-vhf, by s3c, BenSwayne, KD5QLN, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
