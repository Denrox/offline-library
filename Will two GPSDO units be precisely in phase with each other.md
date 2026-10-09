# Will two GPSDO units be precisely in phase with each other?

*Tags: frequency, oscillator, gnss · score 4*

## Question

I always thought of a GPSDO as only a precise **frequency** reference. But the GPS and other GNSS systems also deal with rather precise UTC/TAI-ish time!

Are the outputs of any two GPSDO units generally designed/expected to provide the same **phase** reference as well? That is, could I expect either the 1PPS output to pulse at ± exactly the same time on all GPSO units worldwide, and/or expect that any 10MHz or configurable frequency output would similarly have its phase aligned with the ticking of the constellations' clock(s)?

## Accepted answer (score 3, by tomnexus)

**The PPS outputs** should be in phase, subject to:

- the inherent accuracy of the GPS, depending a but on signal quality, antenna location and ionosphere, also affected by the imperfect a priori knowledge of the orbits
- the configuration of the GPS receiver, whether the antenna cable/filter delay is correctly typed in, etc
- quantisation by the receiver PPS output circuit, which cannot generate a pulse at exactly the right time, it has to be on a clock edge. The GPS might tell you the error in a message.

Together these will add up to a few hundred nanoseconds between GPSs, maybe less if you are careful.

Here's a quick experiment, measuring the time difference between pairs of GPS receivers:  
  
Because this is without any sawtooth correction (so each GPS has a random +-8 ns error), you should expect the distribution to have a smooth top about 30 ns wide. But they're a lot wider, which shows the inherent accuracy of the GPS.

Between brands there is also a fixed offset, and a slightly different shape.  
Note that the total width here at the 1% probability level is about 250 ns.

Note that this is every pulse from the GPS's own PPS output. A good GPSDO will first steer a crystal oscillator, then divide that down to provide 1PPS. This will effectively give a ~10 minute smoothing of the PPS times, so you could probably expect a 10 x reduction in the amount of wander.

**The phase of the 10 MHz signal** depends on all of the above, but also on the control algorithm choices:

- FLL vs PLL. Some GPSDOs are a FLL only, so they don't attempt to perfectly track phase
- holdover recovery strategy - should it attempt to correct the phase, or rather bring the frequency back to 10 MHz as quickly as possible, disregarding phase
- loop bandwidth, how aggressively the oscillator should be steered towards GPS. This will be chosen depending on the quality of the oscillator, the performance of the GPS, and your preference for a particular part of the spectrum to be most accurate.

I suppose these factors could add up to another few hundred nanoseconds of phase difference between two GPSDOs, in poor conditions, less if they're identical units in a stable environment.

You specifically asked about *two* GPSDOs, but for more information here are some graphs comparing *one* well regarded GPSDO, a Trimble Thunderbolt, compared to an atomic clock.  
Notable findings:

- The phase of the 10 MHz signal wanders by about +-8 ns (at peak) over each second, much less if averaged for some time.
- The expected time deviation over 10 minutes to a few hours is in the order of 1 ns

Remember these plots ignore fixed time offsets. Two identical units could be expected to have about 1.4 x the phase error between them. Not bad!

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21423/will-two-gpsdo-units-be-precisely-in-phase-with-each-other, by natevw - AF7TB, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
