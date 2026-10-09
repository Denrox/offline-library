# Broadband antenna for SDR radio

*Tags: antenna, software-defined-radio · score 4*

## Question

I recently bought a very wideband SDR receiver (DX-Patrol MK4, declared covered frequencies are 100kHz-2GHz). I'm experimenting with antenna designs because unfortunately I live in an apartment building in the middle of the city and is not exactly an optimal spot for radio reception.

So far I got decent results on the VHF side with a small loop (around 1m diameter), a simple 1:1 balun (wire wrapped around a ferrite ring) and about 2m coax feedline. **Since somebody asked: I have a feedline because I have access to a balcony. I thought having the loop outside and having some feedline is better than inside with no feedline.**

So, assuming that:

1. There is no way I can get the whole bandwidth with the same antenna, so I can set for two separate antennas if the need arises
2. Because of 1. I want to keep the antenna as broadband as possible
3. Optional: the antenna can be somewhat portable

My questions are:

1. Is the loop (active or not) a good solution also for the 100kHz-20MHz range or should I set for another design?
2. How can I improve the signal/noise ratio of my current loop (I already shielded the DX-Patrol with aluminium and I suppose ferrite beads along the feedline and USB cable would also help)? Would an additional amplifier help (the SDR has already an internal LNA)?

**EDIT: thanks everybody for the answers!** Lots to digest but I will try to keep up.

## Accepted answer (score 4, by Marcus Müller)

Adressing your two questions first:

Is the loop (active or not) a good solution also for the 100kHz-20MHz range or should I set for another design?

**fractional bandwidth of antennas**

Woah! 20 MHz is 200 times the frequency of 100 kHz. No, a loop antenna won't have that amount of bandwidth.

For antennas, we measure the bandwidth in *multiples of the center frequency*. For example, an antenna working well from 2.3 GHz to 2.5 GHz has a bandwidth of 200 MHz, with a center frequency of 2.4 GHz – that's a fractional bandwidth of $\frac{200\,\text{MHz}}{2400\,\text{MHz}} = \frac1{12}$.

**wideband antennas**

We tend to call antennas "wideband" as soon as their fractional bandwidth reaches $\frac15$. Really impressive wideband antennas reach fractional bandwidths of $\frac{11}{10}$ (UWB antennas) – and those really don't have the efficiency of an antenna you'd want to work with (aside from being very very costly to make).

Now, what you demand of your antenna if it has to cover 100 kHz to 20 MHz is that it has a fractional bandwidth of $\frac{19900\,\text{kHz}}{10050\,\text{kHz}}\approx 1.98$. Such antennas have not yet been invented, to my knowledge!

**loop antennas**

Now, a loop antenna especially has what we call high Q – it is narrowband, rather than wideband. That has a lot of advantages; for example, it can be relatively small compared¹ to the wavelength $\lambda$, and it doesn't pick up noise or interference from frequencies that you don't care about – that's primarily important to keep your first amplifier stage from becoming non-linear.

Quite luckily, you don't have to buy an infinite number of antennas – many antenna types can be *tuned* to a specific frequency. Downside of tuning is that it happens mechanically – e.g. by adjusting a variable capacitor – but it works. Still, this means that the 1 MHz from 100 kHz to 1100 kHz is much harder than the 100 MHz between 1 GHz and 1.1 GHz!

**practice**

So, most often, you'd encounter a set of antennas, working on different, usually separated, bands, instead of one antenna that tries to receive all these bands and the spectrum in between.

How can I improve the signal/noise ratio of my current loop (I already shielded the DX-Patrol with aluminium and I suppose ferrite beads along the feedline and USB cable would also help)? Would an additional amplifier help (the SDR has already an internal LNA)?

**to amplify or not to amplify, that is the question**

Gut feeling: If your receiver already has an LNA, you'd need to invest relatively much money to get an LNA with a better noise figure, so, no, that's usually not the way to go, unless your signal is below the sensitivity of your receiver, even without its input amplifier.

**sensitivity, or: the magic of oversampling**

Now, with SDR, defining *sensitivity* is a bit challenging – after all, the *receiver* is not only the thing doing the RF reception, the mixing, and the analog to digital conversion, the actual extraction of the signal of interest from the received signal (for example, the FM-modulated voice, or the PSK31 data) happens *in software*. The trick usually employed by SDR receivers is *oversampling*, which means that you have a signal of a given bandwidth $b$, but you sample it with a multiple of that, let's say $f_s = n\cdot b$. Then, through digital signal processing, namely filtering and decimation by $n$, you can get an SNR increase by $n$ (only applies to white noise)².

**Example**

I don't know the MK4, but I think it's based on an RTL2832. That chip will happily give you (I think) up to 3.2 million samples per second, $f_s=3.2\,\frac{\text{MS}}{\text s}$.

