# SDR Transceiver over LAN

*Tags: software-defined-radio, antenna-system, feed-line · score 3*

## Question

The feed line is a limiting factor when designing a home HAM system. The further the antenna is placed from the transceiver, the greater the cost and attenuation. Is there a way to solve this with an SDR? If the DAC/ADC occurs close to the antenna, maybe the rest of the process could happen anywhere on the LAN.

## Answer (score 5, by hotpaw2)

You can do this currently with any network connected SDR that is capable of streaming raw or IQ samples, and run an SDR application remotely from anywhere there is a network connection, over LAN, WiFi, WAN, optical fiber, etc.

For receive-only, one can plug one of many makes of USB SDR receivers (RTL-SDR, Airspy, SDRPlay, Lime, Colabri, SunSDR, etc.) into a Raspberry Pi (or other small server), and stream IQ data over ethernet or WiFi from the Pi to something that can run an SDR app (PC, tablet, iPhone, etc.) See: rtl_tcp, hfp_tcp, rsp_tcp, et.al.

There appear to be network connected raw ADC's as well, but the full RF bandwidth at the ADC sample rate requires more expensive networks connectivity (optical, etc.), So most of the more affordable SDR receivers decimate to IQ data at a lower sample rate, either for network streaming over consumer-grade LAN, or for transferring data over USB-A, thus requiring a USB to ethernet converter (Raspberry Pi, Beaglebone, et.al.) to pass the data to a network.

Several digital transceivers can stream IQ data bidirectionally over an included network port, including older models of Apache Labs Anan's, OpenHPSDR Hermes, Hermes Lite 2, Red Pitaya, Afedri, Ettus, et.al. The rest of the SDR radio functionality (DSP, user interface GUI, or knobs and buttons, speaker and mic) can happen on some other box (or boxes, or tablets, or iPhones) anywhere there is fast enough network connectivity (not just LAN, but WAN).

Some receivers are small enough that, with a Raspberry Pi Zero W and small battery, one can place them right at (within a few centimeters) the feed point of the antenna, completely eliminating any feedline. Or with a Pi WSPR hat, you could transmit as well. Using WiFi or BLE for control point access.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20765/sdr-transceiver-over-lan, by Christopher J. Grace, hotpaw2. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
