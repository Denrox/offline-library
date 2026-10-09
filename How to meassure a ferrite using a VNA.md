# How to meassure a ferrite using a VNA?

*Tags: ferrite, vna · score 5*

## Question

I want to measure a ferrite toroid using a VNA. I would like to classify it for a whole range of frequencies but if it's too complicated I'm OK to just pick one frequency. I have 3 questions actually: 1: Is there a preferred test jig? My plan is to open a coax cable and route the center of the coax through the ferrite while the ground mesh is bunched together and goes along the outside of the ferrite. 2: How do I deal with the effects created by the test setup, I'm afraid it will throw my data out of whack. 3: Do I need to move the ferrite along the length of 1/2 or full wavelength or what happens if the ferrite is placed at a current null?

## Answer (score 2)

Practical use of ferrite is possible without knowing all the details.

1.

Measure the inductance (connector to CH0) for one single winding (N=1) through the ferrite. Do this at a low frequency, f.e. 50 kHz (*). Then you can calculate what more windings will do by taking this value and multiply that with N^2

2.

Make a transformer with N to N windings, primary-secundary, and measure the inductance when the other side is open and also in case of a secondary short-circuit. The coupling factor k kan be calculated (**).

3.

Measure the transfer from that transformer by using both ports, CH0 transfer to CH1, of the VNA. The frequency transfer and the losses are important: the blue line (**).

Of course after calibration.

(*): not the high precision that the purists want.

(**): frequency dependent; measure this for the frequency that you intend to use.

This is the absolute minimum.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20121/how-to-meassure-a-ferrite-using-a-vna, by Jack0220. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
