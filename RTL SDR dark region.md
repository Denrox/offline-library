# RTL SDR "dark region"

*Tags: software-defined-radio, hf, rtl-sdr · score 3*

## Question

I'm new to RTL SDR, and I noticed there's a "dark region" (around 700-900MHz), and I haven't figured out why this is.

My device's tuner is a Fitipower FC0012, where could I find the pinout and dataspecs for this tuner?

## Accepted answer (score 5, by Hamsterdave)

700-900MHz is "blocked" by law in the US and a number of other countries due to a (now antiquated) law that was designed to prevent wideband communications receivers from eaves dropping on old analog cellphones, which broadcast in the clear.

These days it's entirely unnecessary, but it's still on the books because regulators are lazy like that.

As for removing the limitation, I couldn't say, not being terribly familiar with the current SDR software offerings. In the case of these RTL-SDR dongles, it seems virtually certain the block is being applied in software, not hardware.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12482/rtl-sdr-dark-region, by Andrew Angelo Barrientos, Hamsterdave. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
