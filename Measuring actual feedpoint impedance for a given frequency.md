# Measuring actual feedpoint impedance for a given frequency

*Tags: antenna-theory, antenna-system, impedance-matching, impedance, nanovna · score 4*

## Question

### Background

I'm attempting to tune an antenna with my NanoVNAv2.

I calibrated it using the included open/short/(50-ohm)load standards by screwing them directly onto the NanoVNA one by one and running its calibration function.

The antenna itself is a Hustler RM40, mounted to a MT-4 mount (the 24" short one), screwed into a 3/8-24 mirror mount bracket. The bracket is physically mounted to a 10 foot PVC pole, with the antenna itself passing through a (nylon) zippered opening in my patio's (fiberglass) roof screen. The metal mirror bracket itself is (conductively and electrically) connected to the aluminum pool enclosure frame (**see mechanical details below), providing both a feedpoint ground connection and radials.

Yes, I know this setup sucks. It's temporary, so I can start playing with my new radio during the month or so it's going to take me to get a proper antenna installed.

In theory, it should be mostly kosher. The screen enclosure's grounded aluminum frame provides a fairly large (albeit completely untuned) radial field. The mast, loading coil, and whip are all above and perpendicular to it. The problem I'm having is, no whip length I can discern will actually TUNE it (according to NanoVNA) for approximately 7.05MHz.

I know beyond doubt that this particular RM40 works on 40m... I used it last summer at my dad's house (in the middle of his yard, mounted to a ground rod driven into the earth, with a radial field that was asterisk-like, but still semi-random length). The SWR between 7.04MHz and 7.08MHz was well below 2.0:1, using various masts between 24 inches (the MT-4) and 17 feet (shorter masts had worse performance, but aside from requiring whip-length adjustments, didn't affect SWR nearly as much as I thought they would).

My best guess is, the untuned grid-like arrangement of my de-facto radial field (the screen enclosure frame) is still usable, but is skewing the feedpoint impedance enough to invalidate the NanoVNA's SWR readings (which blindly assume a 50-ohm feedpoint).

My assumption right now is that I might or might not have to build something to tweak the feedpoint impedance, but until I know what my actual feedpoint impedance even *is*, I'm flying blind.

So... how, exactly, does one go about accurately MEASURING feedpoint impedance for a given frequency? It seems like a chicken-egg problem... the only tool I presently own (NanoVNAv2) needs 50 ohms, but (AFAIK) can't itself determine whether the feedpoint it's looking at actually PRESENTS a 50-ohm impedance, or directly determine it.

I assume I'd also need a frequency source, since (AFAIK) impedance isn't constant, and depends upon the frequency you're measuring it at. I could swear I remember reading somewhere that NanoVNAv2 is itself capable of directly outputting a square wave at a frequency within range of its frequency generator. If not, I have a Si5351a on a breakout board, too.

The big million dollar question is... could a cheap (sub-$40) LCR-capable multimeter from Amazon be used in conjunction with a NanoVNAv2 or Si5351a+Arduino to reasonably measure the ACTUAL feedpoint impedance? Or would I still need *other* tools (possibly, tools that are cost-prohibitive) to do it?

(**) Mechanical details of connection to ground:


I drilled 4 holes in the screen enclosure's aluminum frame to match the hole pattern on the 3/8-24 mirror mount


I screwed 4 rare-earth donut-shaped magnets into the holes (one per hole) using flathead stainless-steel screws, and verified 0 ohms resistance between the screw heads and enclosure frame.


At the other end, I used stainless steel bolts with flathead machine screws and 4 more magnets facing in the opposite direction to attach the 3/8-24 mirror mount to a PVC pole. When brought together, the 4 magnets on the mount grab the 4 magnets on the enclosure frame, bringing the screw heads together and making what appears to be good electrical contact.


the 10 foot PVC pole serves two purposes... it enables me to take the antenna down and put it up without needing a ladder, and provides vertical support to the antenna (the magnets secure it horizontally)

## Accepted answer (score 5, by tomnexus)

