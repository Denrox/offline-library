# Choosing capacitor for high-pass filter with cutoff of about 160 MHz

*Tags: equipment-design, rfi, filter · score 6*

## Question

A strong (100 kW) local FM transmitter causes interference to or overloading of receivers in the VHF/UHF bands. It seems like a single, properly chosen, capacitor could make an effective passive high-pass filter. I would like the filter to pass 200 MHz and up effectively, while suppressing 108 MHz and below. I'm assuming that this doesn't require a particularly challenging filter slope. I envision using this in-line with a 50 Ω coax.

Using a filter design app, I put in a cutoff frequency of 160 MHz, and an R of 50 Ω, and got a capacitance of 20 µF. So far, so good.

The question is:

1.

Will this work? Is there an easier way?

2.

**What type of capacitor is appropriate for this application?** Should it be a ceramic, mica or film type or what? I need it to be useable to frequencies up to around 600 MHz.

With this question, I am thinking of over-the-air TV reception as well as amateur radio and scanner reception.

I know specific FM traps are available, but those are band-stop filters. Shouldn't a high-pass filter be easier and have lower insertion loss as long as I don't care about anything below the cutoff frequency?

BTW, I didn't see much in the way of commercial products to do this. I am looking for something competitive with a $5-10 Radio Shack FM trap.

## Accepted answer (score 3, by Phil Frost - W8II)

While that would work somewhat, it won't work great. What you are describing, with a single resistor and capacitor, is a first-order filter. Such a filter has a roll-off of approximately 6dB per octave. This means for each halving of the frequency, attenuation is increased by 6dB.

Say you design your filter to have a a cut-off frequency of 200 MHz. The FM broadcast band ends at 108 MHz, approximately one octave below that. Consequently, you will get an attenuation of about 6 dB. That's not much.

It's a common engineering problem that steeper filters are harder at higher frequencies. If we wanted to separate 8 MHz from 100 MHz, that's still a difference of 92 MHz as in your example, but we'd have approximately four octaves to make the transition.

Given that you are looking for a simple solution, and you are experiencing problems from just one station, I would suggest using a quarter-wave stub of transmission line as a filter. Advantages:

- you can make it from coax or twin-lead, which you probably already have
- attenuation can be very good -- with a loss-less transmission line, attenuation is theoretically infinite
- it's easy to tune (just need a pair of wire cutters)
- it's easy to fabricate
- it will work at any frequency that can be reasonably handled by your transmission line

Disadvantages:

- it will also notch all the odd harmonics, so if you tune the notch to be at 108 MHz, there will also be notches at 324 MHz (108*3), 540 MHz (108*5) and so on.

The theory of operation is a little magic but simple: if you are looking at something through a quarter wavelength of transmission line, you see the conjugate impedance of the thing at the end. For your purposes, what matters is that if at the end of the transmission line there is a short, then it looks open. If the end is open, then it looks like a short.

Remember, it only looks like a short or an open at the frequency where the stub is a quarter-wavelength long or an odd harmonic thereof. To other frequencies, it looks like some other complex impedance, which means it will change the impedance of your antenna, but this is [probably not a big problem for a receive-only application](What%20is%20the%20relationship%20between%20SWR%20and%20receive%20performance.md). If it is a problem, you will need a more complex filter -- even your simple RC filter has this problem. Again, the merit of this approach is simplicity, not perfection.

Anyhow, now you have either a short or an open which you can insert into your circuit. To make a notch filter, you have two options:

- put a short in parallel
- put an open in series

It's easier to tune if you opt for a stub that's open at the end, because you can just cut it. So this is going to look like a short, so we want to put it in parallel, which will effectively short out the antenna for frequencies where the stub is a quarter wavelength:

A further advantage of this approach is that the stub can be added with a T-adapter. You can also just strip the transmission line and solder it together. Don't forget to weatherproof the connections if its outside.

Just for completeness, you can also use a series stub, which effectively disconnects the antenna:

The two work identically, so choose whichever one is easier to fabricate.

Whichever you pick, fabrication is pretty easy. Calculate the wavelegnth of the problematic transmitter, then cut a piece of transmission line that is a quarter of this. Remember to lengthen the transmission line according to the velocity factor. For example, if the offending station is at 108 MHz, and the velocity factor is 66%:

$$ \lambda = c / 108\:\mathrm{MHz} = 2.78\:\mathrm m\\ 2.78\:\mathrm m / 4 = 0.694 \:\mathrm m \\ 0.694\:\mathrm m / 0.66 = 1.05\:\mathrm m $$

Tuning is critical, and it's easier to make it shorter than longer, so cut it a bit longer than this, then keep trimming off little bits until you get maximum attenuation of the problematic station.

## Answer (score 3, by tomnexus)

Mini-circuits is the place for filters and other RF gadgetry. See http://www.minicircuits.com/products/filters_coax_high.shtml for their high pasd catalogue.

For example, the BHP-250+ BNC connectorised high pass filter. It has -40 dB at 100 MHz, -20 dB at 150 MHz and -3 dB at 205 MHz.

These little filters can only carry about 1 Watt, so would only be useful for a receiver, not a transceiver.

MC do also make an FM band filter which is a band stop device with very sharp edges.

The benefit of buying something built up is that it's performance will stay reasonably constant over temperature and time. You need a fairly high order filter to get many dB between 108 and 200 MHz, and these can be sensitive to component drift.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2438/choosing-capacitor-for-high-pass-filter-with-cutoff-of-about-160-mhz, by Jamie Cox, Phil Frost - W8II, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
