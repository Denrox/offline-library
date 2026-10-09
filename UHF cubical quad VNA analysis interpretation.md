# UHF cubical quad VNA analysis interpretation

*Tags: antenna-construction, balun, measurement · score 3*

## Question

I've designed a two element UHF cubical quad. It was designed to resonate at 385 Mhz. I used 0.1mm thick and 1cm wide copper tape instead of wire to lower the antenna Q. I used PVC electrical conduit as a radome. Durapipe (ABS) would be better but i haven't that at hand. I used a 50 to 90 ohm balun (two stage design: trifilar followed by a guanella, based on Jerry Sevick W2FMI design). The transmission line to the balun uses two coaxial cables (using only the center conductor to make the loop legs, the shield is connect on the balun side to the center tap of the guanella). This feedline design part is experimental.

The analysis results are promising but the resonance is way off. (405 MHz instead of 380 and then a near perfect SWR at 460 MHz) the driven element loop is 0.79m long. I know that lowest SWR and resonance are not always matched — frankly i don't know.

So I wonder what may be the cause.


velocity factor issue ?


balun related ? (i used two turns around 37 cores (61 material), which is VHF UHF optimized it seems)


related to the conductor geometry (a copper tape)?


related to measure (done on a wood table inside a building) ?


the experimental transmission line made of coax ?


a mix of all these factors ?

Any ideas? I have not tested the balun itself on two 50 ohm dummy loads yet.

Schematic of the balun and antenna pics attached.

## Accepted answer (score 5, by tomnexus)

**1. You need to re-think your balun**.  
At UHF we don't use toroids and wire, it's always done with transmission lines of varying impedance, on PCB or maybe thin coax.

There are transformers for UHF, mini-circuits sells them, but they're tiny - the cores are say 2 x 4 mm and the wires hair-thin. Power handling is 0.25 Watts. Here's a photo/rendering - the pads are at 0.1" pitch:  
  
Remember 433 MHz is at least 20 times HF frequencies, so you need to scale the balun down 20 times. Yours doesn't look small enough. With microstrip you can make a balun or transformer for hundreds of watts. This link has tons of photos of microwave and UHF stripline impedance matching.

You can measure your balun separately. Does your VNA have two ports?  
Two 50-ohm coaxes make a valid 100-ohm transmission line.

**2. You should measure the impedance right at the feedpoint**.  
Solder an SMA-F directly at the feed.  
Make a thin SMA test lead (say RG316 or RG174), with a very effective choke balun: the last metre completely covered with small beads (say 12 mm long, 7 mm OD 3.5 mm ID, material 43 or 46).  
Calibrate your VNA, connect the cable.  
Now short out the SMA with a screwdriver and adjust the port extension to get a nice small ball on the left of the chart. Now you can see your feed impedance alone.  
**Edit**: Now that I have a VNA, [here's a worked example](Measuring%20actual%20feedpoint%20impedance%20for%20a%20given%20frequency.md).

Here's a photo of a VNA with a port extension to achieve a (very good) short circuit:  
  
(from this very relevant article about measuring impedance of loops)

*By the way, unless you have done a port extension like this, it's meaningless to talk about the impedance, resonance, etc - the only valid quantity is reflection magnitude, or SWR. An unknown length of cable "winds up" the impedance on the Smith chart, so you can't actually say if it's high or low, capacitive or inductive. This obsession with "resonance" on a test instrument at the end of a cable.... /rant*

**3. Measure outdoors**  
At UHF the reflections from the room will spoil the measurement. Try two things:

- Run your hand down the RF cable (at the VNA end) to see if the SWR changes. It should be stable, indicating that the balun is working.
- Also, wave the antenna around, and observe the fast-moving wrinkles run down the SWR chart. These are from reflections in the environment. They give you an idea of the size of the error they're causing, and also an idea of the gain of the antenna. Bring it close to a metal sheet and look at what happens.

**4. 10 mm copper tape isn't particularly fat.**  
At 380 MHz, 25 mm diameter copper pipe would be considered fat. The effective diameter of your copper tape is only a few mm, so you could stick with wire.  
But the impedance bandwidth and gain bandwidth of a yagi or quad is usually not dominated by the self-impedance bandwidth of the feed. The Yagi combination has a narrower bandwidth than its parts, so don't overthink the wire fatness. Put another way, amateurs use 2 mm wire to make quads, at a 20 times lower frequency, and achieve reasonable bandwidth...

Good luck, and come back and ask more questions as you go along.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15188/uhf-cubical-quad-vna-analysis-interpretation, by rodv92, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
