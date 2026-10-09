# Conversion from Baud to Bits per Second and then to Bytes per Second

*Tags: math · score 4*

## Question

How would I go about converting from Baud to Bits per Second (bps) and then from Bits per Second to Bytes per Second (Bps)?

## Accepted answer (score 13, by Kevin Reid AG6YO)

*Baud* is another name for *symbols per second* (a unit of *symbol rate*), so you can't convert between it and the others (which are units of *bit rate*) without knowing *how many symbols are in use*.

A *symbol* is the smallest unit of a digital modulation. For example, suppose we're doing on-off keying (also known as CW): the signal can be either present or absent, so there are two symbols. If we were to also use two intermediate amplitudes between "off" and "full power", that would make a total of four symbols. (Digital modulations in amateur radio use frequency-shift keying (e.g. RTTY, JT65/JT9) but this is easier to picture to start with.)

(Using more than two symbols allows you to encode more bits per symbol, which allows for more efficient use of bandwidth for a given data rate.)

For the conversion, suppose there are $M$ symbols. Then each symbol can be used to encode $\log_2 M$ bits. Inversely, for a whole number of bits $N$, then you need $2^N$ different symbols to encode all those bits in one symbol. Thus the conversion between baud and bits per second is:

$$ 1\,\mathrm{baud} = N\,\mathrm{b/s} \\ \text{ or } \\ 1\,\mathrm{baud} = \log_2M\,\mathrm{b/s} $$

The conversion between bits per second and bytes per second is, in practice, much simpler: there are 8 bits ($\mathrm{b}$) in a byte ($\mathrm{B}$).

$$ 1\,\mathrm{B/s} = 8\,\mathrm{b/s} $$

Historically, the word “byte” was used to refer not to exactly 8 bits, but to the smallest addressable unit of memory in computers, or the size of one character. This is not different in practice, because 8 bits per byte is now essentially universal practice.

If one wants to be entirely unambiguous, the word "octet" refers to a unit of eight bits only. In some countries this is commonly used, giving abbreviations for data sizes like “Mo” instead of “MB”.

As an example, let's combine the above two facts:


A data rate of 2 kilobytes per second is equal to 16 kilobits per second.


If we were to send this data using only two symbols, the symbol rate would be equal to the bit rate: 16 kilobaud.


If we were to send this data using 256-QAM, a modulation which has 256 distinct symbols (used for digital TV, for example), then each symbol encodes $\log_2{256} = 8$ bits, or one byte, meaning that the symbol rate is 2 kilobaud.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/3610/conversion-from-baud-to-bits-per-second-and-then-to-bytes-per-second, by W8AWT, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
