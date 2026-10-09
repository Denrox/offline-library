# Can you base64 encode or compress ham transmissions [US]?

*Tags: united-states, legal · score 3*

## Question

(a) No amateur station shall transmit: <...> Music using a phone emission except as specifically provided elsewhere in this section; communications intended to facilitate a criminal act; **messages encoded for the purpose of obscuring their meaning**, except as otherwise provided herein; obscene or indecent words or language; or false or deceptive messages, signals or identification

Can *encoded* information be transmitted? For example: If you have a defensible reason for encoding (ie compression), does that count as message encoded "for the purpose of obscuring meaning" and is it allowed?

Does this change if you use a custom protocol to encode (not cryptographically secure but technically obfuscated)?

## Accepted answer (score 6, by hobbs - KC2G)

97.113(a)(4) doesn't get involved here at all. Every digital message is "encoded", but that doesn't mean it's "encoded for the purpose of obscuring its meaning".

Instead, much hinges on 97.309(a)(4) and 97.309(b).

97.309(a)(4) says

An amateur station transmitting a RTTY or data emission using a digital code specified in this paragraph may use any technique whose technical characteristics have been documented publicly, such as CLOVER, G-TOR, or PacTOR, for the purpose of facilitating communications.

Which basically says that so long as what you're doing is decodable by anyone in the public, without secret algorithms, or secret keys, it's fine (that "a code specified in this paragraph" is a sticking point that everyone seems to ignore; it only includes Baudot, AMTOR, and ASCII, and therefore would seem to exclude nearly every modern HF digital mode that uses an 8-bit code or convolutional codes like FT8 on a silly technicality... but either my interpretation is wrong here, or, like I said, everyone including the FCC is just happy to ignore that detail). In any case base64 or any widely-known compression algorithm is certainly a "technique whose technical characteristics have been documented publicly".

97.309(b) says

Where authorized by §§97.305(c) and 97.307(f), a station may transmit a RTTY or data emission using an unspecified digital code, except to a station in a country with which the United States does not have an agreement permitting the code to be used. RTTY and data emissions using unspecified digital codes must not be transmitted for the purpose of obscuring the meaning of any communication. When deemed necessary by a Regional Director to assure compliance with the FCC Rules, a station must:  
(1) Cease the transmission using the unspecified digital code;  
(2) Restrict transmissions of any digital code to the extent instructed;  
(3) Maintain a record, convertible to the original information, of all digital communications transmitted.

Which is saying that on some band segments (at a glance, it appears to be the data segments on the 6-meter and shorter bands), you can even transmit data using *completely undocumented* encoding schemes, unless you're doing it internationally to a country that doesn't approve of that, and unless you're doing actual encryption. However, if you do that and the FCC tells you to stop, you have to stop.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20713/can-you-base64-encode-or-compress-ham-transmissions-us, by belkarx, hobbs - KC2G. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
