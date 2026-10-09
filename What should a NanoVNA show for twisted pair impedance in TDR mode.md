# What should a NanoVNA show for twisted pair impedance in TDR mode?

*Tags: impedance, transmission-line, nanovna, vna · score 4*

## Question

Thought I'd try doing some actual experiments with [twisted pair feedlines](Why%20isn%27t%20twisted%20pair%20used%20for%20feedlines.md) and also just some general "non-coax" measurements and testing, but not until after I understood a bit more about using my VNA. Turns out that was probably a good idea as even the basic initial measurements are not what I had expected!

I haven't tracked down any official standards (maybe this is partly where I went wrong?) but "the internet" says that the twisted pairs of network cable have a characteristic impedance of 100Ω. But when I look down a pair of wires with my NanoVNA in TDR mode, the |Z| it says it sees through the length of wire is pretty much right around **50**Ω instead:

The setup here is obviously not super precise, I'm just using a BNC→banana plug adapter to clamp onto both wires of a twisted pair. The NanoVNA is set to sweep from the bottom of it's range up to 750MHz iirc seemed to match the wire, and I've got it showing |Z| with the "transform" option on.

I don't thing the results are *completely* bogus, as when I change the end of the pair from an open to a short the initial disturbance of the banana plug remains the same while the disturbance corresponding to the end of the line "flips" as it were:

But the reading along the whole line shows ~50 ohms instead of the 100 ohms I was expecting to see. Am I doing something wrong, or is the expected result? Is there a way to see the actual characteristic impedance along a transmission line with a VNA, or does it basically just "see" its own (i.e. the VNA's) characteristic impedance in the absense of a disturbance?

## Accepted answer (score 6, by tomnexus)

Your second guess is correct - it's displaying its own system impedance, not the line impedance.

A VNA's fundamental units of reflection are: 1) Magnitude of the reflection, and 2) Phase of the reflection. It measures these at many frequencies. It doesn't measure Z or L or R.

Everything else you see on the screen is transformed from these numbers, using the *system impedance*, 50 ohms. The impedance (seen at the point to which you've calibrated) is $Z=Z_0{{1+\rho}\over{1-\rho}}$. Then you can ask for the magnitude of the impedance $|Z|$ in ohms.

By applying an inverse fourier transform (if you've set up the frequency steps correctly), the complex reflection @ frequency can be transformed into complex reflection @ time. This can also be plotted as |Z| over time, or R+L over time, or dB over time, etc.

Now consider the long transmission line which is as you say about 100-110 ohms. There will be a reflection from the initial impedance step, and you see this on the screen. But the line itself doesn't reflect anything, until you reach the open or short at the end. So the reflection coefficient $\rho$ *at that time* will be zero, and $50{{1+0}\over{1-0}} = 50 \Omega$. You can see that any transmission line will give you that, and indeed even after the last reflection you still see "50 ohms" again.

To accurately measure the $Z_0$ of an unknown line, I recommend a modified $\lambda/8$ procedure.

Note that for a lossless short-circuit line,  
$ X_{SC}=Z_{0}\tan({{2\pi\ell }\over{\lambda}})$  
And if $\ell=\lambda/8$ then $tan({\pi\over4})=1$, so  
$ X_{\mathrm {in} }=Z_{0} $ i.e. the *imaginary impedance* is equal to the characteristic impedance *of the **line**, not the VNA*!

But how do you know where the line is exactly $\lambda/8$ long?

The open-circuit impedance is almost the same:  
$ X_{OC}=-Z_{0}\cot({{2\pi\ell }\over{\lambda}})$  
where $cot({\pi\over4})=1$ too.

My trick, I'm sure not my own invention, is to do this:

1. Calibrate the VNA over a wide frequency range, perhaps from 0 to quarter-wave.
2. Display the Smith Chart, R+jX
3. Short circuit the far end of the unknown line
4. Place a marker at the top of the smith chart, where X = your best guess for Z0.  
For example, marker at 1+j100 ohms.
5. Open circuit the line, and look at the marker value for -X, now at the bottom.  
It won't be quite the same value, eg. 2-j120 ohms.
6. Adjust the position of the marker to be in the middle, say 2-j110 ohms
7. Short circuit the line again
8. and repeat until the value of X and -X doesn't change.  
Now you've found the $\lambda/8$ point, and also the $Z_0$.

Finally, watch out when measuring a balanced line with an unbalanced feed - the whole line becomes an antenna too. The effect will be more pronounced at $\lambda/4$ when it's a resonant monopole, less at 1/8. And with a battery-powered VNA maybe even less of an issue. Some ferrites on the coax wouldn't hurt... as usual just try laying your hands on the circuit to see what changes.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/22418/what-should-a-nanovna-show-for-twisted-pair-impedance-in-tdr-mode, by natevw - AF7TB, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
