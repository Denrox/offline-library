# Problem with sample rate

*Tags: rtl-sdr, software, dsp, software-development · score 4*

## Question

So I am working on a project that involves me to check real time difference between samples.I am fairly new to this so after a bit of researching I wrote a simple python script for it, here is the script. Here is the script: import time

```
from rtlsdr import RtlSdr
sdr = RtlSdr()
sdr.sample_rate = 2e6    # sampling rate
sdr.center_freq = 413e6
sdr.gain = 36
sdr.freq_correction = 60
while(1):

```
s = time.perf_counter()
y = sdr.read_samples(512)
print('seconds elapsed:',time.perf_counter() - s)
time.sleep(0.5)
```

sdr.close()

```

Now this is the output I get:

```
seconds elapsed: 0.00020965299336239696
seconds elapsed: 0.00024505300098098814
seconds elapsed: 0.00026376899768365547
seconds elapsed: 0.000233347003813833
seconds elapsed: 0.00021806899894727394
seconds elapsed: 0.00022980299399932846
seconds elapsed: 0.0002400680023129098
seconds elapsed: 0.0002324250017409213
seconds elapsed: 0.00022879400057718158
seconds elapsed: 0.00018380500114290044
seconds elapsed: 0.00022288499894784763
seconds elapsed: 0.000273057994490955
seconds elapsed: 0.00028443100018193945
seconds elapsed: 0.00027377300284570083
seconds elapsed: 0.00026877300115302205
seconds elapsed: 0.00023158000112744048
seconds elapsed: 0.00024587199732195586
seconds elapsed: 0.00022548100241692737
seconds elapsed: 0.0002632289979374036
seconds elapsed: 0.0002523060029488988
seconds elapsed: 0.00026537499797996134

```

As can be seen it is a fairly random output, ideally the time difference should be constant I suppose, what exactly am I doing wrong? I am using a rtlsdr blog v3

## Answer (score 4, by tomnexus)

512 samples should take 256 microseconds, so your times look about right.

The exact time it takes to execute those lines of code will depend on the rest of what your computer is busy with. And it's unlikely that the elapsed time counter will be accurate to better than 10 us anyway (but I may be wrong, try it yourself by timing a delay loop).

Whats slightly concerning is that the average seems to be less than 256 us. Perhaps it's reading off a buffer, perhaps it will average up a bit later on.

To get the accuate (relative) time of a particular sample, take the sample number and divide by the sampling rate :) Absolute time is more complicated, because of all of the buffers and devices between the ADC and your python code, USB for example will delay the samples by hundreds of microseconds. If you want to know the absolute time of a sample, you need to inject a time marker signal into the front of the receiver, and find its position in the samples later.

What else are you expecting?

## Answer (score 4, by hotpaw2)

The RTL-SDR interfaces to your computer via USB. The USB interface and driver will buffer the data and send it to your software at the requested sample rate on average (baring underflow due to software glitches), but with varying timing due to interface jitter. The RTL2832U USB is likely sending larger chunks of data over USB in blocks of far more than 512 samples at a time, and the driver is chopping up these large chunks at slightly random times. So the per 512 sample time stamps are irrelevant except to indicate if you are losing data long term. Use the sample count divided by the sample rate instead.

Even the time stamps will have OS latency jitter.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18169/problem-with-sample-rate, by RasenRhino, tomnexus, hotpaw2. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
