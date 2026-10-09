# Pre-transmission burst sent by fldigi

*Tags: digital-modes, fldigi · score 6*

## Question

Every time I click on a PSK macro, before transmitting the message, fldigi outputs a burst of something for about a second. This is visible but not readable on my waterfall display. It wastes time and I want to get rid of it.

## Answer (score 5, by Phil Frost - W8II)

That's a Reed-Solomon identification (RSID). It's purpose is to tell other stations what mode you are using. For PSK it's usually pretty obvious.

To disable it, look for the "TxID" button in the upper-right of the window, and click it to toggle it on and off.

(As you might imagine, the RxID button toggles the receiving of RSIDs. When it is enabled, Fldigi will tune the receiver and switch to the correct mode automatically when it hears one.)

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6944/pre-transmission-burst-sent-by-fldigi, by Andrew Rose, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
