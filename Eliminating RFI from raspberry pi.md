# Eliminating RFI from raspberry pi

*Tags: rfi, rtl-sdr · score 5*

## Question

I am trying to eliminate RFI coming from a raspberry pi 4. The Rtlsdr(enclosed in a metal case) is directly plugged into the pi without any USB extension cable. The frequency of interest is at 1420.40575Mhz, few strong spikes that can be seen in the picture attached can be removed easily with a median filter, but the broadband peak around 1.4199e9 and groups of spikes at 1.4208e9 isn't. I am guessing that the raspberry pi is conducting interference straight into the Rtlsdr, or the problem could also be the Rtlsdr itself as it is a counterfeit... I don't think the RFI is coming from the switching power supply, as I record similar patterns of interference when I tried laptop running on battery+rtlsdr. What lengths of USB extension cable do you guys suggest? I am looking at a 6.5mm diameter USB extension cable, from ugreen(no affiliation), that offers good shielding according to the specs.

1.Rtlsdr and Rtlsdr+biast+lna with rpi.

2.Rtlsdr+biast+lna with rpi and laptop.

3.1.8Mhz wide in 100khz step rfi scan, setup plugged into laptop.

## Answer (score 3, by tomnexus)

Do the spikes still appear when you connect the RTLSDR to a laptop instead? Are they definitely caused by the Pi? I can see a few tones near 1420 MHz on my RTLSDRblog (with an antenna), they get stronger near a raspberry pi.

One thing that might make the spikes smaller is to use more RF gain at the antenna, and turn down the gain on the SDR.

Shielding the Pi will be difficult because it has so many cables connected to it, but it's worth a try. Experiment with some aluminium foil, crunched in carefully so it touches the ground part of every single connector entering the Pi - the USB, LAN, Power and HDMI cables. Better would be to use copper tape between the connector and the plastic case, and then wrap that in aluminium foil. You won't be able to use wifi. But the noise might be harmonics of things inside the SDR too, and you can't easily shield that.

Ultimately in a radio telescope, after cleaning up the RF hardware as much as possible, you may have to remove the worst spurs in the data. Manually or automatically flagging and deleting the individual bad channels. You plot the *extra power* at each frequency, so the smooth lumps in the spectrum can be subtracted.

## Answer (score 2, by hotpaw2)

If the suspected RFI is conducted from the Pi, then the RFI spectrum should change if you use a much longer USB cable with both ends of the cable wrapped several turns through large enough ferrite toroids. If the RFI is from switching power supply noise through the Pi, then the pattern should change if you loop the cord to the Pi several turns through a ferrite toroid near the wall-wart end. If there are any other cables connected to the Pi (HDMI, ethernet, keyboard, etc.), suspect them as well. To see if the tuner chip is generating the RFI via mixer feed-thru, try tuning the RTL-SDR to different slightly (say +- 10 kHz to +- 1 MHz) offset frequencies from the center frequency of interest, and see if the interference lines move in frequency with your offset.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20448/eliminating-rfi-from-raspberry-pi, by radastro, tomnexus, hotpaw2. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