Your NanoVNA is perfect for the job, but you need to use some tricks to get what you want.

**First, about the 50 ohms question:**

The NanoVNA, and most others, transmit a low power signal, and measure the magnitude and the phase of the reflection that comes back. This can be used to produce graphs of VSWR, for example. The reflection is measured *in the 50 ohm system that is the NanoVNA*.

For example, if you connect a 100 ohm load to the NanoVNA, then the reflected voltage will be about 0.33 of the transmitted voltage, and this leads to a 2:1 VSWR, **in a 50 ohm system**.

Knowing that its source, directional coupler and receiver are all 50 ohms, the VNA can also calculate the actual impedance in ohms, using this:  
$Z = 50 * \frac{1 + Γ}{1 - Γ}$ where $Γ$ is the measured voltage reflection coefficient.

This works for any impedance, but as there are always errors in magnitude and phase, it will be most accurate for impedances near 50 ohms, and much less accurate for impedances near the edge of the Smith chart. You can think of the errors as making the measured reflection coefficient slightly fuzzy on the Smith chart. Near the centre the blur is just a few ohms, while in the corners it could be a thousand ohms. Put another way: when in a 50 ohm system, there's very little difference between 1000+j1000 and 2000-j1000 ohms, they're all basically an open circuit.

**How to measure feedpoint impedance**

To measure the impedance at the feedpoint, you need to calibrate all the way to the feedpoint. The VNA calibration compensates for everything *before* the calibration point, including all the imperfections of the instrument, and loss and reflection in the cable and adapters. As long as the cable isn't too awful (loose connections etc) the VNA will measure accurately at the very end of the cable.

After you have calibrated, use a screwdriver or knife blade to short circuit the feedpoint and look at the Smith chart. It's best to use a short and not open because it's easier to add a short circuit to an existing antenna without damaging it, making it open involves cutting or desoldering the antenna. If you see a short circuit (small spot on the left of the Smith chart), then you're done. If there is still some residual usually a small curve over frequency, read on.

Most VNAs include the ability to include an arbitrary electrical delay, or port extension. On the NanoVNA it is called Electrical Delay, it's under the Display menu, and a positive number means it will remove an added delay like a bit more cable. With the feedpoint short-circuited, type in a delay and try again until you see a short circuit.

Here's a worked example. I'm doing it at 500 MHz because my cables are short, but the principle is the same at HF if the cables are longer.

1.

Impedance of the cable, open circuit, when the VNA is calibrated at its own port:  
  
Note 1. the cable loss (the open end reflects all the power, but some power doesn't make it there, or back, becaues of the loss, so it's not on the edge of the chart) and 2. the cable length (lots of turns when it should just be an open circuit)

2.

Impedance of the cable, open circuit, when I've calibrated to the end of the cable:  
  
A nice open circuit.

But what if my antenna isn't quite at the connector I've just calibrated to? What if tt includes a short piece of cable itself, or just the body of the connector (which I can't disconnect). Here is how you remove that cable too:

1.

I connect the antenna and short-circuit it with a knife:  
  
  
Note that this does not look like a short circuit! So when I remove the knife to see the antenna impedance, it will be all wrong.

2.

Adjust the electrical delay to get a good short circuit, with the knife in place. I used 3 ns which is the round-trip time of a 1 foot cable. See the Edelay line at the top of the screen.  
Now remove the short circuit and you should see the true antenna impedance measured exactly at the feedpoint.

At HF you can probably get away with port extension through many metres of cable, so if there's no connector closer to the antenna, you could get away with calibrating at the VNA.

## Answer (score 2, by hotpaw2)

The Smith chart displayed by a NanoVNA indicates the complex impedance graphically. Or you can use the “data” command from a serial terminal to dump the raw IQ values for a frequency sweep, and use those to calculate the complex impedances, relative to the 50 Ohm calibration.

Search for how to read a Smith chart (lots of docs available).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20680/measuring-actual-feedpoint-impedance-for-a-given-frequency, by Bitbang3r, tomnexus, hotpaw2. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
