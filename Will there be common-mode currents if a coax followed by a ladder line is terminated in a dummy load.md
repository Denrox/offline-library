# Will there be common-mode currents if a coax followed by a ladder line is terminated in a dummy load?

*Tags: transmission-line, dummy-load · score 9*

## Question

*Assuming an antenna system where a transmitter feeds an ideal coaxial cable which is then connected to an ideal ladder line without a balun:*

It is often said that common-mode currents appear in the transition between a coaxial cable and a ladder line simply because the coaxial cable is unbalanced while the ladder line is balanced. My question is related to whether this mechanism is related to how the load/antenna looks like. Let us say that the two wires of the ladder line end up in a load without reference to ground (probably impossible to achieve with a real antenna). This can for example be achieved with a simple ideal resistor (dummy load) in the end of the line (and hanging the ladder line in completely free air). Let us also for the sake of the example assume that the characteristic impedance of the ladder line is 50 ohm such as in the coaxial cable - in order to avoid standing differential waves. Could there in this case be common mode currents appearing on the coaxial shield?

Then what if the characteristic impedance of the ladder line is not the same as the coaxial cable and we therefore have (differential) reflections at the transition - does it make a difference for the common mode?

And thirdly, what if the characteristic impedances of the ladder line and the coax are the same, but the resistive load at the end of the cable does not match the characteristic impedance of the cables so that we get (differential) reflections at the load - does it make a difference for the common mode?

## Accepted answer (score 6, by tomnexus)

Yes it radiates. How much depends on the lengths of the wires.

The point at which you connect the coax to the two-wire line is a bit like a dipole feedpoint, with about half the voltage applied to it. This is why:

1.

The voltages on the lines look like this at the junction. (Remember when you zoom in to a region much smaller than a wavelength, there's no RF magic; all the usual rules of circuits apply as normal):  
2.

Coax is "shielded" so the outside world sees the voltage on the (outside of) the outer conductor. On a two wire line, the fields are mostly constrained to an area about double the spacing of the lines. Because the spacing is << wavelength, from far away the two wire line looks like a single wire with the *average voltage* on it. Zooming out:  
3.

From far away now, you have a wire with a half voltage source in the centre. One side is the outer of the coax, the other is the two-wire line, just the common mode current. How much this radiates depends on the length of the parts of the wire. The case that radiates the most would be a (physical) quarter-wave of coax and a quarter-wave of two-wire line. From far away now:  
  
So you have a dipole antenna formed by the whole coax on one side and the pair of wires on the other. The dipole currents are the common mode currents.

I'm ignoring some more subtle effects. For example the dipole radiation resistance forms a load which is connected at the feedpoint, which might interact with the voltages on the lines. So the 0.5 V might change when this is considered.  
Also your transmitter is likely to be grounded, so the antenna will work differently.  
Finally, if the load and/or line impedances are mismatched it's possible there would be some impact on the effective voltage applied at the junction. Remember in the zoomed-in picture, there's no impedance (on the two wire line) that would prevent it from being about half the voltage on the coax. I think if the two wire line results in a short circuit there (if it's a quarter wave open or half wave short), then the voltage may be zero at that point.

This is a great question, and directly applicable to hams as we often do connect coax to two-wire line in a G5RV / ZS6BKW type design. A common-mode choke helps prevent the radiation effectively disconnecting one side of the voltage source that appears at the junction. It's easiest implemented on the coax side with a coil or ferrite.  
At microwave frequencies the solution is a Marchand Balun which enforces the balance on the two wire line by embedding the coax in a symmetrical structure.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20130/will-there-be-common-mode-currents-if-a-coax-followed-by-a-ladder-line-is-term, by rubund, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
