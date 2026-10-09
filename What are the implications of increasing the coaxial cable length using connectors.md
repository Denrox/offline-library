# What are the implications of increasing the coaxial cable length using connectors?

*Tags: coaxial-cable, connectors · score 3*

## Question

So the antenna spine (suspended line that was holding up the centre insulator) came apart. I've moved the centre insulator elsewhere. The move means my existing coaxial cable is now around 40ft short. I reckon the cable capacitance will make marrying an LMR400 with the existing RG58u a lossy affair.

- Is my understanding correct?
- Apart from the loss at the connector, what else could be affected by this patchwork?

EDIT: I neglected to mention the rig in use is near QRP with a max output of 15W. It may or may not be pertinent to the question posed here.

## Answer (score 2, by hobbs - KC2G)

I reckon the cable capacitance will make marrying an LMR400 with the existing RG58u a lossy affair.

I'm not sure what that means, particularly the "cable capacitance" part. The loss of the system is just the sum of the losses of its bits — X feet of LMR-400 plus Y feet of RG-58/U plus the insertion loss of one coupler (assuming the coupler's VSWR is reasonable, which it ought to be).

Adding cable will increase your loss, but lower-loss cable will add less loss (shocker!). The coupler adds some loss, but usually it's an insignificant fraction of a dB.

The only other thing to ponder is the effect of an electrically longer feedline on the impedance seen at the radio. If you're talking about a dipole, that's unlikely to be an issue. If you've got a doublet or some other sort of antenna that has a high SWR at the feedpoint, then adding cable might put you at an "unlucky" feedline length for one of the bands you want to use. Equally likely, it could be the same or better :)

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21454/what-are-the-implications-of-increasing-the-coaxial-cable-length-using-connect, by VU2NHW, hobbs - KC2G. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
