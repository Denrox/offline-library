# Rfi in truck with HF transceiver when running

*Tags: rfi, mobile · score 3*

## Question

I have an Icom IC-707 in my truck, a 2003 F150, with a stainless 102 inch whip mag mount on the roof. It has a a coil pack 6 cylinder.

Without it running I have no problem; as soon as I start the truck up I have horrible interference all the way up to S9.

I have tried pretty much everything now that I can think of.

I have researched about spark plugs with resistors: special sorts of cables with high resistance, I've ohmed out my shortest cable and it had 8,000 ohms my spark plugs had about 3200 to 3,600 ohms.

It's not coming from the feed line because I can run it off a separate battery not connected to the truck and it still happens; it's not the fuel pump because I turn the ignition on and it primes it up. You don't hear it it's picking it up through the antenna.

Does anyone have any advice about what I need to do to stop the ignition system, which I believe is a culprit just stopped this interference? Do I need to get spark plug wires with even higher resistance? Also, these are brand new wires, I tried that, and the plugs are not that old, maybe about 6 months. I've also tried grounding the radio to the frame and the antenna to the frame: no difference. I'm 90% sure it's my ignition.

## Answer (score 5, by tomnexus)

There are many things you can still do. Here are a few quick suggestions to start with:

**Proper antenna ground**. A mag mount is marginally OK at VHF / UHF, but there isn't enough capacitance at HF. The antenna needs a solid ground connection to the vehicle body.

Assuming basically no grounding from the mag mount, you have a sort-of dipole antenna, with the whip at one side and the coax+radio on the other side. This unwanted part of the antenna extends to include the microphone cord and the power cables which run all the way to the battery, the battery negative-to-engine block strap and finally the engine ground strap. This maximises the pickup of RF noise from the engine compartment.

If you must use a magnet mount, you should find a way to ground the outside of the coax properly, just as it enters the vehicle. Cut off some of the jacket, solder some braid to the coax, and bolt this to the vehicle. Or install a (SMA) connector, and mount a F-F barrel to the vehicle. Ferrites on the indoor section of the coax will also help.

**Vehicle Panel Bonding**: The next step is to bond the body panels together with earth straps - first the hood, the box (might not be connected to the chassis) and then perhaps the doors. This blog post shows some photos and gives some more hints. I think the straps don't need to be as thick as they show (this is not for lightning) so rather use a few small straps with self-tapping screws. Clean off the paint first, and re-coat after assembly for corrosion protection.

Panel bonding will help with both the performance of the antenna, and the pickup of interference from inside the vehicle.

**Ferrite beads on the power cables**: to reduce the transfer of noise from the engine you can try clipping some ferrites over the power cables. Important to clip over both + and - leads, the ferrites won't work if they see a large net DC current flowing through them. You could try beads both ends of the wire. If you've tried a separate battery then perhaps this isn't the most important step.

**Noise Blanker**: The spark-plug noise will be hard to eliminate completely. Most radios have a NB feature which mutes very short impulses, without spoiling the sound overall. If you have spark plugs, you will need the noise blanker.

You don't describe the noise in detail - I'm assuming it is ignition noise, which is most likely, but there can also be alternator noise and alternator whine, and more general interference from the vehicle electronics.

## Answer (score 3, by niels nielsen)

Just a few random ideas which might help.

With the truck running, tune the 707 all the way down to 160 meters and measure the noise. Then turn on a portable AM radio, or the AM radio in the dash, tune it to 1600kHz, and measure the noise. If the noise is *radiated EMI* then the AM radio will pick it up too. If it is *conducted* then the AM radio will not pick it up.

Next turn on the 707 and tune it for a good strong noise signal. Then *disconnect the antenna coax* and measure the noise. If it disappears with the coax disconnected, it is radiated EMI.

Get you an oscilloscope and make a little air-core loop antenna for it. With the engine running, pop the hood and sweep the antenna around within the engine compartment and look for radiated noise at the frequency of interest. You might be able to focus in on the noise source by moving and rotating the loop around.

Another note: does the noise scale up in frequency when you rev the engine? If so, it's got something to do with the fuel injection, ignition, or charging system. If not, it might be coming from the main "black box" computer that controls the fuel and ignition systems.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/22145/rfi-in-truck-with-hf-transceiver-when-running, by Plumber90, tomnexus, niels nielsen. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
