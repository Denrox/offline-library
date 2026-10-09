# Does effective grounding of mobile (vehicle) antenna mounts address common-mode currents?

*Tags: mobile, feed-line, grounding · score 4*

## Question

While researching how best to install my mobile amateur radio in my car, I didn't understand [if there was optimum Antenna Feedline Length for mobile installations?](Is%20there%20an%20optimum%20Antenna%20Feedline%20Length%20for%20mobile%20installations.md)

Understanding that this is caused when common-mode currents make the feedline part of the antenna, I want to know **if effectively grounding the antenna mount (coax shield) to the vehicle body will help mitigate common mode currents with mobile antenna installations?** (Effective meaning metal to metal under the trunk lip, and maybe an extra ground strap from trunk to car chassis.)

My feedline does run inside the vehicle along the body panels, so it is definitely not a good place to work as a radiator element and I certainly wish to shorten the feedline and obtain the best SWR reading possible. I am using a small 1/4 wave 2M VHF antenna that also doubles as a 5/8 wave UHF antenna (primarily for the shorter height for underground parking).

## Answer (score 2, by Phil Frost - W8II)

Does effective grounding of mobile (vehicle) antenna mounts address common-mode currents?

No. Well, not really. It might help, incidentally. Any 1/4 wave antenna is only half an antenna, and the other half is your car. The antenna designer made some assumptions about your car and how you'd use it to complete the antenna: if you violate those assumptions then you have a different antenna than the one that was designed, which may or may not be worse in any number of facets of performance, including common-mode current.

For example, the antenna designer probably assumed that the car is made of sheet metal. If you put a 1/4 wave vertical on a car with fiberglass body panels, you absolutely will have significant common-mode currents because [the feedline is the other half of the antenna](How%20to%20reduce%20RF%20in%20the%20shack%20when%20using%20vertical%20HF%20antenna%20%28no%20radials%29.md).

Consequently, the best advice is probably to install the antenna according to the manufacturer's instructions. Many mobile antennas are compromise designs, so by deviating from these instructions it may be possible to make an improvement, but it's also just as possible to make things worse. Without all the details it's hard to say which will happen.

My feedline does run inside the vehicle along the body panels, so it is definitely not a good place to work as a radiator element [...]

This is not necessarily the right conclusion. The feedline will be capacitively coupled quite well to the body panels, and the body panels can be decent radiators. RF currents *want* to radiate. If you don't absorb that energy in a loss somewhere, it will radiate, eventually. Indeed, it's more ideal if all the energy is radiated from your antenna as designed and there are no common-mode currents, but if that's not completely what happens I suspect the consequences are not as bad as you imagine.

The bigger problem, if there is one, is probably that some of the radiating structure comes close to electronics in your car resulting in noise when receiving. Remember reciprocity: if it's transmitting well, it also makes a good receiver. But, this is already a big problem in mobile installations: the RF noise from the electronics tends to find its way everywhere, thanks to the metal car. It's not like the antenna is on a tower in a rural area far away from noise sources. It's practically attached to a noise source.

With this in mind, there's an easy experiment you can do which will answer your question better than any musing over theory we can do here. Set up your radio so you can listen to or otherwise measure the noise received. Then, temporarily attach some proposed modification to the antenna system, be it a ground strap or whatever. Can you measure an improvement? If so, you've confirmed your modification reduces noise, perhaps by moving the radiating structures of the car farther away from noise sources. Repeat the experiment listing to some desired signal to be sure you are just reducing noise and not just killing the antenna performance (a dummy load is very quiet, also). If your tested modification reduces noise and increases signal, it is a good modification, and will have an equal improvement on your transmissions, by reciprocity.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1636/does-effective-grounding-of-mobile-vehicle-antenna-mounts-address-common-mode-, by BenSwayne, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
