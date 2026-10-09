# Modulation details of Digital Mobile Radio (DMR)

*Tags: dmr · score 3*

## Question

I'd like to implement a digital demodulator for Digital Mobile Radio (DMR). Note I'm not concerned about decoding of the audio: I realize that requires a proprietary codec.

What are the details of the DMR modem? I've found statements that it's 4-FSK, but few details beyond that.

## Accepted answer (score 4, by Marcus Müller)

ETSI TS 102 361-1 Clause 10 is pretty explicit on that:

## 10.1.2 RF carrier bandwidth

The radio system operates within a 12,5 kHz RF carrier bandwidth.

…

## 10.2.1 Symbols

The modulation sends 4 800 symbols/s with each symbol conveying 2 bits of information. The maximum deviation, $D$ of the symbol is defined as: $$D = 3 h / 2 T$$ where:

- $h$ is the deviation index defined for the particular modulation, and
- $T$ is the symbol time (1 / 4 800) in s.

## 10.2.2 4FSK generation

This clause describes the characteristics of the constant-envelope modulation, entitled 4FSK.

## 10.2.2.1 Deviation index

The deviation index, h , for 4FSK is defined to be 0,27. This yields a symbol deviation of 1,944 kHz at the symbol centre. The mapping between symbols and bits is given in table 10.3.  
[Table 10.3]

## 10.2.2.2 Square root raised cosine filter

Square Root Raised Cosine Filter is implemented for 4FSK so that part of a Nyquist Raised Cosine is used for the transmit splatter filter and part is used by the receiver to reject noise. The input to the transmit splatter filter consists of a series of impulses, scaled according to clause 10.2.3.1, and separated in time by 208,33 microseconds (1 / 4 800 s). The method of splitting the Nyquist Raised Cosine Filter is to define the splatter filter frequency response of the Square Root Raised Cosine Filter as the square root of the Nyquist Raised Cosine Filter. The group delay of the filter is flat over the pass band for |f| < 2 880 Hz. The magnitude response of the filter is given approximately by the following formula:

Sooooo 4FSK, 1944 Hz max deviation, shaping the data with a RRC *before* hitting the frequency modulator.

Note I'm not concerned about decoding of the audio: I realize that requires a proprietary codec.

He, theoretically that's true. But I know people who have shown past tendencies to reverse engineer AMBE codecs running integrated in handsets on dedicated DSP chips. One of the takeaways was that you've got to be relatively smart to do so properly, but on the other hand, also, that parametrizations of AMBE codecs are different, but you can often at least rudimentarily use one for a different standard and still get an understandable starting point.

Ah, and in fact, Travis Goodspeed KK4VCZ, with support from DD4CR, DF8AV, and AB3TL, has simply made the DMR-specific AMBE codec from a Hytera handset run under Linux. So, yay! You *can* decode AMBE in software on a PC (or PC-style computer), if it is an ARM (and not an x86). Even better: QEMU (a popular computer emulator) can both emulate an ARM processor (so that the firmware of the Hytera handset can be run on something that is not an ARM itself), as well as act as a "proxy" for the native host OS – so, you can run a slightly modified Hytera (STM32 microcontroller-)firmware on any of your Linux PCs. Cooool: PoC||GTFO 0x13, p. 38ff (get all PoC||GTFO volumes from Pastor Manul Laphroig's tombs of enshrined wisdom, eg. https://www.alchemistowl.org/pocorgtfo/).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9009/modulation-details-of-digital-mobile-radio-dmr, by Phil Frost - W8II, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
