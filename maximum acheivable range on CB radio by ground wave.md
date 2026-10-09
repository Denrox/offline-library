# maximum acheivable range on CB radio by ground wave?

*Tags: antenna, hf, digital-modes, phased-array · score 5*

## Question

I have 10 watt CB radio system & 0.64 lambda monopole antenna , I think it has a 5 dBi gain .

what is the maximum acheivable range by ground wave in an urban area ?

If I want to increase my range without increase the system’s power , can I make 10 elements antenna array and get another 10 dB gain above my 5 dBi ?

## Answer (score 4, by K7PEH)

First, a "ground wave" is difficult to estimate since it is so dependent on all kinds of things, most importantly frequency and second the conductivity of the ground (or, water). Buildings in an urban area can result in diffraction of the ground wave among buildings that can create strange areas of signal strength and signal weakness that are virtually impossible to predict without actual experiment.

The previous similar question (noted in the comments) is different from this one in frequency. So, I will answer for the US CB frequency (just under 28 MHz). For a 28 MHz signal, with all other features ignored, is about 5 to 7 miles (or, 8 to 11 km).

There is actually three different types of propagation considered as ground wave and they behave quite differently from each other which makes guessing at distance for ground wave to be even more difficult.

1. Tropospheric Bending Ground Wave

This is a ground wave that travels in the atmosphere and ground itself is somewhat independent of the nature of the ground. It is included here because Tropospheric Bending has similar propagation to ground wave. This type of propagation is most notable in VHF and above frequencies so not much use to CB frequencies.

1. Direct Line-of-Sight Ground Wave

This is similar to above in that the ground effects are not pertinent other then the fact that curvature of the surface of the earth limits the effective line-of-sight success. But, this is the most likely type of propagation the OP will see useful in an urban setting for CB (along with benefits of diffraction). For actual distance coverage, line of site computations can be estimated using either of the following approximate formula: $$ D_\text{miles} = 1.415 \sqrt{H_\text{feet}}\\[2ex] D_\text{km}= 4.124\sqrt{H_\text{meters}} $$

Where $H$ is the height of the transmitting (or, receiving) antenna. By including both transmitting and receiving antennas and computing for overlap of the two distance results you can determine the longer line-of-site propagation path available.

1. Low-Frequency Surface Wave

I say *low-frequency* since this type of ground wave, that actually uses the conductivity features of the ground are most effective at lower frequency, or MF (~2 MHz) and under. This is the method used for submarine communications where propagation is measured in the 1000s of miles for the super low frequency. Note that in this case, since frequency is so low, actual information transmission is very slow, measured at only a few characters per second in some cases. Surface wave propagation for super low frequency requires humongous antennas so it is not a practical solution for hobbyists.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2271/maximum-acheivable-range-on-cb-radio-by-ground-wave, by abduoman11, K7PEH. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
