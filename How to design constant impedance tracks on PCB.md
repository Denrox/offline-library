# How to design constant impedance tracks on PCB?

*Tags: diy · score 4*

## Question

I have designed PCB's in the past, but need to draw a constant 50 ohm impedance track on the project I'm planning.

I know the calculations for (for example) a coplanar wave and how to get a **straight** PCB track around 50 ohms. (I can recommend the free Saturn PCB design software).

But how do I create a track that has 45/90 degree angles or something like this while keeping impedance fairly constant?

I am using Diptrace, which does not support this by itself. The PCB above however is (at least) 25 years old, so I cannot imagine you absolutely *need* state-of-the-art PCB layout software...

## Accepted answer (score 6, by MagnusO_O)

Besides not knowing about the dimensions, substrate relative permittivity $e_r$ and backside ground yes/no my guess from the picture is that the transmission line is a **microstrip** line and not a **coplanar** line.

Front sides of the microstrip line printed circuit boards often also have ground metal, but that's for shielding or just practical etching reasons and does not impact the transversal electromagnetic wave mode.  
However just from the front side these may be mistaken as coplanar lines. I would always check the backside for that reason (still there is no definite prove, but another clue).

Anyway for both transmission lines at bends you get a parallel capacitance to ground due to the fringing fields causes by the sharp inner and outer edges.  
That capacitance can to be compensated by adding inductance:

The compensating inductance can be achieved by a narrowed line, e.g. phase cutting the outer edge.

For **microstrip** lines you can either simulate the compensated bend with e.g. sonnet lite or calculate it with an approximation formula as given by e.g. Microwaves101 Mitered bends:

$D = W* \sqrt{2}$ (the diagonal of a "square" miter)

$X= D* (0.52 + 0.65 e^{-1.35 * (W/H)})$

$A = ( X- D/2) * \sqrt{2}$

W, H being width and height of the microstrip line.

For actual **coplanar** lines the compensation is more complex as you have to make sure the slot mode is not excited. Here are two links describing such an option:

Wire-Bond Free Technique for Right-Angle Coplanar Waveguide Bend Structures

Coplanar waveguide bend with radial compensation

For these I presume EM simulation is mandatory and you won't get good approximation formulas.

Finally, when there is enough area you can also form a wide radius circle segment to smoothly bend without having to compensate - for both lines.  
But that is often prevented due to cost and losses by the additional line length.

## Answer (score 4, by Phil Frost - W8II)

At 145/445MHz, things are not so hard. As a rule of thumb, anything under 1/10th of a wavelength doesn't even count as a transmission line. At 445MHz that's about 6.7cm. At 145 MHz, 21cm. Anything shorter than this length and you probably don't even need constant impedance traces.

If you do need such traces (or you just want to do things "right"), you can make mitered bends, like MagnusO_O suggests. But if your design software doesn't support that, you'd probably do just fine making "gentle" bends, with two 45-degree turns. At these low (by today's standards) frequencies you probably won't notice the difference.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15216/how-to-design-constant-impedance-tracks-on-pcb, by Dieter Vansteenwegen, MagnusO_O, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
