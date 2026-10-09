# Yagi antenna isolation from other Yagi antennas

*Tags: antenna, yagi · score 3*

## Question

I have multiple Yagi antennas horizontally polarized. They are all placed in closed proximity at the same height horizontally and operating in a similar frequency.

The yagis are 2.45GHz, bluetooth band, so they are quite small in size. There is an array of them (PCB antennas) mounted in a radial array of 180. The back of the antennas are very close together, like an 1" apart. The purpose of this design is to be able to gather where a signal is coming from. Is there a way to make them so directional or introducing an element, such as a metal panel that would prevent them from overlapping?

The back lobe from the antenna's is overlapping with the from lobe with other antennas. I'm wishing to be able to prevent that.

The only idea that does to mind but I don't know if it would work is to place a solid piece of metal, grounded, in between the antennas.

Will this work? Are there better ways of creating this antenna to antenna isolation?

## Answer (score 2, by Wireless Learning)

You are using a high enough frequency to be considering patch antennas as a practical solution.

You may try to calculate the size with this site : https://www.pasternack.com/t-calculator-microstrip-ant.aspx With a standard 4.4 FR4 PCB it gives you a size of 38mm x 29mm. If you print yours on JLCPCB for example you may even be able to put two patches on a PCB to make an array. There standard size for PCB is 102mm x 102mm over that you pay a little more.

The more patch you will be putting for the same antenna the more gain and directivity.

Moreover for what I understood you are doing, having a lot of antenna for quick and cheap may be useful.

Theses antenna doesn't mind being put in close proximity with others, we are doing that in FPV without problems.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18492/yagi-antenna-isolation-from-other-yagi-antennas, by PHOLAN, Wireless Learning. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
