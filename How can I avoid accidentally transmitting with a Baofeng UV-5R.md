# How can I avoid accidentally transmitting with a Baofeng UV-5R?

*Tags: receiver, baofeng · score 27*

## Question

I don't have $500 for a radio scanner. If I know the few (analog) frequencies that I would like to listen to, I think one can use the Baofeng UV5R (which doesn't cost much). The only problem is that one accidentally can transmit with this and this isn't allowed unless one has a license. From watching some Youtube videos it seems like one maybe can set the transmitting frequency to the same FRS frequency. That way, if one accidentally, presses the transmit button, then one wouldn't accidentally talk to the police or something.


My question is whether this is true?


More generally, what is the best way to prevent accidental transmitting on the Baofeng UV5R?

(I understand that the best way would be to not even have it, but I don't have money enough right now to buy an expensive scanner.)

## Accepted answer (score 26, by Chris)

It'll be easier just to buy a programming cable and use the free Chirp software to turn off transmit permanently. I did this, and used my Baofeng as a receiver only before getting my licence.

EDIT - When I mean permanently, I mean the radio will not respond to the transmit key being pressed. If you get your license in future, you can reenable this feature to turn the radio back into a transceiver.

## Answer (score 13, by William)

If you haven't seen them, the RTL-SDR dongles are really hard to beat for scanning. They let you see a waterfall display so that you can see visually which frequencies are active. It's wonderful!

## Answer (score 7, by Tony M)

Chirp can only disable Transmitting on pre-programmed memory frequencies, if you select the vfo it will still transmit.

Searching Google for 'uv5r transmit inhibit' yielded this on the fifth hit

http://www.bytebang.at/Blog/Locking+down+a+Baofeng+UV5R%2B+to+disable+unintentional+TX

"Within the Uv5R there is a thin rubber pad that pushes against the TX button. This pad can be easily cut of with a sharp knife. After that the TX button on the UV5R does not work any more while the TX circuitry is still untouched. This means that the TX with the headsed plugged in is still working."

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/4938/how-can-i-avoid-accidentally-transmitting-with-a-baofeng-uv-5r, by user4777, Chris, William, Tony M. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
