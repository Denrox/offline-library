# Ground plane connection to screen

*Tags: antenna, antenna-construction, vertical-antenna, microwave · score 3*

## Question

Assuming that I have a quarter-wave monopole for roughly 1GHz, mounted roughly 15' above ground, with a lightning suppressor connected via an N-type sealed with self-amalgamating tape.

I have a convenient perforated stainless steel disc of somewhat larger diameter than the wavelength which I believe would make a good groundplane, however the centre hole is oversize (20 rather than 16mm).

Would I be better off getting a washer TIGed into the middle, or fabricating a sufficiently-strong plastic adapter?

In the either case, to what extent does the antenna characteristic change as the conductivity/insulation of the connection varies, e.g. due to salt-laden wind?

## Accepted answer (score 5, by tomnexus)

You should definitely arrange to connect the ground screen to the body of the connector. If you can have a suitable washer tig welded to the screen, and screw the connector tightly into this, that will be ideal.

The ground screen or counterpoise only works if the RF current can flow out into the screen. If it's not connected, like if you use a plastic washer, it won't do anything (since it lies almost on an equipotential contour, it won't have any current). Instead the whole length of coax becomes the counterpoise, and because it's $>>\lambda/4$ it causes a) pattern break-up and b) VSWR peaks in random places, all depending on the length and arrangement of the coax.

Here are the two cases side by side.

One further thing to consider - depending on your application - is that the pattern of a monopole on a circular groundplane is not ideal for terrestrial communication. The antenna gain on the horizon is just under 0 dBi, not 2 dBi, and it drops fast below the horizon. It's not symmetrical like a dipole would be. If you have access to a machine shop, a better configuration would be a $\lambda/4$ tube or sleeve hanging down over the coax, instead of the ground screen. Something like this:  
The classic "groundplane" design with four wires bent down at about 60 degrees is also good.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/22968/ground-plane-connection-to-screen, by Mark Morgan Lloyd, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
