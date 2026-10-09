# Replacing hand-wound inductors with store-bought versions

*Tags: diy · score 6*

## Question

I'm wading through some schematics for a direct conversion I-Q SDR receiver, and there is an L-C band-pass filter on the input. Each inductor is specified by an inductance, a toroidal core material, a wire gauge (AWG), and a number of turns. I understand that this is all the information that is required to replicate the exact specified inductor (and all the values check out), and I know I could replicate the part described in the schematic.

However, I would like to avoid manually building a component like an inductor if I can ( because of logistics and personal enjoyment). While I can certainly select an inductance value from a menu on Digikey, there is more to inductors than just the value. I suspect the self-resonant frequency (SRF) needs to be well above the frequency of interest, and the Q of the inductor should be high, but past that I'm not sure what is important.

What problems am I going to run into if I switch from hand-wound toroidal inductors to a "store-bought" inductor such as this one?

## Accepted answer (score 3, by Phil Frost - W8II)

I'm going to say a lot of stuff that could go wrong, but really, don't be discouraged. I think mostly ham equipment is built with self-wound inductors because cores and magnet wire is cheap and easy to source. Take apart a cell phone and you may not find a single wound inductor on it. None of the problems to follow are insurmountable, if they are even problems at all. Of course, it always depends on the application and circuit.

You are right to care about the self-resonant frequency and Q. Generally a high SRF and Q is good, but in some circuits it may be a problem merely that they are *different*, if the design already compensates for the non-ideal components of the self-wound part. Probably not an issue except in the most critical filters, and probably nothing that can't be fixed by adjusting a capacitor or resistor to compensate. This is why high SRF and Q are desirable: you can always make them lower by adding parts, but you can't make them higher.

All ferrite-cored inductors get lossier with increasing frequency. Generally, ferrites for low frequencies can provide a higher permeability (thus increasing inductance per turn), but as frequencies increase so do losses, necessitating lower loss ferrite materials with a lower permeability. [How does one read a ferrite datasheet?](How%20does%20one%20read%20a%20ferrite%20datasheet.md) gives some insight into the parameters of the ferrite itself.

So, also check the intended frequency of operation for your considered chip inductor. If the datasheet doesn't say otherwise, you can assume that the test frequency is near the top of frequencies for which the part is suited. You could go a little higher if you don't much care about losses or Q. If you go a lot higher you might as well buy a resistor.

Other problems you might encounter, generally:

**Reduced power handling**

The smaller surface area of a chip inductor makes it less able to radiate heat, and its smaller mass makes it heat more quickly for a given power. Probably a non-issue for receive filters, maybe an issue for transmit filters.

**Lower saturation current**

Again driven by smallness, chip inductors will typically have less ferrite material per ampere-turn of wire in it, which increases inductance per physical size, but decreases saturation current.

Besides the possibility of outright saturating the core, you can probably measure higher non-linear distortion in a chip inductor with the right equipment. This is because saturation isn't a hard wall, but something that sets in gradually. The less magnetized the core is, the more linear it is. If the core is made smaller but inductance is held constant, the core must be more magnetized, and thus less linear. The difference may be slight, and not important for many applications.

**Higher ohmic losses**

The smaller size of surface mount components usually dictates smaller conductors, which have higher resistance, and thus higher loss and lower Q.

**More leakage** (in some designs)

Some, but not all chip inductors do not have a closed magnetic circuit. This can lead to mutual inductance with others on the board, making transformers where you don't want them. Read the datasheet to see what you are getting. The example you provided says it is "magnetically shielded", suggesting a closed magnetic circuit.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1993/replacing-hand-wound-inductors-with-store-bought-versions, by W5VO, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
