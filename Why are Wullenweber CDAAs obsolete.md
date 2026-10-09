# Why are Wullenweber CDAAs obsolete?

*Tags: hf, direction-finding · score 14*

## Question

Wullenweber circularly-disposed antenna arrays (CDAAs) are large HF direction-finding antennas, sometimes colloquially referred to as "elephant cages", that were popular in the Cold War. They allowed the bearing of an incoming signal to be located to perhaps 0.5° (for the US Navy's AN/FRD-10). I've been fascinated by them ever since I saw the one on the Silver Strand south of San Diego, California. Dozens were built all over the world. Now nearly all have been demolished. The Wikipedia article for the US Air Force's AN/FLR-9 says "advances in technology have made the FLR-9 obsolete."

What advances in technology made Wullenweber CDAAs obsolete? What technologies are used for military HF direction finding now?

EDIT: I'm talking about *fundamental* advances in technology. I presume if the technology were still broadly useful, then the electronics would be modernized. To rephrase the question, why do modern militaries not use giant circular antenna arrays for HF direction finding any more? What do they use instead?

## Accepted answer (score 7, by Hamsterdave)

Two major reasons HF direction finding arrays like that aren't particularly useful any more (you won't find many fixed HF DF stations at all, even more modern ones):

- As William said, HF is not used very frequently for military communications these days, it is primarily a backup to satellite systems for long distance communication, and what communications occur tend to be more mundane and of less tactical and strategic interest. You aren't likely to hear a carrier group in theater chatting on HF these days, they know that's easily intercepted and will use systems that require geographic proximity to detect (like satellites). You're much more likely to hear encrypted links between fixed stations (bases) or inconsequential communications between assets not of much interest. Some asset phoning home because of a maintenance issue, or a routine training net, etc, and you already know where those sorts of assets are: "At home".
- Why use a massive, fixed array such as this, when an aircraft (there are several in the US inventory) can use synthetic aperture to do direction finding of similar or better accuracy, from a position much closer to the transmission in the first place, perhaps eliminating the uncertainty injected by the ionosphere, and making the intelligence far more actionable?

These days, direction finding work is of the most acute utility on the tactical level, not strategic. You've got satellite imagery and various long distance surveillance platforms for finding carrier groups in the middle of the ocean. Those assets *can't* help you find smaller elements such as a platoon or even just a lone operative, so you employ an asset that is operating on the level where the things they're going to look for are of most interest, primarily the local/regional scale, and a single aircraft may be able to cover an area the size of a small country for such work.

## Answer (score 7, by Poe)

First, there are better DF antennas now and they take up way less real estate. Some of them are .. the Pusher and "L" and "T" arrays. The electronics for these is more sophisticated than the conventional "Elephant Cage" CDAA but they are faster if the electronics is designed and implemented correctly. The FCC in Laurel Maryland took their CDAA down and installed an "L" and "T" array (I can't remember which now) In addition, since the solution is an electronic one instead of mostly mechanical (manual goniometer run by a motor) it is far easier to remote ALL of the controls so that it can be operated from anywhere given the correct control protocols.

Second, the old HF BULLSEYE NET as we knew it has been disabled now with various sites being returned back to the host governments in most of the foreign countries.

I hope this has helped answer your question.

## Answer (score 6, by Marcus Müller)

First of all: why is it surprising that a radio device built in the 1960s has become obsolete?

I don't know the specific reasons why this specific type of direction finder has become obsolete, but among these reasons might simply be:

- cost of renovation > benefit
- Shift in strategic demand for localization of these boring HF signals
- instead of a few circular setups, a lot of smaller setups can actually do the same or a lot better. We can now phase-synchronize distributed receiver systems through e.g. GPS. That wasn't possible in the 60s!
- distributed smaller multi-antenna systems allow for actual localization instead of just direction finding; the localization happens inherently and with less error instantly, instead of detecting multiple directions of arrival on multiple old systems, and then crossing lines on a map, manually, after communicating these bearings.
- terrible, terrible receiver bandwidth, noise, power consumption, reliability, operation cost. (best case: noisy germanium transistors. More likely in the early 60s: tube amps that eat kW of power for such a big receiver array). Noise Figure 7dB for a low-bandwidth receiver? That's not even remotely good nowadays.
- Operation manual suggest these amplifiers are lock-in amplifiers, and thus would be unsuitable for everything but AM and low-modulation index FM, and thus especially unsuitable for digital communications, probably.
- terrible antenna setup for systems where computational power allows to get higher resolution with fewer antennas
- antennas optimized for narrowband reception. Modern RF localization systems can track and find a lot of signals at once, spread over a large bandwidth, with a single set of antennas, through DSP
- Have you seen how **large** these are? They're positively a big waste of space.
- Resolution of this system is very bad (15dB directional gain of the beamforming system) compared to modern 3-antenna setups, which are smaller, cheaper. Manual says "nominal resolution 4°". That is seriously sub-par for anything built since the 90s with that many antennas to increase resolution.
- analog beamforming depends on physical properties of a system that are hard to maintain over time, and costly to re-calibrate
- availability of mobile systems that are better
- seriously, these are from the early/mid sixties. That's 50 years in the past. Even with ever so slight improvements in technology, it's not very likely that these would still be on par with modern technology. We have better

 - cables,
 - lacquer,
 - power supplies,
 - displays,
 - operation monitoring,
 - building materials,
 - thermal isolation,
 - cooling,
 - antenna materials,
 - antenna simulation and
 - measurement tools,
 - higher construction placement accuracy  
  
just to name a few things where there has been gradual, but not necessarily revolutionary improvements with respect to construction of antenna array systems in the last, I repeat, **50** years.

It's really no surprise that the military has adopted different systems since then.

Generally, however, CDAAs aren't obsolete – circular antenna sets still have nice properties when paired with the appropriate DSP algorithms. Thus, they are still in active usage in SIGINT; it's really just that 1960's analog systems are really not relevant anymore.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6864/why-are-wullenweber-cdaas-obsolete, by rclocher3, Hamsterdave, Poe, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
