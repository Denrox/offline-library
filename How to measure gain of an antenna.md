# How to measure gain of an antenna?

*Tags: antenna, yagi, antenna-analyzer, spectrum-analyzer · score 6*

## Question

I have dual stacked crossed yagi antenna. How can I practically measure the gain of the antenna combination? I know that this can be done in an anechoic chamber. But this is not feasible for me (transportation and cost). Please guide me.

The antenna is designed to work in the 430-440 MHz band. I have a spectrum analyzer and network analyzer with me. If I wish to maintain a weekly of of the antenna gain, what can I do? Also while testing how much does the position of reference antenna matter? For testing at the same position, won't the yagi antenna cause interference in power received by reference antenna?

## Answer (score 3, by Phil Frost - W8II)

Measuring received power is pretty straightforward. Set up a receiving antenna some distance away. Make it at least 10 wavelengths, but even farther is better. Make sure the receive antenna has the same polarization. Transmit a carrier at a fixed power. Read the received power at the receive antenna with your spectrum analyzer.

If it's more convenient, you can also run this test in the other direction, transmitting with some other antenna, and receiving with the Yagi. Due to reciprocity, the results you obtain will be identical.

This doesn't tell you gain unless your spectrum analyzer is calibrated and you know the gain of your receiving antenna. Without the tightly controlled conditions of an anechoic chamber you probably can't know the receiving antenna's gain.

However, what you can do is perform the same test again and compare the results. If you are testing modifications to the Yagi you can compare the received power before and after the modification and quantity the change. You can also replace the Yagi with a reference antenna like a dipole for comparison.

If you receive twice the power with your Yagi versus the reference dipole, then you know the Yagi has 3 dB more gain than the dipole. While this isn't exactly a carefully calibrated, quantitative measurement of antenna gain, it is an objective way to validate that you have indeed constructed an effective antenna, that your Yagi is better than a $1 dipole, or that some modification or adjustment you've made to the Yagi has made a measurable improvement.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/3704/how-to-measure-gain-of-an-antenna, by Vaibhav Rekhate, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
