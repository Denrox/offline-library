# Maidenhead Locator System

The **Maidenhead Locator System** (a.k.a. **QTH Locator** and **IARU Locator**) is a geocode system used by [amateur radio](Amateur%20radio.md) operators to succinctly describe their geographic coordinates, which replaced the deprecated QRA locator, which was limited to European contacts. Its purpose is to be concise, accurate, and robust in the face of interference and other adverse transmission conditions. The *Maidenhead Locator System* can describe locations anywhere in the world.

Maidenhead locators are also commonly referred to as *QTH locators*, *grid locators* or *grid squares*, although the "squares" are distorted on any non-equirectangular cartographic projection. Use of the terms *QTH locator* and *QRA locator* was initially discouraged, as it caused confusion with the older QRA locator system. The only abbreviation recommended to indicate a Maidenhead reference in Morse code and radio teleprinter transmission was **LOC**, as in **LOC KN28LH**.

John Morris [G4ANB](Amateur%20radio.md) originally devised the system and it was adopted at a meeting of the IARU VHF Working Group in Maidenhead, England in 1980.

### Description of the system

A Maidenhead locator compresses latitude and longitude into a short string of characters, which is similar in concept to the World Geographic Reference System or GEOREF. This position information is presented in a limited level of precision to limit the number of characters needed for its transmission using voice, [Morse code](Morse%20code.md), or any other operating mode.

The chosen coding uses alternating pairs of letters and digits, like so:

- BL11BH16

In each pair, the first character encodes longitude and the second character encodes latitude. These character pairs also have traditional names, and in the case of letters, the range of characters (or "encoding base number") used in each pair does vary.

To avoid negative numbers in the input data, the system specifies that latitude is measured from the South Pole to the North Pole, and longitude measured eastward from the antimeridian of Greenwich, giving the prime meridian a false easting of 180° and the equator a false northing of 90°.

To simplify manual encoding, the base for the first pair of letters—traditionally called a *field*—was chosen to be 18, thus dividing the globe into 18 zones of longitude of 20° each, and 18 zones of latitude 10° each. These zones are encoded with the letters "A" through "R".

The second pair of numbers, called a *square* and placed after the first pair of letters, uses a base number of 10, and is encoded using the digits "0" to "9". This is where the alternative name "grid squares" comes from. Each of these squares represents 1° of latitude by 2° of longitude. For additional precision, each square can optionally be sub-divided further, into *subsquares*. These are encoded into a second pair of letters, which should be presented in uppercase, but are sometimes (incorrectly) presented in lowercase as a legacy from the old QRA. The error has unfortunately been incorporated into various software packages, several examples of which can be seen on this page. Again, to make manual calculations from degrees and minutes easier, 24 was chosen as the base number, giving these subsquares dimensions of 2.5' of latitude by 5' of longitude. The letters used are "A" through "X".

The resulting Maidenhead subsquare locator string is hence composed of two letters, two digits, and two more letters. To give an example, W1AW, the American Radio Relay League's Hiram Percy Maxim Memorial Station in Newington, Connecticut, is found in grid locator ​FN31pr. Two points within the same Maidenhead subsquare are always less than 10.4 km (6.5 mi) apart, which means a Maidenhead locator can give adequate precision from only six easily transmissible characters.

For even more precise location mapping, two additional digits were proposed and ratified as an *extended locator*, making it altogether eight characters long, and dividing *subsquares* into even smaller ones with dimensions 15" of latitude by 30" of longitude. Such precision has uses in very short communication spans. Beyond this, no common definition exists to extend the system further into even smaller squares. Most often the extending is done by repeating alternating subsquare and square rules (base numbers 24 and 10 respectively). However, other bases for letter encodings have also been observed, and therefore such *extended extended* locators might not be compatible.

To summarise:

- Character pairs encode longitude first, and then latitude.
- The first pair (a *field*) encodes with base 18 and the letters "A" to "R".
- The second pair (*square*) encodes with base 10 and the digits "0" to "9".
- The third pair (*subsquare*) encodes with base 24 and the letters "A" to "X".
- The fourth pair (*extended square*) encodes with base 10 and the digits "0" to "9".

(The fifth and subsequent pairs are not formally defined, but recursing to the third and fourth pair algorithms is a possibility, e.g.: BL11BH16OO66)

On shortwave frequencies, positions are reported at *square* precision, and on VHF and UHF, *subsquare* precision is used. At high microwave frequencies *extended square* and *extended subsquare* precision is often used.

### Adoption and use

Like the QRA system before it, Maidenhead locators were enthusiastically adopted by radio amateurs beyond contesting, and it is now in widespread use.

Maidenhead locators are still used as part of the formulas for scoring in many VHF amateur radio contests and as the basis of earning awards like the American Radio Relay League's VHF/UHF Century Club, URE TTLOC, etc. operating contests.

Under IARU Region 1 rules, VHF distance calculations are carried out between Maidenhead subsquare centres, assuming a *spherical* Earth. This results in a small error in distance, but makes calculations simpler and, given the inherent imprecision in the input data used, it is not the biggest error source. Until the adoption of WGS 84 as the official geodetic datum of the Maidenhead locator system in 1999, operators had usually specified their location based on their local national datum. Consequently, stations very near the edges of squares (at denoted precision) may have changed their locators when changing over to the use of WGS 84.

The relatively new [FT8](WSJT%20%28amateur%20radio%20software%29.md) narrowband digital mode transmits Maidenhead locator square as part of standard messages, with the 4 character locator square being efficiently represented within 15 bits of the transmitted string.

In 2019 the IARU clarified the latest position on use of the IARU locator at various levels of precision, including a fifth pair of characters and that all letters should be uppercase.

### Hardware and software support

In 1985, the Radio Society of Great Britain published a small set of BASIC language routines to convert from locator references to geographical coordinates (latitude and longitude) for further processing. A complete program in BASIC called *Universal Gridlocator* was made available the following year by ARRL for a nominal cost of US$3.

Many other utilities exist to convert latitude and longitude to locators, as this is a favourite hack for programmers who are also radio amateurs. Perl supports conversion between geographical coordinates and Maidenhead locators in module Ham::Locator by Andy Smith, available on CPAN.

The Python maidenhead module is on pypi.org for installation via pip.

Many commercially available general purpose (civil) Global Positioning System (GPS) receivers (e.g. Garmin GPS-12) have the option to display positions in Maidenhead Locator format.

---

*Source: Wikipedia, Maidenhead Locator System (https://en.wikipedia.org/wiki/Maidenhead_Locator_System), by Wikipedia contributors, CC BY-SA 4.0.*
