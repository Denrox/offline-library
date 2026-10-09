# Under what circumstances does intermodulation become an issue in a filter after LNA setup?

*Tags: software-defined-radio, amplifier, filter · score 3*

## Question

I'm reading about using software-defined radio for picking up ADS-B signals at 1090MHz. There is this blog which considers (among others) a setup as follows:

```
Antenna -> coax -> low noise amplifier (LNA) -> filter -> software-defined radio dongle

```

After that, it mentions swapping the LNA and the filter with the following note:

At some point a very strong "Blockers" signals will push any LNA into the saturation where IMD products will be created spoiling the reception. To avoid that, the filter should be placed in front the LNA protecting the system from the unwanted signals leaving only the targeted signal. Such a filtered signal is then amplified in the chain. Both the LNA and filter are close to the receiver (indoor).

I found that *"IMD products"* refers to intermodulation, but the blog is not detailed enough to go into the circumstances under which this becomes an issue. Since they mention both options, I assume there is some trade-off going on, possibly based on some of the following factors (these are just factors I can think of, there may be more and these may not be factor after all):


how well out of band signals are filtered out by the filter


how much the LNA amplifies in-band signals


initial signal to noise ratio


signal to noise ratio after the filter

Which of these factors play a role, and what's the theory behind choosing between the one option over the other? I'm aware that one can simply try both and compare the results in any specific setup, but I'm really looking for the theoretical idea behind it.

## Accepted answer (score 3, by MagnusO_O)

I see two main factors about the options in the blog.

- IMD
- Noise figure

Option 4 is just option 2 but for a considerable cable length along with distortions and recommending to put the filter after the cable. Which is a good point for that case.

Option 1 is the basis as the blog discusses the application of a filter.

From there we have:

- a) Amplifier -> Filter

 - Advantage: lower noise figure
 - Disadvantage: IMD **if** there are **very strong** blockers
- b) Filter -> Amplifier

 - Advantage: **very strong** blockers don't impact the amplifier (**if** they are present)
 - Disadvantage: higher noise figure

In receiving environments blockers usually are low power, that means << 0 dBm (except you are located close to a high power transmitter).  
And I would expect most receiver amplifiers 1dB compression point to be >10dBm.

The theory behind the noise figure is The Friis formula for noise factor - Wikipedia, in a nutshell:

- the 1st elements noise figure is the most important one and therefore should be as low as possible
- attenuation, like the insertion loss of a filter, is the same as noise figure

The concern behind considering IMD is most likely third Order Intermodulation - Wikipedia, in a nutshell:

- Intermodulation causes unwanted additional frequencies
- The 3rd order products are more critical than the 2nd order products as they fall close to the intended frequency (e.g $2 * f_1 - f_2$) when they are nearby and therefore can't be filtered as easily as the 2nd order ones (e.g $f_1 + f_2$) .

Concerning your points:


how well out of band signals are filtered out by the filter

 - When saturation is not of concern the filter/amplifier position has no impact on that item.

how much the LNA amplifies in-band signals

 - In the context of the blog I would say no. Because you can drive any single signal into saturation with enough amplification, but that's general and neither related to filter/amplifier positions nor discussed in the blog.

initial signal to noise ratio

 - You can't impact that one, but you can receive lower signals with a lower noise figure in your setup.

signal to noise ratio after the filter

 - Yes, to be able to receive low signals (from further away).

In summary:

- a) Amplifier -> Filter

 - For best reception of low signals (far away sources) due to the better noise figure
- b) Filter -> Amplifier

 - Only **if** there are **very strong** blockers

When in doubt I would go with a) as strong blockers that actually drive a common amplifier into compression are rare and also as the applications (receiver behavior) that are very critical to IMD are not very common.

To note an actual case where IMD could be of concern is for example when you transmit at the same time in a nearby frequency, e.g. in a cellphone call, and the isolation is poor.

## Answer (score 5, by hobbs - KC2G)

Simply put, the LNA amplifies everything that comes into it. If you think about it, it's actually kind of amazing. It's dragging its output value up and down in response to nanosecond-by-nanosecond changes in its input, reproducing signals at *every* frequency up to its bandwidth limit.

A good amplifier is as linear as possible (meaning its output is precisely proportional to its input) but nothing is perfectly linear, and non-linearities result in distortion. For our purposes, distortion means that part of the amplifier's response to an input signal will be on a different frequency from the input signal. Mainly we're interested in harmonic distortion (where output energy is present on multiples of the input frequency) and intermodulation distortion (where two different frequencies combine to make an output frequency that is the sum or difference of the input frequencies, or the sum or difference of multiples of the input frequencies).

Out of all of these distortion products of all of the signals coming into the amplifier, some of them will end up on the same frequency as the signal you're trying to receive. All of that junk constitutes noise, and we say that it's lowered the signal-to-noise ratio, or raised the noise floor.

By filtering out frequencies that you're not interested in before they get to the amplifier, you're denying the amplifier the chance to amplify those signals, which means you're denying it the chance to create those distortion products, which means that most of what the amplifier outputs on your desired frequency will be what it *received* on that frequency, and you will have an improved signal-to-noise ratio.

Note that the filter can't do anything at all about noise that's actually *received by the antenna* at 1090MHz; no amount of magic will remove that. What it's doing is decreasing the amount of noise that's *added to the system* by imperfections in the amplifier. When this noise reduction is greater than the signal reduction, your SNR improves and you get more decoded signals.

## Answer (score 3, by Phil Frost - W8II)

I believe this blog post is trying to show the evolution of a good setup, rather than present a number of equally appropriate setups.

You might want to first read [How can I calculate the effects of an LNA, antenna gain, etc. on noise performance?](How%20can%20I%20calculate%20the%20effects%20of%20an%20LNA%2C%20antenna%20gain%2C%20etc.%20on%20noise%20performance.md)

Assuming the LNA is good enough to justify using, you want to:

1. minimize losses between the LNA and the antenna, and
2. keep the LNA as linear as possible.

Two the first point, this means putting the LNA at the antenna so you don't have the loss from a long coax run between the antenna and the LNA introducing noise.

Usually the filter would then be between the LNA and the antenna. By reducing the power going into the LNA that isn't even in the band you care about, the LNA can operate in a more linear region. Theoretically it's possible with a really terrible filter and a really good LNA that the filter would introduce more noise than it would eliminate distortion, but in practice if you're using filters and amplifiers of comparable quality it's always better to filter first.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15192/under-what-circumstances-does-intermodulation-become-an-issue-in-a-filter-afte, by JJJ, MagnusO_O, hobbs - KC2G, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
