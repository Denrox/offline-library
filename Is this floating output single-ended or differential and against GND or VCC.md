# Is this "floating" output single-ended or differential and against GND or VCC?

*Tags: antenna, electronics, balun, transmitter, testing · score 3*

## Question

I'm looking at a simple FM transmitter output (see picture). It is from the collector of a transistor and it goes through a DC blocking capacitor before the antenna would be connected. The entire circuit is floating from true ground. I'm thinking of making the antenna a dipole and suddenly I'm stumbled whether to make the other leg the circuit GND or positive rail. The supply voltage is 3VDC and the RF signal is about 1.8Vpp 100MHz. Part of me thinks that the main antenna port will be floating somewhere between GND and VCC. The other part of me thinks that the DC blocking capacitor will be a low impedance at RF so that the RF is actually "pushing against" GND or VCC but I don't know which one. I also know that if I didn't make it a dipole, the one antenna lead would form a capacitor back to the circuit to complete the circuit, again I don't know if it's to GND or VCC, for some reason I just can't wrap my head around this. I thought maybe I measure it with an oscilloscope, I even tried to clip the ground leads from the scope to VCC or GND trying to figure this out but I think the 1M-Ohm probes just pull the RF to one or the other. I hope someone can help me understand this and I would really appreciate any help.

Note: Decoupling capacitors are not shown but they are between GND and VCC. You can see them here:

## Accepted answer (score 6, by Phil Frost - W8II)

The other part of me thinks that the DC blocking capacitor will be a low impedance at RF so that the RF is actually "pushing against" GND or VCC but I don't know which one.

This appears to be a kink in your understanding. RF doesn't "push against" one or the other.

Let's be more specific about what we mean by "pushing against": let's talk about the flow of electrical charge: "current". The charges move because they are moving through an electric potential gradient: "voltage". Charge wants to follow the voltage gradient just like mass wants to follow the gravity gradient.

Like mass, charge is conserved. It is neither created nor destroyed. So if some charge comes out of one node of the circuit, an equal amount must go into another node. So the power supply doesn't produce charge nor consume it: it's a "pump" for charge that sucks charge in one side and pumps an equal amount out the other side. It's not "one or the other": it's both.

If a rock is dropped from an airplane, is it falling from the sky or plummeting towards the ground? It's not one or the other: it's both.

I'm thinking of making the antenna a dipole and suddenly I'm stumbled whether to make the other leg the circuit GND or positive rail.

Why does it matter?

Firstly, remember that there's nothing special about ground except that it's 0V by definition. We could easily call the node labeled "+3VDC" ground instead, and then label what's currently "GND" as "-3VDC" instead, and the circuit would be precisely the same.

And because the output capacitor is effectively an open at DC, the amplifier doesn't really care if at DC there's a 0V difference between the dipole legs or a 1000V difference. Whatever the difference happens to be, the amplifier will superimpose the RF input on top of that. And since only RF radiates, and this being an antenna that's probably all we care about, does it matter if the other leg of the dipole is connected to 3VDC or GND?

In fact, for the purposes of AC analysis any node which is a constant voltage is "ground". If that isn't intuitively obvious, ruminate on how the circuit might "know" the difference between 3VDC and GND.

In practice, there might be some factors not captured in your schematic that favor doing it one way or another. For example, you might anticipate people could touch the antenna, completing a circuit between ground and the antenna. In that case it would be much better if the antenna was at ground, since no current would flow. With this circuit's 3VDC supply there's no real hazard either way, but imagine if Vcc was 1000V instead.

Or you might prefer that the antenna is (as much as possible) grounded for lightning protection. If the antenna should be struck, it would be nice if you could shunt a lot of that current directly to a ground rod, rather than going through your power supply then to ground.

But if all you care about is making the antenna radiate, then it doesn't really matter if you consider the output to be the difference between ANT and GND, or ANT and +3VDC.

What does matter though, if your antenna is a dipole, is that the current to each dipole leg is equal and opposite. Consider the impedance between each dipole leg and the parts of the circuit driving it, including capacitive coupling. If this device is powered by a battery and the entire thing is floating, and it's physically small, then there's really no significant difference between ANT, GND, and +3VDC, and you can just hook up the dipole either way and there's no problem. But if GND is connected to Earth, maybe through the power supply, a USB cable, or some coax imput, now the impedance to that node is very different from the others because it's attached to a giant ball of iron. In this case you will want to [consider a balun](Using%20a%20balun%20with%20a%20resonant%20dipole.md).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17501/is-this-floating-output-single-ended-or-differential-and-against-gnd-or-vcc, by pgibbons, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
