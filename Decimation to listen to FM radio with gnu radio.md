# Decimation to listen to FM radio with gnu radio

*Tags: software-defined-radio, gnuradio · score 7*

## Question

I am trying to listen to FM station using an SDR and GNU radio. I have followed this procedure

Is there a reason that the decimation is done gradually? For example would it make a difference if I change audio decimation to 1 in WBFM Receive and change the decimation to 50 in rational resampler block?

## Accepted answer (score 5, by Phil Frost - W8II)

One reason in general to perform decimation in multiple steps is it reduces the computational requirements of the low-pass filtering. To achieve a sharp transition width in the filter requires a longer convolution kernel and thus, more computation. Also the sample rate is very high before decimation, requiring yet more computational power.

So generally, we want the sample rate to be as low as possible at each stage. The minimum sample rate will be dictated by the Nyquist Theorem.

What we can do instead is use a less sharp filter, then decimate, then another less sharp filter, then decimate again, and so on. There's a further advantage here in that the tails of the filter can extend beyond the output bandwidth such that they alias or "wrap around", since further filtering and decimation steps will remove that aliasing. The filter just needs to be narrow enough to avoid aliasing into what will eventually be the passband.

Thus by filtering and decimating in multiple stages we can use fast filters where the sample rate is high, and put the more expensive filters with the sharper transition where the sample rate is low.

In this particular case, the aim was to get from a sample rate of 20M to 480k. That's a ratio of:

$$ 20000000 / 480000 \approx 41.666 $$

We can't decimate by fractional samples, so we must write that as a ratio of integers:

$$ {20000000 \over 480000} = {500 \over 12} $$

GNU Radio's low-pass filter block can perform decimation but not interpolation, so we can refactor that fraction as:

$$ {20000000 \over 480000} = {100 \over 1} \cdot {5 \over 12} $$

Since 5 is prime, that 5/12 fraction can't be refactored any more. We usually don't want to interpolate any more than we need to since that just creates more data that must be processed, so this is the cheapest way to do it. And you'll notice these numbers (100, 5, 12) match the parameters in your blocks.

The FM demodulator further decimates its audio output after demodulation by a factor of 10 to get 48kHz since this is a common audio rate, and covers the entire range of human hearing.

would it make a difference if I change audio decimation to 1 in WBFM Receive and change the decimation to 50 in rational resampler block?

This would reduce the sample rate into the WBFM demodulator to 48k. On the plus side, it will require less computational power with the lower sample rate.

However, the passband of the low-pass filter upstream is 75k, with a transition of 25k. That means the signal coming out of that filter has a bandwidth of:

$$ 2(75 + 25) = 200\:\mathrm{kHz} $$

Thus, it can't be represented with a sample rate less that 200k. If you were to decimate this to 48k the excess bandwidth would cause aliasing, and you'd be feeding the demodulator garbage.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6506/decimation-to-listen-to-fm-radio-with-gnu-radio, by Jack, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
