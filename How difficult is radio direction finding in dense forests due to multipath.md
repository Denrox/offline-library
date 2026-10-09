# How difficult is radio direction finding in dense forests due to multipath?

*Tags: antenna, direction-finding · score 5*

## Question

I'm an engineering student studying RF direction finding techniques and trying to understand the practical challenges of locating a transmitter in forested environments.

In theory, many DF methods assume a fairly clear signal path. But in forests signals may reflect from terrain, tree trunks, and other obstacles before reaching the receiver.

From my research so far, common DF methods include:


rotating directional antennas (e.g., Yagi)


Doppler direction-finding systems


sometimes antenna arrays for direction-of-arrival estimation

For my project I'm exploring the idea of using a small antenna array (around 4–8 elements) to estimate the direction of a beacon signal, but I'm trying to understand how realistic this would be in dense vegetation.

I'm curious about the experience of people who have done radio direction finding or fox hunts in wooded terrain:

- How much does multipath affect the apparent direction of a transmitter in forests?
- Do reflections from trees or terrain often cause the signal to appear to come from the wrong direction?
- What DF methods tend to work best in these environments?
- Are there situations where signal strength measurements become unreliable because of multipath?

Any practical insight would be greatly appreciated!

## Answer (score 5, by Ryuji AB1WX)

Vegetation itself is not much of a problem in HF and lower VHF. Terrain and uneven soil conductance (rocks vs wet soil) are bigger problems. Vegetation attenuates UHF and higher frequencies more severely, and uneven density along the path may fool your reading.

Multipaths can fool your reading, especially where the direct path is obscured by a hill or a building structure. If the direct path is unobscured, it is usually the strongest. If your beacon uses direct spreading and allows differential latency estimation, that information may also be useful.

If you are measuring total received power, multipath can definitely fool the signal strength. If you decorrelate using the spreading code first, the signal strength is accurate.

The antenna choice depends on the frequency. In UHF, you can build a sharp directional antenna rather easily, but in lower frequencies, antennas with a sharp null are easier to build (smaller, often dimensionally tolerant/insensitive). A sharp null is equally useful in direction finding.

Depending on the modulation scheme, you may have a way to know how significant the multipath is. In old analog television broadcasts, you could see the multipaths as ghosts. In FM broadcast, severe multipaths sound like a noise/distortion and are unpleasant. But direct spread is the easiest approach if the measurement of multipath is the objective.

## Answer (score 2, by Marcus Müller)

Just an extension to Ryuji's excellent answer; go and upvote that!

You will generally find that in anything related to EM propagation, random structures smaller than, say, quarter of a wavelength, just combine to a "diffuse" material.

So, for something with a 10 m wavelength, horizontally, a forest full of tree trunks are just "lossy, slightly scattery air"; for something with a 12 cm wavelength, that's not true, but the treetops made of leaves, being fractions of millimeters thick, just looks like "lossy, slightly scattery air". And the amount to which these approximations hold is dominated by volume percentages.

A common example is that a styrofoam box is practically RF-transparent for most wavelengths you will encounter – because while the polystyrene making up the solid parts of the foam is indeed slightly lossy at RF, and having a different $\varepsilon_r$ than air, will "bend" a wavefront (and thus making direction finding potentially ambiguous!), the percentage of solid material in the wall of the box is just not enough to make that a significant effect, and the thicknesses of individual bubbles are much smaller than HF and most microwave wavelengths. Not true for shorter wavelengths like visible light or infrared radiation – you can't look through a styrofoam box.

Same principle, though, extends also to structures closer to or even larger than wavelength, when the volume fill percentage stays low enough. You can see the sun, even when there's a lot of dust (e.g. a storm picked up dust over a faraway desert, or a wildfire raging) in the air, and that dust typically is much coarser than visible light wavelengths.  
Your picture will get tinted, and at some degree of fill, you will just almost certainly have an opaque particle in your way in every direction you might look, but it works pretty good for a long time.

Stand in the middle of dense fog, and instead of the moon as a sharp disk in the sky, you see a blurry shape that fills much more steradian of the sky than the actual moon does.

So, in the end, how well you can resolve the direction of something you observe "naively" is not a very binary thing. This "**naively**" is something that deserves more attention, see below!

How much does multipath affect the apparent direction of a transmitter in forests?

Much, if your wavelengths are shorter than the elements of trees in the direction you want to resolve (tree trunks are tall, but not very wide, so the E-field is anisotropically affected). Not much, if your wavelengths are much larger.

