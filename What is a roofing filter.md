# What is a "roofing filter"?

*Tags: receiver, filter, jargon · score 13*

## Question

What are roofing filters? Are there different kinds of things that are called roofing filter? Why would a circuit or component be called a roofing filter instead of just a IF bandpass filter? Why is the word “roofing” used? (as it seems to have nothing to do with keeping the rain out of the chassis.)

## Answer (score 11, by Phil Frost - W8II)

The roofing filter is the filter through which the first IF must pass. The roofing filter is an IF filter, specifically the first one. AB4OJ provides a block diagram:

As for why it's called a "roofing" filter, Elecraft suggests it's about protecting the subsequent stages from spurious signals:

The term "roofing filter" has most often been used in relation to triple- or quadruple-conversion receivers. Such receivers have an IF above the highest RF band covered; it's typically something in the range of 30 to 70 MHz or higher. But "roofing" as a term should be interpreted as "protective," not "high in frequency." A roofing filter protects later stages, including amplifiers, mixers, narrower filters, and DSP subsystems, just as the roof on your house keeps rain out of all of the rooms. But a roofing filter can be equally at home at a low first IF, if that is how the radio is designed. It still provides the same protective function.

Not long ago, it was uncommon to find a high-quality radio that did not have 2 or more IFs. This was largely a consequence of the design constraints imposed by an all-analog design. In this world, a roofing filter would be unambiguous and ubiquitous.

But today, many high quality HF receivers are direct-sampling, so they have no IF at all. Higher frequency receivers are often direct-conversion, so you could say they have one IF of 0 Hz. These designs have been enabled by the recent lower cost and higher performance of digital hardware.

So do these modern radio topologies still have roofing filters? Even a direct-conversion receiver will have *some* filter, is it a roofing filter?

I would say no: any SDR is probably going to have a preselector and an anti-aliasing filter, but that may be the only analog filter it has. Talking about a roofing filter in an SDR is like talking about a carburetor in a fuel-injected car. It simply doesn't exist, although there are other parts (fuel injectors) which serve a similar function.

But reading the Elecraft article and taking a cursory look through some search results from various amateur forums, I get the impression that manufacturers are broadening the definition of "roofing filter" to include just about any analog filter which is near the antenna, simply because a radio which does not boast an "excellent roofing filter" is not as marketable.

## Answer (score 2, by Ryuji AB1WX)

Roofing filter is the first IF filter in the IF chain, right after the first mixer.

Roofing refers to the idea that it prevents the rest of the IF chain (very high gain) from getting saturated or distorted. That means, everything ahead of the roofing filter must have a much much wide dynamic range (and consequently lower gain) than what follows the roofing filter.

The concept and beefy implementation of the roofing filter were to improve the receiver performance in bands crowded with strong stations, such as 40m when broadcast stations existed in the middle of 7.0xx MHz range and more commonly during contests and DXpeditions. In receivers of 20th-century designs, when a strong S9+ station appeared just a few kilohertz off your QSO partner at S2 or S5, you may no longer copy easily or at all. Receivers in 2010 or later designs and used in some of the performance transceivers (such as Elecraft K3, KX3 or Kenwood TS590) are much better, in part due to roofing filters.

Even in DSP rigs, many use IF DSP architecture, where the RF signal is downconverted to a low frequency (a few hundred kHz or lower, sometimes even 0Hz) and then sampled. In that case, the roofing filter may even be an active filter using OPamps (such is the case with KX3 roofing filter module).

In direct sample DSP architecture, the notion of roofing filter no longer applies. The dynamic range (bits) of the A/D converter and the preselector are the key elements determining the immunity from strong signals at nearby frequencies just outside the receiver bandwidth.

In particular, noise blankers and AGC are nonlinear devices in the IF chain, and NB operates on a wideband signal (wider bandwidth than the one required for communication signal) and it is very susceptible to interference from strong signals at nearby frequencies. When AGC malfunctions due to strong nearby signals, the target signal can be suppressed entirely or reverse-modulated by the interfering signal. With sophisticated roofing filter and overall refinement in the receiver architecture, these problems became much alleviated in the post-2010 performance equipment.

Sidenote: leave NB off when you don't need it, especially in older rigs, for better experience.

Roofing filter's bandwidth is usually wider than the communication bandwidth. The ultimate IF bandwidth (such as 2.7kHz for SSB or 50 to 500 Hz for CW) is determined by a narrower filter later in the IF chain. A common misconception among amateurs (e.g., the Facebook KX3 group) is that people often argue that they installed an optional roofing filter, but it did not help reduce QRM. Of course!

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/19932/what-is-a-roofing-filter, by hotpaw2, Phil Frost - W8II, Ryuji AB1WX. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
