# What is the external mic/speaker pinout for the Yaesu FT-4XR / FT-65R / FT-25R / SSM-16B?

*Tags: yaesu, audio-interface · score 3*

## Question

These newer HTs seem to have a different pinout than the older Yaesu HTs. The older HTs used a single 3.5mm TRRS plug - these use a two-plug connector, with a 2.5mm jack and a 3.5mm jack, similar to the [Kenwood/Baofeng style](What%27s%20the%20pinout%20for%20Kenwood%202.5mm%20TRS%203.5%20mm%20TRS%20connector.md), but with the two plugs closer together.

What are the the different contacts on these two plugs, and how would you trigger PTT?

## Answer (score 3, by Olivier F4IHA)

I figured out a way to be able to trigger the PTT properly using a transistor. It requires a high value resistor. I used a potentiometer to find the correct position.

Based on a feedback I had, I recommend this update (adding a resistor between the potentiometer and the transistor) which is ensuring the collector to have always a resistance for the collector.

I fully documented the way I found it on my blog.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/11776/what-is-the-external-mic-speaker-pinout-for-the-yaesu-ft-4xr-ft-65r-ft-25r-ssm, by Evan Krall, Olivier F4IHA. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
