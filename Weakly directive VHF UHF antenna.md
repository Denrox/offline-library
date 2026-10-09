# Weakly directive VHF/UHF antenna

*Tags: antenna, vhf, uhf · score 3*

## Question

Most resources around the Internet discuss common antenna types, classifying them between directive (like Yagi) and nondirective (like a simple dipole). Directive antennas are good when you know from which direction you are receiving a signal and would like to collect as much of it as possible. Nondirective antennas are good when you do not know from where you are receiving, or you want to receive from many directions at once without moving your antenna.

I would like to build a weakly directive antenna: i.e., I don't know the direction from which I will be receiving, but I know it must be in a certain half plane or quadrant around my position (because in the other directions there are buildings that screen any interesting signal, and unfortunately I do not have easy access to an unobstructed position).

I could use a nondirective antenna that also listens in the useless directions, but maybe I can squeeze some dB more if I can exclude them. What are good antenna types for this kind of application? Pointers to designing resources are welcome!

**EDIT** As specified in the comments, my band of interest for this antenna in VHF/UHF. Mostly UHF, actually. I am looking for antennas whose radiation pattern is something like one of these two pictures.

I would consider an antenna nondirective when it has a radiation pattern more or less like a circle, and strongly directive when the radiation pattern is a circle sector with a small angle (and therefore a strong gain in that sector), like 10 degrees or less. Since this is intermediate between the two extremes, I would consider this weakly directive, but if this is non standard terminology just ignore it.

## Answer (score 4, by Brian K1LI)

With your expressed interest in "listening," you might consider this portable 2-element VHF yagi presented by K3MT:

The "rabbit ears" are collapsible whips taken from an indoor TV antenna, but they should be available from the usual electronics hobby retailers. Using the element dimensions on the web site - 37in driven element, 42in reflector - gives this free-space azimuth pattern with forward gain of 4.6-dBi:

Optimizing this antenna in 4NEC2 with equal weights on forward gain and front/rear ratio yields slightly different dimensions with 1/4in diameter elements:

- reflector: 38in
- driven element: 37in
- spacing 21.75in

## Answer (score 3, by Brian K1LI)

A center-fed half-wave dipole mounted a half-wavelength above ground isn't as directive as you might expect. The deep nulls off the ends of the antenna are not as pronounced as they are in free space.

Simulation with *EZNEC* shows this azimuth pattern at the elevation angle of maximum radiation:

Drooping the ends of the dipole to form an "inverted V" with a 90$^\circ$ included angle further fills in the nulls:

This antenna's low cost, simplicity, good SWR and relatively low directivity may satisfy your requirements.

You may want to consider downloading the free 4NEC2 antenna modeling program. It comes with many antenna models, from simple verticals and dipoles to complex beams and arrays, which will give you a jump start, and its optimizer simplifies and accelerates the process of obtaining a useful based on your goals and constraints.

## Answer (score 2, by Zeiss Ikon)

I recall from one of the license exams that a double vertical, fed with a phase delay to one pole, will produce a cardiod radiation (and sensitivity) pattern. As I recall (it's been a couple months since my exam, and I memorized this just long enough to pass the test), this requires a pair of half wave elements, separated by a half wave, and fed a half wave out of phase, with the main radiation going toward the undelayed element. This is more or less like a Yagi with only the radiator and reflector elements, but no directors. You'll get a strong null, but a very wide pattern otherwise.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/14475/weakly-directive-vhf-uhf-antenna, by Giovanni Mascellani, Brian K1LI, Zeiss Ikon. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
