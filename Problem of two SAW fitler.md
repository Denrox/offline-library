# Problem of two SAW fitler?

*Tags: filter · score 3*

## Question

When I series two SAW filter, why the attenuation less than sum both of them in stop band region. Each of them (in stop band) have 60dB attenuation but when series them, the attenuation is equal to 85dB. What happening? Why didn't reach to 120dB?

Then, I put a 20dB attenuation between them ( SG --> SAW1 --> 20dB attenuation --> SAW2--> SA ), and the attenuation is equal to 90dB, this meaning only 5dB attenuate with 20dB attenuation. What happening again?

However, the insertion loss is true when series. Each of the have 8dB insertion loss and when both of them is series the insertion loss equal to 16dB.

Thanks in advanced

## Accepted answer (score 0, by Mahdiehtesham)

First, I measure it by RG316 cable.The test structure following blow:

SG --> RG316 --> SAW1 --> Thru male SMA --> SAW2 --> RG316 --> SA

Signal Generator output power is 0dBm and when applied to SAWs, only 85dB~90dB attenuated. So, change RG316 cable to N Type cable and measure again and achieve to 120 dB attenuation.

It was cable leakage and measurement error.

## Answer (score 4, by Marcus Müller)

So, probably a combination of different things:

- You physically can't isolate things arbitrarily much. My experience with well-designed RF PCBs is that they have -60 dB to -49 dB crosstalk – simply through the board, shields, grounds, power supplies
- You're not telling us how you're measuring isolation. Measuring more than 90 dB in dynamic range is tricky, and requires you think a lot about signal leakage.

I'd mostly chalk this up to measurement error, because if an attenuator doesn't attenuate according to your measurements, then it's probably your measurements.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16636/problem-of-two-saw-fitler, by Mahdiehtesham, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
