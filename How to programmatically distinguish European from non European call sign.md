# How to programmatically distinguish European from non European call sign?

*Tags: callsign, logging · score 5*

## Question

Any ham radio log processing app developers?

I am creating web application to manage our club award and I need to programmatically distinguish European from non European stations by call sign.

I cannot find viable solution so any hint is valuable.

I use PHP but I guess any other platform experience could be helpful.

## Answer (score 11, by Mike Waters)

Jim Reisert AD1C regularly publishes various downloadable country files containing an up-to-date list of callsign prefixes with their associated countries, continents, etc. *Those files are meant to be used by ham software.*

Here's three lines from a 2016 cty.dat file. **Notice how the fourth column indicates the continent** (SA, **EU**, AF).

```
Guyana:  09:  12:  SA:    6.02:    59.45:    4.0:  8R:
 8R;
Croatia: 15:  28:  EU:   45.18:   -15.30:    -1.0:  9A:
 9A;
Ghana:  35:   46:  AF:    7.70:     1.57:     0.0:  9G:
 9G;

```

You can download the source of TLF and see how tlf reads and processes it. I rely on Jim's cty.dat file when I use TLF, a contest logging and dupe-checking program for Linux.

Here is Jim's latest country file.

## Answer (score 4, by Glenn W9IQ)

The ITU is the international body responsible for the allocation of call sign prefixes to each country. You can consult this table of allocations in order to build the necessary logic in your program to determine if the call sign in question meets your award requirements.

An example of this table of ITU allocations can be found at: http://www.arrl.org/international-call-sign-series

Here is a snip of that table:

As an alternative, you could subscribe to the QRZ.COM call sign lookup service. The data is exchanged via XML so you could resolve the country from the appropriate XML tag. This may not be fool proof, however, if the call sign in question is not in their database or if the entry contains an error.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9311/how-to-programmatically-distinguish-european-from-non-european-call-sign, by Pedja YT9TP, Mike Waters, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
