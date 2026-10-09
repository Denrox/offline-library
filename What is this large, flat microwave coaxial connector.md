# What is this large, flat microwave coaxial connector?

*Tags: connectors, microwave · score 7*

## Question

I picked up a random piece of RF hardware at a flea market. I'd like to know what these unusual connectors on it are.

The jack is flat on its face except for the gold ring. Inside the gold ring appear to be fingers gripping the central pin (which does not extend out of the connector). The plug's center contact is a helical spring which presses flat against the gold ring.

The diameter of the threads is 17.4 mm outside the jack and 16.2 mm inside the plug (slightly larger than N or UHF connectors). The insulating gap is 11.8 mm and the outer diameter of the gold ring is 7.43 mm.

The plug is actually an adapter to a BNC jack (which does suggest the possibility that these are not standard connectors at all); here's a picture of them fitted together:

The entire unit has two of these connectors, one N connector, and what looks like a mechanically tuned stub for somewhere above 900 MHz. I haven't been able to clearly determine any of its functionality yet.

## Accepted answer (score 2, by Kevin Reid AG6YO)

Martin Ewing AA6E got it right in his comments on the question, which he hasn't posted as an answer yet himself so I'm copying here for the record:

Can't verify the dimensions, but is it possible this is a diode detector? Maybe you can gently pull out the gold piece and find that it's the base of a 1N23 or similar.

I'm guessing it's not really a connector, but a spring fixture for holding the diode in place. This could be a simple mixer or power detector, with the (IF) output going out the BNC jack. The diodes have a tendency to burn out with overloads, so it's important to have a way to replace them.

I finally got around to disassembling the thing further, and you are completely correct about this “connector” actually being a diode holder. The gold part does indeed pull out revealing the diode (unfortunately I did not actually try hard enough to confirm this before disassembling the main body).

One of the diodes was marked 1N416D (according to the Internet, a "X-S BANDS POINT CONTACT MIXER DIODE") and the other MA450D (a varactor diode), so again Martin's theory about this being a mixer or detector fits.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5340/what-is-this-large-flat-microwave-coaxial-connector, by Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
