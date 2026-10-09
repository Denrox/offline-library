# How big is a decibel?

*Tags: snr · score 5*

## Question

Say I've calculated that my feedline losses are 3dB, or I'm considering an antenna with 10dB gain, or trying to decide between a transmitter with 10dBm output power versus 16dBm (6dB difference).

I understand [a decibel is a degree of change in signal quality](Why%20do%20we%20use%20decibels%20in%20radio.md), similar to a degree of temperature. But how much change? For example, if I increase my antenna gain by 3dB, how much better will that make my signal?

## Accepted answer (score 4, by Phil Frost - W8II)

Here are some visual examples, corresponding to what you'd see receiving an analog TV transmission. I've picked an image with features of varying detail. Look for:

- the letters "IPI"
- individual jelly beans
- contrast between the beans, especially the darker ones that are very close in brightness
- reflections on the beans

Here are sets of three images side-by-side, each adjacent image some number of decibels apart in signal to noise ratio. Our eyes are good at picking out fine detail in noise, about as good as a well-designed digital mode. So this should give you an intuitive sense of the difference a decibel makes for digital modes, and also slow-scan TV.

Audio samples are past the images, if SSB is more your concern.

1dB:

1dB:

3dB:

3dB:

10dB:

10dB:

Ears don't work like eyes, so I've also generated some audio samples such as you'd hear for SSB. Again they are normalized to a constant volume like AGC would do. The numbers refer to the noise power, so -48 dB is the highest quality (lowest noise power), and -06 dB is the worst quality (highest noise power)

-06 dB  
-12 dB  
-18 dB  
-24 dB  
-30 dB  
-36 dB  
-42 dB  
-48 dB

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6676/how-big-is-a-decibel, by Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
