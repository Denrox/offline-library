# What makes JT65 preferable for VHF, and JT9 for HF

*Tags: hf, digital-modes, vhf, jt65 · score 3*

## Question

Are the bands really that different in characteristics where JT65 works better for VHF, and JT9 for HF? The claim comes from the WSJT website:

JT65 was designed for EME (“moonbounce”) on the VHF/UHF bands and has also proved very effective for worldwide QRP communication at HF; in contrast, JT9 is optimized for HF and lower frequencies.

## Accepted answer (score 1, by user)

According to Wikipedia, JT65 uses 65-tone MFSK (Multiple Frequency-Shift Keying), whereas JT9 uses 9-tone FSK (Frequency-Shift Keying); probably hence the numerals in the respective names.

By only ever transmitting exactly one out of a set of fewer tones, it would appear intuitively that JT9 would be better suited to the variable signal strength commonly found in ionospheric propagation; there are fewer possibilities, and on the receiver side you only need to identify the *one* tone that is currently being transmitted. Similar to [how CTCSS tones can make it through noise so well](How%20do%20PL%20tones%20make%20it%20through%20so%20much%20noise.md).

On the other hand, JT65 probably achieves a higher data transmission rate but would seem to put higher requirements on the *stability* of the received signal strength, as one would see on VHF and up where the major propagation mode is line of sight (with a reflector thrown in for good measure in e.g. the case of EME).

So it would appear not to be so much JT65 being preferred for VHF, as JT65 being better suited for line of sight links and JT9 being optimized for ionospheric propagation links. In the vast majority of cases, this simplifies to a rule of thumb of "use JT65 for VHF and up, and JT9 on HF".

## Answer (score 4, by hobbs - KC2G)

Both modes are FSK, and both have the same effective data rate (72 data bits in about 50 seconds), but there is one very big difference between them: bandwidth. JT9 is 20Hz wide. JT65A (the mode commonly used in HF) is 180Hz wide, JT65B (often used for 2m EME) is 360Hz wide, and JT65C (often used for 33cm and up) is 720Hz wide. Why does this matter and how does it relate to which one you would use on which band?

The first reason is noise. The power of the natural noise we receive is proportional to the width of our passband in Hz. If we can make a signal narrower, and the receiver filter narrower, while keeping the same signal power, the amount of noise goes down proportionally and the SNR goes up proportionally. This is basically free sensitivity!

The second reason is stability. Given the first argument, you might think that JT9 is always going to be the best choice for a low-data-rate, high-sensitivity mode. But to receive a message using an FSK mode where the tones are only separated by 1.75Hz, the transmitter and the receiver had both better be stable to better than 1Hz. Even on HF, not everyone is that good. As the frequency goes up, it becomes borderline impossible. JT65A has a tone spacing of 2.7Hz, JT65B 5.4Hz, and JT65C 10.8Hz. That makes them approximately 1.5x, 3x, and 6x as forgiving to drift as JT9.

So for MF and HF, where you want to be heard over the QRN and frequency stability isn't a big problem, JT9 works great. For higher frequencies, where the natural noise generally becomes less and less, and frequency stability becomes more and more of a challenge, JT65 is more suitable.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1748/what-makes-jt65-preferable-for-vhf-and-jt9-for-hf, by PearsonArtPhoto, user, hobbs - KC2G. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
