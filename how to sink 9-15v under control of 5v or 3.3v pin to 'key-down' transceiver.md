# how to sink 9-15v under control of 5v or 3.3v pin to 'key-down' transceiver?

*Tags: cw, transceiver, computer-aided-transceiver · score 3*

## Question

I want to use an Arduino to control keying transmission on a simple CW-only transceiver (think: forty-9er or Pixie).

Looking at the schematics of various such transceivers, they basically 'key down' by connecting part of the circuit to ground through a button or morse key.

Somehow, I need to be able to use a GPIO pin with 5v or 3.3v logic to control whether or not 9-15v from the "radio" side of the metaphorical 'key' can flow to ground (triggering carrier transmission).

Any ideas how to accomplish this? I want to say "open-drain logic" and "MOSFET" come to mind, but I'm not sure. Up to now, the most challenging things I've ever had to interface with Arduinos were a 3.3v i2c sensor I had to connect to a 5v Arduino (using a MOSFET-based level shifter board), and a 5v string of WS2811 pixels to a ESP32 (using a SN74LVC1T45 dual-rail shifter, because the MOSFET level shifter boards didn't quite work for this). Switching 9-16v (potentially, up to 3-5 watts) to ground is completely new territory for me.

My knowledge of MOSFETs can be succinctly summarized as, "I know they exist, I own a bag of them, and I'm vaguely aware that they're used for implementing open-drain interface logic".

For reference, here's the schematic to a "Forty-9er":

here's a "Pixie" schematic:

## Accepted answer (score 2, by tomnexus)

Keying to ground is simple enough with a single transistor and a resistor. This will work at 3.3 or 5 volts.

The Pixie seems to put all the PA current through the key, so you might use a smaller resistor, 220 ohms, to guarantee the transistor is saturated.

You could also use a MOSFET if you have a logic-level one in your junk box, the circuit is the same but no resistor required.

A small capacitor might reduce the amount of RF noise from the micro leaking into the radio circuit, but that will be a problem even just putting them anywhere near each other. Better might be to use an opto-isolator. For the 49-er you could probably use it with no external driver:

Choose an isolator with a photo-transistor, not a photo-diode, and for the Pixie, you need to check whether its maximum current and "on" resistance will be good enough.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20505/how-to-sink-9-15v-under-control-of-5v-or-3-3v-pin-to-key-down-transceiver, by Bitbang3r, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
