# FM Receiver on GNU Radio with RTL-SDR fails to produce any output sound

*Tags: rtl-sdr, gnuradio · score 4*

## Question

Here is how the FM Receiver I made using the GNU Radio Companion.

(Basically, I was following this tutorial by VYE6Y on youtube.)

## FM Receiver

- Problem: Unfortunately for me, the GNU Radio gives no output. It opens a window as you can show below but no matter what I click or change, there is nothing to be heard. I think, the signal is being processed as the Bandpass spectrum can be seen(as shown in the 2nd image below, which shows the characteristic peak at the center-frequency of the channel).

I am using *GNU Radio Companion 3.7.11.1*, which is fairly new, on Windows 8.1.

*What cannot be a problem:*

1. The RTL-SDR Dongle works. I can run it, for example, without any problems on CubicSDR, where it produces crisp clear sound.
2. Also, I can run a different FM Receiver also made on GNU Radio Companion (though the parameters and scheme of the receiver are different and not quite tuned.)

- Any ideas why there is no sound?

## Accepted answer (score 2, by Duck Dodgers)

Indeed, as I suspected this morning, it was the Multiply Const block. After changing it to accept&work with floats instead of ints, I can hear sound.

Also as Marcus suggested, I changed the Sample Rate for the Audio Sink to 48KHz from 24KHz. But then I noticed that I could only hear every other second. I realized then that the Rational Resampler Interpolation rate nees to be double also from 24 to 48.

Honestly, I don't hear a big difference between 48KHz and 24KHz, but then again, I am not much of an audiophile. :)

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12833/fm-receiver-on-gnu-radio-with-rtl-sdr-fails-to-produce-any-output-sound, by Duck Dodgers. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
