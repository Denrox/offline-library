# Acceptable RF radiation exposure to electronic equipment

*Tags: antenna-system, rf-power · score 5*

## Question

I'm wondering if there are any general guidelines or rules of thumb about the exposure of electronic equipment to RF transmissions, 150 MHz - 900 MHz.

The background is that we are looking to install an LMR antenna for a 35 to 50 Watt radio above an office, inside of the drop ceiling. Using the FCC guidelines we would be well below the limit for human exposure. On the other hand, the office will operate as an LE dispatch center and have a lot of PC based, and other electronic equipment. Inside the drop ceiling there's quite a few network cables and others that are unidentified. I've also run into dispatchers with pacemakers, and don't see that covered in the FCC human exposure guidelines.

I know that the FCC part 15 limits the permissible amount of radiation from an electronic device, but is there a general rule about what the acceptable power density is around any class of equipment?

## Accepted answer (score 4, by tomnexus)

The FCC does not regulate what is called Radiated Susceptibility for consumer electronics, the sensitivity of an electronic device to external RF but many manufacturers will test their equipment.

For example a cellphone generates up to 30 V/m near the phone, and is pulsed on and off a few hundred times per second. When cellphones first appeared, they would announce themselves by interfering with any nearby audio device. These days phone audio breakthrough is not very common and you expect car radios and computers to work normally even with a phone lying on top of them.

**MIL-STD-461G test RS103** describes the tests in detail. The device under test must operate normally when exposed to 10, 50 or even 200 V/m, depending on the intended mounting position of the device. The test uses 100% AM at 1 kHz, which is the most disruptive radio interference. The frequency is swept slowly over the chosen range, 30 MHz - 3 GHz or wider.

At your frequency, for vehicle electronics in Navy and Air Force, the test limit is 10 V/m, so this seems like a reasonable limit to start with. This would cover handheld radios in a vehicle. 10 V/m is present about 5 m from a dipole transmitting 50 W, call it 10 m to be safe considering reflections and guiding from metal in the building.

It does seem like a bad idea to put 50 Watt transmitting antenna in the room space. It won't harm the people but

- the transmit performance of the radio will be degraded by 10 or 100 x compared to being outdoors, due to the metalwork of a false ceiling, and concrete and reinforcing above, and the long path to get out of the building, through a window eventually.
- the receive performance will be further degraded by noise from all the consumer electronics in the room, including nearby network cables.
- there is some potential for disruption of electronics in the room, especially if it is near to network, phone or power cables. Network cables, analog monitors using VGA cables and amplified speakers will be the first to be affected.

If at all possible the antenna should be routed outside. If not, consider reducing the transmitter power to 5 Watts and placing the antenna against a window - the performance outdoors will be the same but the interference potential will be much reduced.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18221/acceptable-rf-radiation-exposure-to-electronic-equipment, by Frank, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
