# How do I receive ATSC with GNU Radio?

*Tags: software-defined-radio, united-states, gnuradio · score 13*

## Question

How do I receive ATSC video with GNU Radio so I can play the A/V in, e.g., the VLC video player? Are there any example GNU Radio block diagrams to accomplish such a task?

## Accepted answer (score 1, by n0p)

It depends of what signal do you want to receive: ATSC and DVB are digital standards and you have blocks and scripts to deal with as you have seen in the webpage you linked.

DVB has a lot of different modulation and encoding possibilities and dealing with this in GNURadio is a bit of a headache if you do not know the exact parameters to begin with. You can also try LeanDVB

Analog television is a totally different beast and I don't know yet how to deal with it. IIRC, the next version of GNURadio has a MJPEG sink on the wishlist to help deal with analog TV signals.

Using RTL receivers you can try a windows only software: tvsharp.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7047/how-do-i-receive-atsc-with-gnu-radio, by Geremia, n0p. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