Now, let's say you want to hear a CW/morse station whose bandwidth you can limit to let's say $b=1\,\text{kHz}$; therefore, our $n= \frac{f_s}{b}= 3200$; assuming perfect filtering (we can't, really, make that assumption without a bit of mathematical justification, but bear with me for the time being), that's an SNR win of $3200\approx 35\,\text{dB}$. Now, assume your actual morse decoder (might be your ear) needs an SNR of $6\,\text{dB}$ – then you can still work with an input SNR of $-29\,\text{dB}$ That's nearly thousand times the signal energy in noise!

We can see that in action every time we activate our GPS receivers: The GPS signal reaching earth is really weak – in fact, it's weaker than the thermal noise in any non-cryogenically-cooled receiver. But: due to the high processing gain (correlation) of GPS receivers, that's no problem.

**advantages of SDR and their limits**

Also note that it's digitally trivial to select *any 1 kHz* from your sampled bandwidth – building an analog filter that could do the same would be terribly complicated, and that filter would be much worse in all relevant aspects (suppression, steepness, loss)!

Basically, that's why we rather do high-sampling-rate SDR than analog narrowband receivers these days. As hinted at above, this hits limits when the RX chains becomes nonlinear (meaning that the amplified signal amplitude at every time instant isn't really the same factor times the input signal amplitude), because then you get intermodulation. This can happen, for example, if you put your receiver to maximum gain (to receive a weak signal), but your antenna also picks up a strong signal, which isn't filtered out before it reaches the amplifiers. The amplifier does its best, but it can only scream so loud, and suddenly, things that aren't actually there "on the air" get mixed into the signal of interest. But: that can often be countered with relatively relaxed analog bandpass filters (or bandstop filters, to suppress known narrowband interferers) and gain limitation.

Since frequency-selective antennas basically *are* bandpass filters, that explains SDSolar's comment:

With the wideband capability of those receivers you will want specific antennas to focus on specific frequency ranges, even if the signal is very close to you.

Since your SDR receiver can receive such a huge swath of spectrum (100 kHz to 2 GHz), it's impossible it has a narrow bandselection filter in front of the LNA³, thus it's likely that an interferer much stronger than your signal of interest will get picked up by your receiver. If that interferer is sufficiently strong to bring your receiver into nonlinearity, you get problems. Notice that the spurious free range of LNAs is often not that small – but I haven't tested the MK4 myself, and I generally have learned not to trust marketing brochures and manuals, so I can't say at which interferer power that will happen. But: the LNA will definitely be much nicer to your signal than the RTL2832-integrated amplifiers, so do try to keep the LNA active (and if it has adjustable gain, as close as possible to maximum), and use the gain of the RTL only to make the signal "fit" the whole ADC range. You'll probably notice when you're overdriving any amplifier in the chain – you'll see "ghost" frequencies becoming stronger faster than the real-world signals.

¹: $\lambda(f) = \frac{c_0}{f}\implies \lambda(100\,\text{kHz}) \approx \frac{3\cdot10^8\,\frac{\text m}{\text s}}{10^5\,\text{s}^{-1}}= 3\cdot10^{3}\,\text m=3\,\text{km}$, by all means, that's HUGE!

²: Beinaymé formula

³: In fact Dynamic Range-optimized special-purpose SDRs (e.g. for localization) do have exactly that, a bank of band-selection filters, but that's *really* expensive; good filters are actually what makes things like professional wideband measurement equipment so freaking expensive.

## Answer (score 3, by user103218)

When I was investigating antenna geometries for 2.4 GHz, looking for extremely wideband antennas that wouldn't need tuning, I came across (article) a very simple wideband antenna. Picture two discs (pizza pans?) as elements of a dipole. One connected to the coax shield and the other connected to the center conductor; this is NOT the antenna I was simulating, but it is a similar one:

In simulation using XfDTD it worked out quite well, and was very resistant to detuning by nearby metal surfaces. "nearby" of course being relative to wavelength.

At 2.4 GHz I was only looking for a fraction of the bandwidth you are, but I suspect you could experiment with this and have some fun.

## Answer (score 2, by Kevin Reid AG6YO)

I'm assuming that you're space-constrained and entirely indoors — if that's not correct, please update your question with more details.

First, the simplest thing: you talk about feed line, ferrite beads, LNAs. The simplest effective thing to do is skip the feed line and connect your receiver directly to the antenna feed point, or with as short a piece of coax as you can acquire (and use an active USB extension cable if you need one to make it reach). This minimizes loss and prevents feedline radiation/reception because there isn't any.

You also don't need an amplifier that way *unless* the signals you're looking for are weak compared to the inherent noise floor of your receiver. Amplifiers are always a last resort because they add noise.

Ferrites **on the USB cable** may be useful to prevent noise from the computer from reaching the receiver, but:


Try different computers (or e.g. an Android phone if you have one) to check if your chosen computer is particularly noisy, and use a different one for the purpose if so.


If you do use ferrites, it is a much more efficient use of ferrite material if the hole is large enough to pass the cable through multiple times; the suppression increases with turns squared (to a point), whereas multiple beads strung on the cable are merely linear in dB.

As to designing suitable antennas: having an antenna of the proper configuration makes a big difference. Trying to make a broadband LF-HF antenna that's also very small just doesn't work very well.

What I recommend you do is acquire a generous supply of insulated stranded wire and mess around with antenna configurations — see what works for you in your environment. Watch the SDR waterfall as you experiment. and remember that *more signal is better* whether it's a wanted signal or if it's atmospheric noise. (On the other hand, for specific interference sources that you can identify, it's reasonable to try to fiddle your antenna to null them out.)

One design I'd suggest you try is to string a wire in a loop around your apartment's ceiling — as much open area as you can find, even if it ends up with all sorts of bends around corners.

Also, buy or build a simple cheap manual antenna tuner (I got the MFJ-902B) and use it to play with matching at the feed point. This is something you have to adjust for different frequencies, but a tuner *can* make a significant difference for receiving when you're using a badly-chosen-for-the-band antenna.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/8948/broadband-antenna-for-sdr-radio, by Luca, Marcus Müller, user103218, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
