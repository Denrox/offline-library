# How do I have a full signal of noise on a handheld?

*Tags: antenna, ht, baofeng, noise · score 5*

## Question

I'm new to ham (although I've had a license for a long time) and I'm having issues with receiving on a basic handheld. I have a cheap BaoFeng UV-82HP and I keep getting full signal noise at random times. I have gotten this on different channels in different locations. When I'm not getting the noise, I get clean and clear transmissions.

**Video Evidence:**  
https://youtu.be/nupqlH3-eQ0

**Power/Ground Troubleshooting:**  
The unit is a battery operated handheld, so I don't have to worry about power input.

**Antenna Troubleshooting:**  
I have tried three different antennas including a rubber duck and they all have the same issue. I assume the rubber duck doesn't need grounding as it is very small and not really ground-able.

I assume that means that means the noise is a defect in the radio?

## Accepted answer (score 3, by Phil Frost - W8II)

That's not noise, it's digital voice. DMR, DSTAR, and P25 are digital modes that find popular use on the amateur bands.

Some repeaters are digital-only. Others are dual-mode, so you will encounter a mix of digital and analog FM, depending on what the other station is transmitting. If you can find information on the repeater, you will probably discover what modes it supports.

On a cursory look, it does not appear the UV-82HP supports any digital modes, so unfortunately you won't be able to participate without a different radio or some software.

Related: How to scan while avoiding digital/noise frequencies?

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/11977/how-do-i-have-a-full-signal-of-noise-on-a-handheld, by Eric Fossum, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
