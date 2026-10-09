# How to reduce VFO sensitivity to the hand capacitance?

*Tags: diy, electronics, equipment-troubleshooting, capacitance, vfo · score 8*

## Question

I got a little tired of Si5351 and decided to build an analog CW transceiver. It's almost done and works pretty well. However, I discovered one problem. When I reach the VFO control with my hand the frequency shifts a little, about 100 Hz or so. It's not a big deal, but a little annoying. When the frequency is higher, ~5.070 MHz (the capacitance is less) it gets worse. I wonder if it's curable.

Here is the schematic:

And here is how it's physically implemented:

The enclosure is made of thick aluminum and as you can see I did my best to shield the VFO properly, but it didn't save me.

I never encountered such an issue before and I don't recall that it was well described in the literature. For instance, I don't know for sure if the choice of the component values matters, and if so, what are best practices worth considering. Is there anything I can do in my next rig to avoid this problem? Or is it simply the price to pay for using a capacitance-controlled VFO, instead of, say, varicap-controlled VCO?

## Accepted answer (score 7, by Andrew)

As mentioned in the comment by henryflower, make sure that the shaft (and thus the frame) of the variable capacitor are grounded.

You need to use rubber mounting grommets around the screws which bolt the tuning capacitor to the PCB or chassis. Then run one thick wire from the frame of the tuning capacitor from a point away from the front panel to one point on the ground of the PCB. You may have to experiment with the exact location of the ground point on the PCB.

Just about all old valve radios with these types of large tuning capacitors use this method of isolation to reduce hand capacitance.

Also, you could try changing the value of the inductor which is in series with the tuning capacitors, as this may make the frequency determining components of the oscillator less susceptible to the problem by changing the Q of the circuit and making it less sensitive to external influences.

And yes as mentioned in another answer, a lid on the box is probably a good idea.

## Answer (score 4, by glen_geek)

Circuit looks OK.  
Note that the highest impedance point in this circuit is near the box open end. RF voltage here is highest in this oscillator, and is susceptible to coupling out the top.  
A shield lid (soldered to the box) should help.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/19970/how-to-reduce-vfo-sensitivity-to-the-hand-capacitance, by Aleksander Alekseev - R2AUK, Andrew, glen_geek. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
