# FM radio in car gets interference from APRS beacon

*Tags: mobile, vhf, rfi, beacon · score 6*

## Question

The FM broadcast radio, factory installed in my car and usually tuned to 88.6 MHz, gets some interference from the 5W APRS transmitter on 144.800 MHz. It sounds like if the sensitivity of the broadcast FM receiver would go down a bit temporarily: more static FM noise is heard during the APRS "brraaap". The effect is more pronounced when I'm far away from my favourite station's transmitter and the signal is already weak. When I'm in town, it's barely noticeable.

The APRS transmitter has a properly mounted antenna (hole-through-roof, 1/4 wave vertical). The broadcast radio of the Volvo V70 does not have visible external antennas - there's one painted on the left trunk window, and apparently a second one embedded within the back right light assembly.

What can I do to fix this?

## Accepted answer (score 4, by Adam Davis)

There are a few ways the noise could be transmitted to the car radio, and the way to fix it will depend on how it's getting in there.

1. Antenna
2. Power or ground
3. Other EMI

If the transmission is swamping your radio's receiver, then it's not blocking the higher frequencies strongly enough. It might be worth looking at the output of the transmitter to see if it's broadcasting noise on other bands within the radio's region, and to take another transmitter that's not connected to the vehicle's power or ground and keying it up nearby. If it disturbs the radio, then it's likely that the radio may need to be replaced. Other options would be a different antenna.

If the transmission is coming through the power or ground, you might be able to add additional filtering and regulation at the radio. This can be tested by attaching a dummy load to the transmitter while it's transmitting. If the noise is present, it's likely EMI or power conduction. Again, keying a separate radio outside the vehicle may narrow it down. Alternately, connect the APRS transmitter to a battery power supply and disconnect it from the car's power supply. It'll still be grounded to the car, but it should narrow things down a little more.

EMI is a tougher one without a spectrum analyzer. If the transmitter and radio are far apart, though, and each have their own metal case, it shouldn't be the cause. I'd look for antenna and power problems first.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/414/fm-radio-in-car-gets-interference-from-aprs-beacon, by oh7lzb, Adam Davis. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
