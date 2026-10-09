# What is dBm and why is it used rather than watts?

*Tags: rf-power, jargon, equipment-design, amplifier · score 16*

## Question

Reading through an RF power amplifier datasheet, I found the sheet only referenced dBm output power, rather than watts.

- What is dBm?
- How do I convert it to watts?
- Why, or when, would you use dBm to specify power output rather than watts?
- Are there specific problems or equations that are easier to deal with in dBm vs watts?

## Answer (score 18, by Kevin Reid AG6YO)

What is dBm?

dBm stands for *decibels* relative to *one milliwatt*. Decibels represent multiplicative factors, or ratios; by establishing a specific reference level they can instead be used as absolute values: 0 dBm is 1 milliwatt, 3 dBm is approximately 2 milliwatts, etc.

How do I convert it to watts?

Convert the decibel value to a scale factor and multiply by one milliwatt. That is,

$$x_{\mathrm{mW}} = 10^{x_{\mathrm{dBm}}/10} \cdot 1 \,\mathrm{mW}$$

$$x_{\mathrm{W}} = 10^{x_{\mathrm{dBm}}/10} \cdot 0.001 \,\mathrm{W}$$

For example, the datasheet you link mentions a value of

$$17 \,\mathrm{dBm} = 10^{17/10} \,\mathrm{mW} \approx 50.1 \,\mathrm{mW}$$

Why, or when, would you use dBm to specify power output rather than watts? Are there specific problems or equations that are easier to deal with in dBm vs watts?

Gain and loss in all stages of an RF system (feed line, filters, amplifiers) **is multiplicative** (if it were not, that would be nonlinearity), and therefore is typically written in dB so that the total gain or loss may be computed by adding, rather than multiplying, all the individual values together.

If you add a value in dB to a value in dBm, the result is in dBm. (Adding two dBm values is not usually meaningful since it would correspond to power squared.)

## Answer (score 9, by Phil Frost - W8II)

Are there specific problems or equations that are easier to deal with in dBm vs watts?

Decibel units, dBm being an example of such, provide a more intuitive measure of some property that responds logarithmically, like power frequently does.

Consider, if you are transmitting now with 1W, and you add 1W more, you have *doubled* your transmit power. That's a *big* difference.

If you are transmitting with 100W, and you add 1W more, your transmit power is 101W. This is only 1% more power: hardly a relevant change.

Decibels account for this. From 1W to 2W is a +3dB change. From 100W to 101W is a +0.043dB change. If you were to increase +3dB from 100W, the result would be 200W, which is the same degree of improvement as 1W to 2W is.

## Answer (score 5, by San Roy)

Power dB = 10 log10 (ratio)

Power in dBm helps in quickly calculating the power at Rx end. Say a launch power of +13 dBm (=10^(1.3) mW = 20 mW) - with link loss of 6 dB - would give 13-6 = 7 dBm at the Rx end. We can verify.

6dB = 10^(.6) = 4.

-6dB = 1/4.

So output power = 20 mW * 1/4 = 5 mW.

10*log10 (5) = 7 dBm.

So, it checks out.

As suggested when launch power is in dBm - one can just subtract the losses in dB to get the dBm power received at the Rx end.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1440/what-is-dbm-and-why-is-it-used-rather-than-watts, by Adam Davis, Kevin Reid AG6YO, Phil Frost - W8II, San Roy. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
