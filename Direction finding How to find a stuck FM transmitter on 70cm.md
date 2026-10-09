# Direction finding: How to find a stuck FM transmitter on 70cm?

*Tags: uhf, fox-hunt, direction-finding · score 13*

## Question

There's a blank carrier on a 433 MHz FM voice frequency here. How should we go on about finding the transmitter's location? Practical procedure? Could be somewhere downtown.

## Accepted answer (score 12, by PearsonArtPhoto)

The best way is to get a high gain antenna, and figure out what direction it's coming from. Do this from 2-3 points. Take a map, and draw lines from each of the point of origins from the direction you heard the signal the strongest. That should give you at least an idea of where the signal is coming from.

Once you have a rough idea, the next step is to go to said area, and repeat the process. You should be able to get a better idea of where the signal is coming from. Eventually, you're going to be unable to pick up the transmitter, as you will get high signal anywhere you point your antenna. The next step would require an attenuator, or even just using a rubber duck antenna and using your body as a shield.

FYI, this is essentially the same thing as a fox hunt, except for a less cooperative subject, and you don't have to find the transmitter exactly.

## Answer (score 2, by Adam Davis)

You can build a special rig that will give you direction finding capability with a standard radio here:

[How would a time-difference-of-arrival receiver with two antennas know which side the signal is from?](How%20would%20a%20time-difference-of-arrival%20receiver%20with%20two%20antennas%20know%20which%20side%20the%20signal%20is%20from.md)

It works by switching between two antennas, located less than a wavelength apart. If the two antennas are exactly the same distance from the transmitter, then the signal is undistorted into the radio, and you know the transmitter is perpendicular to the line between the antennas. If the antennas aren't the same distance, then switching between the two introduces a phase modulation, which, on an FM receiver, results in a tone on top of the demodulated transmission.

Use this to locate the direction of the transmitter, move a mile, then do it again, and you'll locate the transmitter to within a very small area. Then walk toward it with this setup and you'll soon find the offending transmitter.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/412/direction-finding-how-to-find-a-stuck-fm-transmitter-on-70cm, by oh7lzb, PearsonArtPhoto, Adam Davis. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
