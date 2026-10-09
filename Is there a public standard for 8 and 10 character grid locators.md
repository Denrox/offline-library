# Is there a public standard for 8 and 10 character grid locators?

*Tags: location, maidenhead-locator · score 7*

## Question

We have a question about the algorithm for conversion from coordinates into grid squares [here](How%20can%20one%20convert%20from%20Lat%20Long%20to%20Grid%20Square.md), and this is an extension of that.

I've noticed that there are several web-sites (for example here, or here, or here) and Android applications which will happily show me my 8 or 10 character locator. However, I've been unable to find an exact specification for that extended system.

So my question is: Is there a publicly available specification for the 8 and 10 character locator systems, and if yes, where?

## Answer (score 3, by Scott Earle)

The Maidenhead locator system (which you correctly tagged) is described in detail in this Wikipedia page.

A short summary from that page is:

To summarise:

- Character pairs encode longitude first, and then latitude.
- The first pair (a field) encodes with base 18 and the letters "A" to "R".
- The second pair (square) encodes with base 10 and the digits "0" to "9".
- The third pair (subsquare) encodes with base 24 and the letters "a" to "x".
- The fourth pair (extended square) encodes with base 10 and the digits "0" to "9".
- The fifth and subsequent pairs are not formally defined, but recycling the third and fourth pair algorithms is one possible definition: BL11bh16oo66

On shortwave frequencies, positions are reported at square precision, and on VHF and UHF, subsquare precision is used. More precise position reports are very rarely used.

Note that this means the formal standard does not define anything past the first eight characters (four pairs), but that people tend to extend the system used in the third and fourth pair if they need to be more accurate.

Also note that this extension (only as far as five pairs, or ten characters) is the one used at the APRS website.

## Answer (score 2, by SandPiper)

The Maidenhead system breaks down a grid into increasingly smaller chunks. The fourth pair is defined as an evenly spaced 100 square grid, or 10x10. This site has an excellent image that breaks that down for you:

In this picture, the black box outline is MK80ht. You can see this box was further subdivided, and the user's location of Kalpathy, India is located in MK80ht80.

As noted by the Wikipedia article, there is no formal definition for anything smaller than that, however some users apparently recycle the formula for the third and fourth pairs if needed:

- The first pair (a field) encodes with base 18 and the letters "A" to "R".
- The second pair (square) encodes with base 10 and the digits "0" to "9".
- The third pair (subsquare) encodes with base 24 and the letters "a" to "x".
- The fourth pair (extended square) encodes with base 10 and the digits "0" to "9".
- The fifth and subsequent pairs are not formally defined, but recycling the third and fourth pair algorithms is one possible definition

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/14590/is-there-a-public-standard-for-8-and-10-character-grid-locators, by AndrejaKo, Scott Earle, SandPiper. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
