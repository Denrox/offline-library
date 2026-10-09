# Signal generator giving DC output?

*Tags: rf-power, equipment-troubleshooting · score 5*

## Question

My signal generator is giving DC at its RF OUT port. At 500 MHz & 1GHz it's giving nearly 1.5V DC when I measure the voltage between the centre pin & outer conductor with a multimeter.

I don't know whether this is the right way to measure or whether this output voltage is normal. The equipment is working fine and passing its self-test.

What would be the reason for this?

## Answer (score 2, by rclocher3)

Multimeters are generally used to measure AC volts at line frequencies, i.e. 50/60 Hz, and yours is almost certainly not accurate at 1 GHz. Similarly your multimeter's DC volts setting is designed to measure static DC volts, not the DC bias of a 1 GHz signal. To sum up, your multimeter measurements are probably completely meaningless.

If you want to see what's really going on with your signal generator, look at the output some other way. (Whether there is a DC bias probably isn't important, because you will almost always use a capacitor to couple the output, and the capacitor will block the DC.) You could connect the signal generator to a radio, through a capacitor and an attenuator of course, and listen for the output. You can make an attenuator with a few resistors. If you hear the signal in the radio, then the signal generator probably works fine.

The ultimate way to check what's going on with the signal generator would be to look at the output with a 1 GHz-rated oscilloscope and/or a spectrum analyzer, but those instruments probably cost a lot more than the signal generator did.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6797/signal-generator-giving-dc-output, by Geoabs, rclocher3. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
