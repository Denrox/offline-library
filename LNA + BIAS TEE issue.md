# LNA + BIAS TEE issue

*Tags: equipment-troubleshooting, lna · score 3*

## Question

I have an issue of LNA getting damaged. The setup is shown in the image attached. I have an LNA (5V DC powered, max 100mA, max 25dBm RF input) and a bias-tee (3.3-30V DC, 500mA capacity) next to the antenna over rooftop.

At the base station, I have the same bias-tee as shown in the image. The RF loss on the cable is around 1.2dB @ 145MHz. I get 5V from bias-tee next to the LNA. The antenna is of 5dBi gain and there were no high power transmissions nearby.

This setup works fine a day or two and the LNA gets damaged. I already lost two minicircuits LNA. Even with the antenna disconnected and the RF IN of LNA is terminated with 50ohm, one more LNA got damaged after 3 days.

Any ideas why the LNA is getting damaged? I am using both bias tee and LNA from minicircuits and also a good 5V DC power supply.

## Answer (score 2, by tomnexus)

A few possible sources of damage:

First is that under some conditions the Bias T can pass significant energy from the DC port to its RF port. This happens when the coax, already powered, is connected to the bias T. The near-instantaneous connection of the DC power has some high frequency components, so a full 5 V pulse will appear on its RF pin, for several microseconds, and then later the 5 V will appear on its DC port.

This won't happen if you connect the coax before turning on power.

I had mini-circuits amplifier + bias tee modules, destroyed randomly, until we figured this out.

One vote against this is that you're only using 5 V, and the amplifier bias is probably most of 5 V on the output pin anyway, so it won't matter much. We had +24 V or something.

The other possibility is static build-up on an isolated part of the structure, sparking through to the RF pin. Is the antenna DC shorted? And if it is, *is there any conductive part of the antenna which is not grounded?*  
Even a DC short via an inductor or quarter-wave line, is no match, ha ha, for the thousand-volt nanosecond impulse of a static discharge. The only way to protect the amplifier is to have nothing which can get charged up in the first place. This can be done with 1 k resistors or short circuits.

I don't think it will be damaged by nearby high power transmissions, (though it might be overloaded and perform badly). If the damage level is ~ 0 dBm, this requires a few watts within a few metres of the antenna. This is unlikely unless it's your own transmitter.

What about overheating? An aluminum box in the sun could reach 60 C, if the amplifier runs warm and it's mounted insulated from the walls of the box, its case temperature could reach over 100 C.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/22673/lna-bias-tee-issue, by enemra, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
