# Any SDR radios that receive FM BCB

*Tags: receiver, software-defined-radio, fm · score 3*

## Question

Are there any software defined receivers capable of receiving Regular FM broadcast band stations and displaying a waterfall of the band from 88 MHz to 107 MHz or a significant portion of that range?

## Answer (score 6, by Kevin Reid AG6YO)

Almost every SDR receiver is capable of receiving the FM broadcast band. The ones which can't are typically SDR transceivers designed for specific HF bands.

The harder part of your requirements is the waterfall of “the band … or a significant portion of that range”. The FM broadcast band is 20 MHz wide, and to display all of it straightforwardly requires delivering that entire bandwidth to the attached computer (I assume you are looking for that type as opposed to a single-box SDR).

When evaluating a receiver, look at the bandwidth (MHz) or sample rate (MSPS), and that tells you approximately how much you will be able to see ay once. (Approximately because there will be band-pass filters which have some rolloff at the edges.)

However, another option if you are not looking to *demodulate* any one station while you are displaying the wide-band waterfall, then you can use software which rapidly steps the receive frequency across the range to construct a composite image. The most well-known tool to do this is *rtl_power*, but I understand that it is a non-real-time tool (I could be wrong); I hear from comments that SDR# can do it real-time.

## Answer (score 2, by Richard Hum)

The HackRF is a relatively inexpensive SDR that is capable of capturing the entire FM broadcast band. It costs around $300 and can sample up to 20MHz of spectrum at a time. It can tune between 1MHz all the way up to 6GHz.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5816/any-sdr-radios-that-receive-fm-bcb, by neilbell, Kevin Reid AG6YO, Richard Hum. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
