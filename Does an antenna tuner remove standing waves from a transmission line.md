# Does an antenna tuner remove standing waves from a transmission line?

*Tags: transmission-line, antenna-tuner · score 4*

## Question

Does an antenna tuner remove standing waves from a transmission line ?

## Accepted answer (score 10, by Brian K1LI)

An antenna matching network (aka "tuner") does not affect the conditions of the load (antenna) or the transmission line between the load and the matching network. The matching network transforms the impedance "looking into" the transmission line to a more desirable value, typically 50$\Omega$ for ham applications.

If the network manages to achieve such a "perfect match," then there will be no standing waves on the transmission line between the transmitter and the matching network and there will be no additional mismatch loss in that line. This is the primary reason that "remote tuners" have gained some popularity in the marketplace.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15257/does-an-antenna-tuner-remove-standing-waves-from-a-transmission-line, by Andrew, Brian K1LI. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
