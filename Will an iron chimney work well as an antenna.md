# Will an iron chimney work well as an antenna?

*Tags: antenna, antenna-construction · score 6*

## Question

There is an iron chimney near my house that is not used anymore. It is ~15 meters in length and ~0.5 meter in diameter. How good will it be as an antenna for rtl-sdr?

## Accepted answer (score 5, by Mike Waters)

Assuming that your RTL-SDR covers VHF and up, 15 meters is too tall. You would be better off using it as a support for a suitable antenna.

Iron has *far* more losses than copper, aluminum, or other non-magnetic materials. Having said that, on HF a 15 x .5 meter pipe should have considerably less loss than a thin 15 meter iron wire and could be used for receiving with just a ground rod at the base. However, for transmitting you will need to minimize the losses with a good RF ground at the base, the feedpoint (and not just a ground rod!) consisting of suitable radial wires, either elevated or laid on the surface of the ground.

## Answer (score 2, by sm5bsz)

It is a quarter-wave at 60 meters, 5 MHz. With the large diameter, losses would be negligible despite the poor conductivity and magnetic losses in iron. This would be a good transmit antenna if you can find a way to feed current into it with low losses. I think that would be possible with an appropriate set of ground plane wires and maybe a better metal (aluminium foil) on the lowest couple of meters so you could couple by use of fairly short high Q couplers.

For receive with an rtl-sdr, just use it to support something for the frequency of interest. For HF, a thin wire from the top, for vhf a 15 m high tower to mount antennas on is excellent:-)

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10074/will-an-iron-chimney-work-well-as-an-antenna, by vasili111, Mike Waters, sm5bsz. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
