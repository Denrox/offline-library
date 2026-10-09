# How to correctly model a small helix antenna

*Tags: antenna-modeling · score 4*

## Question

I am getting weird results trying to model a small 433 MHz helix antenna similar to this one with 4nec2:

In particular I am not able to obtain a resonable SWR value. This is the antenna an example of the nec file.

```
CE
SY L=0.0205 'Length of helix
SY S=0.001  'Pitch
SY R=0.0003 'Wire radius
SY N=(L-2*R)/S  'Turns
SY D=0.005  'Helix diameter
SY L1=0.008 'Length of base wire
SY L2=0.0055    'Length wire to be soldered
GW  1   3   0   0   -L1 0   L2  -L1 R
GW  2   1   0   0   0   0   0   -L1 R
GW  3   1   D/2 0   0   0   0   0   R
GH  4   N*12    S   L   D/2 D/2 D/2 D/2 R
GM  0   0   -90 0   0   0   L1  L2  0
GE  1
GN  1
EK
EX  0   1   2   0   1   0   0
FR  0   0   0   0   433 0
EN

```

I tried also adding a reflector to the model but still the results waren't right. I think that the problem could be the segments length, near the $0.001\lambda$ limit.

Here an example of the outputs I am getting:

## Accepted answer (score 3, by tomnexus)

In my experience this can't be modelled in NEC. It doesn't handle tight corners, close segments, short segments like this. Your geometry input file looks technically correct, but you're asking too much of the kernel.

Your best chance would be to specify the helix so that it uses only 4 or 5 segments per turn, ensuring that they overlap perfectly, i.e. it forms a rectangular box, not a staggered cylinder.

```
GH  4   **N*4**    S   L   D/2 D/2 D/2 D/2 R

```

And make the wire thinner so that the spacing is about 2 * Diameter. The self-resonant frequency will be wrong, but it's wrong anyway.  
Use the model checker to catch obvious errors first.  
Use the 3D radiation pattern integration to find total radiated power, and check this against input power for sanity.

I really think think the only way to use NEC here would be to first manually calculate the inductance per metre of the coil, and then model the antenna as just three fat segments, loaded appropriately. With such fat segments, be careful of length/diameter and diameter/diameter rules, and don't try to turn corners. It won't help you choose the exact number of turns or the thickness of the wire, but you'll get some indication of the impedance, the bandwidth, radiation pattern, etc.

After several years of near-daily modelling in NEC, I tried an inductor in FEKO and was amazed to find that it just simulated it correctly, without a fuss.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20152/how-to-correctly-model-a-small-helix-antenna, by stenio, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
