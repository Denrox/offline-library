# Very odd and wide 30m signal. What is it?

*Tags: software-defined-radio, hf, signal-identification · score 4*

## Question

A local ham friend copied this strange, wide signal on 30 meters on his Flex 5000. Anybody know what it might be?

## Answer (score 5, by Marcus Müller)

If I read the instrumentation correctly, this is but 20 kHz; that's pretty wide for what I'd expect for Ham operation on HF. It's not "very wide" per se. (I'd define "wide" based on the ratio of bandwidth to center frequency, and that's but 0.2% here.)

This looks a bit like an OFDM signal, especially with the hints of side lobes. 20 kHz OFDM in HF sounds a lot like *Digital Radio Mondiale*.

I don't know of any specific allocation of 10 MHz spectrum to broadcast licensees. However, since there is a really good free and open source DRM transmitter, built atop of GNU Radio, named gr-drm, this might very well be legitimate Ham usage; admittedly, using the high-quality channel mode for DRM does use a lot of bandwidth compared to a classical AM voice channel, but at the same SNRs, DRM sounds worlds superior if using the right voice codecs.

In Germany, for example, 10.000 – 10.150 MHz is reserved to FESTER FUNKDIENST (fixed radio service) application with "messages to one or multiple recipients" as primary, and Amateur Radio as secondary usage. p. 94 of the Frequenzplan

## Answer (score 2, by Rowan Hawkins)

I also didn't notice that box before, but it has the date as well, 2017-01-08 in it(YMD), a Sunday.

The center is 10.130, and at S7 that's fairly strong. Also I think the actual signal is 26khz wide with the 3khz side lobes.

I don't think its DX. At 9am the sun is well up, the ionosphere E layer has merged back into D. There would be no grey line propigation in play. I realized there is a viable alternative answer...QRM.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7216/very-odd-and-wide-30m-signal-what-is-it, by Mike Waters, Marcus Müller, Rowan Hawkins. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
