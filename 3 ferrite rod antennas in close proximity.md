# 3 ferrite rod antennas in close proximity

*Tags: antenna, ferrite · score 3*

## Question

I want to control a trio of radio controlled clocks. DCF77 (77.5kHz), JJY (40kHz), and WWVB (60kHz). Suitable signals can be generated with a microcontroller or Raspberry Pi. I will use ferrite rod antennas for this, with an expected range of a few metres.

Can I place the rods in relatively close proximity? Ideally in a U shape, with one alone each edge, or parallel like this: 三

I have a 70mm^2 enclosure, or I could get a bigger one if more separation is needed.

## Answer (score 2, by Ryuji AB1WX)

Do you really need a range of a few meters? Typically, those standard time signal emulators don't transmit a propagating wave but just create a magnetic field for near-field coupling, which fades rapidly with the distance.

I would question the need to use three separate ferrite rods. Since this is low power and low efficiency anyway, I would use one amplifier to drive the ferrite rod (untuned) for all three frequencies.

Another way to do it is to use one of those inductive couplers for non-contact chargers. Those Qi Standard coupler inductors are about 10 uH and they are typically tuned to minimize leakage flux. But for this application, the efficiency is not a goal, so untuned may be ok, though 10 uH may be a bit low for 40 to 80 kHz.

Another way to do it is to use a cheap audio loudspeaker. It may emit some ultrasonic sound, but we are, of course, interested in the magnetic field leaking from it. If you want to attenuate the ultrasonic sound, you can make the cone heavy by gluing something.

#### Addendum

From the comment exchange, the OP wants to mix two or three PWM modulated carriers and drive one antenna. Since all of these antennas are extremely low impedance and high loss, I would expect single-sided driving with high current capacity (emitter follower) is a good choice. Complementary push-pull would also be good, but I don't think the bottom transistor would contribute very much.

I just wrote this down and didn't do any calculations but I would suggest the following values as a starting point.

R1, R2, R3, R4 = 1k ohm

It assumes that the drive is 0 to 3.3V or 0 to 5V logic. It makes a class C amplifier, but it will be adequate for what it does. Adjust R4 (and R1, R2, R3 as needed) for the output power.

C1 set the cutoff frequency at 90 or 100kHz with the R's.

R5 22 to 68 ohm. Maybe start with 47.

C2 and C3 to form a very broad tuning and matching with L.

C4 and C5: 0.01 and 1uF.

R6: Maybe 100, maybe 10, somewhere between. Enough to protect the transistor when it is driven hard. Also, measure the voltage drop here to calculate the power dissipated in the transistor.

JJY has two transmission sites. One transmits 40kHz and another 60kHz.

I have a Seiko Astron (JDM) that picks up one of these signals, but the US East Coast is tough. I have an iPad/iPhone app that works, but I might be interested in building one of these projects. Please come back with updates.

### Addendum 2 iPad app emulating JJY/WWVB... corrected 29 Mar 2025 (Sat)

I tried to monitor what this app is doing. My watch can pick up any of: JJY (both 40kHz and 60kHz), BPC (68.5kHz), DCF77 (77.5kHz), MSF (60kHz), WWVB 60 kHz, and probably RBU 66.66kHz.

My app has a switch to select one station at a time (though missing RBU).

The setup looks like this. It's an iPad pro (larger size) with four speakers. The ferrite bar is placed above one of the speakers. It is very similar to Fair-Rite 61 mix, and it has about 11 turns.

The pickup above is totally adequate for diagnosing switching regulators, PWM drivers, etc. and parasitic oscillation in HF frequencies. However, I wasn't satisfied with the quality of measurement in AF to 40 kHz (for JJY 40 kHz emulation signal). So, I just made another pickup inductor with 3 bars bundled together, and wound a long-ish silicone rubber jacketed wire to increase the inductance and magnetic flux coupling.

My usual pickup is in the background of the above photo.

As you see, my environment and TinySA's background spectra contain deceptive peaks. So the difference between those traces are the real spectra from the iPad + app.

So, the app seems to use a single carrier at 20 kHz to emulate JJY at 40 kHz. The peak at 24-ish kHz is a small mystery since the iPad's internal D/A converter must be using an oversampling digital filter so aliasing shouldn't be there.

Not shown in the trace (outside the frequency range) but this setup also picks up the PWM switching frequency starting at 600 kHz range in the case of this iPad.

This setup is very handy when trying to detect noise sources or when something is suspected of parasitic oscillation at a rather low frequency.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/23431/3-ferrite-rod-antennas-in-close-proximity, by user1211, Ryuji AB1WX. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
