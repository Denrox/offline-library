# Help on identifying signal type and extract audio from a signal

*Tags: signal-identification, audio · score 3*

## Question

I Just recorded a signal using SDR++ and RTL-SDR.

I can recognize even without any demodulation so I think it should be an AM modulation but AM demodulation doesn't give me a clear audio.

I also tried NFM and got the same results (unclear audio)

Can anyone help me and give me some hints on identify this signal modulation?

## Accepted answer (score 6, by hobbs - KC2G)

It's narrow FM with a "voice scrambler". Before getting passed to the FM modulator the voice signal has its frequency components "inverted", in this case by being subtracted from a frequency of about 3,330 Hz. Some radios (not amateur ones, but then again this isn't the amateur band) use this as a sort of basic privacy feature, but it doesn't do much.

You can get clear voice by passing the output of the FM demodulator to the input of an lower sideband demodulator with a carrier frequency of 3330 Hz and a passband of 300 - 3000 Hz (give or take). This may or may not be directly possible with SDR#. I was able to do it with gqrx by running two copies of the app — one using the IQ file source and outputting to a PulseAudio "null sink", and the second one using the SoapySDR Audio source connected to the output of the first one.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20915/help-on-identifying-signal-type-and-extract-audio-from-a-signal, by Ariyan, hobbs - KC2G. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
