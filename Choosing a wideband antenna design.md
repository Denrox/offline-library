# Choosing a wideband antenna design

*Tags: antenna, software-defined-radio, equipment-design · score 4*

## Question

[On a previous question](Broadband%20antenna%20for%20SDR%20radio.md) I asked about proper antenna design for wideband SDR receiver and ways to improve signal/noise ratio. Ideally the reciever has a range of 100kHz-2GHz. Keeping in mind is impossible to cover the whole spectrum with one antenna, I'm trying to settle with as few antennas as possible.

Searching for wideband antenna designs I stumbled upon this examples. I would like to know which of these designs to choose, or any other you can recommend:

1. The PA0RDT mini-whip design. Allegedly 10kHz-20MHz, used also by the famous WebSDR of the Uni Twente. Uses JFETs and I don't have a cheap source for them. I would settle for an equivalent.
2. The Dressler-type antenna for 50MHz-2GHz
3. This or variations thereof, loop-amplifier-balun. Here a more complicated one that claims LW reception and up until 50MHz (just found this also).
4. Bonus: just found this antenna for 3.1-10.6GHz, can it be scaled down (or up? Down with the frequency up with the size)?

## Accepted answer (score 4, by Marcus Müller)

This is definitely not a definite answer, but let's start an answer to gather insights:

## The PA0RDT mini-whip design. Allegedly 10kHz-20MHz […] Uses JFETs and I don't have a cheap source for them. I would settle for an equivalent.

That's just an active antenna. The antenna part is a really small rectangle, and thus, the reception efficiency is extremely small. The power levels coming out of the device are only high because noise and signal have both been amplified.

- An "active antenna" such as the mini-whip is really just an antenna with an integrated amplifier, nothing more or less.
- The mini-whip isn't a wideband antenna at all – the antenna part is just consistently bad across all frequencies of interest.
- I don't know whether we've talked about this – but usually "I can't source JFETs" is more of a misunderstanding, and not a fact, lest you're living in a really remote region of this world. Also, you can usually replace old JFETs (depends on the type, of course) with modern MOSFETs and get even higher input impedance with same gain & noise specs.
- Being kilometers in wavelength, the 10 kHz – 20 MHz range will definitely require you to use an electrically short antenna, so might as well just use this
- Beware that the high gain of this amplifier, plus the fact that the rectangular aperture antenna actually used by the mini-whip means that it's extremely susceptible to noise pickup from nearby electronics – there's nothing "preferring" your signals of interest over noise of anything close to the amplifier. I'd argue you'd want to mount this antenna far away from your electronics.

## The Dressler-type antenna for 50MHz-2GHz

That's a very, very interesting antenna design, from an antenna theory point of view. It's a true wideband antenna, and that's by the fact that it's basically made of a gap between two conductors that increases over its length – think of an array of dipoles, each one with a different length.

- Larger, hard to build, probably not really all that efficient at the lowest frequencies, but pretty!
- I'd argue that it might pay most to restrict it to 200 MHz – 2 GHz; that makes building easier

## Loop-amplifier-balun

Loop antennas is actually what I'd go for in the lower frequency regime.

But: Loop antennas inherently have very bandwidth. They're never wideband. You'll need to *tune* them to achieve more frequency coverage (the bandwidth of an antenna is what it can receive at any *single* point in time, without detuning it). The article claims its antenna is "wideband", but that's not true – it's just "consistently good enough with amplification", see the mini-whip (of course, a large loop diameter makes for a much more efficient receive antenna than a small patch of metal, but still, not an efficient antenna at a wavelength that is 3 orders of magnitude larger than the antenna).

And: Amplifier circuits based on the transistor BF494... sigh. These transistors have become obsolete a long time ago – there's simply cheap replacements that are superior in every technical aspect, especially temperature behaviour, noise and inter-device variations, that engineers designing a circuit post-1990 wouldn't even consider these devices. But, that's the beef I have with ham magazines, schematics are covered by the editors for decades (not only years, decades), without critical inspection.

And that's the primary reason why there's a huge disconnect between what is technically possible and cheap these days and what's used by amateurs all over the world. Whilst the physics governing how antennas must be shaped haven't changed over the last 90 years, semiconductor device state of the art has.

