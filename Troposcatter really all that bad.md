# Troposcatter: really all that bad?

*Tags: digital-modes, propagation, vhf, uhf, microwave · score 7*

## Question

The previous question,

Packet Radio at 100 miles

and specifically, Phil's answer raised an interesting question:

In a 50–100 km distance situation where Line-Of-Sight beams aren't an option for communicating data, can we, given the technological advances of the last decades, again consider troposcatter a sensible mode of operation for moderately high-rate bidirectional communication?

I ask because troposcatter typically has the reputation of needing pretty large TX powers, and pretty high-gain antennas. Which does sound reasonable, since, obviously, we rely on the reflection of something which isn't such a great reflector at all, plus the area we'd illuminate with an isotropic antenna would be huge (considering a sphere with r=100 km or more).

On the upside, we get great ranges if we actually do blast out a lot of power and aim large antennas at the horizon.

I'd assume you'd want to operate somewhere around 2.3 GHz. The best model description I've found (that wasn't "oh, we've always used these 2 models, and it doesn't really work all that well, but we didn't check for other models" example ) is from this nearly ancient Master's thesis:

UNDERSTANDING TROPOSCATTER PROPAGATION  
by  
JOSEPH HENDERSON REYNOLDS  
B.S., United States Air Force Academy, 1982

available online

After inspecting the summaries on the different models, I think that for VHF, UHF frequencies, probably what the call CCIR method II (by Boithias and Battesti) is what I'd want to look at. However, best graph I could produce on short notice (p.162 from that thesis):

for other frequencies, a factor of $30\log f_\text{GHz}$ is added.

so, I'd need to add another 3 dB; OK. Now, going for a < 1% outage time, I'd have to read both the upper (year average) and lower (worst month) chart's lower two curves (99% and 99.5% temporal availability). That yields something between 212 dB and 216 dB (average) / 218 dB to 222 dB (worst month) attenuation for a 150 km link.

Now, assuming we don't want to overdo it with antennas, an antenna gain of ~ 18dB on each end sounds realistic. Swinging with -220 dB tropo path loss, we thus get an overall loss of -184 dB.

Admittedly, not very little, still much better than GPS reception, and we legally get up to 10 MHz of bandwidth in that band! (as far as I understand)

Ok, rough capacity estimate:

Rolling a few numbers in my head, assume we want to get a code bit rate of let's say 200 kb/s. We'd want to stay a solid factor of 4 below the channel capacity (**please correct me!**), so that requires about 46 dBm transmit power – 40 W.

I don't think the atmosphere will allow for reliable amplitude estimation, (**please correct me!**) so I'd roll with QPSK for an initial estimate.

That gives me the rough feeling that we have plenty of headroom (like, 99 times what we use) to add robustness – be it through spreading, channel codes, or stupid spectral repetition.

This all breaks down on one thing, though:

I could find out *nil* about the properties of the 2.3 GHz tropo channel w.r.t.

- Doppler Spread
- Coherency Time
- Deep Fade probabilities

I might very much be coming from an indoor / close-range background, but this feels like I might be missing something important.

So

- **Does anyone have info on the above properties of the wireless troposcanner channel**?
- **Am I looking the wrong way, using the wrong tools to understand that channel?**
- **What (amateur) digital modes over tropo are *state of the art* (rather than *used because everyone uses them since the 70s*)?**
- **Is a 40W 2.3 GHz amp suitable for PSK realistic?**

## Accepted answer (score 2, by Phil Frost - W8II)

I don't think a better answer will come along, so I'll summarize a combination of assembled anecdotes and opinion.

As far as I can tell, your calculations are accurate. I did a little research for [Can tropospheric scatter effect be used by 802.11 links?](Can%20tropospheric%20scatter%20effect%20be%20used%20by%20802.11%20links.md) and determined the requirements aren't absurd, and at least within the grasp of a typical amateur.

Anecdotally, I've read of hams doing troposcatter on 2 meters. Many of the troposcatter studies I've seen don't consider anything below 2.4 GHz, so I guess it's possible.

Of course a 40W amplifier for 2 meters is common ham gear. 2.4 GHz isn't nearly as popular for hams, but a quick search turned up plenty of 10W amplifiers intended for 2.4 GHz WiFi.

I also was not able to find any details on the channel besides loss. However, I see many examples of military systems like these:

Some are mounted on trucks. I've read each horn has two polarities. We can infer the quad antenna diversity setup is to counter channel fading which must be significant. Although, the military certainly has higher reliability requirements than an amateur. HF channels have similar properties and that hasn't stopped anyone.

Anecdotally, most of the amateur troposcatter seems to be SSB or CW from VHF DX enthusiasts. I'm not active in this space personally, but I do know some weak-signal digital modes are gaining popularity there. WSJT is notable, and JT65 in particular which I have used personally on HF. It's very slow and not meant to exchange anything but a call sign and a signal report over a QSO that lasts several minutes.

D-STAR is a popular GMSK digital voice mode since Icom puts it in all their radios. It must be the most common digital mode on amateur VHF with a moderate bit rate. It has a data mode which enables a payload of arbitrary data instead of the usual proprietary AMBE codec for voice. I've no idea how suitable for troposcatter it would be.

## Answer (score 4, by Mike K6ML)

Troposcatter is the common mode for beyond line of sight on the 10 GHz ham band when the band is not otherwise open, good for 100's of miles. A radio with just a few watts output power and a moderate sized dish (60cm or more) gets enough ERP for troposcatter.

For a few random references, check out:

1. Pages 64-70 of http://www.mike-willis.com/Tutorial/RT%20Propagation%20Lecture.pdf
2. https://bobatkins.com/radio/troposcatter.html
3. http://www.nitehawk.com/w3sz/W3SZ-PackRatsConference2014.pdf
4. http://www.mgef.org/wa2aau/uWaveUp9.PDF

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7494/troposcatter-really-all-that-bad, by Marcus Müller, Phil Frost - W8II, Mike K6ML. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
