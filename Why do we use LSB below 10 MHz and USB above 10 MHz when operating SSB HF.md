# Why do we use LSB below 10 MHz and USB above 10 MHz when operating SSB HF?

*Tags: hf, ssb · score 24*

## Question

As a relatively new ham operator, I understand that it is customary to use lower-sideband below 10 MHz and upper-side band above 10Mhz when operating single-sideband HF. I'm curious how we got to such a standard instead of just picking one or the other for all bands.

To further complicate it for new hams, it seems that RTTY operators use lower-sideband everywhere and PSK operators use upper-sideband everywhere. (Reference)

Is there any technical reason not to use upper-sideband everywhere? Or is this purely tradition to be passed on for the sake of tradition? Does anyone know some verifiable history for how this de-facto standard came to be?

## Accepted answer (score 20, by Adam Davis)

Amateur Radio operators use this rule of thumb for historical technical reasons. SM0AOM on the QRZ forums writes:

The changing of ISB sideband positions at 10 MHz actually has an engineering background.

In the earliest ISB exciters, it was found appropriate to change the final mixer scheme from subtraction to addition mixing at around 10 MHz due to spurious suppression concerns. This sometimes caused interoperability problems in international point-to-point ISB circuits.

To overcome this, a practice was formalized in 1959 by the ITU/CCIR as the Recommendation 249, which prescribed that the ISB sideband positions could either automatically or manually be interchanged when the output frequency went through 10 MHz. An often quoted reference where ISB exciter design considerations are handled with German thoroughness is W Kleische: "Fernbedienbarer Steuervorsatz für Kurzwellen-Nachrichtensender" in "Telefunken-Zeitung" December 1962.

Later advances in exciter design made this Recommendation obsolete, and later generations of exciters only had this facility as an option, and current production ISB equipment lacks it entirely.

## Answer (score 4, by Brian K1LI)

I think that there was also a practical reason to do so, apart from any ITU rules. Most, if not all amateur equipment used 9 MHz as IF. Mixing 80m and 40m up and the rest down towards 9 MHz in simple transceivers with one BFO (Beat Frequency Oscillator) was a logical solution. – jcoppens Nov 14 '14 at 12:56

Unfortunately, this is an incorrect answer, but one which I believed as legend until I recently simulated the heterodyning of an SSB signal up and down in frequency. The "sense" of the sideband does not change, regardless of the "direction" of the frequency conversion.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1336/why-do-we-use-lsb-below-10-mhz-and-usb-above-10-mhz-when-operating-ssb-hf, by BenSwayne, Adam Davis, Brian K1LI. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
