# How to operate on HF if an AM transmitter is only 540 feet away?

*Tags: digital-modes, rfi · score 10*

## Question

I'm a General Class Licensee, and due to pulmonary disease I cannot operate voice. I am also about 540 feet from a 24/7 1 kW AM station. The signal is so pronounced that most audio devices in the house pick up the station. Every shortwave receiver I've tried overloads (without an antenna) from 1-30 MHz. Any suggestions?

## Answer (score 4, by tomnexus)

First, find a transceiver which is properly shielded. When connected directly to a dummy load, there should be no breakthrough on any frequency (except the MW transmitter itself). Portable broadcast radio receivers are completely out of the question, but fairly recent ham gear should be ok.

Then, try a highpass filter to reduce the impact of the MW. I'd suggest starting on one of the higher bands, 15 m or 10 m. A simple highpass filter can be made with a quarter wavelength short circuit stub. On 15 m that's about 2.2 m of coax. Ideally for the stub you should use double screened coax like RG223, RG400 or hardline etc. Solder the stub into the radio end of a short jumper lead. A better filter can be made with more stubs or with discrete components.

Finally, take some precautions to reduce the pickup of the RF in the shack. Keep loop areas small - run coax, 12 V and power cables close to each other. Make a filter or trap for common-mode currents on both coax and power lines that enter the rig. Ground the coax shield to shack ground as it enters the shack. (forget about ground stakes, you're trying to keep differential voltages to a minimum). Use a horizontal dipole antenna, broadside to the MW source, as the MW fields are mostly vertical, and still somewhat *radial* as you're so close. Use a balun with good choking well below your HF frequency.

You may still be in trouble, if there are any non-linear effects in any gutters, downpipes, fences or electric cables outside anywhere near the transmitter. They could cause significant harmonics and intermods on your HF frequency, which cannot be filtered out.

## Answer (score 3, by scivision)

This is not necessarily an impossible problem. You might approach the problem iteratively, with a simple monoband receiver and expand from there as you see what works. Assuming you are able to solder, you could start with a 40m SoftRock receiver kit for $21, which plugs into your computer line-in sound card input for decoding of digital modes. On 40m (7MHz) you'd receive stations hundreds to thousands of kilometers away with a simple outdoor antenna, particularly on sensitive digital modes like WSPR and JT65. I would build that receiver inside a metal box, and start with a few meters of wire as an antenna.

If you don't have interference with no antenna and short antennas, but longer antennas bring interference, consider building a medium-wave bandstop filter, like these demonstrated to attenuate AM broadcast by over 50 dB.

Finally, consider that after filtering the fundamental on-channel AM transmitter, the N-th harmonics of that transmitter will be present and will have N times the bandwidth of the fundamental channel. If the AM transmitter was on 1000 kHz, it will have significant modulation energy from about 995-1005 kHz (more if using HD Radio transmission). The second harmonic will spread from 1985-2015 kHz and so on.

## Answer (score 2, by hotpaw2)

Assuming the AM station doesn't wipe out your internet connection, how about setting up a remotely operated HF rig far offsite (friend or relative's house, etc.)?], and operating it from your home computer (laptop, et.al.)?

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6874/how-to-operate-on-hf-if-an-am-transmitter-is-only-540-feet-away, by Gordon C, tomnexus, scivision, hotpaw2. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
