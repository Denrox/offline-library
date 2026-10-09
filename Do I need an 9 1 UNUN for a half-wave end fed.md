# Do I need an 9:1 UNUN for a half-wave end fed?

*Tags: balun, antenna-tuner, end-fed-antenna · score 4*

## Question

I was using a 10-ish meter wire as my HF rx antenna. That's all I can install in my QTH. However I realised that my ~10 m wire can be turned into an end fed dipole for 20 meter band.  
But there is a question: If I install my tuner close to antenna end, can i just plug it into the autotuner or should I connect a 9:1 UNUN first?

## Accepted answer (score 4, by Glenn W9IQ)

An end fed, 1/2 wavelength antenna will have a relatively high impedance of 5k ohms or more. So a 9:1, or greater, ratio of balun may reduce the impedance sufficiently to help your tuner get a match and help avoid a voltage flash-over in your tuner.

However, there is another issue that may require some planning. When using an end fed antenna, the current on the antenna needs a return path. If you do not provide a good RF ground or counterpoise, the return current will be via your tuner and radio cabinets. This can lead to RF "bites", RF in the shack causing interference, and even RF burns. If you are running QRP, this may not be an issue. But if you are running 100 watts or more, the effects can be quite pronounced.

I recommend you try to install at least a 10 meter counterpoise wire - multiple wires spread out are even better. These can be run vertically down to the ground with the other end attached to the coax braid by the antenna connection. If you lay it in grass, within one season it will disappear into the thatch and sod and will not be seen again - you can even mow over the area.

## Answer (score 3, by user15108)

Half wave end-fed has appr. 5k impedance, you need a 49:1 transformer to match 50Ohms cable. As the impedance of the antenna is very high a small counterpoise of only 1/10 of a wavelenght does the trick. Do use some form of coax-choke at the antenna-end of your coax to stop RF current flowing in the coax-outside. Usually some 10 turns of coax with a diameter of say 5" will be sufficient.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12389/do-i-need-an-9-1-unun-for-a-half-wave-end-fed, by Hose Dias, Glenn W9IQ, user15108. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