From personal experience based on a demo given by a former colleague: With a 72 GHz radar, you can clearly make out the different cadences at which individual leaves on the tree in front of the microwave lab window oscillate in the wind. Same radar antenna system, but for 72 MHz would mechanically be hard to build and not really fit the lab anymore, and could barely tell you there's a tree, maybe, somewhere.

Do reflections from trees or terrain often cause the signal to appear to come from the wrong direction?

Yes. As Ryuji says, super common effect. If you're in a valley surrounded by mountains, you will observe the FM radio tower serving the next town beyond the valley coming through the only pass that's low enough to conduct (through reflections, refractions) the FM waves, which might well not at all be the direction in which the tower is.

Smaller scale, in an urban scenario, your phone, which, if it's not a lower-end one or rather old, is equipped with multiple antennas to make use of the fact that there's independent paths for microwaves to travel from base station antennas to itself (we call that "MIMO channel", multiple input, multiple output channel) cannot reliably tell which direction the base station antenna is. But it optimizes such that the beams it forms with its multi-antenna frontend by phase-delaying and amplitude-scaling signals are maximizing the SNR it gets. So, highest power the receiver gets cannot be solely from the direction of the emitter, because there's multiple beams!

So, yes, very much the case.

Are there situations where signal strength measurements become unreliable because of multipath?

But, here's where I pick up on the term "**naively**" I used above.

I should have called it "power-detecting" instead. The first methods you describe just point an antenna in different directions to find the direction that has the highest power coming in. That fails in true multipath environments without a dominant direct path.

You can't do anything about these environments. To put it extremely: If I put a coax cable from close to the emitter right to just next to you, you would think the emission would come from the end of the cable, not from the true position of the emitter. That' also applies to ducts made of stone, rivers, vegetation or even precipitation corridors. Unless you have a very precise model of your environment and a very capable EM simulator, you can't even list candidate locations, and even with this (unlikely) availability of information, these solution would generally be ambiguous. You just can't know in which direction the emitter is at the far end of a pinhole channel! Is the antenna left or right of the far end of the coax? can't tell by the thing coming out of the coax.

The next most general case is environments where there's a direct path, but it might not be the strongest one, for example, because its partially occluded, filled with lossy material, subject to atmospheric variability…

In that case, you can still find the most likely direction by finding the path with the shortest distance. Unlike your eyes with moonlight, which famously is not a laser, your radio receiver can compare what it receives from multiple directions in time.

You can hence take an antenna array, apply a beamforming algorithm, find the top $N$ directions, and let a blind equalizer figure out an estimate of the channel impulse response for the signal from only that direction. That's as if you pointed a directive antenna in that direction, and then your receiver tries to figure out whether the received signal looks like it contains echos of itself, and if so, at which delays, phases and amplitudes.

Comparing these different channel impulse response estimates from different angles, you can pick the one that has the "earliest and most lone-standing" component, and proclaim it's the most direct path.

There's a catch: your transmit signal must allow for that. It needs to be wideband enough. A sine wave won't do at all! You cannot compare a sinewave to itself and say anything about multiple paths, because it's identical to itself, just one sine period later. Can't tell paths apart.

So, typically ham fox "beepers" are the most useless signal there. A good signal is wideband and comes with features specifically engineered to allow the receiver to estimate the channel impulse response (typically, to correct for it, to cancel all the echos). An example of such a class of signals is digital TV!

Late in the 1990s, early in the 2000s, high-end analog TVs appeared that had equalizers to cancel exactly the ghosting people were seeing on their screens, especially on higher channels, due to multipath. Analog TV signals are pretty wideband (order of 6 MHz), so you "see" things happening on the relatively small spatial scales ($c_0 \cdot \frac{1}{6\,\cdot10^6\,\text{Hz}} \approx 3\,\cdot 10^8 \frac{\text{m}}{\text{s}}\,\cdot\,\frac{1}{6}10^{-6}\,\text{s} = 50\,\text{m}$, which is a path length difference pretty realistic to appear in cities! Things get worse for color TVs due to phase sensitivity, but I digress).

The technological implementation of an analog equalizer was harrowingly complex and expensive. Easy game for digital TV to do better – because the designers of digital TV standards made it such that the signal can easily be analyzed in a way that allows for (frequency domain) estimation of the channel. That's why there's a lot of *passive radar*, which just uses digital TV signals from existing TV towers to estimate e.g. the presence of ships in harbors.

So,

What DF methods tend to work best in these environments?

digital beamforming methods based on multi-antenna receivers paired with channel state estimators and a model of how likely a given degree of attenuation is on the direct path vs indirect paths.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/23834/how-difficult-is-radio-direction-finding-in-dense-forests-due-to-multipath, by Cookie Pookie, Ryuji AB1WX, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
