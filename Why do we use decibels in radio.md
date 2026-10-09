# Why do we use decibels in radio?

*Tags: theory · score 10*

## Question

We can measure power in watts, and gain or loss in unitless ratios. So why bother using decibels for these things?

## Accepted answer (score 17, by Phil Frost - W8II)

We use decibels because they are the most intuitive representation when our primary concern is signal quality. Signal quality changes not in proportion to the power added (in watts), but rather to the percentage change. Decibels put "percentage change" on a linear scale which is easy and intuitive.

I can't show you with a radio here, but I can show you with a visual analogy. Your monitor is emitting visible electromagnetic energy. Your eye receives this power just like a radio.

I'm going to "transmit" an image, with some added noise. The noise power remains constant, but I'll vary the transmit power. After "receiving" the image, I'll normalize the contrast of the image to make use of all the pixel values between black and white. This is analogous to what Automatic Gain Control (AGC) does in a radio. Your job is to decode the image.

Here it is at my maximum transmit power, which we will say is 100 watts, or equivalently 50 dBm.

The noise is detectable but the image is still quite clear.

Now I turn my power way down to 30dBm or 1 watt:

I'm totally buried in the noise.

Now let's explore between these two extremes. I'll show a sequence of 100 images, starting and ending at these extremes. The steps between are each an equal increase in either watts or dBm.

Watts first. I'll go from 1 watt to 100 watts, so each step increases power by about 1 watt.

Notice how the image emerges from the noise almost immediately. About 1 second in you can already see individual jelly beans. By the 2nd half there's no noticeable improvement in quality, even though the power is still increasing by 1 watt each frame.

Now in dBm. I'll go from 30 to 50dBm, so each step is about 0.2dB.

This time the image goes through stages of "I think there could be something in there", "I can read 'IPI'", and "Hey, those are jelly beans!" The noise continues to improve up to the end.

By taking the logarithm of power we change watts to dBm, and so "percentage change", the real determinant in signal quality, becomes a more intuitive linear unit. I'll demonstrate with a dilemma: would you rather:

1. Have 64x antenna gain, while increasing your power from 1 to 2W, or
2. Have 8x antenna gain, while increasing your power from 1 to 100W?

The dilemma is easier in decibels:

1. Have a 18dB antenna gain, while increasing your power 3dB, or
2. Have a 9dB antenna gain, while increasing your power 20dB?

It's easy to see 18+3=21 is less than 9+20=29, so option 2 is the better choice. And it's easy to quantify how much better: 29-21=8dB. With experience you'll learn [what a difference 10dB will make](How%20big%20is%20a%20decibel.md), and you can know that 8dB is just a bit less than that.

*This is a 10dB improvement*

*This is an 8dB improvement*

Power in watts still has some utility. Heat generated and electrical costs are linearly proportional to watts. And it's more convenient to calculate voltages and currents with power in watts. But at the transmitter's output our primary concern ceases to be electrical engineering and becomes signal quality, and decibel units make more sense.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6672/why-do-we-use-decibels-in-radio, by Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
