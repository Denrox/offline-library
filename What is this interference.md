# What is this interference?

*Tags: software-defined-radio, rfi, signal-identification, panadapter-and-waterfall · score 3*

## Question

When on a SDR, at LF, I saw a cluster of interference. A little researching told me they were LF broadcast stations. But wikipedia said most of them are decommissioned, so what is the noise? What even is causing it? This is what it looked like at the left:

On bad days, it would be completely orange.

## Accepted answer (score 3, by Marcus Müller)

These look *so* sharp and narrowband that I'd presume it's self-interference, i.e. parts of your SDR leaking into your receive path.

You need to look at the color scheme here: there's very strong signal at the lower frequencies, and there's a sharp tone a little above 5 MHz.

Look up how much power the color they have mean (maybe your SDR receiver program also has a different visualization than this waterfall spectrogramm? A simple line plot of the power vs frequency would be much more useful here!).

Then, reduce the receiver gain by 20 dB.

- Do the signals retain the same power?

 - Then they are inside your receiver itself, bleeding into your receiver *after* the adjustable receive gain stage
- Do they completely disappear, or become weaker by much more than 20 dB?

 - Then they are intermodulation products, caused by driving the receive amplifier at too high gain
- Do they change power, but their relative strength stays the same? (e.g., the stronger remains 5 dB stronger than the weaker tone)

 - Then they actually external signals at somehow reaching your receiver.  
In this case, they are very likely not LF broadcast stations: look at them, they are onmodulated! So, they might be other device's clocks, or they might be pilot tones, or they might something else.

**BUT**: As long as it's not in your band, it's **not** interference; one person's signal is another person's interference, and unlike amateur usage, there's static assignments allowing some users to emit whatever they applied for. *These 20 MHz aren't your band, so this isn't interference*, but just *emissions* (or effects of your receiver itself). So, you need to **not** think of this as interferers, but as other emitters, which might simply have the right to be there! This is the norm, not the exception. This also applies for spurious emissions of devices like switch-mode power supplies, DSL and powerline communications: while it's annoying to the amateur radio user, it's not justifiable that these things that provide a general utility should be completely emission-free, as long as they stay below their legal limits when it comes to emitting in bands they don't "own".

To drive that point home: as an operator of an amateur radio station in the USA (and only there), you'd be right to call emissions that fall into the bands that I marked in green below **and** aren't amateur radio emissions "interference"; the rest is just there, and not interference:

The 2.2 km and 630 m band are so small, they're smaller than a pixel of your visualization, and we can't say anything about them. On 160 m, amateur radio is the secondary user, so it's not clear whether the bursty emissions we see there are the primary use case (radiolocation services) or some ham mode. There's one emitter active on 80m, which might be your receiver itself, or it might be an active amateur radio enthusiast on the air! So, all in all *there seems to be no interference to you as ham in what you show, at all*!

**What's the practical difference between emissions in general and interference to me?** You'll ask, understandably, **I want these emissions to not be there, ideally!**. But here's the deal: If something *interferes* with something that you have a license to (e.g. if a device emits noise above it's legal power density limit in an amateur radio band), then the interfering party needs to fix their device, legally. If your receiver malfunctions because of something *not* in its dedicated band of operation, it's just broken; in many cases, for example consumer electronics, that also means it's illegal to sell, import or operate that receiver. So, things outside of your band that are bad for your receiver are *your* problem to solve, things within your band that are bad for your receiver need to be solved at the source!

The fair remark of people operating devices that indeed emit in amateur radio bands (but within legal power limits) here has historically been, "sure, my spread spectrum modem raises the noise floor in a wide band. Why exactly is this a problem to your narrowband amateur radio communications? Is it possible that your receiver is just overly sensitive to noise because you're 100 years behind technological progress?", but these days a significant amount of amateur radio communications does indeed use robust modes, and the onus of actually staying within their limits is getting easier to put on non-ham emitters, intentional or not, as wideband monitoring becomes broadly available: As can be seen in your question!

GENERALLY, questions of the kind "{Screenshot} what interference is that?" are usually only answerable using the same method that you already perused: looked into which transmitters are allowed to transmit in a given band. I don't know which country you're in, but the local spectrum regulation authority (FCC in the US, BNetzA in German, OFCOM in the UK…) has a table with several hundred pages worth of information who might be operating where. In many to most bands, the specific modulation to be used there is *not* specified, only maximum powers, so, looking at a spectral shape alone rarely is as helpful as looking at the table.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/22857/what-is-this-interference, by John Doe, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
