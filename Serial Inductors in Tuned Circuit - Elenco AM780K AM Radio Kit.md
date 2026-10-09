# Serial Inductors in Tuned Circuit - Elenco AM780K AM Radio Kit

*Tags: antenna, antenna-construction, receiver, diy, electronics · score 3*

## Question

I'm trying to understand a component of an AM radio kit that I have. (There is a document available here: https://www.elenco.com/wp-content/uploads/2017/10/AM-780K_REV-K-2.pdf describing the build procedure and the circuit in more detail.) I was researching coil windings for a regenerative receiver, that had me come back to this circuit, and there are some things I don't understand. The radio works great, I just have some questions about it.

The part I'm confused about is the bottom left of the circuit diagram (L1, L2, and C2):

Is there any reason why L1 and L2 are in series like this? Is there any difference between a component with C2 and L3 = L1 + L2 and a component with C2, L1 and L2?

Also, I'm a little confused by the diagram showing 1,2,3, and 4 as antennas. Can I add an external wire to act as antenna somewhere in this component?

Other diagrams show taps in the coil to switch between different resonant frequencies (adjusting the length of the coil) along with the variable capacitor. I was wondering if these points are potentially taps, as well.

## Accepted answer (score 4, by Kevin Reid AG6YO)

Is there any reason why L1 and L2 are in series like this? Is there any difference between a component with C2 and L3 = L1 + L2 and a component with C2, L1 and L2?

There is essentially no difference than a single coil (other than the impedance effects of the extra bit of wire leaving the coil and coming back, which will not be much at all). They probably used whatever pre-wound coil was available cheaply, or was used in another kit they sold, and decided that the inductance of the two coils in series best suited this circuit.

Also, I'm a little confused by the diagram showing 1,2,3, and 4 as antennas.

That is not an antenna symbol, but a symbol for a contact or test point. The antenna symbol you are thinking of looks like this, with three spreading lines in a triangle:

The antenna symbol can also lack the horizontal bar of this example.

Notice that the same symbol appears on the connections of the speaker. They seem to have used this symbol simply to label the points in the diagram where, when you assemble the circuit, you solder a wire from a component (the coil and the speaker) to a labeled point on the circuit board. I would not call this good practice in a schematic, because the signal does not actually pass *through* those connection symbols. It would be more conventional to simply place a label next to the wire itself.

The antenna in this circuit is the coils — a *ferrite rod antenna*. Perhaps you could in fact usefully improve its reception by attaching an external antenna somewhere, but I don't think this circuit was particularly designed for that.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21529/serial-inductors-in-tuned-circuit-elenco-am780k-am-radio-kit, by Jared, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
