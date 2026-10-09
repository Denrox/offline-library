# Phased array (rx only) with separate complete receivers

*Tags: receiver, phased-array · score 6*

## Question

Is it possible to have a network of separate (but co-located) 'receivers' (antenna + adc) act as a phased array receiver?

Supposing one can get very precise timestamping on each receiver, couldn't all the receivers be assembled as a phased array?

I'm thinking about putting a bunch (4 for starters, at least 16 after) of uwb antennas and space them on a panel pointing all in the same direction, then for each antenna having a rtl-sdr or something better if necessary to acquire the signals with a very precise clock.

I want to receive specific signais, timestamp them precisely and then record them. Later in post processing, for some specific timestamp, I need to check the presence of the signals (using the whole array) and perform some analysis on them.

## Accepted answer (score 10, by hobbs - KC2G)

In short: yes, it's possible, but it's a bit harder than that. You want to drive all of the receivers from a shared clock, and sample them in phase with one another, to form a "coherent receiver". This requires some hardware work; you can't just plug multiple regular RTL-SDR sticks into a computer and make it work.

There *are* some coherent RTL-SDR projects that you can find by searching, though. Some of them seem to be available for purchase, and others are research projects. Some of them have code to illustrate how you can take the streams from those multiple receivers and use them to do things like direction finding or passive radar; studying them would probably be helpful if you want to figure out how to do similar things on your own.

I've seen something related from people who are doing VLF/ELF experimentation. Since they're working with frequencies under 100kHz, they can use commercial audio interfaces (sound cards) as direct-sampling receivers. If they set up two antennas at 90° angles from one another, and connect them to two channels of the same audio interface, they get a phase-coherent recording of both of them. Then they can phase and combine the two recorded channels to "electronically steer" the antenna *after the fact* of receiving a signal, to maximize the signal-to-noise ratio and the decode probability. Pretty crazy, isn't it? We're probably not far from being able to do similar things with HF using off-the-shelf hardware.

## Answer (score 5, by uhoh)

In Radio Astronomy, arrays are phased either by a distributed local oscillator, or by reconstructing the timebase (local atomic clocks synched to GPS) during analysis by also listening to known strong signals.

- this answer to *Why does the Event Horizon Telescope (EHT) not include telescopes from Africa, Asia or Australia?* describes *some of how* this is done at 230 GHz.
- this answer
- this answer

Source

Data sampled at a baseband of 2 GHz, recorded on hard drives, air shipped to a central location where interferometry is reconstructed from independent local oscillators using an algorithm exploiting known stronger signals in the same field of view.

This also allows for off-line geometrical corrections and light-path corrections (ionosphere, water vapor)

See also

- this answer to *Precise Event Horizon Telescope locations?*

For a distributed local oscillator via fiber optics, see answers to

- How does ALMA produce stable, mutually coherent ~THz local oscillators for all of their dishes?

https://www.youtube.com/watch?v=lbjCq8-ksBQ

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18870/phased-array-rx-only-with-separate-complete-receivers, by Touisteur EmporteUneVache, hobbs - KC2G, uhoh. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
