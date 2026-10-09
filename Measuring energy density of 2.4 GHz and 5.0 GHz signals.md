# Measuring energy density of 2.4 GHz and 5.0 GHz signals

*Tags: rf-power, wifi, measurement · score 3*

## Question

I'm a math and computer science student, starting to mess around with using amplifiers and antennas to build long-range wifi hardware in my spare time.

Calculating the expected power density of a system is easy enough, but--I'd like to measure power density directly. Namely, in the neighborhoods of 2.4 GHz and 5.0 GHz.

I went to the Physics department at my university to borrow equipment. They said EMF meters, gauss meters, etc. that work in the 5.0 GHz range are extremely expensive, and suggested I use a normal wifi antenna to measure field strength. I have since downloaded some software that gives me measurements from my laptop's antenna in dBm; I have no way of knowing how accurate those measurements are, however.

Also, given that I get to choose input wattage on the systems I build and can buy just about any antenna off the Internet as well as the next guy--I'd really, really like it if the meter were capable of measuring power densities in the "you should probably be worried" level ( and above, to some degree ).

Are there any meters out there that measure EMF power in the neighborhoods of 2.4 GHz and 5.0 GHz? Meters that are priced so that one can hope to afford them without the financial backing of an institution?

Ninja Edit : I'm perfectly aware of FCC regulations and follow them in my designs. I'm simply looking for tools with which to empirically verify the system *is* behaving as expected.

I'll hit up the EE department and local government for access to testing facilities.

## Answer (score 5, by Marcus Müller)

I'm a math and computer science student, starting to mess around with using amplifiers and antennas to build long-range wifi hardware in my spare time.

You're potentially breaking the law. In fact, I'm pretty sure you're breaking the law.

WiFi operates in the ISM bands, which sets a very strong limit on how much power your device might send in any direction, no matter how directive your antenna is. For most regions, you **must not** send more energy in any direction than what a theoretical antenna, which perfectly distributes power in all directions evenly, would emit when fed with 100mW. Take the same 100mW and feed it to an antenna with gain, and you're breaking the law.

Calculating the expected power density of a system is easy enough, but--I'd like to measure power density directly. Namely, in the neighborhoods of 2.4 GHz and 5.0 GHz.

Well, you need measurement equipment, and calibrated microwave equipment doesn't come cheap. I wouldn't let an untrained student anywhere near my calibrated measurement setup. Just too much work and money on the line here.

I went to the Physics department at my university to borrow equipment. They said EMF meters, gauss meters, etc. that work in the 5.0 GHz range are extremely expensive, and suggested I use a normal wifi antenna to measure field strength. I have since downloaded some software that gives me measurements from my laptop's antenna in dBm; I have no way of knowing how accurate those measurements are, however.

They're straight up unusable. Simple as that. Without an anechoic chamber, you'll have both fading and interference in the ISM bands. You can't do these measurements like this. Also, WiFi cards will tell you how much "WiFi-alike" energy they can detect. Which has pretty much nothing to do with how things are with the antenna. WiFi cards do amazing correction, self-adjusting amplification and other things that make them completely unusable as measurement devices.

Also, given that I get to choose input wattage on the systems I build and can buy just about any antenna off the Internet as well as the next guy--I'd really, really like it if the meter were capable of measuring power densities in the "you should probably be worried" level ( and above, to some degree ).

Did I mention the law? I think I did. To measure the radiation pattern of your antennas, you don't need much power. Cleanly detectable is enough. And for clean detection you'll need a clean room without interference (this is the ISM bands, where everyone is *allowed* to interfere) and reflections (these are microwaves. They will show very surprising non-line-of-sight propagation if you do not work in a room with echo-swallowing walls).

Are there any meters out there that measure EMF power in the neighborhoods of 2.4 GHz and 5.0 GHz? Meters that are priced so that one can hope to afford them without the financial backing of an institution?

Obviously, that depends on your budget. Still, you'd not only need the meter, you'd need an antenna measurement setup, which is a meter, a calibrated transmitter, calibrated reference antennas, calibrated cables, calibrated reference attenuators, calibrated stands, and an anechoic chamber. This will not be affordable to a normal person.

Really, don't try to measure an antenna yourself. Ask someone from the electrical engineering department or a specialized company if you'd ever need to do something like that. They might have an anechoic chamber, and they might have rates at which you can rent that, and rates at which you can pay a technician to conduct the measurement.

I really think you should first read up a bit on antenna theory, to be honest. You can analytically understand a lot of the simpler antennas, and for the more complex one, the manufacturer typically delivers measurements.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6319/measuring-energy-density-of-2-4-ghz-and-5-0-ghz-signals, by StudentsTea, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
