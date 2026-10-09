# RFID extension cable

*Tags: antenna-system, balun, amplifier · score 3*

## Question

I am trying to build an extension cable to relay an RFID signal (125kHz) to various distances (2,5,10m). I am using 2 identical antennas at the two ends of a 75Ohm coax cable, and I also put 2 identical baluns between the antennas and the cable ends. By using HackRF coupled with HamItUp, I was able to verify that the signal from the rfid emitter does seem to reach the end of the cable with seemingly identical waveform and amplitudes; however, when the passive element of the RFID is put in the proximity of the antenna (<2cm), it is not recognized.

Do I need an amplifier, even if the signal seems to be relayed with virtually no loss? If so, what kind would be most appropriate for my need?

Thanks!

## Answer (score 4, by natevw - AF7TB)

Most RFID systems work more like two halves of an air-core transformer. If I'm not mistaken the initiator (RFID reader unit) basically measures a varying amount of energy *as it is taken up* by the target (RFID transponder card/fob/etc). The "antennas" are more just inductors that get coupled to each other.

This is less like a normal radio system, and more like a metal detector; so this part of your question is easy for me to answer:

Do I need an amplifier […] If so, what kind would be most appropriate for my need?

By putting an amplifier in your circuit you would almost certainly end up fully **decoupling** the initiator from what it's trying to *measure*. Signals from a normal radio transmitter are "let loose" from the antenna and what happens to the waves past a certain distance has really no affect on the transmitter. Even a radar isn't looking for an affect on its own *transmissions* but rather is listening for later echoes. Whereas most forms of RFID are usually monitoring the transmission itself to see how well it gets taken up right out of the antenna itself.

To press the above point, image a trumpet played at the edge of a stadium. If the bleachers are crowded the echoes will be different than if they are empty but that doesn't change how the trumpet plays — that's like a radar/sonar. But RFID works more like putting a sock in the end of the trumpet for some notes and not others. The player can feel if the sock is there directly in their breath without even listening by ear. Adding an amplifier would be like putting a mic in front of the trumpet, and then sticking a sock in the speaker — the trumpet player can't feel any change.

An RF engineer might be able to explain where/what exactly goes wrong in your current setup, but I suspect already between the transformers in the baluns and the two additional coils you're maybe dampening too much of the direct feedback the RFID reader expects. Whereas if you instead extend the wires of the reader's original coil that should have far less effect even adding quite a length.

Instead of:

```
initiator ↔︎ reader coil ↔︎ coil A ↔︎ balun A ↔︎ transmission line ↔︎ balun B ↔︎ coil B ↔︎ transponder coil ↔︎ target

```

Just:

```
initiator ↔︎ hookup wire ↔︎ reader coil ↔︎ transponder coil ↔︎ target

```

At only 125 kHz the wavelength is a full 2.4 km so your main concern is just the series resistance of the hookup wires rather than any "transmission line" coax/balun impedance stuff.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21243/rfid-extension-cable, by gcaglion, natevw - AF7TB. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
