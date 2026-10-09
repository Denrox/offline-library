# Interpreting (noise) signals from a small untuned shielded loop

*Tags: antenna, loop · score 3*

## Question

This a follow up from this question: [QRN: How to chase down a solid S9 noise floor on 40m only](QRN%20How%20to%20chase%20down%20a%20solid%20S9%20noise%20floor%20on%2040m%20only.md)

Focusing on how to interpret the signals received with an electrically small, untuned "shielded loop". The following background articles/questions on this type of antenna explain how it works, how **not** to construct it (eg ARRL 1998), and what it can and cannot do:

http://www.w8ji.com/magnetic_receiving_loops.htm

[What does the addition of a shield to a small loop accomplish?](What%20does%20the%20addition%20of%20a%20shield%20to%20a%20small%20loop%20accomplish.md)

[Is it possible to make a shield that blocks time-varying electric fields, but not time-varying magnetic fields?](Is%20it%20possible%20to%20make%20a%20shield%20that%20blocks%20time-varying%20electric%20fields%2C%20but%20not%20time-varying%20magnetic%20fields.md)

I followed the construction advice in this blog article quite closely, including the use of a pre-amp and a tinySA to amplify and analyse the signal (photos of my implementation in [original question](Is%20it%20possible%20to%20make%20a%20shield%20that%20blocks%20time-varying%20electric%20fields%2C%20but%20not%20time-varying%20magnetic%20fields.md))

The core of main challenge, which to find the source of my S8-S9 white noise floor, amounts to these tinySA screenshots.

Elevated noise floor when tinySA connected to my fan dipole:

Signal from the loop when standing under that dipole:

The elevated noise floor is not present. (Note that that I have (hopefully) eliminated conducted noise and feed line shield noise in [original question](QRN%20How%20to%20chase%20down%20a%20solid%20S9%20noise%20floor%20on%2040m%20only.md)).

So the questions are:


How to interpret the loop signal relative to the dipole?


Why is there no elevated noise floor on the loop?


Is it a matter of sensitivity / level of amplification? The comparative levels of identifiable signals (best reliable example is 7.074MHz FT8) seem to vary with FFT bin width on tinySA. If I scan 7Mhz to 7.2Mhz (as opposed to the wideband 3-12Mhz shown in pics above) which gives me a 3kHz bin width (very similar to LSB bandwidth used for S-level indication of about 2.7kHz) then FT8 is show on tinySA at about -90dBm on the loop after pre-amp (vs S9+20dB on the FT450D meter). The noise floor being about S8 on the radio at that time, would be 26dB down from that and would put it below the noise floor of the tinySA. Yet other information suggests that the loop with a 20dB pre-amp should show similar signal levels to the dipole?


Or are the dipole and the loop just detecting different signals? ie the loop is not seeing the noise floor? Lower height above ground? Near field vs far field debate.. etc.


How can I further narrow this down? ie if I can't see the noise floor with the loop, I can't locate its source and can't hope to eliminate it.

**Update 28/4/2021** Further to some very good suggestions from Phil Frost I have carried out some of the tests he suggested. Results below.

**Baseline for today** (somewhat lower noise yeah! lowest I have ever seen during daytime - slight drizzle outside...) Normal Antenna setup at radio:

FT450D: 7.074Mhz FT8 S9+10 to S9+30 and baseline noise in 40m Band is 6.5S-units

tinySA: on dipole via 22m feedline => 3-12Mhz span base -80dB peaks -50dB

**Loop standing under dipole**

Direct to tinySA via 10cm feedline => -95dB with peaks to -70dB **no raised floor**

FT450D via 22m feedline => ft8 S4.5 on radio. Noise floor in Band **S0**.

TinySA via 22m feedline => -95dB baseline with peaks to -70dB

**Dipole fed with short, vertical 5m RG58 feedline into tinySA**

tinySA standing under Dipole fed by 5m coax => Very similar to via the 22m feedline -80dB base with peaks to -50dB. Maybe slightly higher (less attenuation?)

**Conclusions from these measurements**


The raised noise floor is not coming from the feedline. Both the above tests, and earlier tests terminating the feedline at feedpoint (under original question) agree on this.


