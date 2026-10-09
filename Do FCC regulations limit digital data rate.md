# Do FCC regulations limit digital data rate?

*Tags: united-states, legal, digital-modes, bandwidth · score 10*

## Question

Are there FCC regulations that specifically limit digital data rate on the amateur bands? Are there any recent or proposed changes? If so, what are they specifically?

## Accepted answer (score 11, by Glenn W9IQ)

#### The Current FCC Regulations (as of July 2018)

Parts 97.305(c) and 97.307(f) regulate digital modes primarily by symbol rate. The table in 97.305(c) maps bands/frequencies to specific symbol rate limitations in 97.307(f) as follows:

(2) No non-phone emission shall exceed the bandwidth of a communications quality phone emission of the same modulation type. The total bandwidth of an independent sideband emission (having B as the first symbol), or a multiplexed image and phone emission, shall not exceed that of a communications quality A3E emission.

(3) Only a RTTY or data emission using a specified digital code listed in §97.309(a) of this part may be transmitted. The symbol rate must not exceed 300 bauds, or for frequency-shift keying, the frequency shift between mark and space must not exceed 1 kHz.

(4) Only a RTTY or data emission using a specified digital code listed in §97.309(a) of this part may be transmitted. The symbol rate must not exceed 1200 bauds, or for frequency-shift keying, the frequency shift between mark and space must not exceed 1 kHz.

(5) A RTTY, data or multiplexed emission using a specified digital code listed in §97.309(a) of this part may be transmitted. The symbol rate must not exceed 19.6 kilobauds. A RTTY, data or multiplexed emission using an unspecified digital code under the limitations listed in §97.309(b) of this part also may be transmitted. The authorized bandwidth is 20 kHz.

(6) A RTTY, data or multiplexed emission using a specified digital code listed in §97.309(a) of this part may be transmitted. The symbol rate must not exceed 56 kilobauds. A RTTY, data or multiplexed emission using an unspecified digital code under the limitations listed in §97.309(b) of this part also may be transmitted. The authorized bandwidth is 100 kHz.

(7) A RTTY, data or multiplexed emission using a specified digital code listed in §97.309(a) of this part or an unspecified digital code under the limitations listed in §97.309(b) of this part may be transmitted.

(13) A data emission using an unspecified digital code under the limitations listed in §97.309(b) also may be transmitted. The authorized bandwidth is 100 kHz.

In general, the HF bands impose symbol restriction number (3) above limiting data to a symbol rate of 300 baud. A notable HF exception is 28.0 to 28.3 MHz where restriction number (4) above applies, raising the symbol rate to 1200 baud.

On the 6 and 2 meter bands, restriction number (5) above applies, limiting the data to a symbol rate of 19.6 kbaud.

From 219 to 220 MHz, restriction number (13) above applies, limiting the data transmission to a bandwidth of 100 kHz - a notable regulatory exception.

From 222 to 225 MHz and the entire 70 cm band, restriction number (6) above applies, limiting the data to a symbol rate of 56 kbaud.

For all frequencies higher than the 70 cm band, restriction number (7) above applies, effectively removing any symbol rate restriction.

#### The ARRL Petition

On November 15, 2013 the ARRL filed a petition, now designated RM-11708, with the FCC to eliminate the HF symbol rate restriction in favor a data regulation built upon a 2.8 kHz occupied bandwidth:

Specifically, ARRL proposes to delete all references to symbol rate from 97.307(f) of the Commission's rules; to create a conforming amendment to part 97.305(c) of the rules; and to establish a bandwidth limit of 2.8 kilohertz for Amateur data emissions below 29.7 MHz.

When asked why the ARRL felt this petition was needed, it responded in a Q&A document:

HF data emissions are now limited to symbol rates that are based on the long-obsolete technology of the early telephone modems. Regulation by symbol rate is not appropriate for present and future generations of digital data modes because it prohibits the use of some new, efficient modes but does not prevent the introduction of digital data modes that have much wider bandwidths than are now in use.

This proposal has languished in the FCC's hands for a number of years. I would encourage any interested US Amateur Radio operator to file comments with the FCC.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10556/do-fcc-regulations-limit-digital-data-rate, by Phil Frost - W8II, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
