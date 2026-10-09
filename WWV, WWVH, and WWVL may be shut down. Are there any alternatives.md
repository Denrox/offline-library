# WWV, WWVH, and WWVL may be shut down. Are there any alternatives?

*Tags: transceiver, equipment, testing, calibration, wwv · score 15*

## Question

The US government is proposing to shut down the NIST standard time and frequency stations WWV, WWVH, and WWVB in Colorado and Hawaii.

If that actually happens, are there any free or inexpensive **alternative frequency standards** available so that we can accurately calibrate our transceivers, frequency counters, etc. with at least 1 Hz accuracy?

- https://www.google.com/search?q=wwv+discontinued
- https://www.eham.net/articles/41765
- http://www.arrl.org/news/concern-rising-within-amateur-radio-community-over-wwv-wwvh-shut-down-proposal
- https://forums.qrz.com/index.php?threads/wwv-discontinuing-operations.624002/

WWVB is a time station only; without its radio transmissions, millions of consumer "atomic" radio clocks would have nothing to keep them accurate.

## Accepted answer (score 4, by Jim MacKenzie VE5EV)

Don't forget about CHU (and here is the official site) which is the Canadian equivalent to WWV. It's at lower power and it's not as well-located geographically (it's located near Ottawa), but it's receivable in most of the eastern US and increasingly less well as you head west. Here in VE5-land (Saskatchewan) I certainly receive it sometimes, but I also don't have an ideal HF antenna setup either.

It transmits at 3 kW at 3.33 and 14.67 MHz as well as with 10 kW of power at 7.85 MHz.

One nice feature is that it frequently transmits time data in Bell 103 modem format, which is fairly easy to decode. It of course also has spoken word time.

## Answer (score 13, by Marcus Müller)

## GPS-based frequency standards

@larsks answer rightly pointed at devices that use GPS to generate the 1-second pulsing.

That's the correct way to go.

Curiously, these modules only address the once-per-second accuracy issue, not the frequency standard issue, which GPS is indeed commonly used to solve:

You'll find a lot of modules on the market that will not only give you a Pulse Per Second (PPS), but also a frequency standard signal, most commonly 10 MHz, but there's other frequencies, too.

### Frequency standards in cellular infrastructure

GPS-discplined oscillators (GPSDOs) are really common in cellular base station technology, where you must very accurately coordinate frequency (and time), to be able to use the (billions of euros) licenses for the limited spectrum you've got most efficiently – avoid the guard band between you cell's "own" band and the neighboring cell, as well as minimize frequency-error induced losses in transmission.

#### GPS-disciplined oscillators

Thus, in the professional world, WWVB and similar things are pretty much forgotten, since the signal simply is too narrowband to give you a good frequency and timing estimate within short time.

You can find a lot of these modules on the surplus/used market – Trimble GPS comes to mind, for example – but you can also build such things yourself:

The Opendigitalradio project (a project to establish broadcasting systems for digital audio broadcasting), or rather Matthias HB9EGM himself, has built a GPSDO:

Aside from the uBlox LEA-M8F GPS receiver, reference clock + PPS generator module, there's barely anything on that board – a chip to regulate the supply voltage, and one to protect against ESD if one decides to solder on the USB debugging plug. Then, one buffer for 30.72 MHz (or configurable frequency, IIRC) and PPS each.

