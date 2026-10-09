# Why are commercial SDRs so limited in operating frequency?

*Tags: hf, software-defined-radio, transceiver · score 10*

## Question

I spent a bit of time researching SDRs, mostly looking into the possibility of building an all-FPGA-based TRX. There are a lot of commercial ready solutions; some are cheap, some not, but they all tend to be operating from 50/70 MHz frequency range.

I am a complete newbie in RF processing and what escapes me is: if the circuitry is able to process a 50 MHz signal, why can't it do the same with lower frequencies? Is it some physics limitation? I guess it must be — otherwise everyone would advertise an operatiing range from DC to X MHz. Or is operating on lower frequencies uninteresting to everybody except hams?

My question is TRX specific — not RX only.

## Accepted answer (score 5, by Phil Frost - W8II)

Largely it has to do with filtering and bandwidth. An ADC requires an anti-aliasing filter to remove all input frequency components that are more than half the sample rate. Otherwise, these higher frequency components get aliased onto lower harmonics.

As an example, if I have a 40 kHz ADC, it should be able to handle at its input anything from 0 to 20 kHz. If I should feed it 25 kHz, it will appear as 15 kHz...not what you want in a radio. The anti-aliasing filter removes everything above 20 kHz so this does not happen.

If I have that same 40 kHz ADC, but I want to handle radio frequencies above 20 kHz, I need to introduce a mixer. This is a device that shifts one band of frequencies to another. So, if I want to work in the 40 meter band, I need a mixer that converts frequencies around 7 MHz down to 0 - 20 kHz for my ADC. However, my mixer will again require filters to avoid intermodulation and aliasing.

All of this is equally applicable to transmitting -- the process is identical, except in the other direction. However, some stages of the transmitter must handle high power, which makes the filters larger and more costly. This is why it can seem easier to find a receiver with coverage of more bands.

So greatly simplified, the coverage of an SDR, or in fact, any radio, is determined by what filters it includes. As an example, take a look at the SoftRock RX Ensemble, which includes filters for four bands, and by changing the component values, can be built to cover LF or HF. With a sufficient selection of filters it becomes possible to cover the entire RF spectrum, but this would be expensive.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2230/why-are-commercial-sdrs-so-limited-in-operating-frequency, by Ulterior, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
