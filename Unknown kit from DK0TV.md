# Unknown kit from DK0TV

*Tags: receiver, diy, electronics · score 3*

## Question

When my father - who became a ham years after I did - passed away, I found an unstarted project (board + components), which I only re-discovered again years later.

The board is marked DK0TV-001, and uses three ICs (as marked on the silk layer) SO42P, TCA1047 and TAA611. Apparently it converts 30 MHz to 10.7 MHz using the SO42P (with a 40.7 MHz crystal), then demodulates and amplifies.

Looking over the internet DK0TV barely pops up, a little strange considering this seems to have been the club callsign of a german broadcast station (ZDF2?).

Even though this call/kit probably pre-dates the internet, I am somewhat saddened I could find so little, and somewhat intrigued what this kit was about. Anyone remembers this?

**Added images**

## Accepted answer (score 7, by BERNARD)

This kit is a FM receiver built in 1977 by DK0TV. The receiver works on a single fixed frequency 30.000 MHz FM and has a very good sensitivity. It is used with a 10 GHz Gunnplexer to listen to the 3 cm band with a 30 MHz intermediate frequency.

Here are details on how it works:

- The input at 30 MHz is amplified by a dual gate MOSFET
- The S042P is a mixer with a local crystal oscillator at 40.7 MHz delivering an intermediate frequency at 10.7 MHz (40.7 - 30 = 10.7)
- The TDA 1047 is the FM demodulator working at 10.7 MHz and giving the demodulated audio at its output (*not* a TCA 1047)
- The TAA611 is the audio amplifier

This receiver can be used for example with a 10 GHz cavity with a Gunn diode to generate a local oscillation which is 30 MHz up or down from the frequency you want to receive on the 3 cm band. The 10 GHz elements are not in the kit.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15880/unknown-kit-from-dk0tv, by jcoppens, BERNARD. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
