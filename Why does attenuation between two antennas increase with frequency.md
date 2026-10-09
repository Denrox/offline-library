# Why does attenuation between two antennas increase with frequency?

*Tags: antenna-theory · score 4*

## Question

While studying for a HAM license exam I ran into a question that I am having trouble with answering. There are two aspects that I cannot explain, given my current admittedly little understanding of the subject.

Given the following statement in the exam text...

The dampingattenuation between two vertical half-wave dipoles is measured at a certain frequency. The antennas are set up in free space. If the frequency is doubled and the dimensions of the half-wave dipoles are adjusted accordingly, the dampingattenuation will increase by 6 dB. *(Translation is my own, original is in Dutch)*

... I have the following questions:

- Why does dampingattenuation *increase* rather than decrease with increasing frequency, with their relative distance of the antennae being (assumed) constant?
- What is the appropriate logic or formula to apply here that explains why there is a 6 dB increase rather than (say) 3 dB?

Should you wish to look at the original dutch wording, it's question 37 in the 6 November 2019 full-license exam. The answer table lists answer A (6 dB increase) as being correct.

## Accepted answer (score 1, by Frank Geerlings)

As explained in the Wikipedia article on Link budget, 'the loss due to propagation between the transmitting and receiving antennas, often called the path loss, can be written in dimensionless form by normalizing the distance to the wavelength:'

$ L_\text{FS}\text{(dB)}=20\log_{10}\left(4\pi{\text{distance}\over\text{wavelength}}\right) $

This equation shows that when you reduce the wavelength by a dB, $L_\text{FS}$ will increase by twice that many dB. So if we halve the wavelength (cut in half = -3 dB) the loss will increase 6 dB.

The comment about the Friis transmission equation set me on the right path to the answer.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16292/why-does-attenuation-between-two-antennas-increase-with-frequency, by Frank Geerlings. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
