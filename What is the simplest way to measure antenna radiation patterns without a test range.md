# What is the simplest way to measure antenna radiation patterns without a test range?

*Tags: antenna, antenna-theory, antenna-system, microwave, radiation-pattern · score 3*

## Question

Measuring antenna radiation patterns usually requires access to an anechoic chamber or a dedicated antenna test range.

However many amateur radio operators build their own antennas and do not have access to these facilities.

I am curious if anyone has experimented with measuring antenna radiation patterns outdoors using simpler setups.

For example:

- using a reference antenna at a fixed distance
- rotating the antenna under test
- measuring S21 with a VNA (NanoVNA or LiteVNA)

In theory it seems possible to reconstruct the azimuth radiation pattern if measurements are taken while rotating the antenna.

But I wonder what the main limitations would be in practice:

- ground reflections
- multipath
- distance requirements for far-field conditions

Has anyone in the amateur radio community tried something similar?

## Answer (score 2, by Marcus Müller)

- using a reference antenna at a fixed distance
- rotating the antenna under test
- measuring S21 with a VNA (NanoVNA or LiteVNA)

That's an antenna test range / stand setup.

- ground reflection
- multipath

Eliminating these makes it a *good* antenna test range. Which one would be dominant fully depends on your setup's geometry. (and: ground reflection is just a special case of multipath. Ground being in the near field, directly affecting radiation pattern is a different problem, though.)

distance requirements for far-field conditions

Physics does not negotiate. If you want to measure far-field, you need far-field.

Has anyone in the amateur radio community tried something similar?

yeah, I've seen numerous rotator tables in self-built setups, mounted on wooden towers. Built something like that myself for an ad-hoc characterization of a pair of dual-band wifi antennas. Effort is a rotating base, enough wood and knowing how to make dovetail joints, because you don't want to have nails or screws affecting the reactive near field, a VNA, patience, and piece of paper.

Works for small wavelengths, because when your wavelength is 12.5 cm, it's easier to mount the DUT more than two wavelengths away from anything else than it is when the wavelength is 10 m.

For larger wavelengths, you either need a humongous setup, and then we're approaching budgetary needs that are reserved for the likes of large research institutions, or you need to say, OK, this antenna will anyways never be used "floating free in space", it needs to be measured *including* its surroundings.

That's standard procedure.

I don't know whether these were hams, and I also don't think that makes *any* difference (why would I trust a ham more than a non-ham engineer of the relevant qualifications?):  
Determining radiation patterns of large stationary antenna systems using drones with sufficiently precise positioning systems and mounted measurement devices is something that RF system engineers do, yes.

This can be found all over the internet – the phase when that was new was around 10 to 15 years ago.

You can these days buy systems, for example this one (random pick, first search result, no affiliation).

From skimming this quickly,

Kandregula VR, Zaharis ZD, Ahmed QZ, Khan FA, Loh TH, Schreiber J, Serres AJR, Lazaridis PI. A Review of Unmanned Aerial Vehicle Based Antenna and Propagation Measurements. Sensors (Basel). 2024 Nov 20;24(22):7395. doi: 10.3390/s24227395. PMID: 39599171; PMCID: PMC11598646; available online.

is a sensibly well-written survey on techniques employed.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/23828/what-is-the-simplest-way-to-measure-antenna-radiation-patterns-without-a-test-, by Umut Bulus, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
