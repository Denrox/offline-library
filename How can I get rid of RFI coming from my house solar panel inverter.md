# How can I get rid of RFI coming from my house solar panel inverter?

*Tags: rfi · score 11*

## Question

The solar system on my house creates horrible rfi on all hf bands during the day when the sun is out, it goes away when it's not sunny. Any one got any ideas how to get rid of the rfi ? I already tried putting capacitors across the high voltage solar panel inputs on the inverter, made no difference.

## Accepted answer (score 5, by Andrew)

See below a summary of what i did to remove most of the RFI coming from my house solar panel system.

Problem = horrid RFI across the entire HF spectrum. It's only there when the sun's out. The RFI sounds like a lawn mower. I normally like the sound of lawn mowers but not in this case. If i point my yagi towards the solar panels the RFI signal strength goes up. My solar panels are not the type with inverters on the back.

The fix is to connect an RF choke between each solar panel array and the solar panel inverter right at the input to the inverter.

1. Turn off solar panel inverter to see if that stops the noise.
2. Noise goes away so inverter is probably the source.

Then for each solar panel array (or for each postive/negative solar panel cable input pair on the inverter) :

1. Obtain 2 x type 43 ferrite rings from Element 14 FAIR-RITE 5943003801 FERRITE CORE, TOROID, 43.
2. Obtain about 2 meters of 4mm2 solar panel extension cable and cut it in half.
3. Obtain 2 pairs of IP67 MC4 solar panel plugs/sockets.
4. Make 2 series RF chokes. Each choke has about 7 turns of two solar panel extension cables wound in a bifilar fashion (two cables next to each other) on one ferrite ring. Make the two chokes using the same two single 1 m pieces of cable such that the two chokes are in series with no joins in the middle.
5. Fit the MC4 connectors to the chokes. The set of two chokes in series will have two connectors at one end and two connectors at the other end. The connector sex must be such as to preserve the original polarity of the solar panel array connections to the inverter.
6. Follow your solar panel system's proper procedure to power down.
7. Connect the chokes at the inverter between the inverter and the solar panel array. Make sure the polarity is correct. If you get it wrong your inverter will have a heart attack and die. Be careful as solar panel arrays output approx 300 - 500 VDC. If you're afraid like me do it at night.
8. Follow your solar panel system's proper procedure to power up.
9. Jump up and down (well that's what i did) as you tune across the bands and see that the noise is mostly gone.

Note that clip-on ferrite chokes won't do anything to cure solar panel inverter noise.

## Answer (score 8, by Glenn W9IQ)

The inverter in your solar panel system utilizes a high frequency switcher to regulate the voltage and convert it to AC for feeding back into the mains. Some solar panels also use an "optimizer" on the back of the solar panel that is a smaller switching device designed to optimize the usable energy from the individual, or small group of, panels. Both of these devices can radiate switching noise through the wires connected to them which act as antennas This switching noise is generally rich in harmonics that can easily pollute the entire HF spectrum.

You may not be able to entirely eliminate the switching noise but judicious use of ferrite suppression devices may knock it down to an acceptable level. Before considering any modifications to your solar panel system, be aware that both the mains and the DC side of the system can contain voltages that are capable of producing lethal currents in the human body. You may also be subject to local regulations that limit what you or anyone else can do in the way of modifications. Don't overlook the effect of any modifications on your solar system warranty.

Since you are working with existing wiring, the easiest form of ferrite suppression is the clamp on variety:

You will need to acquire an assortment of type 31 and type 75 ferrite clamp on beads (don't use uncharacterized, junk box beads). The type 75 material is most effective at low HF frequencies while the type 31 material covers the balance of the HF and low VHF spectrum. Place at least one of each type of bead on all well insulated wires, as close as safely possible to where they enter and exit the inverter and any optimizers. Do not place beads on bare wires or in locations where they can come in contact live conductors such as screw terminals. Don't overlook control and network cables. Multiples of each bead per wire will increase the RFI suppression effectiveness. If you can wrap more than one turn of wire through the snap on core, its effectiveness is generally multiplied by the square of the turns. For example, 3 turns is the equivalent of 9 beads.

Ferrite material choking performance degrades in the presence of strong DC current. For this reason, it is better to pass both DC wires from the solar panels through the same snap on ferrite as this will eliminate the DC bias in the core. This may necessitate purchasing some snap on ferrites with a larger dimension hole in order to accommodate both DC wires.

If you work through a disciplined process of noting the noise level at a given frequency, adding beads to a selective location and then checking for any change in the RFI level, you may be able determine where installing more beads would be most effective.

It is also a good time to review the location of your HF antenna system relative to the solar panel system. Increased distance of the antenna and feedline from the solar system will tend to reduce the RFI. Also check to make sure you don't have common mode currents on your antenna feedlines as this will couple the locally produced RFI into your receiver. Proper current baluns and balanced antennas help to mitigate these common mode currents.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12463/how-can-i-get-rid-of-rfi-coming-from-my-house-solar-panel-inverter, by Andrew, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
