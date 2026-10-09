# What is the legality of data modes over UHF/VHF in the US?

*Tags: united-states, legal, aprs, weather, automation · score 3*

## Question

Cheap & simple transceivers are readily available online that allow you to transmit serial data over UHF/VHF frequencies such as 433MHz (approximate range of 1000m). It seems that these are popular in places like Europe where these devices operate in the EU ISM bands.

What is the legality of using these devices in the US if you are a licensed ham operator?

Here is the specific device in question: https://www.elecrow.com/download/HC-12.pdf

On ebay: https://www.ebay.com/itm/433Mhz-HC-12-SI4463-Wireless-Serial-Port-Module-1000m-Replace-Bluetooth-TOP/401051275954?epid=26007567495&hash=item5d6084d2b2:g:JawAAOSwMHdXS9OD

I'm interested in using these to transmit temperature data from a body of water to my house for non-commercial purposes. I can include my callsign in the data transmission and make it visible on the outside of the transmitting device. I would only be transmitting once per hour for no more than 1 second (probably milliseconds) unencrypted.

I understand that there are existing solutions on different frequencies and using different protocols (APRS etc). Just curious if I wanted to use these little 433MHz transceivers if it will be more trouble than it is worth due to legal reasons or people getting upset with me doing non-standard stuff.

## Accepted answer (score 3, by Phil Frost - W8II)

Telemetry is explicitly allowed in §97.111.

You must use an authorized "digital code", which probably means ASCII. And you must use a publicly documented technique. I don't see any specification in the manual of how this device works, but it's probably something simple like FSK, so no difficulty there.

§97.309 RTTY and data emission codes.

(a) Where authorized by §§97.305(c) and 97.307(f) of the part, an amateur station may transmit a RTTY or data emission using the following specified digital codes:

(1) The 5-unit, start-stop, International Telegraph Alphabet No. 2, code defined in ITU-T Recommendation F.1, Division C (commonly known as “Baudot”).

(2) The 7-unit code specified in ITU-R Recommendations M.476-5 and M.625-3 (commonly known as “AMTOR”).

(3) The 7-unit, International Alphabet No. 5, code defined in IT--T Recommendation T.50 (commonly known as “ASCII”).

(4) An amateur station transmitting a RTTY or data emission using a digital code specified in this paragraph may use any technique whose technical characteristics have been documented publicly, such as CLOVER, G-TOR, or PacTOR, for the purpose of facilitating communications.

§97.307 is where data transmissions are authorized. For the 70 cm band these two paragraphs apply, permitting just about any reasonable digital transmission. I don't see any specification of the bandwidth used by the module, so be sure it's under 100 kHz.

(6) A RTTY, data or multiplexed emission using a specified digital code listed in §97.309(a) of this part may be transmitted. The symbol rate must not exceed 56 kilobauds. A RTTY, data or multiplexed emission using an unspecified digital code under the limitations listed in §97.309(b) of this part also may be transmitted. The authorized bandwidth is 100 kHz.

(8) A RTTY or data emission having designators with A, B, C, D, E, F, G, H, J or R as the first symbol; 1, 2, 7, 9 or X as the second symbol; and D or W as the third symbol is also authorized.

I would not assume a $3.55 radio from China does not spew spurious emissions. With an amateur license you can operate uncertified equipment, but still the lack of a regulatory certification should raise suspicion.

§97.307 (c) All spurious emissions from a station transmitter must be reduced to the greatest extent practicable. If any spurious emission, including chassis or power line radiation, causes harmful interference to the reception of another radio station, the licensee of the interfering amateur station is required to take steps to eliminate the interference, in accordance with good engineering practice.

Somewhat surprisingly, it seems numbers are put to spurious emission requirements for HF equipment, and 30-225 MHz, but not above. So:

§97.101 (a) In all respects not specifically covered by FCC Rules each amateur station must be operated in accordance with good engineering and good amateur practice.

With such a low transmit power (100 mW max), there's really no excuse for spurious emissions strong enough to be detectable by your neighbors.

## Answer (score 4, by Glenn W9IQ)

You may be able to operate the device without consideration of your amateur radio status. CFR 47 Part 15.231 permits the low power use of 433 MHz without a license provided certain transmission repetition rates and maximum field strength rates are met. 433 MHz is commonly used by non-licensed home weather stations under part 15 provisions.

If you need to increase the range under part 15 use, consider increasing the receive antenna gain as this is not restricted under part 15.

If you wish to use a part 15 device in Amateur radio service that does not use one of the specified encoding methods enumerated in part 97, you can do so on any amateur band 33 cm and up. See the table in 97.305(c) and note where the right column references 97.307(f)(7). This is the reference that additionally allows "any" code (encoding technique) that is not called out specifically in 97.309. This would include the allowed use of undocumented codes.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10045/what-is-the-legality-of-data-modes-over-uhf-vhf-in-the-us, by Bonfire, Phil Frost - W8II, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
