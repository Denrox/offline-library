# RX antenna and RTL SDR with upconverter ..How to hear something?

*Tags: antenna, software-defined-radio, rtl-sdr, transverter · score 6*

## Question

I mounted a small RX antenna (mini whip, bought from eBay) (on 10-th floor) and I want to try to listen to something. I bought a RTL-SDR with Upconverter which supports HF. RX antenna's operating range is 100kHz - 30Mhz.

- If I want to listen something. I need to set some frequency with SDR app? And wait all the time. At now I'm using CubicSDR and sometimes Gqrx. Frequency spectrum is so big 100kHz - 30 Mhz. Is it possible use auto search?
- Which frequencies to try ? I'm live in eastern Europe, Lithuania. Near Baltic sea.
- Is it possible to make SDR app to disable big loud noise. I want to set trigger. If threshold exceeded I want to hear something. Are current SDR apps capable of doing this ?

I am willing to try SDR Sharp or HD SDR.

I successfully hear AM radio stations. But I want to hear something from ham radio operators (even though I can't transmit).

My antenna:

## Accepted answer (score 7, by natevw - AF7TB)

Fun setup! I have many of the same components and need to try them out myself, but here's a general outline. (Plenty of this may be review for you, but I'm including it for others who may not be as familiar with your equipment.)

### The antenna

A miniwhip (see also this article and this PDF) is an active antenna taken to the extreme: it uses a tiny conductor to intercept a tiny bit of broadband electromagnetic field, and then amplifies it by a huge amount — perhaps on the order of +35dB gain.

Being an active antenna it will either need to be plugged in to a DC power source, or (as is more typical) you can "phantom power" it via a bias tee.

Also, the antenna is amplifying the difference between its whip/plate and its ground:

without any conductive connection to the outside, the entire circuit will be at the same potential

The typical installation recommendation has you attach the ground (or the shielded outside of its coax connection) of the miniwhip to a conductive and grounded mast. For example, this eBay listing mentions:

For max. sensitivity:

- this antenna should be positioned as high and free from metal conductors as possible.
- the ground plane of the PCB must NOT be lower than the top of the mast. (the connection to and the antenna surface itself must be ABOVE the top of the mast).

For best signal-to-noise ratio:

- install the Miniwhip onto a well grounded mast.
- connect "GND" of the Miniwhip PCB to that mast.
- place HI-Ui ferrite cores […] on the beginning and end of all cables to block cable noise currents.

Generally with this antenna you are encouraged to avoid electrical noise on the whip and/or its grounding as much as possible. However, that may be something to go back and optimize *after* you've addressed the next topic…

### Avoiding overload

Feeding a broadband active antenna into an 8-bit SDR without filtering will almost certainly cause all sorts of distortion/intermodulation/overload issues in the presence of strong signals.

You mentioned that you *could* hear "radio stations" which I assume are high-power broadcast transmissions. These loud signals might be preventing you from receiving anything else.

For the "AM broadcast" band in the USA, I found this AM band-stop filter. These MW broadcasts do vary from region to region, for example I also found a design apparently for blocking similar in Australia. In Europe you may need a couple bandstop filters for various local AM and shortwave bands.

(As mentioned above, nearby electrical noise from computers and power supplies can also make strong interference.)

### Upconverted frequencies

Since the RTL-SDR only tunes down to about 27MHz or so, you will need either a direct sampling modification or an upconverter to tune in to most of the HF and lower frequencies.

It sounds like you have an upconverter, so you need to find the "local oscillator" frequency, it may be written on the device or should be listed amongst its specifications. My "full band" RTL-SDR unit has an integrated upconverter using 100MHz.

The external Ham It Up v1.3 uses 125MHz.

Basically what an upconverter ends up doing is "adding" its local oscillator frequency to every signal. So if you wanted to listen to 1040 kHz using a 125MHz upconverter, you would need to tune your SDR app to 126.04MHz at first.

However, this is a common technique and so most apps let you enter in this frequency offset so that the display becomes more natural. For example, Gqrx calls this the "LNB LO" input control. CubicSDR has something similar, iirc. Note that in some apps you have to enter "-125 MHz" (negative) and in others you just use "+125". Once you configure this, to tune e.g. 1040kHz you type in 1.040MHz directly in the display and the SDR app calculates the proper actual frequency for you.

### Which frequencies to try?

If you're looking to hear Amateur Radio activity, you can start by consulting a band chart for the overall ranges where hams are allowed to operate.

Within each of these allocations, there is typically a band plan that divides the available spectrum into particular frequencies recommended for particular activities.

The band chart/plans linked above are published by ARRL, the big ham lobbyist organization in the USA. Note that amateur allocations vary slightly between nations and regions. But since it's all ultimately coordinated via the ITU, there's typically a lot of overlap.

When I am looking for amateur signals, I often start with the JT65 frequencies since those "channels" tend to provide a good density of long transmissions despite the low power typically used. E.g. if you listen at 7.039 or 7.076 MHz using an upper sideband decoder, you might hear a few 40m transmissions piled close together, sounding almost like bad music.

### Squelch the static

You are looking to "disable big loud noise", which made me first think of a [noise blanker](What%20does%20a%20noise%20blanker%20really%20do%2C%20and%20what%20are%20the%20side%20effects.md) but your description about setting a trigger level sounds more like squelch.

Most full-featured SDR apps have both noise blanking (NB) and squelch too. Sometimes there are even separate RF (radio frequency, meaning the input signal) and AF (audio frequency, meaning the decoded/demodulated signal) squelch options. They vary from app to app and sometimes I've found using them to be confusing, but most SDR apps should have them if you know where to look.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9220/rx-antenna-and-rtl-sdr-with-upconverter-how-to-hear-something, by kesrut, natevw - AF7TB. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
