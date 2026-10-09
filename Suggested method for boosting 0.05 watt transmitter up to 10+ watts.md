# Suggested method for boosting 0.05 watt transmitter up to 10+ watts?

*Tags: software-defined-radio, amplifier · score 7*

## Question

Long time ham operator here, new to this particular challenge -

I have a software defined radio transceiver that I'd like to try and use to make contacts on HF, in particular 20-meters. Tuning within the 20-meter band is no problem but the transmitter only puts out about 0.05 watts! Great for the lab but arguably not enough power to make any reasonable contacts.

I'd like to amplify the signal up to at least 10 watts, 50 would be perfect if possible.

Being that I may need two amplifiers I am concerned about noise and keeping the signal clean on the way up to the desired output power.

A typical linear amplifier won't even trigger unless the input power is at least 1-5 watts and so this is why I think I may need a two-step amplifier chain, although I'd like to just have a single amplification stage if possible.

So I'm looking for help coming up with a solution, perhaps specific amplifier(s) that I should use to get to the desired output power, based on your experience.

## Accepted answer (score 5, by Phil Frost - W8II)

There is nothing especially unusual about this situation: a modulator in most radios will output only some very tiny power which then goes through multiple amplification stages. You just don't have all the stages.

Building a little amplifier to take your 50 mW and amplify it enough to drive a typical linear amplifier could be a fun little homebrew project, but if you are looking for a kit, try the TAPR PennyWhistle. It's designed for the HPSDR, which just like your SDR has a very low power output. The PennyWhistle design is also greatly simplified by the lack of any output filtering: the assumption is that it will feed another amplifier stage which will be followed by filtering to remove any harmonic distortion introduced by the amplifier. It has 19 dB (about 80x) of gain, so with your 50 mW drive, will output about 4W, which should be enough to drive another amplifier.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2010/suggested-method-for-boosting-0-05-watt-transmitter-up-to-10-watts, by Brad Hein, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
