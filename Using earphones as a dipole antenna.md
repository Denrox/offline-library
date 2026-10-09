# Using earphones as a dipole antenna

*Tags: antenna, antenna-theory, antenna-construction, diy, mobile · score 7*

## Question

I would like to know how the earphones work as a dipole antenna for a smartphone to receive the FM bands?

Usually, one arm of a dipole needs to be connected to the ground and the other arm needs to be connected to the receiver. But in the case of a earphone, the headphone coil would work as a resistor and there is a resistance of 32 ohms. So, how do the two arms of the dipole antenna work when there is a resistance between the two arms?

## Answer (score 11, by glen_geek)

Headphones used as an FM antenna do not have a **dipole** form, but more like a **monopole** type.  
Various radio-coupling techniques are used: an example that uses headphone cable as antenna:  
  
The common earphone return currents flow on the red-coloured wire, which would be the shield of the cable. I hesitate to call it "ground" because a portable battery-operated radio has no RF ground. Nevertheless, the 3.5mm headphone jack would connect the cable's shield to the jack's "ground" terminal.  
Inside the radio, an inductor is connected to radio circuit cold terminal (the schematic shows a "ground" symbol because functionally, this is a reference point from which all RF currents are measured).  
Both audio currents that drive headphones, and RF currents that feed the radio's RF input flow through this inductor. A small-value coupling capacitor rejects audio, but allows radio-frequency into the radio's RF input amplifier.  
Ferrite beads in left and right audio paths from the audio amplifier are high-impedance for RF, but very low impedance for audio, so that audio currents are not impeded.

A monopole antenna often has its bottom-end carefully coupled to earth, to make it a low-impedance point. This makes its top-end higher impedance.  
A headphone antenna doesn't match this scenario, since both ends of the headphone cable have an unknown impedance above ground. It is a complex antenna, since neither end is grounded.

## Answer (score 2, by user10489)

FM broadcast is close to 3m wavelength, which makes the ideal quarter wave antenna around 75cm or 30in, which is not far from the typical headphones wire length. Of course, if the antenna, I mean headphones are in your ear, then your body may extend the length further.

Also, the wires in the headphone are parallel, which would make them closer to a (bad) transmission line than an antenna, so your diagrams are wrong. The wires are not used as separate legs of the antenna, but are treated as a single wire with a loading coil at the end (for the purposes of the antenna use at least).

So your headphones wire is acting like a quarter wave monopole or random wire, possibly using either the internal loop stick or your hand holding the radio as the other half of the dipole.

Side note -- there are many antenna designs that put a resistor at the end of the antenna. But a speaker coil is not anywhere near a resistor, especially in radio frequencies. So that part of your diagram is also wrong.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/22998/using-earphones-as-a-dipole-antenna, by Prabhat Karpe, glen_geek, user10489. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
