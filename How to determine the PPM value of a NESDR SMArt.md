# How to determine the PPM value of a NESDR SMArt?

*Tags: software-defined-radio, rtl-sdr, calibration · score 6*

## Question

a) Given that I don't have a frequency standard or other known transmitter available, what is the easiest way to calibrate the NooElec NESDR SMArt which is using a TCXO rated at 0.5 PPM.? I.e. to determine the PPM calibration value?

b) Also, is this value frequency dependent? (How so?)

c) Are there any European frequency standard transmitters I could use?

## Accepted answer (score 6, by Kevin Reid AG6YO)

Given that I don't have a frequency standard or other known transmitter available, what is the easiest way to calibrate the NooElec NESDR SMArt which is using a TCXO rated at 0.5 PPM.? I.e. to determine the PPM calibration value?

Find *any* continuous broadcast signal that has a carrier and you know the nominal frequency of, and adjust the PPM value until its peak in the spectrum display is centered on that frequency value.

The higher the frequency of the signal you are calibrating to, the more your local oscillator's error is magnified, so the more precise this eyeball procedure can be. (If you have a large error, it may be useful to start at a low frequency before moving up, so you don't have trouble finding the expected signal in band.)

Of course, it's only as good as the transmitter, which you don't know, but you can easily get it good enough for accurate tuning (as opposed to frequency measurement).

Also, is this value frequency dependent? (How so?)

No. The physical oscillator generates a signal at a fixed frequency, and the tuned frequency is derived from that in a way which more or less involves counting — there is no systematic “analog” error in it.

## Answer (score 4, by not2qubit)

I want to add some solutions to Kevins answer. Apparently I'm lucky to own the SMArt device as it is really stable with a **PPM** between 0.5 - 1.0 at all bands I've looked at. (Just as advertised.) So how do you calibrate your less stable RTL-SDR?

Basically there are many different ways out there. The easiest is indeed what Kevin Reid posted, whose method is shown nicely in this and this videos. However, a much more accurate way, is to calibrate against a GSM station whose known ARFCN frequencies are exact. This is what the ADS-B people usually do with older SDR sticks, before using *dump1090*. The best explanations I found, are the ones provided by [1] and [2].

The public available code to do this is called Kalibrate was originally made by Joshua Lackey from here. Since then there have been many iterations and alternatives, but at the end of the day the original is the best, as others are either device dependent, broken or dependent on libraries that are too new or outdated. There are now dozens of variations of this.

Finally I just used the old Windows version as the latest Linux one didn't compile. It worked great and made sense. This is a two step process.

1. Find the GSM channel (ARFCN) with the highest power.
2. Use this channel to calibrate to.

```

# We use an arbitrary gain of 30 dBm and a starting PPM of ~1,
# and throughout most of Europe we only have EGSM for 2G.

$ ./kal.exe -g 35 -e 1 -s EGSM -v

E-GSM-900:
chan: 6 (936.2MHz + 481Hz)      power: 297161.97
chan: 13 (937.6MHz + 427Hz)     power: 80136.18
chan: 45 (944.0MHz + 173Hz)     power: 72538.40
chan: 74 (949.8MHz + 264Hz)     power: 1357267.92
chan: 81 (951.2MHz + 157Hz)     power: 91010.07
chan: 104 (955.8MHz -  35Hz)    power: 426084.14
chan: 108 (956.6MHz + 128Hz)    power: 61358.88
Found 1 device(s):
 0:  ezcap USB 2.0 DVB-T/DAB/FM dongle

Using device 0: ezcap USB 2.0 DVB-T/DAB/FM dongle
Found Rafael Micro R820T tuner
Exact sample rate is: 270833.002142 Hz
Setting gain: 35.0 dB
meh: Scanning for E-GSM-900 base stations.
channel detect threshold: 28151.015811

```

We see that the ARFCN **74** is the strongest one, so we use it for the calibration.

```

$ ./kal.exe -v -e 1 -c 74

average         [min, max]      (range, stddev)
+ 235Hz         [228, 243]      (15, 4.489251)
overruns: 0
not found: 0
average absolute error: 0.753 ppm
Found 1 device(s):
 0:  ezcap USB 2.0 DVB-T/DAB/FM dongle

Using device 0: ezcap USB 2.0 DVB-T/DAB/FM dongle
Found Rafael Micro R820T tuner
Exact sample rate is: 270833.002142 Hz
meh: Calculating clock frequency offset.
Using GSM-900 channel 74 (949.8MHz)
offset   1: 230.82
...

```

And thus, for this test, we get a PPM of 0.753.

**References:**

[1] and [2]

For other implementations see:

- https://github.com/steve-m/kalibrate-rtl
- https://github.com/viraptor/kalibrate-rtl
- https://github.com/scateu/kalibrate-hackrf
- https://github.com/Nuand/kalibrate-bladeRF
- https://github.com/ttsou/kalibrate

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7347/how-to-determine-the-ppm-value-of-a-nesdr-smart, by not2qubit, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
