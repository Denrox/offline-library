# HF antenna design for high-altitude balloon

*Tags: antenna, hf, antenna-construction, wire-antenna · score 5*

## Question

I'd like to put a WSPR or JT65-like transmitter on a high-altitude balloon, but lacking much experience with HF antennas, I don't quite know where to start. I'm thinking it will operate on 20 meters, at (obviously) low power, say 100 mW or less. Building a lightweight little transmitter with an Arduino seems do-able, and I can hang a wire from it as long as I like, within reason, but I'm not sure how to match to it, what to use for a counterpoise, and so on. Radials longer than about a foot are out, for example.

I've googled a bit, and found all kinds of stuff about HF antennas lofted by balloon, but all those are tethered to the Earth. This will be free-floating. No ground plane to be found anywhere, no transmission line (if I can help it), no big structure holding wires apart. Weight is a big issue.

Edit: another concern. The problem with a dipole occurs on the way down, after the balloon bursts at altitude. Things go thrashing around pretty badly at that point, until the atmosphere gets thicker and the parachute can take hold. I have read at least one claim that the whole package can almost go supersonic!

So I worry about what a weight at the end of a 5 meter wire might do. Especially since this won't be the only payload on this balloon. I can just imagine what a 5 meter wire weighted at both ends could do, which is what I'd be looking at if I hung the electronics package in the middle of a dipole. Far better to put the weight as close as possible to the parachute, in one place if I can do it.

Maybe I worry too much. I thought about a simple quarter-wave wire, but then what's the counterpoise? There has to be something.

## Answer (score 4, by Seldon2k)

May I suggest coaxial sleeve antennas and variants, see links below:-

http://www.eham.net/ehamforum/smf/index.php?topic=46338.0;wap2

https://www.youtube.com/watch?v=w8hQRjI3BPk

This last is a smaller 6m version, the choke balun is not needed if your Transmitter is directly connected at this point.

The bazooka variant could also be of use. Do a search for 2m Bazooka and hamuniverse for more details. Also on hamuniverse is the 20 Meter "Vertical Zepp Dipole" Antenna.

This hanging upside down from the balloon should radiate as a vertical.

None of these require grounds, radials or counterpoises. Hope this is useful.

**Edit** I have just seen the comment about weight.

For RG-174 the spec is here http://www.belden.com/techdatas/metric/8216.pdf

For a 20m dipole, we have the following calculations:-

WSPR Freq = 14.097MHz & JT-65 Freq = 14.076MHz, so wanted average = 14.0865MHz.

Therefore Lambda = 3E8/14.0865E6 = 21.297m A half-wave coaxial dipole = 10.648m if we ignore velocity factor (worst case) we see from the specs above that the feeder weight is 11.906 Kg/Km so 11.906 g/m.

Therefore the weight would be 11.906*10.648 = 126.78g or approx. 127g.

I am from the UK so here we switch to Imperial measurements: 127g = 4.48 ounces or approx. 4.5 ounces.

Using RG-58 from the specs https://www.pasternack.com/images/ProductPDF/RG58C-U.pdf we see 40g/m so the weight would be 40*10.648 = 425.92g or approx. 426g. or 15 ounces, just under an imperial pound.

Being unfamiliar with high-altitude ballooning I am unsure if this exceeds and safe/maximum loads. Also, it seems that most people are using 434MHz licence exempt kit requiring much smaller and lighter antennas.

## Answer (score 4, by tomnexus)

The most sensible antenna is a wire dipole extending above and below the electronics package.

This seems to be how all the QRP Labs transmitters work.

Self-supporting radials, or a coax cable feed to the centre of the antenna, will be much heavier.

You could optimise the weight by trading some length for some inductance at the transmitter, without reducing the efficiency much.

## Answer (score 2, by JSH)

I'd seriously consider the 1909 predecessor of the J antenna by Hans Beggerow. It is, indeed, an antenna designed to hang below a balloon.

Like the modern J antenna (aka J-pole) it is a half-wave single linear conductor fed with a quarter-wave parallel wire transformer, fed in turn near or at the closed end of the transformer. With your payload/electronics package as small as it is likely to be, you can probably get by without the spiffy link coupling and figure out a simpler solution. I'd start by breaking the shorted end of the transformer, flay the feedline and just feed it there. If the impedance is too low, re-short the transformer, run some RG-174 down the transformer line a bit and find the sweet spot... just like a J antenna.

All together this will be about 15 meters in length for the 20m band, but that half-wave wire can be very thin. This will whip around a bit, but I suspect the mass of the wire will tend to keep things reasonably plumb at most times.

If you can find it, super thin 300 ohm twin lead parallel transmission line will serve as the 5 meter quarter-wave transformer.

Best of all this needs no additional counterpoise (or equiv.) to operate as an efficient half-wave radiator. Plus there are no concerns of coupling from the high voltage end of the sleeve to the feedline in a coaxial sleeve style antenna.

With some planning and design you might be able to position your payload/transmitter directly at the feedpoint sweet spot by attaching it to the quarter-wave transformer at that spot. In this way the entire payload (antenna plus electronics) attaches to the balloon at the shorted end of the transformer. The potential problem is the higher voltage portion of the quarter-wave transformer wants to be well away from other conductive or dielectric materials. Still the "50 ohm" feedpoint isn't too far down the transformer so this might be viable.

A link to the patent (in German) along with other references is available on the J-pole antenna Wikipedia page.

https://en.wikipedia.org/wiki/J-pole_antenna

If it was good enough for 1909, it's well worth a good long look now.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/8955/hf-antenna-design-for-high-altitude-balloon, by Rodney Price, Seldon2k, tomnexus, JSH. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