The raised noise floor is not coming from my rig (FT450D) or anything connected to it, like power supply or ground, because the tinySA fed via 5m short coax standing under dipole produce same results as in shack and as the radio. The is also corroborated by earlier tests in original question, where I ran radio on battery with whole house turned off.


The loop receives far field signals (eg 40m FT8) much more weakly than the dipole. Compare S9+20dB to S4.5 on FT450D via the same 22m feedline. That's a difference of 40dB+. The tinySA shows less of a difference but still 20-30dB. This is true when measured by 10cm coax feedline or via 22m feedline back in shack. The raised noise floor is not visible via the loop, could be because both wanted and unwanted signals are much smaller. Smaller signals could be because:


 1. the loop is lower to the ground / obscured by nearby buildings

 1. the loop has much lower sensitity for which the 20dB preamp cannot compensate

 1. anything else?

It's hard to ascertain where the raised floor is coming from because our loop seems not sensitive enough. Or we need to get it experimentally closer to source of noise by trial and error. (eg area around tips of dipole).


The author of blog article I followed (KA7OEI) for loop construction seems to suggest that from his experience, such a loop with such a pre-amp should give signal strengths roughly comparable to a full size antenna. I tested the pre-amp with AWG and Oscilloscope, so I am pretty confident about that. So either my construction of the loop or some other factor is making my loop much less (20-40dB!) less sensitive than it should be??

-- end of update

Many thanks

## Answer (score 4, by Phil Frost - W8II)

You've stated in your other question that you've tested the loop and you are able to receive signals, so it works to some extent. So a few possibilities remain.

Firstly, the presence of signals does not necessarily mean the loop is working well. It could be that the noise you are trying to find with the loop is below the receiver's noise floor. Hard to test this for sure without an anechoic chamber, but you can get a pretty good idea just by comparing the number of signals you can hear (especially the weak ones) with your other radio. If the loop can hear many more stations, it's working. If it can't, it's likely the loop's noise floor is masking them.

Another possibility is the noise isn't being received by the antenna, but something else in your station. That could be the feedline, the receiver, or any of the other wires connected to the receiver, including the power cord, all the electrical wiring in your home, any cables you may have to interface your radio with your computer, anything attached to your computer, or any ground connections or even the ground itself. Or anything connected to those things, such as the power lines, your neighbors, or communications cables running around the neighborhood. It could even be a noise source simply in the same room as the receiver: the receiver's shielding isn't perfect.

To check this, I'd run a short feedline from the dipole to where you were standing when you made the measurement with the loop that showed no noise. Then listen to the dipole with the same receiver you used with the loop, while standing in the same spot.

If the noise goes away, you know the antenna isn't the problem. Start walking around the house and disconnecting things and turning off things until you've narrowed down the source. Powering your radio from a battery and turning off your home's main circuit breaker, then turning circuits back on one at a time can be informative. It could be you need a better balun on the antenna: you can [test your current balun for effectiveness](How%20to%20detect%20common-mode%20currents%20or%20RF%20in%20the%20shack.md). Or you may discover some noise sources in your house that can be controlled with ferrite beads or simply need to be removed.

If you still get the noise even with the short feedline and the portable receiver, then you may just have to look around more. Of note, the near field of the loop and the dipole are substantially different, which means if the noise source is in the near field of the antennas then one may be very sensitive to it while the other is not. It could be you just need to explore the area immediately around the antenna a little more with your portable receiver.

## Answer (score 2, by hotpaw2)

Did you try the loop sideways? (flat in a vertical plane both N/S and E/W, but with the feed out the side, not the bottom). Did you try the loop higher up, closer to the height of the dipole? Did you try the loop near the tips of your fan dipole? Are the broadband lines in the near field of your fan dipole? (much less than a full wavelength away?) If so, did you try the loop (in all 6 orientations) near the broadband lines.

Added: How does the hump in your fan dipole's RF noise correspond with the SWR and impedance curves as measured by your nanoVNA? Your RF noise floor may actually be closer to flat (no hump), as measured by your small loop antenna and tinySA. No hump.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18390/interpreting-noise-signals-from-a-small-untuned-shielded-loop, by Oliver Schönrock, Phil Frost - W8II, hotpaw2. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
