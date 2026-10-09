# AIS and RTL-SDR Dongles

*Tags: software-defined-radio, rtl-sdr, gnuradio · score 11*

## Question

I am looking for an Windows-based AIS Decoder for RTL Dongles. Currently, there is a solution available using GNU Radio and SDR# but it is complicated to set up and keep running.

ADSB has a dedicated solution called RTL1090 that connects directly to the RTL-Sdr stick and decodes the ADSB messages in one application.

Does anyone know of a project like this for AIS Ship Tracking?

## Answer (score 9, by Peter Grace)

You could check out ShipPlotter which appears to be a windows-based AIS receiver. It mentions in the webpage that it accepts audio through your sound card. In the case of RTL-SDR, you'll want to use something like "Virtual Audio Cable" or "VB-Audio Cable" to route the audio from sdrsharp to ShipPlotter.

## Answer (score 4, by KD7KUJ)

Check out AISMon; I've never used it, but it looks like it fits the bill. Here's a thorough tutorial: http://www.rtl-sdr.com/rtl-sdr-tutorial-cheap-ais-ship-tracking/

## Answer (score 3, by Marcus Müller)

Three years later:

Currently, there is a solution available using GNU Radio … but it is complicated to set up and keep running.

Well, you're referring to Nick Foster's gr-ais, which is a GNU Radio out-of-tree module, and actually, not that hard to set up.

In fact, it's included in current versions of the GNU Radio Live DVD, and you should be able to just boot that, and run ais_rx; haven't tried that out lately, because I've installed it directly on my normal system; I've got GNU Radio installed, so the dependencies are already there:

```
git clone https://github.com/bistromath/gr-ais
cd gr-ais
mkdir build
cd build
cmake ..
make
make install

```

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/173/ais-and-rtl-sdr-dongles, by Mark Cupitt, Peter Grace, KD7KUJ, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
