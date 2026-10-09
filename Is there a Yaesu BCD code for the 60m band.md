# Is there a Yaesu BCD code for the 60m band?

*Tags: yaesu · score 3*

## Question

I'm thinking of making my own band decoder (arduino or raspberry pi) for my Yaesu and my SunSDR.

Online there are multiple sources with the BCD codes Yaesu uses but nowhere do I see a specific code for the 60m band.

Is there a code for this band? If there is, what is it?

## Accepted answer (score 2, by Neil VK5ZEE)

The bcd code for 60 metres is the same as 40 metres. (03 Hex) 0A is the code for 6 metres. I used a Arduino and monitored the output (HEX on LCD) while winding the radio tuning knob through the whole of the radios frequency range.

Below is a table showing the decoded output for an Australian Model FT-857D If you look at the Begin / End Frequency you can find the Binary / Hex output for the bands. (ie: 60 metres and 40 metres is Bin 0011 or 03 Hex)

```
General Coverage

BeginMhz  EndMhz  BINARY HEX
 0.100   0.499   1101  0D
 0.500   1.499   1110  0E
 1.500   2.499   0001  01
 2.500   4.449   0010  02
 4.500   7.449   0011  03
 7.500  10.449   0100  04
 10.500  14.449   0101  05
 14.500  18.449   0110  06
 18.500  21.499   0111  07
 21.500  25.499   1000  08
 25.500  32.999   1001  09
 33.000  56.000   1010  0A
 76.000 108.000   1011  0B
 118.000 137.000   1011  0B
 137.000 164.000   1011  0B
 420.000 470.000   1100  0C

```

## Answer (score 2, by Glenn W9IQ)

Hex 0A is used for 60 meters on Yaesu radios that natively operate on 60 meters.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9215/is-there-a-yaesu-bcd-code-for-the-60m-band, by ON5MF Jurgen, Neil VK5ZEE, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
