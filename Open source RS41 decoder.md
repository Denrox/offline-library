# Open source RS41 decoder

*Tags: digital-modes, software, signal-identification, weather · score 4*

## Question

I would like to decode the signal from a RS41 radiosonde (from a weather balloon), which are suggested open-source software to do that?

I tried RS but after compiling the code and executing sox wav/20140717_402MHz.wav -t wav - lowpass 2800 2>/dev/null | ./rs41 --crc -vx it only returns

```
sample_rate: 48000
bits       : 8
channels   : 1
samples/bit: 10.00

```

without any actual decoding of the wav recording.

Sorry if this is a stupid question, but I'm new in the "radio-world" and the documentation I found online was quite limited or outdated, thanks.

EDIT:

I came across my own question 4 years later, and with further investigation, I found out that I had probably used the wrong receiver configuration in GQRX. Now, I have successfully decoded the signal using the following options:

- Filter width -> Wide
- Filter shape -> Soft
- Mode -> Narrow FM
- AGC -> Medium
- Noise blanker -> NB1

## Accepted answer (score 3, by cygeus)

You have to provide the -i option to invert the signal in order to decode it properly. The lowpass filter is not really required as this is a quite strong signal (but does not harm either).

```
$ ./rs41ptu -i --crc -vx wav/20140717_402MHz.wav
sample_rate: 48000
bits       : 8
channels   : 1
samples/bit: 10.00
[ 5047] (K1930308) Do 2014-07-17 12:32:13.999  lat: 45.66939  lon: 15.87963  alt: 28527.17   vH:  9.8  D: 251.8  vV: 6.1  # [00000]
[ 5048] (K1930308) Do 2014-07-17 12:32:14.999  lat: 45.66937  lon: 15.87951  alt: 28533.45   vH:  8.4  D: 259.7  vV: 6.3  # [00000]
[ 5049] (K1930308) Do 2014-07-17 12:32:15.999  lat: 45.66936  lon: 15.87939  alt: 28541.13   vH: 10.6  D: 270.8  vV: 8.7  # [00000]
[ 5050] (K1930308) Do 2014-07-17 12:32:16.999  lat: 45.66936  lon: 15.87924  alt: 28549.00   vH: 13.8  D: 273.0  vV: 6.5  # [00000]: fq 402000
[ 5051] (K1930308) Do 2014-07-17 12:32:17.999  lat: 45.66937  lon: 15.87905  alt: 28554.51   vH: 16.3  D: 270.9  vV: 4.6  # [00000]: fw 0x4e25
[ 5052] (K1930308) Do 2014-07-17 12:32:18.999  lat: 45.66937  lon: 15.87883  alt: 28560.22   vH: 17.6  D: 267.7  vV: 6.8  # [00000]: BK 01
[ 5053] (K1930308) Do 2014-07-17 12:32:19.999  lat: 45.66935  lon: 15.87862  alt: 28567.80   vH: 15.7  D: 262.6  vV: 8.7  # [00000]
[ 5054] (K1930308) Do 2014-07-17 12:32:20.999  lat: 45.66933  lon: 15.87843  alt: 28574.92   vH: 14.1  D: 258.0  vV: 5.4  # [00000]
<SNIP, output abbreviated>

```

```
$ sox wav/20140717_402MHz.wav -t wav - lowpass 2800 2>/dev/null | ./rs41ptu -i --crc -vx
sample_rate: 48000
bits       : 8
channels   : 1
samples/bit: 10.00
[ 5047] (K1930308) Do 2014-07-17 12:32:13.999  lat: 45.66939  lon: 15.87963  alt: 28527.17   vH:  9.8  D: 251.8  vV: 6.1  # [00000]
[ 5048] (K1930308) Do 2014-07-17 12:32:14.999  lat: 45.66937  lon: 15.87951  alt: 28533.45   vH:  8.4  D: 259.7  vV: 6.3  # [00000]
[ 5049] (K1930308) Do 2014-07-17 12:32:15.999  lat: 45.66936  lon: 15.87939  alt: 28541.13   vH: 10.6  D: 270.8  vV: 8.7  # [00000]
[ 5050] (K1930308) Do 2014-07-17 12:32:16.999  lat: 45.66936  lon: 15.87924  alt: 28549.00   vH: 13.8  D: 273.0  vV: 6.5  # [00000]: fq 402000
[ 5051] (K1930308) Do 2014-07-17 12:32:17.999  lat: 45.66937  lon: 15.87905  alt: 28554.51   vH: 16.3  D: 270.9  vV: 4.6  # [00000]: fw 0x4e25
[ 5052] (K1930308) Do 2014-07-17 12:32:18.999  lat: 45.66937  lon: 15.87883  alt: 28560.22   vH: 17.6  D: 267.7  vV: 6.8  # [00000]: BK 01
[ 5053] (K1930308) Do 2014-07-17 12:32:19.999  lat: 45.66935  lon: 15.87862  alt: 28567.80   vH: 15.7  D: 262.6  vV: 8.7  # [00000]
[ 5054] (K1930308) Do 2014-07-17 12:32:20.999  lat: 45.66933  lon: 15.87843  alt: 28574.92   vH: 14.1  D: 258.0  vV: 5.4  # [00000]
<SNIP, output abbreviated>

```

Note: I assume your rs41 executable is compiled from rs41.c The documentation lists rs41.c as an old version (source code was last updated 4 years ago). The latest implementation is in rs41ptu.c I did not do a detailed analysis of the source code, but based on this output from this one sample there do seem to be some (small) differences in the decoded values:

```
$ ./rs41 -i --crc -vx wav/20140717_402MHz.wav
sample_rate: 48000
bits       : 8
channels   : 1
samples/bit: 10.00
[ 5047] (K1930308) Do 2014-07-17 12:32:13.999  lat: 45.66939  lon: 15.87963  alt: 28527.17   vH:  9.8  D: 251.8°  vV: 6.1
[ 5048] (K1930308) Do 2014-07-17 12:32:14.999  lat: 45.66937  lon: 15.87951  alt: 28533.45   vH:  8.4  D: 259.7°  vV: 6.3
[ 5049] (K1930308) Do 2014-07-17 12:32:15.999  lat: 45.66936  lon: 15.87939  alt: 28541.13   vH: 10.6  D: 270.8°  vV: 8.7
[ 5050] (K1930308) Do 2014-07-17 12:32:16.999  lat: 45.66936  lon: 15.87924  alt: 28549.00   vH: 13.8  D: 273.0°  vV: 6.5 : fq 402000
[ 5051] (K1930308) Do 2014-07-17 12:32:17.999  lat: 45.66937  lon: 15.87905  alt: 28554.51   vH: 16.3  D: 270.9°  vV: 4.6
[ 5052] (K1930308) Do 2014-07-17 12:32:18.999  lat: 45.66937  lon: 15.87883  alt: 28560.22   vH: 17.6  D: 267.7°  vV: 6.8 : BK 01
[ 5053] (K1930308) Do 2014-07-17 12:32:19.999  lat: 45.66935  lon: 15.87862  alt: 28567.80   vH: 15.7  D: 262.6°  vV: 8.7
[ 5054] (K1930308) Do 2014-07-17 12:32:20.999  lat: 45.66933  lon: 15.87843  alt: 28574.92   vH: 14.1  D: 258.0°  vV: 5.4
<SNIP, output abbreviated>

```

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17729/open-source-rs41-decoder, by Paa, cygeus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
