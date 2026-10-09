# Can a Baofeng UV-5R Display Both Name and Frequency Simultaneously?

*Tags: baofeng, uv-5r · score 10*

## Question

The Baofeng UV-5R style radios have a 2 line display that can display the Name, Frequency, OR Number of the selected memory location for each of 2 memory locations.

Is it possible to display the Name AND Frequency using both lines for just one memory location?

## Accepted answer (score 10, by Edwin van Mierlo)

No, you cannot display "Name & Frequency" if the unit is in "Channel Mode".

what you could do is program (part of) the frequency in the "Name field" of the channel. This way it helps you, like a hint, of what frequency the channel is set to.

Obviously it will get more complicated if you have different RX and TX frequencies programmed in the Channel, you need to be very creative with the name you will give it. (if not using standard offsets that is, as standard offsets will display as a little + or - in the display)

The second line of the display is really for A/B of your VFO.

## Answer (score 12, by SandPiper)

Yes, kind of. You can program the A and B settings separately. Set channel A to display name, and set B to display frequency. Also, set the receiver to only listen to the monitored channel to ensure you won't run into problems.

Then, in channel mode, use your programmed station (ex station 12) on both A and B simultaneously. A will show your channel name alias, and B will show the frequency. It is a workaround, but it will give you what you're looking for.

## Answer (score 2, by W6FCC)

A new Menu 24 on the BTECH UV5X3 Triband radio is "SYNC" and is ON or OFF. This is a great addition. You can program a Marine channel 16 and see "CH 16" in one display and "156.80" in the other display. For Amateur repeaters, it's nice to know the repeater callsign in one display and the actual Frequency in the other.

The only downside is dual monitoring.

If ON, and you have FREQ in the A display, and CHAN in the B display, changing either channel, either UP DOWN or by typing in a channel number, you will see the NAME in one VFO and the Frequency in the other display.

On the UV5 models, there is no such capability.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7501/can-a-baofeng-uv-5r-display-both-name-and-frequency-simultaneously, by Lance, Edwin van Mierlo, SandPiper, W6FCC. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
