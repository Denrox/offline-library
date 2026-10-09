# Identification of valve

*Tags: electronics, repair, vacuum-tubes · score 4*

## Question

My favorite receiver used for 40 m AM broadcasts has a cracked valve, but the valve type normally printed on the glass has rubbed away. Can anyone tell me what the numbers for this valve are ?

The radio is mid - late 40's, made in Australia and has no brand or model on it.

The valve is the one audio output valve in the radio. The valve has "Philips Miniwatt Australia" printed on the black base. You can just see the crack in the 3rd picture at the lower left of the valve glass.

Clues are that it has 7 pins and they all seem connected when you look inside so 2 for the heater and 5 left over probably makes it a Pentode. CORRECTON, -> there are 7 pins but only 6 pins are connected, so i'm not sure if it is a pentode now. - It's a Tetrode.

The heater voltage is : 6 VAC. The cathode resistor is : 240 ohms. The G1 resistor is : 543 k ohms

That should narrow it down a bit.

See the pictures of the radio, chassis and valve.

You can see how clean the glass on the front dial is, that took a while to get it like that, i hardly ever clean the valves like that any more.

## Accepted answer (score 3, by PeterH)

Are you sure that you are correct in the comments about your pin 2 and pin 7? (The conventional numbering for these tubes is as in your drawing, so conventionally pins 8 and 5).

If you look very carefully or use an ohm meter you might find that your pin2 is actually the cathode and your pin8 is G1, as in your drawing of the 6L6.

This would be more normal for an octal beam pentode.

If the drawing is correct for your valve then it's likely a 6v6 (lower power but same pinouts as the 6L6).

It's a 10 watt max audio output tube used in lots of radios from that era. Grid 3 is internally connected to the cathode, so doesn't have a pin.

Max rating currents of 45 mA anode + 5mA G2 would give max 12v across the 240 ohm cathode resistor, approximately right for self biased class A1 operation (6v6 has -12.5v G1 cutoff voltage). Should be probably sitting around 5 or 6v across the cathode resistor at no signal.

I'd give a 6v6 a go if the pinouts are correct, check the quiescent anode and G2 currents (by measuring cathode voltage, I'd expect somewhere around 1/2 max or less) and that the peaks never exceed the max ratings. If there's any distortion find out why.

Capacitors, particularly electrolytics, can fail or change value in sets of this age so worth checking they are good where possible.

If your pinout description in the comments is actually correct then it's a valve I'm not familiar with, sorry.

Good luck.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16152/identification-of-valve, by Andrew, PeterH. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
