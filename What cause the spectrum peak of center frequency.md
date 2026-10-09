# What cause the spectrum peak of `center frequency`?

*Tags: gnuradio, frequency, usrp, spectrum-analyzer, fosphor · score 7*

## Question

I use gnuradio and fosphor to view the spectrum from USRP B210, default gain set to **34**, output looks like concave as below:  
Nothing changed just set gain to **35**, output become flat, looks like convex:  
Whatever center frequency I set,0 frequency always has a peak.Why?

## Accepted answer (score 5, by Thomas)

Internal interference in the radio. There's a clock ticking at that frequency in order to downmix the signal, and spurious emissions from that clock is being picked up by other circuitry.

The clock is at the center frequency because it's being converted from your center frequency to a lower one. You get a spectrum around 100MHz from your SDR by this clock being set to 100MHz and mixed in with the signal the antenna picked up. This translates 101MHz to 1MHz, and 100MHz to 0Hz. Which means yeah you're actually receiving the clock you configured.

In other words the clock needed to receive is acting like a transmitter, because hardware is not perfect.

It's very common to set the radio's center frequency outside of your desired signal location, and then do a frequency translating FFT filter (it's a gnuradio block) as your first stage, to combine "retuning" (frequency translating, to avoid this "DC bump"), filtering (to just the signal bandwidth), and downsampling (to reduce CPU use for downstream blocks).

SDRs, especially higher end ones like the USRP B210, try to remove as much as possible of this DC (DC because it's at 0Hz of the final output) interference, using hardware and in-radio processing. But it's not perfect, and will leak out under certain settings.

Even if I didn't actually see the DC bump, I'd not trust 0Hz as much as I'd trust a few kHz off of 0Hz, so I recommend always tuning off frequency.

## Answer (score 7, by hotpaw2)

In addition to the clock leakage mentioned in the other answer, a DC offset spike can also show up in the downmixed IQ if the mixer(s) and/or the ADC(s) aren’t perfectly balanced (exactly equal gains and steps for both positive and negative voltage signal swings over the full range).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20099/what-cause-the-spectrum-peak-of-center-frequency, by kittygirl, Thomas, hotpaw2. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
