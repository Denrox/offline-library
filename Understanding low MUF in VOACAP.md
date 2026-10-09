# Understanding low MUF in VOACAP

*Tags: hf, propagation, citizens-band · score 3*

## Question

I've started playing with VOACAP to better plan and predict conditions on 27 MHz (CB). To my utter astonishment, VOACAP says that I won't be able to communicate on that frequency, regardless of antenna, desired reliability and length of path (tried very short with high take-off angle, medium and long ones).  
VOACAP simply predicts that MUF will be around 14 MHz in the best of conditions (noon, artificially high SSN, long distance)!  
I do understand that those predictions are statistical and don't mean "propagation conditions RIGHT NOW"; however, MUFDay of 0.00 means zero or very low probability of contact in the given month... and it is simply not true! Every day I get **lots** of transmissions from stations 500-1500 miles away, and I have a small whip antenna now!

*Note that I'm sure I'm using VOACAP correctly because the results in a tutorial on voacap.com are very similar to mine (MUF of around 13 MHz, but they plan to transmit on 40 or 80 band so not an issue and their MUFDay is close to 1.00)*

#### So how should I treat those predictions?..

- Am I missing something obvious, either in using VOACAP or my understanding of propagation?
- Is VOACAP useless for 10m band?
- Maybe I should tweak some parameters?

## Accepted answer (score 2, by AG5CI)

The VOACAP MUF is defined as "the **median** maximum usable frequency for a given ionospheric path, month, SSN and hour".

The median is a statistic representing the value of a random variable for which there is an equal probability of values falling below or exceeding the value.

Another way of stating the VOACAP definition is that there is a 50% chance that a frequency above the MUF will be useable (i.e. a coin toss).

## Answer (score 2)

500-1500mi are *probably* ground-wave propagation distances (or radio "line-of-sight" if you like), especially given the vertically polarized antenna I think you are using. So ionosphere propagation, which is what "MUF" is referring to, *probably* doesn't enter into this situation. 10m might be out of range for any software-based predictor; or at least for *this* software predictor.

The highest frequency at which the ionosphere bends radio waves back to a desired location on Earth is called the maximum usable frequency (MUF).

This doesn't mean you can't use ionospheric propagation for 10m. But you usually have to deliberately try to do so with clever antenna design and placement. And you are probably depending on "sporadic E" propagation and not the F-layer refraction that most people mean when they talk about dependable skips based on the MUF.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18620/understanding-low-muf-in-voacap, by Alexander, AG5CI. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
