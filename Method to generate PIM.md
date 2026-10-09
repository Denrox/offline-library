# Method to generate PIM

*Tags: rfi · score 3*

## Question

I would like to have a go at measuring PIM. ( Passive Intermodulation ) in UHF.

To test my ability to measure PIM, I need to find something that generates PIM.

I either envision a 50Ω device that generates PIM, or a 2-port thru device which can be terminated on one end.

If anybody has any links to PIM sources, or home-brew build ideas, let me know.

## Accepted answer (score 3, by tomnexus)

For generating PIM - for testing and calibration, you want a known level signal at the expected intermodulation frequency. This will let you calibrate the whole setup though the losses of the various combiners and filters, and by switching it on and off, measure the level of PIM in your measurement system.

I'd recommend using a signal generator at the correct frequency, feeding that in through a suitable attenuator.

You probably don't want to use a non-linear device to actually generate PIM. Connecting a diode or something to the test point (with an attenuator, and some DC bias) will generate plenty of PIM, but at an unknown level, so you'll have to start by fully characterising your non-linear device.

You can make a low-PIM high power attenuator with a roll of very thin coax. In a 30+30 watt, 900 MHz test set, we used something like this 1.19 mm diameter EZ-47 which has 32 dB/100' attenuation. 50 feet is not a large roll of this cable.

You will need a low-PIM termination for the other side of your device under test, this gives you a way to upgrade your ordinary 50 Ohm termination. Combined with some ordinary attenuators, it also provides a way to measure the final incident power and apply your fake PIM signal.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16524/method-to-generate-pim, by Skyler 440, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