Don't know if it'll need special communication via the serial port headers soldered on below to start (don't actually think so!), but these could be trivially supplied using just any $5 USB-to-TTL adapter out there.

#### Why are those more expensive than the typical GPS module?

Note that the LEA-M8F is much more expensive than your average GPS module, just because it's also supplying a reference frequency, not only location and PPS. I know that people also simply use digital PLLs (i.e. counters) and VCOs to generate reference clocks from the PPS signal – it's easy: I count the oscillations between two rising PPS edges (there's a lot of microcontrollers that can do that in hardware for you, without any need for running a counter in software). If it's higher than it should be, lower the control voltage to the VCO, and vice versa. Of course, the better your VCO gets, and the better you filter that control voltage, and the smartser you get at calculating the adjustment, the less overshoot and beat frequency you'll have.

That means that if you don't need the speed at regulation and the full accuracy that a proper GPSDO can give you, a simple GPS receiver that gives you only a PPS can also be used as a frequency standard. About it's quality compared to WWVB, see the next section.

#### Comparison of even cheapest GPS-based solution to what you can achieve using WWVB

But: if you can leave your microcontroller + GPS running all day, have a good place to put your GPS antenna (i.e. any roof) and thus your oscillator can have all time in the world to reach a stable frequency, well, pretty sure that $10 in hardware will give you a better frequency standard than most WWVB receivers; leave alone the timing accuracy, which is (really) laughable in WWVB:  
GPS specifies some +- 50 ns accuracy, whereas you're free to calculate which SNR you'll need to achieve that in a receiver that has maybe 100 Hz of bandwidth. Hint: It's a lot of SNR; the diagrams you find online for WWVB act as if the edge of the PPS are "straight up", of course, that's physically/mathematically impossible within limited bandwidth, so these edges are very sloped actually, and to get a reliable timing estimate, you'd have to "count the second" when you cross a very exact voltage threshold – but noise will make these slopes "jiggly", and thus, you'll need to average enough of these crossing times to get a good estimate. GPS isn't *that* different there, but the bandwidth is much higher, so that each PPS is already the result of quite a lot of averaging.

#### Commercially availability of GPSDOs

As said above, such devices are *necessary* for cellular infrastructure – and there's a lot of demand for that, so there's company specializing in such devices, Trimble, or Jackson Labs for example.

#### Observation/Correction based approach

**also known as: give me a lousy clock, but tell me its error.**

A completely different approach can be taken if you've got a device from which you can extract the mixing frequency (base): There's tools like kalibrate (I think that's even shipped with some Linux distros!) with which you can just scan the frequencies on which GSM works, and estimate the GSM "carrier frequency" (it's a tiny bit more complicated, but in essence it's just estimating a carrier), *based on your device's inaccurate clock*.  
Now, GSM is cellular, and is, you guess it, frequency-based off GPS. You use those estimates to measure the error of your receiver's frequency, and thus, you can now just incorporate that relative error (e.g. "the frequency is off by -0.0008%") to just adjust the frequency you configure e.g. your classical transceiver to, if you base it off the same reference frequency.  
I've not done it, but if you have a (modified) RTL-SDR dongle with a slightly more stable oscillator (which is ... not hard to achieve), you could add a high-z-input buffer to that oscillator, modify Kalibrate to work with the RTL-SDR, and use the estimated error. You'd have a "correctable" 28.8 MHz oscillation – which *can* be extremely helpful, especially when you consider that there's a lot of very flexible LO synthesizers, which you could feed with 28.8 MHz and use to generate a Phase-locked 10 MHz (or 20 MHz, or 2.4 GHz or, really, whatever rationally related frequency) directly from that.

There's a whole bunch of so-called *clock nuts* (I call them like that, because the only two I personally know call themselves such) that specialize in having good frequency and time standards. If that's your thing: Go for their community ;)

## Answer (score 13, by larsks)

In No WWVB? No problem!, KB6NU points at two projects that show you how to build your own low-powered WWVB-replacement to keep your clocks in sync:


μWWVB: A Tiny WWVB Station. This project uses an attiny44 microcontroller and a USGlobalSat EM-506 GPS module to simulate WWVB.


One Component Radio Clock Time Transmitter: This project uses an attiny45 microcontroller to simulate WWVB. As is, you set the time by changing some defines in the code. You’ll probably want to change that to get the time variables from a GPS source or an ntp source, but at least you’ll be able to generate the 60 kHz once you have that time information.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/11816/wwv-wwvh-and-wwvl-may-be-shut-down-are-there-any-alternatives, by Mike Waters, Jim MacKenzie VE5EV, Marcus Müller, larsks. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
