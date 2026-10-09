# Do Loading Coils Supply "Missing Degrees" to Electrically Short Radiators?

*Tags: antenna-construction, short-antenna · score 5*

## Question

References are made on this and other websites to the effect that loading coils can/will supply "missing degrees" to electrically short radiators. But do they?

## Answer (score 3, by Richard Fry)

Antenna theory, M-o-M software, and experience all show that although a properly-sized loading coil at the feedpoint terminals of an antenna can offset the capacitive reactance of an electrically short radiator to create a terminal impedance of R **±j 0** Ω (resonance), that loading coil does essentially nothing as far as increasing the *radiation resistance* of that short antenna.

The loaded radiator system may become ~self-resonant over some range of frequencies, but at reduced SWR bandwidth and with reduced radiation efficiency for the system, because the ESR of the loading coil must be added to the loss of the network needed to match the feedpoint terminal impedance to a transmission line connected there.

However those effects may be acceptable if they enable installing an antenna suited for the physical constraints of an installation site.

*The text and graphic below were added 21 Sept 2018*

There may be some who believe that a loading coil has an electrical length and radiation resistance related to the **linear** length of the conductor used to construct that coil. However as stated by J. Kraus in *Antennas*, 3rd Edition, p. 296 and shown by NEC4.2, such coils have very nearly the same electrical length and radiation resistance as a single, linear conductor having the same end-end, overall length (aperture) as the coil.

Note in the NEC study below that the coil contains a conductor of about 100 meters in length, which is greater than one-half wavelength at that operating frequency.

If that 100-meter, ~1/2-wavelength conductor was straight (linear), its radiation resistance at that frequency would be (approx) 100 Ω. Yet as shown in the Comment block in that graphic, when that 100m conductor is wound in the form a self-resonant coil, its radiation resistance is only **0.23 Ω**. (Also note that the gain of the antenna system modeled in this NEC study is at least 15 dB below what it would be if using a ~1/2-wavelength, base-driven, linear monopole.)

Therefore, such loading coils are very ineffective in adding "missing degrees" to an electrically short, linear radiator.

The only practical value/purpose of a loading coil is to offset the capacitive reactance of an electrically short radiator, to provide resonance for that antenna system.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/11929/do-loading-coils-supply-missing-degrees-to-electrically-short-radiators, by Richard Fry. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
