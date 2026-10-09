# How to compute the required length and turns for an air-cored antenna

*Tags: antenna, antenna-theory · score 5*

## Question

I'm experimenting with RF reception in the 433MHz band and have made the most simple "whip" monopole antenna with 17.6 centimeters of wire.

Out of curiosity, I tried various designs for the antenna among which the one described in the step by step instructions created by Ben Schueler in 2013 and republished a large number of times since then, such as here

This design also works quite well for my application and using online calculators such as this one and this one, I can compute the inductor value.  
But why is 0.220µH right?  
And what about the size of the two straight parts? They are given as 17 and 53 millimeters but how does one gets these values?

I'm asking because I would like to replicate this design, but tuned for 868MHz reception.

Would you have the link to a reference document so that I can compute the values for 868MHz myself? Or should I just go ahead and divide every value by two as 868 is roughly 433 multiplied by two?

Thanks for any pointers.

## Accepted answer (score 4, by Brian K1LI)

A quick simulation with NEC2 indicates that scaling the wire lengths and the inductance by a factor of 0.5 will give the results you seek.

As for why a smaller, loaded monopole gives better results than a full-sized monopole, that is a mystery.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18214/how-to-compute-the-required-length-and-turns-for-an-air-cored-antenna, by OBones, Brian K1LI. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
