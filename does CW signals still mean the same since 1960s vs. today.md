# does "CW signals" still mean the same since 1960s vs. today?

*Tags: cw · score 3*

## Question

I think my 1964 my CW transmitter was just an on-off carrier. I think today's CW is a modulated sideband with no carrier. (This makes tuning today's CW signal non-intuitive to my old paradigm.)

## Answer (score 4, by Marcus Müller)

I think today's CW is a modulated sideband with no carrier.

No, that's not correct.

a modulated sideband with no carrier

that's called SSB-SC (single-sideband-suppressed carrier), not CW.

(I mean if that sideband itself only contains a tone that gets switched on and off, that's identical to CW, but that's a very strange special case of SSB-SC, and nobody would call it that, and one wouldn't produce CW with a SSB transmitter with carrier suppression; you'd instead really modulate the carrier. A device that can do SSB-SC can almost certainly inherently do CW, simply by suppression or not-suppression of the carrier.)

## Answer (score 4, by gschro)

Most all of today's transceivers transmit CW in the traditional way by keying the carrier on and off (controlling the rise/fall time to prevent clicks).

I believe there are some very simple SSB radios will support CW using a "keyed tone" with SSB, as you mention. There are disadvantages to doing it this way, but it is better than nothing. It might require a few less parts at the expense of more microcontroller software. That software might (?) also be able to play with the VFO display to make it seem like a traditional CW radio.

Some digital modes might start or end transmission with a CW ID, and that would typically be done using SSB. But that is a very special case, and not plain old CW operation.

## Answer (score 3, by kj7rrv)

CW signals are the same thing they always have been, but there are new ways of generating them. It is possible to generate CW signals using an SSB (single-sideband, or, as you describe it, "modulated sideband with no carrier") transmitter by generating an *audio* CW signal (consisting of a single tone keyed on and off) and transmitting that over SSB. In this case, the SSB transmitter essentially acts as an upconverter and amplifier. The end result, however, is the same as the output of a traditional CW transmitter; a wave at a single radio frequency is keyed on and off. Stations using the two methods can intercommunicate without issues.

The main benefits of the SSB method are that it can be done with radios that are not designed for CW, and that it can be sent from a computer using the same hardware as digital modes (useful for operators like myself who mostly use digital modes but occasionally use computer-generated CW).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/23442/does-cw-signals-still-mean-the-same-since-1960s-vs-today, by TDL, Marcus Müller, gschro, kj7rrv. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
