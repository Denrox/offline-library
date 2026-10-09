# Power rating of a selfmade air coil

*Tags: antenna, antenna-theory, rf-power, inductor · score 6*

## Question

A colleague was winding an air coil himself. It's a 110µH coil with 200 windings for an 80m antenna, intended to be used on a 600 W transceiver. He used a copper lacquer wire with 0.6mm diameter. After finishing the coil, he wondered whether 0.6mm wire was sufficient for the expected 600 W.

**How would I calculate the power allowance for such a coil?**

These were my thoughts so far:

1. 0.6 mm diameter is 0.283 mm².
2. Looking up a table, I can find an allowed current of 3.4 A.
3. If the copper lacquer wire was made for transformers, we could potentially use it in a 220 V scenario, giving 748 W.
4. For a typical 50 Ohm antenna, P = I²R = 3.4² A² * 50 Ohm = 578 W.

Then, someone else mentioned that the skin effect should be considered, but unfortunately didn't respond any more upon request. Maybe he's still calculating ;-)

1. The table for copper sais 65 µm @ 1 MHz and 20 µm @ 10 MHz. 80 m should be somewhere between those, let's say 35 µm.
2. The circumference of the wire is 1.885 mm.
3. The area where the current flows is then 1.885 mm * 35 µm = 0.066 mm².
4. Looking up the table again, I get a current rating between 0.59 A and 0.85 A.
5. Going the P=I²R formula again, that coil would only withstand 36 W.

The values 578 W and 36 W are very far apart, so I didn't want to make a recommendation to use the coil with 600 W.

## Answer (score 5, by tomnexus)

The coil needs to dissipate approximately **all of the transmitted power** so it sounds a bit lightweight. It's not so much the copper wire thickness itself, but the rest of the mechanical details.  
Final performance will depend on

- the former that the coil is wound on
- what temperature the former can cope with
- the duty cycle of the transmitter (eg. 600 W SSB PEP is only ~150 W average while talking)
- the mechanical stability of the coil as it heats up - any change in dimensions will de-tune the coil.

The wire thickness isn't all that important, within reason, as much of the heat dissipation will be through whatever it's wound on. I'd start by looking at the overall surface area of the coil as it's wound and estimate the temperature rise.  
In house wiring, the figures for allowable current in a certain diameter copper cable, are really taking into account the heat that can be dissipated by a typical *cable* containing two of these wires, and its overall dimensions and materials.

Some calculations about the power loss:  
(**edit:** typed in formulas, redone calculation in metres, all the numbers change slightly)

110 uH at 80 m (3.5 - 3.8 MHz) has a reactance of ~2500 ohms.

I look up two useful formulas at antenna-theory. Note:

- We are definitely in Short Dipole territory here, length << wavelength, so the current distribution is triangular (if you like, the very end of a sinusoid, the part where sin(x) ≈ x )
- Remember all these are for *dipole antennas* so the length and impedance is double that of the monopole case.

First, the reactance, to match that of the coil:

$$ X_{dipole} = {{-120\lambda}\over{\pi L}}\left( \text{ln}\left( \frac{L}{2a}\right)-1\right) $$

Experimenting a bit (I can't solve it) I find a 4 m long *dipole* of diameter 4 mm has about -5000 ohm reactance, i.e. -2500 ohms on a 2 metre *monopole*, which will resonate with that coil, and is a reasonable whip length for a vehicle. So you're probably making a base loading coil for a whip antenna (this is just me reverse-engineering the intended application).

Knowing the antenna type and length we can estimate the radiation resistance (on a perfect ground plane):

$$ R_{rad} = 20 \pi^2\left(\frac{L}{\lambda}\right)^2$$

The radiation resistance of a 4 metre dipole on 80 m is 0.5 ohms, so the monopole antenna will be about **0.25 ohms** and there will be a few ohms of ground loss.

The coil Q might be as much as 100, to be generous, meaning it will have a *resistance* of 25 ohms.

Now I can draw a circuit model of the whole antenna:

The series circuit of coil loss resistance, radiation resistance and ground loss, shows you that over 90% of the power is lost in the coil, depending on the size of the vehicle and the type of ground, more likely 99%. (you can estimate the coil Q just by looking at the bandwidth of the antenna when it's tuned).

So you need to plan for the coil to dissipate 100-200 watts without catching fire or getting out of shape. This also means that less than 1% of the power is radiated. This is the unfortunate reality of mobile HF antennas, especially for 80 m.

There are ways to raise the Q of the coil to several hundred - making it a larger diameter, thicker wire, keeping metal away from the ends, and using a ferrite core. It's also more efficient to put the coil halfway up, as Hustler does. These can dramatically improve the transmitted power, but you can see they won't make a big difference to the power dissipated in the coil.

Here's an example of a commercially available resonator for 80 m, capable of "1000 W" (right):  
From memory, the Hustler RM-80S is about the size of a 0.5 to 1 litre water bottle.  
So for 600 W, you probably want your coil to be about half this size.

## Answer (score 3, by hobbs - KC2G)

Sorry for not putting a simple positive answer here, but:

- "Allowed current" ratings for domestic wire aren't applicable at all to something like an antenna matching coil. They're based on fire safety requirements, allowing for a certain amount of temperature rise, for wires run behind walls, installed in certain ways. Your coil is something different, its shape is different, its duty cycle is different, and its acceptable temperature range is different.
- You can't account for skin effect just by pretending the wire is smaller. Although the resistance (and thus heat generated) are those of the imaginary smaller wire, the mass and surface area (and thus ability to absorb and dissipate heat) are those of the real, larger wire.
- You can't just use a 50-ohm impedance to convert between current and power. You're using a coil because the antenna *isn't* a nice 50+j0 ohms. In particular, you're using it to cancel out a reactance, so there will be some reactive power flowing between the coil and the antenna, in addition to the real power flowing through the coil from the feedline to the antenna.
- You can't really calculate power handling capability without taking into account the shape of the coil (diameter, length, distance between turns) because they affect the ability of the coil to dissipate heat into the environment.

Now I don't have the tools to calculate this, and in reality I don't think that it's common for anyone to do the calculations — they just build and test. Start with a low power, see if the coil gets warm, and then increase. If it gets too hot, try again but make it bigger / lower loss. Or otherwise change the antenna design so that the coil current is lower.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20465/power-rating-of-a-selfmade-air-coil, by Thomas W., tomnexus, hobbs - KC2G. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
