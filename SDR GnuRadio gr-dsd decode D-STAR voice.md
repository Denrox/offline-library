# SDR GnuRadio gr-dsd decode D-STAR voice

*Tags: software-defined-radio, d-star, gnuradio · score 3*

## Question

Hy i found this projekt: gr-dsd i compiled it and it seems to work so far.

My problem is i don't find any Example just a Youtube Video (www.youtube.com/watch?v=DtkiC_Li_GI) wher it is used. Can some One tell me how i have to use this?

I tryed the folowing: osmocom source(hackrf 1) > nfm demod > dsd > audio sink I don't know if that is right how is D-STAR Modulated?

My Flow graph looks like this:

## Accepted answer (score 5, by Kevin Reid AG6YO)

You have the right general idea, but a couple of problems:

- **The sample rate entering the DSD block (hence the output of the FM demodulator) *must* be 48000 Hz; this is hard-coded in gr-dsd.** From your screenshot, you have 35k where you need 48k.
- The deemphasis (a.k.a. tau) of the FM demodulator should be set to None, rather than the default of 75.

In my experience gr-dsd will work for D-STAR. As a development strategy, first build an analog narrow FM receiver, test it on analog radio (e.g. on amateur FM or weather radio) to make sure the filters and rates are correct (you can hear the output, and there is no over/underrun), then add the DSD block to the chain.

Also note that it is possible for there to be a digital signal present but no audio to decode. Silence doesn't mean it isn't working; gr-dsd will print text whenever it successfully decodes packets.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5844/sdr-gnuradio-gr-dsd-decode-d-star-voice, by maxbit89, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
