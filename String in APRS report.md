# String in APRS report

*Tags: aprs · score 4*

## Question

Here are two messages I received:

```
10:50:53R W2MEB-9>SX2X9U,W0BJ-1*,K0ATT-10*,WIDE2* <UI R Len=34>:`vNN" dk/]"64}Monitoring 144.905=
10:50:58R WB9QPM-4>APBPQ1,AD9OV-8*,WIDE2* <UI Len=47>:!3924.30N/08848.72WI Shelbyville Igate EM59oj

```

What I'm asking about are the 6 characters after the > (the beacon "To" field). I've found that values starting with "A" indicate software version (in this example, APBPQ1 maps to "John G8BPQ Digipeater/IGate" from http://aprs.org/aprs11/tocalls.txt) by I can't find any resource that defines values starting with "S". Is there one somewhere? What does it mean?

## Accepted answer (score 4, by hobbs - KC2G)

You're looking at a Mic-E packet. The Mic-E format uses the TOCALL to encode part of the position data (the entire latitude and two bits of the longitude) and a three-bit "message ID". This allows for very small packets. See Chapter 10, "Mic-E Data Format", of the APRS spec.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17067/string-in-aprs-report, by Duston, hobbs - KC2G. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
