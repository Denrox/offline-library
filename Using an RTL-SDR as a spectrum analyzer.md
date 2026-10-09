# Using an RTL-SDR as a spectrum analyzer

*Tags: rtl-sdr, spectrum-analyzer · score 10*

## Question

I've been trying to get into RF electronics, but one thing that is holding me back is lack of test equipment. I have an old analog oscilloscope, but that doesn't help much for things like verifying filter frequency or looking at harmonics. So far I have been keeping most of my experiments to lower frequencies (say less than 10 MHz). This way I can use a breadboard and not have things go way out of spec when I wave my hands nearby. As an example, I've built a 1-MHz LC oscillator and would like to determine if there are significant harmonics present.

I have been considering buying an RTL2832U USB SDR dongle to use as a spectrum analyzer. The basic device doesn't go below 24 MHz, but there are some that support "direct sampling mode" or that contain an up-converter. E.g. https://www.amazon.com/RTL-SDR-Blog-RTL2832U-Software-Defined/dp/B0129EBDS2/ and https://www.amazon.com/Usmile-100KHz-1-7GHz-UpConverter-Receiver-radio/dp/B01422FJMK/

From what I've read, the direct sampling mode is prone to noise and requires a filter to be useful. If I understand correctly this is because the tuner chip is bypassed, allowing signals above the Nyquist frequency to alias in and potentially overload the receiver. For use as a directly-connected (through an appropriate attenuator) spectrum analyzer, would this likely still be an issue?

If I were to choose one with an upconverter, should I worry about it creating spurious harmonics? What about the SDR chip itself? I realize that performance isn't going to be great for such a cheap module, but I'm hoping things like frequency-dependent sensitivity can be canceled out in software.

## Answer (score 4, by Phil Frost - W8II)

If you have a commercial transceiver you can reasonably assume it's free enough of harmonic distortion. You can then use that as a signal generator or a narrow-band spectrum analyzer to validate your other devices.

Besides looking at harmonic frequencies directly, you can perform intermodulation tests to get a sense of linearity without needing a huge bandwidth.

If you don't have a commercial transceiver, then maybe you can perform a measurement anyway. Plug your oscillator into the SDR, and if you see an absence of harmonics you are probably in good shape. If you do see harmonics you won't know if it's the SDR or the oscillator.

You might eliminate some unknowns with the SDR by using one intended for HF. For example the Softrock kits cost about $20 and work with your computer soundcard. Still many unknowns granted, but at least you are using a validated design for its intended purpose.

Worst case, hook these devices up to an antenna and can still make it work. Broadcast stations can be your signal generators, and public WebSDR installations can be your spectrum analyzers. Other stations will complicate measurements, but using this method you can probably rule out egregious design flaws.

Of course, none of this will get you the precision that would come with a proper spectrum analyzer, but it may be sufficient to determine if your equipment is within limits for spurious emissions, etc.

## Answer (score 3, by Marcus Müller)

In principle: yes, that will work.

I've never used an RTL dongle without a tuner / bypassing the same; I didn't know that was an option. But yes, as every ADC, you need to sufficiently limit the bandwidth of the signals you digitize in order to avoid aliases.

So, you'd be getting into a slight chicken/egg situation here – you need a good filter, but have very limited ways to test it. I do think it's pretty possible to build e.g. a 3-stage LC at 1.5 MHz cutoff, and use a > 2 MS/s sampling rate and come out just fine, but I've never seen the analog characteristics of such RTL dongles in tuner bypass mode, so I simply can't tell.

You'd have basically the same problem in upconverter and any "normal" tuner operation, though – you're trusting the behaviour of an unknown device, so yeah, I'd just try with the RTL-SDR dongle in direct sampling mode with a "probably working well" low-pass filter, and see; at USD 25 it might not break your neck, financially.

Regarding your specific application:

As an example, I've built a 1-MHz LC oscillator and would like to determine if there are significant harmonics present.

Ah, that's exactly the kind of application I'd be careful about before I've made some attempts at characterizing my low-pass filter – after all, it becomes very important how effective and flat that filter is if you want to assess spurs' energies.

## Answer (score 2, by Amin Shah Gilani)

It's possible and there are tools out there to aid you in this.

E.g. Please see [RTLSDR-Scanner][1] which describes itself perfectly:

A cross platform Python frequency scanning GUI for USB TV dongles, using the OsmoSDR rtl-sdr library.

In other words a cheap, simple Spectrum Analyser.

The scanner attempts to overcome the tuner's frequency response by averaging scans from both the positive and negative frequency offsets of the baseband data.

It comes preinstalled with Kali Linux if you have a copy, and will look like this (taken from the linked page):

That said, I'm not sure if it supports direct sampling. If you plan on doing that, though, I'd consider chaining an upconverter.

If I were to choose one with an upconverter, should I worry about it creating spurious harmonics?

The RTL-SDR is a receive-only SDR, so no, you won't be transmitting. If you plan on transmitting as well—after checking which bands you can legally transmit on—you should consider getting another SDR like the HackRF One or something. It can operate between 1 MHz to 6000 MHz. That said, I'm not sure if it's compatible with the RTLSDR-Scanner since I've never used a HackRF One.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7132/using-an-rtl-sdr-as-a-spectrum-analyzer, by user9103, Phil Frost - W8II, Marcus Müller, Amin Shah Gilani. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
