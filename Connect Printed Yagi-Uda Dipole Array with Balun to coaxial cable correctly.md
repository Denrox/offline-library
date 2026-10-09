# Connect Printed Yagi-Uda Dipole Array with Balun to coaxial cable correctly

*Tags: antenna-construction, feed-line, coaxial-cable, yagi, balun · score 5*

## Question

I am making the Printed Yagi-Uda Dipole Array with Balun (that is the full name). I used Antenna Magus to calculate dimensions. I am not sure how to properly connect it to coaxial cable.  
Here is what the antenna looks like:

In the Feed Method it states:

Feed Method

The printed Yagi structure requires a balanced feed. Typically, however the antenna is fed using an unbalanced coaxial cable and a balun is required to provide the required balanced feed.

An integrated balun structure is taken into consideration in the Antenna Magus design procedure and the Antenna Magus export models include a co-planar quarter-wave balun construction. If a coaxial cable is used, the outer conductor is simply soldered along the one line of the balun from the reflector element all the way to the driven element. At this point the inner conductor is extended across the gap of the driven element and soldered onto the opposite arm.

The antenna could be fed using a balanced source or a different balun construction. (Note that for these cases, the balun design will need to be done independently of Antenna Magus, and the co-planar balun structure may need to be removed from the export models for simulation purposes.)

**Does the image below show the correct way of connecting coax to the antenna?**  
*Orange dots are solder spots.*  
  
I do not have much experience making antennas.

## Accepted answer (score 4, by Kevin Reid AG6YO)

I'm no expert on balun designs, but I think they mean to construct a folded balun, as follows. The coax's outer conductor is soldered to the same part of the antenna, but it is *left on the coax*, not peeled away, so the final balun structure includes a length of the coax.

(The interpretation you proposed in your question is unlikely because if the outer conductor is separated from the coax, attaching it along the length of the trace won't function any differently from a single-point junction.)

When soldering, make sure not to melt the dielectric in the coax:

- Perform the soldering quickly, so the heat does not spread.
- Do not use foam-dielectric coax.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/3587/connect-printed-yagi-uda-dipole-array-with-balun-to-coaxial-cable-correctly, by Triak, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
