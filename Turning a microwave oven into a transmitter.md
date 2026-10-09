# Turning a microwave oven into a transmitter

*Tags: microwave · score 7*

## Question

I know this sounds dangerous and crazy, but those microwave transceivers like the IC-905 are expensive. So, I was wondering if I could make a microwave transceiver with a microwave. You can buy 1200-watt microwaves for under $300. The 1200 watts is the RF output, right? Or is it the wattage going into the microwave? If I opened up the microwave and take out the magnetron, could I use it as a radio? I made a schematic below. I know this won't work, but does this contain the basics?

Would the relay break if it's switched on and off very quickly? If I add a transistor to it, the transistor might break under the high voltages. Is there another component I can use? According to my research, the IC-905's output power is only 10 watts, so would 1200 watts be too much? Google says the microwave oven operates at 2.45GHz. Would that interfere with WiFi? I didn't get any useful results on if hams can operate on 2.45GHz, but I'm guessing not. Can I change the frequency of the magnetron so it operates on, say 10GHz?

People are saying that microwaves will damage devices and humans nearby. But, if someone drilled a hole in their microwave door and run it, wouldn't it have bad consequences? Or if somebody bought a cheap microwave from eBay that has a leaky body, wouldn't the devices break? I'm pretty sure this stuff occasionally happen. I think if devices aren't in the same room as the microwave, they would function normally, and if humans aren't directly in front of the hole in the door, they won't feel any heat.

## Answer (score 17, by Marcus Müller)

The 1200 watts is the RF output, right?

Typically, it's the High Voltage transformer's input, but the RF conversion in microwave ovens is relatively efficient, which you can see by the fact that they don't burst into flames very often.

If I opened up the microwave and take out the magnetron, could I use it as a radio?

You need a magnetron, the excitation electronics, and then something to actually modulate the output of the magnetron with information. Additionally, you'll need output power and frequency stabilization that domestic microwave ovens don't need.

Magnetrons are, if you will, just a RF cavity resonator that can be "pumped" with external high voltage. They need to be operated in a continuous mode, at relatively constant power.

That means that your method of getting some information on the generated RF needs to deal with the high-power signal as is.

Therein lies the technical challenge!

When you just switch your magnetron on and off, you'd get terrible spurs due to the process of getting your non-radar magnetron up to power. You'd need to account for that by more high-power RF switching and filtering, which is where you quickly cross into "more expensive than a good microwave amplifier".

Generally, you can't switch a relay with a microphone. A relay can be switched a few times per second, and will wear out after a couple million switchings, whereas audio has more than "on/off" information, and also crosses zero a couple thousand times per second. So, nope, this is architecturally not possible at all.

According to my research, the IC-905's output power is only 10 watts, so would 1200 watts be too much?

If you want to fry birds in-flight, it would be appropriate. I don't know any communication signal standard that would use microwave frequencies and require that much power from an amplifier.

I didn't get any useful results on if hams can operate on 2.45GHz, but I'm guessing not.

You've got the KC3WCR call sign, and that means you're in the US; and as you know, legal bands are subject to local legislation! So yes, you can (that is extremely simple to research!).

Can I change the frequency of the magnetron so it operates on, say 10GHz?

No. The range of resonant frequencies is defined by the shape of the magnetron.

Also, 10 W *is very significant output power*; I'm not quite sure what your motivation is going for 1200 W? You would literally damage a lot of devices in your vicinity, you would probably cause bodily harm to yourself, and you seem to be vastly underestimating the cost and complexity of even transporting 2.4 GHz, let alone 10 GHz, at these high powers for any significant distance.

Note that it makes little sense to say "I want high power, but I only want to transmit voice". What would you need high power for? Free Space Path Loss at microwave frequencies means you're not doing far links, anyways: Adding a factor of 10× in power is very expensive, but only means a minor range increase. The high bandwidths you can use in the microwave bands mean that you can take your voice information, and spread it in bandwidth as needed, so that you can work at low spectral density. "More power == more good" is a falsehood that's sadly very common in the ham hobby, but in reality, systems need to be designed for transmitters to use *as little output power as possible* – otherwise, you just end up in a screaming match where everyone in range tries to scream louder than all the others, leading to overall *worse* performance than if everyone was using only little power.

## Answer (score 9, by Ryuji AB1WX)

There are several problems with magnetrons for communication system. Just a few to start with, the frequency is very unstable. That is actually an advantage when used to heat food, because the hot spots are diffused due to frequency drift. Also, the output power is unstable. The reason why microwave oven can't adjust the output power very well is because the pulse width modulation to control the heat output needs to be very slow, like 10 seconds or longer. Even then the power is unstable. So, one could theoretically think of very slow Morse code like a half word per minute with very bad QRH so that the receiver constantly needs to track the transmission frequency. That is no fun.

HOWEVER, there are new generation solid-state microwave ovens. Those use LDMOS RF power transistor. Those components may become useful for amateur radio in the near future.

Here's an example of 350W LDMOS transistor for 900MHz ISM band.

https://www.nxp.com/docs/en/data-sheet/MHT1002N.pdf

### Addendum / response to your additional questions

Microwave ovens have safety mechanisms by the door switch. The RF power is cut off when the door opens. However, there is a brief period of time when significant RF power can leak through the narrow door gap when an operator opens the door but before the power is completely cut off. This is a well-known RF exposure and cause of RFI. It is always best to stop the oven on the panel control and then open the door.

Holes on the RF shields on the chassis/door cause much more significant leakage of the RF power than in the above scenario, and I would not operate such a defective oven.

Even with a microwave oven with completely intact shields, the leakage is significant enough that many Bluetooth devices drop the connection or lose data packets, especially early generation products. Things became better, but that is because of the improvement in the Bluetooth chips, not reduced RF leakage.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/23249/turning-a-microwave-oven-into-a-transmitter, by John Doe, Marcus Müller, Ryuji AB1WX. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
