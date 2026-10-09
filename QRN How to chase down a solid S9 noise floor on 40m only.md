# QRN: How to chase down a solid S9 noise floor on 40m only

*Tags: hf, rfi, noise, direction-finding, reception · score 4*

## Question

I am new to this, having just set up my station. I have "very bad" QRN on 40m: S9. Here is the setup:

- High density suburb with flats and houses
- Yaesu FT450D with fan dipole at 6m-9m above ground (sloping), this is lower than a building with flats to the North East. Wires for 40/20/10m, nicely resonant, checked with NanoVNA.
- 1:1 Balun (ie choke) at feedpoint. 15 turns on FT240-52. No evidence of RF in shack.
- 22m RG58 run back to station which is on first floor
- Station earth dropping about 3m from 1st floor to 1m driven ground stake (I realise this may not be effective, as run is too long)

These are the things I have tried:

- 40m QRN is consistently > S8 mostly S9 during the day. Grainy white noise.
- 20m and 80m are only S3.
- Noise drops slightly at night but only 1S unit.
- Turning off all power in house with radio on battery reduces it to ~S7.5 so about 1 S-unit. Still a long way from level on 20m and 80m.
- I have tested calibration of S-meter on all bands with signal a generator and a 40db Attenuator. It's within spec acc to the service manual.
- There are some "VDSL" (UK broadband) training tones giving me a "birdie" every 4kHz. But this is only on some days and appears not related to the background S9 "grainy white noise floor".
- Our own broadband line runs almost parallel to the dipole (I have put as much angle as I can but it's < 20 degrees). But turning our router off (as above) doesn't remove the "main" source.
- I cannot detect the "VDSL guard bands" at 5.2, 8.5, 12Mhz
- Noise appears solid across all of 40m, ~6Mhz to about 8Mhz
- I can make contacts on 40m but only with "booming" stations.

**Edit: additional info from discussion in comments below** To test for radiated vs conducted noise I also performed these tests:

- I have a second FT240-52 toroid with 10 turns of RG58 at the radio end about 10 inches before the PL259. It was spare so I thought I would add it. Made no difference.
- The radio running on battery without antenna is totally quiet on all bands.
- With linear 12V power supply it is also totally fine without antenna.
- As soon as I plug in the antenna I get S9 noise on 40m.
- The same even with a "random 5m wire thrown out the window and shoved into the centre of antenna connector on the back of the radio."

**Also**: I was taking HTs for a walk with my son today, and we walked past one of those green (UK colours) Telecom boxes about 100m (?) from my dipole. The interference coming off that thing was enough to break through the squelch of our Baofeng HTs tuned to 2m. On FM! Similar cabinets around the neighbourhood showed no sign of interfering with the radios, even with the squelch fully off. Could be a lead?

What is my logical next step?

Run around the neighbourhood with a portable HF radio and a directional loop antenna? Requires some investment? How about a NanoSA, which might be a useful tool anyway?

If I find source, what are options: 1. work with neighbours 2. use a phasing noise canceller?

Any tips much appreciated

**Update:** I am in the process of building this loop: https://ka7oei.blogspot.com/2021/02/rfi-radio-frequency-interference.html The pre-amp is built and tested. Have made a wooden frame for the loop. Just needs putting together. I am hoping it will help me understand if I have one or many (major) noise sources. There is an 11kV distribution transformer about 40m from dipole, which would be a great candidate!

**Update#2**: Loop is built and seems to be working. I can receive distinct signals on the tinySA (see above link) and the loop is definitely very directional - able to completely null strong signals. What does it mean? I don't know yet. There is a contest on, so 40m band is drenched in "wanted" signals. :-) -- I may need another amplifier stage to look at the "noise" in more detail, but I suspected that, and left room for it on the circuit board. TBC... If anyone has experience in using such a loop with spectrum analyser please comment or add answer. I have a feeling operating the loop in a structured way to get meaningful results is going to be key.

**Update#3**: First test results with loop - hard to interpret: This is the Loop:

And the preamp:

And the tinySA fed from my dipole from 3-12Mhz, clearly showing the raised floor that I am also seeing on the S-meter.

And the tinySA showing the signal from the amplified loop **standing under** the dipole.

The loop is clearly working and showing signals. And these can be nulled by rotating, but it does not show the "raised floor". Why? I am not sure how to interpret this.

M7BTU

## Answer (score 4, by Fritz - V51WF)

Look around your neighbourhood or Google satellite imagery for new solar panel installations. We recently discovered a solar panel installation with noisy regulators creating noise at a neighbours house.

Also as you mentioned that LED lights are also creating noise. Look for new street lamp installation nearby that is using the new LED replacement lamps.

## Answer (score 3, by hotpaw2)

If the RF noise is that strong, then you should be able to pick it up with a much smaller movable antenna. Even scrap wire or conductive tape on a large cardboard box. That may allow you to build small directional antennas (tiny loop and stub dipole) to determine if the noise is stronger from some specific directions, or a polarized antenna to determine the noise polarization, if any.

## Answer (score 2, by rclocher3)

I'd suggest trying a different time of day, a different radio, a different antenna, and a different location; not necessarily all at the same time though. There's probably nothing wrong with your antenna, but you might get different results at different heights, or if you raise the height of the ends to the same height as the middle.

Have you tested the noise level at different times of the day? Maybe there is a lot less noise at 4 AM. That would be a clue.

You could ask other local hams who are on 40m. What are their noise levels? Are they using vertically-polarized or horizontally-polarized antennas? Your high noise level might be particular to your neighborhood, and asking several different hams might help answer that question. If a local ham reports that his or her noise level is lower, you might ask if you could test your radio in his or her shack. The problem isn't likely to be the radio, but it's possible, and testing your radio against another radio with the same antenna could help determine whether the radio is the problem or not.

You could try a portable HF radio and a loop antenna, but those can be expensive; you could also try your existing radio powered by a battery connected to a 40m dipole flung up into the trees in a nearby park or wilderness area, if you have such places in your area that allow such things. If your problem is local noise, which it likely is, then your radio and a dipole in a rural or wilderness area would likely be quite an improvement (assuming that you live in an urban area).

Once you have a better idea of the source of the problem, then you can think about potential ways to narrow the problem down further, or ameliorate or solve the it. If your problem is local noise, then there are lots of questions and answers on this site about tracking down and dealing with local RFI. Feel free to ask a new question once you know more.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18285/qrn-how-to-chase-down-a-solid-s9-noise-floor-on-40m-only, by Oliver Schönrock, Fritz - V51WF, hotpaw2, rclocher3. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
