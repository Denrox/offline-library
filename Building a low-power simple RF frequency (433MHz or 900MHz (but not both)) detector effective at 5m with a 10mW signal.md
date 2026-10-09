# Building a low-power simple RF frequency (433MHz or 900MHz (but not both)) detector effective at 5m with a 10mW signal

*Tags: antenna, rfi, equipment-design, testing · score 3*

## Question

I am looking for a simple schematic for building an effective RF detector which can trigger a GPIO. The goal is to (passively?) detect a 10 mW RF signal (10% duty cycle) and have that raise voltage on a pin to somewhere north of 0.5V within 2 seconds of the signal going live.

I have some Avago/Broadband/Agilent/HP HSMS-2855 chips coming my way, which I understand are wonderfully good zero-bias RF detectors. However, it's not clear to me whether I can slap a random antenna on and go have some fun, or if I still need to pay careful attention to impedance matching, filtering, etc...

I have read An Ultra-Low Power Wake-Up Receiver for Real-time constrained Wireless Sensor Networks, but the pictured board shows a complex PCB with a high part count and large footprint.

Radio-Triggered Wake-Up for Wireless Sensor Networks is wonderfully well written and gives great hand-holding in case the designer wants to add range. However, Figure 3, where it gives a simple RF detector schematic, is confusing to the layman because there's no ground drawn to the antenna [Update: see comment section below]. Here's Figure 3 from that paper:

Design Optimization and Implementation for RF Energy Harvesting Circuits (related spinoff papers 1 and 2) is another very well written resource, diving into fascinating detail on practical optimality choices, but it does not present the final tested schematic.

I'm hoping this is the RF detector equivalent of a paperweight, that is to say there's no need for refinement, it doesn't matter if it's ugly, and there's almost no way to do it wrong.

### Appendix

Typically, one would want an OOK stage in order to disambiguate between other signals which might trigger a false positive, but because in my application the nearest possible source of EM radiation is hundreds of meters away, and because the consequences of a false positive-- even if it's tens of times a day-- are negligible there's much less need for complexity. KISS, price, and compactness are higher priorities.

## Answer (score 2, by Phil Frost - W8II)

I'm going to disagree with Marcus and say that you can probably get this to work, for some relaxed definition of "work".

The detector you've drawn has poor *selectivity*, meaning it will detect quite a lot of stuff besides the intended signal. The inductor and capacitor provide some amount of filtering, but not nearly as good as you'd get in any basic receiver.

Aside: the better that filter is, the more sensitive to temperature variation it will be. Also, at 900 MHz you'll have to give some thought to the circuit layout, since at this frequency parasitics can be pretty significant.

On the other hand, path loss at 900 MHz and 5 meters is only 45.5 dB. Assuming 0 dBi of gain on both antennas that means you're looking at a received power around -36 dBm. That's pretty strong, even feasibly the strongest thing around if there are no other electronics nearby. This is good news because it means poor selectivity of the detector is not much of a problem. If you're near any WiFi radios, cell towers, broadcast stations, or even very near any digital electronics, you'll probably have trouble.

The one area you'll probably need to improve is amplification of Vout. Although -35.5 dBm is fairly strong for a received RF signal, it's probably not going to be enough to reach the GPIO's threshold. Addressing that is a simple matter of adding a comparator, op-amp, or even a simple transistor.

If you want a step up in sophistication, there are integrated RF transmitters and receivers that are *really* cheap. Besides helping with a lot or all of the amplification and filtering, they also provide digital modulation and demodulation.

Or if you want the satisfaction of building something yourself, it wouldn't be too complex to make a mixer, which would convert the 433 or 900 MHz down to a frequency low enough that it could be sampled by the ADC on a microcontroller. Then you can do some very simple demodulation to confirm the signal is from your device and not noise. A good receiver will include some filtering to reject image frequencies and maximize dynamic range, etc., but if your performance requirements are low then you can skip all that stuff and simplify the circuit substantially.

## Answer (score 2, by Marcus Müller)

Well, your GPIO will need a defined voltage level and a couple of µA of drive strength, so completely "passive" is probably not really possible.

Now, you'll need the following:

1. Antenna

 1. potentially, amplification here
2. Filtering

 1. potentially, amplification here
3. Rectification
4. Thresholding
5. GPIO activation

For antenna choices, see Texas Instrument's antenna selection guide.

1. Will probably simply be a stumpy coil antenna for 433 MHz, and might be PCB antenna or even a chip antenna for 900 MHz.
2. Antenna -> capacitor -> LNA (example, ca 10 ct) -> Filter (example, ca 40ct)
3. RF Schottky Diode (example) -> RC low-pass filter with cutoff above 1/(minimum pulse length)
4. opamp in comparator configuration (DON'T use any opamp before 1984): connecting the non-inverting input to a virtual ground defined by a trimmer between VCC and ground
5. (optional) buffering of opamp output with MOSFET or BJT

Important: learn to use SPICE so that you can simulate the elements of your detector. It's time well-invested, as "KISS" means "don't try to measure something for hours that simply doesn't work, which you could have seen in simulation".

Your RF detectors can take jobs 3 to 5, but you'll still have to make the things frequency selective, so there's little way around 2.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17337/building-a-low-power-simple-rf-frequency-433mhz-or-900mhz-but-not-both-detecto, by Kenn Sebesta, Phil Frost - W8II, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
