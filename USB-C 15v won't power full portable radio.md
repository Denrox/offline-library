# USB-C 15v won't power full portable radio

*Tags: voltage, power, cables · score 4*

## Question

I bought this USB-C to 15 volt, thinking it might allow radio to work with any USBC laptop charger, USBC power bank/car charger, etc.

https://www.newegg.com/p/2B7-003A-00052?Item=9SIA20PJYZ7273

It gives nearly exactly 15v.

I plugged it in to a Mac/laptop charger (Nimble GAN charger: https://www.gonimble.com/products/wally-wall-charger) which should provide 65 watts. It powered up the Yaesu ft2980, but keying up, even on low power, turns the radio off immediately. Just like it does trying high power on battery power.

Is this just a device that's not going to work with this - do I have to use a different charger, maybe one that provides more 12-volt amperage?

## Answer (score 6, by hobbs - KC2G)

As John Custer mentions in comments, the usual way of things for USB-PD "chargers" is that they support 3A on all voltages except their highest, and the specs you linked to agree with that: they say "5V/3A, 9V/3A, 12V/3A, 15V/3A, 20V/3.25A". So when used with a 15V trigger it will provide a max of 3 amps, or 45 watts.

Meanwhile, the FT-2980 manual's specifications page says that its "typical current draw" is 4A when transmitting on the lowest (5W) power setting.

So no, you shouldn't be surprised if it doesn't work.

## Answer (score 2, by Ryuji AB1WX)

Yaesu ft2980 has multiple low power settings. The only setting that most likely does not exceed the 65W (4A) limit is "low1" or 5W setting. "Low2" or 10W may still be under 4A but iffy.

So, I would test this:

1.

Make sure the transceiver is set to "Low1" and 5W setting. Connect to a dummy load or proper antenna and test again.

2.

Test the USB power with another 15V 2 to 3A load, such as a resistor, lights, motor, etc. other than radio transmitter.

If 1 fails but 2 passes, there is another possibility. The RFI caused by the transmitter may be triggering the safety feature or malfunctioning something in the USB power supply. This kind of things happen more often than you might think. If this is the case, you might have to insert a good common+differential mode choke filter in the DC power line. It is also preferable to put RF common mode choke in the feedline.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/23561/usb-c-15v-won-t-power-full-portable-radio, by NoBugs, hobbs - KC2G, Ryuji AB1WX. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