It's beyond me how that happens – Circuits with transistors you can't even buy (aside from the astronomic prices of people who've bought up devices as soon as they went out of production) can't really be a selling point for magazines.

## just found this antenna for 3.1-10.6GHz, can it be scaled down (or up? Down with the frequency up with the size)?

Exactly, down with the frequency, up with the size, inversely proportionally. So, to get this from 3.1 GHz – 10.6 GHz down to 3.1 MHz – 10.6 MHz, the thing needs to be increased in size by a factor of 1000.

I'd argue that this is a relatively hard design to scale up. Stick with the common wideband antenna types that can be implemented "flatly", being:

- logarithmic-periodic antennas (logper)
- Vivaldi Antennas
- Other tapered slot helicals (like the "Dressler"-type you mentioned)

## Other, commonly encountered things

- For the 50 – 250 MHz range, I'd really just go with a telescope monopole antenna – exactly the thing your old portable stereo has (had?). I'm advising someone who's been designing, testing and verifying a DAB+ receiver with nothing more than that. It works well, and is easily tuned to any specific frequency by extending/pushing it back together to be ¼ wavelength
- For the impressively low frequency ranges below 30 MHz, you'll probably want a resonant antenna (I think SDSolar would agree :) ), and that means you'll need a tunably capacitor or inductor. You noticed that, and asked a question pertaining to the design of tuners. It's easier than it looks (again... ham articles being 40 to 50 years stuck in the past).

## Answer (score 4, by Phil Frost - W8II)

Broadly speaking, there are two ways to make a broadband antenna:

## 1: self-similar designs

If an antenna looks the same at any scale, then it will work the same at any frequency. Examples of such antennas are the Dressler you link, but also the bowtie, spiral, fractal, and log-periodic dipole antenna designs. Practical considerations always dictate the self-similarity can't extend to infinity, but realistic designs can cover several octaves of frequency with a match good enough for reception purposes.

These designs will be best suited to the upper ranges of your 100kHz-2GHz objective, as they typically require that the lowest frequency has a wavelength on the order of the size of the antenna.

## 2: equally bad everywhere designs

If an antenna is small (say, less than 1/10th wavelength), it can be a bad antenna for a very wide bandwidth. The trouble is the impedance of this antenna will be very far from the typical 50 ohms, and so power transfer from from the antenna to the receiver may be so poor that it's unable to overcome the receiver noise floor.

Consequently, designs of this sort will almost always be "active", meaning there's an amplifier involved. A challenge with a wideband amplifier is overload. If you live near any commercial broadcast station it may drive the amplifier into saturation, causing harmonic distortion everywhere, rendering the antenna unusable. Some designs include filters to reject broadcast bands for this reason.

Since these antennas are electrically small, they will work best at the lower range of your 100kHz-2GHz objective.

Broadband active whips and dipoles are relatively common. A similar design can be achieved with a loop, although it's not common.

Most "small" or "magnetic" loop designs involve some capacitance at the feedpoint to make the antenna resonant at a particular frequency. Tuning the antenna this way is equivalent to putting inductance at the base of a dipole. This can very much improve the impedance match at a narrow range of frequencies, but it totally destroys the wideband characteristic.

Thus to get a truly wideband design, it's necessary to design an amplifier to work with the antenna that does not require reactive components to tune the antenna. For dipoles, this means an amplifier with a very high input impedance. For loops, a very low input impedance.

High impedance JFET amplifiers as you've found are a common design. Often, these designs will specify some JFET that's inexplicably difficult to source, and expensive if you can find it. More often than not, it's because the part is decades old. You will find designs with germanium diodes for the same reason.

Usually, these parts can be replaced with a more modern JFET. Or with some adjustment to the biasing, a MOSFET. Given that you'll likely be designing this antenna for relatively low frequencies, transistor selection is really not that critical, and just about anything can be made to work with a little engineering. Unfortunately that's a broad topic, but maybe it gives you some ideas for further questions :)

I recommend taking a look at LZ1AQ's homepage. In the articles along the left there's some great information on wideband active antennas, including some designs which look very reasonable.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/8965/choosing-a-wideband-antenna-design, by Luca, Marcus Müller, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
