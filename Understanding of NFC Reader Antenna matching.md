# Understanding of NFC Reader Antenna matching

*Tags: antenna-theory, antenna-construction, hf, impedance-matching · score 3*

## Question

I have been designing a 20 x 20 cm square NFC reader antenna which looks like this:

In order to make it work and detect NFC tags at certain distance, it needs to be matched. To do that I was trying to implement a really easy three component matching procedure described in here http://www.ti.com/lit/an/sloa135a/sloa135a.pdf. Unfortunately it did not work for me. The first step in this procedure is to measure the impedance of the unmatched coil. What would you ideally expect is to have a neglectably low resistance (like 1-2 Ohm) and some positive reactance (like 450-500 Ohm). At this step I'm having a surprisingly high resistance - up to 200 Ohm. This ruins the whole matching procedure.

However, I was still able to make this antenna work trying various capacitors and resistors with different values. You can see the resulting equivalent circuit that I have drawn on the second picture of the antenna. I have a 27 pF capacitor in series with the coil and a 51 kOhm resistor in parallel with it. I have measured the inductance of the coil - it is approximately 3.5 uH. Measured S11 curve for this antenna can be seen here:  It has a quality factor of approximately 15.5. Antenna is working and it works pretty good, detecting the tags up to 12 cm distance.

The problem is that I completely don't understand how this antenna works and I'm puzzled with the fact that it is resonating at 13.4 MHz. With 27 pF capacitor and 3.5 uH coil in series it should have been resonating around 16.37 MHz.

Does anybody have any idea about why this is happening and how the antenna works? I would really appreciate any considerations or ideas about my design. Probably I'm doing something wrong or matching procedure is wrong or layout is incorrect.

## Answer (score 4, by Glenn W9IQ)

It is very difficult to help you with analyzing a circuit when clearly, and as you stated, your measurements were in error. The electrically fractional wavelength loop will have a very low feedpoint resistance of less than 1 ohm - not the ~200 ohms you incorrectly measured. Until you correct your measurement error, any further analysis will be conjecture.

You mentioned that you measured the inductance of the loop antenna. This is not a helpful metric. The complex impedance of the antenna at the design frequency, prior to adding any matching network components, is the critical metric for calculating the matching circuit components.

Also take note that your measured Q is a little too high. It should be no more than 7 in order to properly pass the sidebands associated with NFC. Reducing the Q will likely increase your effective NFC distance provided the reduced Q is not obtained through additional resistive swamping.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10459/understanding-of-nfc-reader-antenna-matching, by Vlad Ekaterinichev, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
