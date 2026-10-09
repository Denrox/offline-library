# Is a VHF antenna on a vehicle's body a bad idea?

*Tags: antenna, mobile · score 8*

## Question

For context, I'm brand new, with nothing but an HT & 19" dual band (2m/70cm) whip on it.

While I'll likely go with a magnetically mounted vertical antenna, I've been thinking of other more covert options.

For instance, could I do a 1/2 wave dipole mounted along the roof? A 2m dipole is just a little over 3 feet and would easily fit along the edge or middle. I'd need to insulate it, I'm sure, but would that work or be worth the effort? What about vertically along a door frame?

The bumper is already insulated. Even if the car body reflects the RF in one direction, could I then combine one in the front and one in the back bumper?

## Accepted answer (score 6, by Phil Frost - W8II)

A horizontal VHF dipole above a (presumably metallic) car roof is not a good idea. Because the car roof is relatively large relative to wavelength, and is a good conductor, you will get a lot of RF current in it through capacitive and inductive coupling. This isn't a bad thing in itself, but because the geometry of your car isn't designed as an antenna, the result will be difficult to predict and probably not very good.

Here's one problem: if we think of the car roof as an infinite conductive plane (just a rough approximation of reality), it will make an image antenna. If your dipole is very close to the roof, then this image antenna will cancel most of your antenna's radiation. As you get it higher you will get less cancellation, but most of the radiation will be up, towards the sky. [When you get it to half a wavelength high, then this is no longer a problem](What%20causes%20ground%20losses%20in%20a%20HF%20antenna%20system.md), but then why not just use a mag-mount vertical, which is just as tall? For a vertical, the ground plane and resulting image antenna is a good thing.

Of course your car isn't an infinite plane. RF currents will flow all over the car body, and probably you will get a lot of radiation from slot antennas formed by seams in the car body. The trouble is we don't know what they will be. They probably won't offer a good match to your 50Ω coax.

Also, the polarization could be anything. By convention, FM on VHF uses vertical polarization. If you happen to radiate with horizontal radiation, you will only be heard by most people through paths that rotate your polarization. In practice, this means a loss on the order of 30dB. Radiation from your car body probably won't be entirely horizontal, so it may not be so bad, but most likely, it won't be so good.

Another issue may be the electronics in your car. With the dipole laying against the car body (anywhere), the coupling between the dipole and the car body is so good you might as well have soldered the feedline directly to the car body and skipped the dipole. It's obvious then how much RF current is in the car body, and all the wiring attached to it. Automotive electronics are usually pretty robustly engineered, but I'm not sure I'd trust them to work with an RF transmitter hooked up to them.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1618/is-a-vhf-antenna-on-a-vehicle-s-body-a-bad-idea, by conan, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
