# Should I add call signs with /R suffix to the logbook?

*Tags: repeater, ft8, wsjt-x · score 4*

## Question

Sometimes in FT-8 mode I receive calls like this one:

It happens 2-3 times a week.

The problems are: 1) I never could look up such call signs 2) I tried to reply, but never got answer 3) I don't know what /R means.

Are these real calls or maybe just a noise that WSJT-X somehow managed to decode? So far I didn't log such events as QSO's. Maybe I should?

UPD: As Marcus pointed out, the checksum collision in FT-8 is very unlikely. Also I managed to figure out that "/R" means a repeater https://en.wikipedia.org/wiki/Amateur_radio_call_signs I believe it means that the signal was sent automatically by the device, not that the operators works through the repeater. Still I wonder - should I add repeaters to the logbook?

## Accepted answer (score 7, by Glenn W9IQ)

FT8 decoding can use a technique called *a priori* (AP) whereby it uses naturally accumulating information for the purposes of increasing apparent sensitivity by about 4 dB. There is an increased chance of false decodes when AP is enabled since AP is essentially sophisticated guess work. The technique looks at its guessed result and compares it to the parity information and displays the guess if there is a specified level of confidence of it being correct. There is no assurance that it is correct. The term often used for these false AP decodes is *exotica* - referring to a rare, decoded call sign that doesn't exist.

While it is entirely possible that the sender is a pirate station, the fact that the V0 prefix is not allocated by the ITU is a good indicator that you are experiencing exotica. The /R is likely part of the exotica decode - not an indication of a repeater. Another good indication of an exotica decode is a decode of an unlikely grid square.

Because the decoded call sign does not exist, when you respond, the other station does not recognize the exotica call as their call sign so no QSO takes place.

If you wish to avoid exotica, at the expense of some loss of apparent sensitivity, simply disable the AP feature under the decode menu.

## Answer (score 2, by John)

I agree with Glenn's answer about AP decodes since this V0 is an invalid callsign, but I'd like to add that in general /R on a callsign typically means it is a "Rover", or a mobile station that roves to multiple locations to operate, often during a contest. You'll sometimes see these on FT8. It can also indicate a repeater callsign, but there are no repeaters on FT8.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12930/should-i-add-call-signs-with-r-suffix-to-the-logbook, by Aleksander Alekseev - R2AUK, Glenn W9IQ, John. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
