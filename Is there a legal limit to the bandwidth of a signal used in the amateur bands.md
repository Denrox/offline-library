# Is there a legal limit to the bandwidth of a signal used in the amateur bands?

*Tags: united-states, legal, digital-modes, bandwidth · score 8*

## Question

While a normal voice channel is ~10kHz-15kHz in bandwidth, some digital modes can be significantly wider.

Are there any legal restrictions on how much bandwidth I could use for amateur radio communications (e.g. video chat over ham radio)?

## Answer (score 12, by Phil Frost - W8II)

Summary:

- In all cases, no more bandwidth than necessary. §97.307(a), (b)
- In data portions of LF, MF, and HF bands, 500 Hz. §97.3(c)(2)
- In the phone portions of LF, MF, and HF bands, no more than "the bandwidth of a communications quality phone emission of the same modulation type." 4 kHz is a good number to put on it, being a typical limit of an SSB emission. §97.307(2)
- 6 and 2 meters: 25 kHz. §97.307(5)
- 1.25 m and 70 cm: 100 kHz. §97.307(13), (8)
- everything above 70 cm: no explicit limitation: follow "good amateur practice."

For reference, relevant sections of §97.307 (emphasis added):

(a) No amateur station transmission shall occupy **more bandwidth than necessary** for the information rate and emission type being transmitted, **in accordance with good amateur practice**.

(b) Emissions resulting from modulation must be confined to the band or segment available to the control operator. Emissions outside the necessary bandwidth must not cause splatter or keyclick interference to operations on adjacent frequencies.

[...]

(f) The following standards and limitations apply to transmissions on the frequencies specified in §97.305(c) of this part.

[...]

(2) No non-phone emission shall exceed **the bandwidth of a communications quality phone emission of the same modulation type.** The total bandwidth of an independent sideband emission (having B as the first symbol), or a multiplexed image and phone emission, shall not exceed that of a communications quality A3E emission.

[...]

(5) A RTTY, data or multiplexed emission using a specified digital code listed in §97.309(a) of this part may be transmitted. The symbol rate must not exceed 19.6 kilobauds. A RTTY, data or multiplexed emission using an unspecified digital code under the limitations listed in §97.309(b) of this part also may be transmitted. **The authorized bandwidth is 20 kHz.**

(6) A RTTY, data or multiplexed emission using a specified digital code listed in §97.309(a) of this part may be transmitted. The symbol rate must not exceed 56 kilobauds. A RTTY, data or multiplexed emission using an unspecified digital code under the limitations listed in §97.309(b) of this part also may be transmitted. **The authorized bandwidth is 100 kHz.**

[...]

(13) A data emission using an unspecified digital code under the limitations listed in §97.309(b) also may be transmitted. **The authorized bandwidth is 100 kHz.**

The definition of "Data" in §97.3(c) includes a limitation on bandwidth:

(2) Data. Telemetry, telecommand and computer communications emissions having (i) designators with A, C, D, F, G, H, J or R as the first symbol, 1 as the second symbol, and D as the third symbol; (ii) emission J2D; and (iii) emissions A1C, F1C, F2C, J2C, and J3C having an occupied **bandwidth of 500 Hz or less when transmitted on an amateur service frequency below 30 MHz**. Only a digital code of a type specifically authorized in this part may be transmitted.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10313/is-there-a-legal-limit-to-the-bandwidth-of-a-signal-used-in-the-amateur-bands, by Stack Tracer, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
