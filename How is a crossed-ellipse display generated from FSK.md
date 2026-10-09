# How is a crossed-ellipse display generated from FSK?

*Tags: software-defined-radio, rtty · score 5*

## Question

What is the algorithm or circuit needed to generate a (vintage?, retro?) crossed-ellipse display from RTTY and/or 2FSK signals?

(as per the (obsolete?) questions in some FCC exam pool)

(assume already down-converted from HF RF to either/or a baseband IQ data stream, or audible AFSK)

## Accepted answer (score 4, by hobbs - KC2G)

Judging by this blog post from AI4SV and an inspection of the source code for fldigi (which supports such a scope in its RTTY mode), it's pretty simple — you just run the AF signal through two narrow filters at the mark and space frequencies (exactly as you would normally do when decoding RTTY), and then use the mark signal to drive the X axis and the space signal to drive the Y axis (or vice versa). You should AC-couple each signal (digitally, subtract it from a lowpassed version of itself) so that the display remains centered regardless of the signal strength.

You can also downmix each signal, after filtering, to a lower frequency and use the downmixed signals to drive the scope axes. Fldigi does this, apparently as a digital convenience to make it so that there will be a whole number of ellipse-cycles per audio block / per display update, which makes the digital nature of the scope a little bit less obvious.

## Answer (score 6, by Kevin Reid AG6YO)

The display is simple:

1. Pass the incoming signal through two band-pass filters, one at the mark frequency and one at the space frequency.
2. Use the two filters' output signals as the X and Y coordinates of the plot.
3. (Since you are in the SDR domain:) Do as much as you want to make a nice-looking digital oscilloscope display of that signal. The simplest accurate way to do it is to keep a buffer of the last however-many filtered samples and draw them as dots (**not** lines).

If you had perfect signals and perfect filters, the display would not display ellipses but a straight line on one axis or the other. Since instead filters have roll-off, the signal is merely highly attenuated in the other axis, and an elliptical trace (for an input signal at a single frequency) results. The sharper your filters, the narrower the ellipses will be. The exact shape of the ellipse depends on the phase response of the filters (for example, an ellipse that is perfectly axis-aligned implies a 90° phase shift).

The "crossed" ellipses result from the modulated signal alternating between the mark and space frequencies and thus between the two possible displayed ellipses. A signal between the two frequencies will appear as a severely off-axis ellipse or a circle (because both filters are passing the signal), and one outside them will appear as an attenuated ellipse. Thus, you can tune a RTTY receiver by changing the receive frequency until the distinct horizontal and vertical ellipses appear.

(Disclaimer: I have neither used or implemented one. All of the details in this answer are based on reasoning from signal processing theory.)

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15253/how-is-a-crossed-ellipse-display-generated-from-fsk, by hotpaw2, hobbs - KC2G, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
