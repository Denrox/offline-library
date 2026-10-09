# How do I specify that wires are connected in 4NEC2?

*Tags: antenna, antenna-theory, vertical-antenna, antenna-modeling · score 3*

## Question

I've been trying to get acquainted with the 4NEC2 antenna modeling program. Perhaps this is obvious, but it's not clear to me that wires with one end in the same place are connected. I'm attempting to model a simple quarter-wave antenna with four radials, but I'm getting results that seem suspect. I shouldn't be seeing this symmetric pattern (picture below) along the $z$ direction. It makes no sense. It's as if the radials weren't even there.

I've compared my results to those of a vertical with four radials from Dick Reid, KK4OBI (NEC file here). Those show a strong asymmetry, as I would expect. There seems to be some deep magic going on here in the NEC file that I don't understand.

-Rod AD0YX (call sign updated too!)

Here's the NEC file I'm using (updated)

```
CM High-altitude balloon 70cm antenna
CM Rodney Price AD0YX July 2017
CE
SY freq=434.65             'In wideband simplex band
SY len=71/freq             'meters/sec over MHz
SY rlen=len                'length of radials
SY angle=30                'angle at which radials droop
SY rdroop=rlen*cos(angle)  'droop along x or y axis
SY zdroop=-rlen*sin(angle) 'droop along z axis
SY height=0                'height of bottom of vertical element above radials
GW  1   11  0   0   height  0       0       height+len    #8
GW  2   11  0   0   0       rdroop  0       zdroop        #8
GW  3   11  0   0   0       0       rdroop  zdroop        #8
GW  4   11  0   0   0      -rdroop  0       zdroop        #8
GW  5   11  0   0   0       0      -rdroop  zdroop        #8
GE  0
GN  -1
EK
EX  0   1   1   0   1      0   0
FR  0   0   0   0   freq   0
EN

```

Here's the radiation pattern from 4NEC2:

Here's what I get when I run the KK4OBI model:

## Accepted answer (score 3, by Dick Reid)

Rod,

Ends of wires are connected if they are at the same location. Your model is correct in this regard. However, the wires need to be about one-quarter wavelength long rather than the full wavelength shown.

The 4NEC2 software provides the Automatic Gain Test (AGT) check box when you Generate (F7) the results of your model. Use this in the early stages of modeling. If the Gain correction is too large the results will be in red indicating the model needs to be corrected.

Height for a model over ground needs to be one-half wavelength for optimum conditions. After your model is satisfactory, adjust height according to your real conditions and see what changes. Your model at one-tenth wavelength will show most of the radiation being reflected upward. Use the free space option if you wish to eliminate ground interactions.

The radial angle downward will need to be 40-45 degrees to get a minimum SWR around 50 Ohms. The 30 degree setting you show will be an impedance under 50 Ohms. Since you use Symbols, you can use the Optimizer function to find the best (L)lengths. Similarly, you can optimize for best angle if you use Sin()*L and Cos()*L of the element Length.

Here is the 4NEC2 model information about elevated radials.  
http://www.qsl.net/kk4obi/Elevated%20Radials.html

Your model should be able to reproduce the results of the 4-radial model included in the study. (That model coding is not directly comparable because it uses spherical geometry and adjustable center-fed/off-center feed at any angle for all elements).

The Load card (LD) is an unnecessary complication at this stage of development.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/8915/how-do-i-specify-that-wires-are-connected-in-4nec2, by Rodney Price, Dick Reid. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
