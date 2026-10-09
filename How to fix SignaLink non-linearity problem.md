# How to fix SignaLink non-linearity problem?

*Tags: digital-modes, testing, linearity · score 3*

## Question

I decided to check the linearity of my Yaesu FT-891 signal using an RF sampler and an oscilloscope. To generate two-tone (1550 Hz, 2150 Hz) signal I used Audacity. To connect the transceiver to the PC (MacBook Pro 2018) I used SignaLink.

Surprisingly turned out that the signal is not quite linear:

No matter how I change to output volume this is the best I can get. For a comparison, here is the exact same signal when another (DIY) digital interface is used:

Thus I'm quite sure that the problem is with SignaLink. However I have little idea what exactly is causing it or even where to start from. I wonder whether this is a known problem and maybe someone already described a mod to fix it (I didn't manage to find one). If there is no known solution a little piece of advice on how to debug the issue would be much appreciated.

## Answer (score 2, by pidloop)

It might be the transformers frequency response is not flat. Try replacing them with reputable units that have a published frequency response such as here. See more signalink tweaks here.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15809/how-to-fix-signalink-non-linearity-problem, by Aleksander Alekseev - R2AUK, pidloop. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
