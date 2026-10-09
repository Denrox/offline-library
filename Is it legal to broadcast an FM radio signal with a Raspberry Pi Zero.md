# Is it legal to broadcast an FM radio signal with a Raspberry Pi Zero?

*Tags: united-states, legal · score 3*

## Question

I saw a video lately where someone soldered an antenna to a Raspberry Pi Zero and broadcasted radio signals. https://www.youtube.com/watch?v=GXedC5dQyNk&t=9s They said they were not worried to do it because they were only going to do it for a few seconds, but I'd like to know if I could do it for extended periods of time. I am in ME, US.

## Accepted answer (score 2, by Mike Waters)

**Probably, as long as you don't interfere with others' FM reception.**

You are allowed a maximum range of 200 feet.

Judging from the length of the antenna and the apparent lack of a power amplifier, it is likely legal. I doubt whether that thing has a 50 foot range, and that's why I said that.

Here is the specific FCC rules page (which I didn't read, *but you should!*).

## Answer (score 5, by hotpaw2)

When running rpitx or pifm on a Raspbery Pi, the "transmitter" output uses an unfiltered digital I/O pin. Thus you not only need to worry about FM band interference, but emission laws and interference on any of the harmonic frequencies of the Pi transmit frequency setting, especially odd harmonics, but various non-linearities can even cause radiation on the even harmonics.

If you only want to worry about the Part-15 legality of low power transmission in the FM broadcast band, you will need to add a low-pass filter with a cut-off below the second harmonic (or a band-pass filter, or both) between the Pi and the antenna.

Added: The concept that seems not to be known by PiFM hobbyists is that a digital output does not produce anything close to a sinewave, but that the rectangular pulses produced by any periodic digital output consists of a spectrum containing lots of different sinusoidal components (Fourier's theorem) spattered across a huge portion of the entire RF spectrum, much of it well outside the RF band of interest.

## Answer (score 3, by jed martin)

the limit according to https://transition.fcc.gov/Bureaus/Engineering_Technology/Documents/bulletins/oet63/oet63rev.pdf is 150uV/m measured 3m from the antenna. however, if one of the harmonics or IMD products interferes with another service the FCC won't care about the radiation measurement anymore, and tell you to stop transmitting immediately. since the pi uses a GPIO pin for output, and the signal is unfiltered, the 7-or-8 bit modulation is sure to generate a lot of IMD and harmonics. the IMD may splatter in the aircraft band, and the harmonics may interfere in the emergency services bands.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7267/is-it-legal-to-broadcast-an-fm-radio-signal-with-a-raspberry-pi-zero, by anonymous, Mike Waters, hotpaw2, jed martin. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
