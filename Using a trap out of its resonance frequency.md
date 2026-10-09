# Using a trap out of its resonance frequency?

*Tags: antenna, trap · score 4*

## Question

I have a vertical antenna, about 7M total length, with a loading coil at 6M height. This is just because aluminium tubing is sold in 6 meter lengths. The loading coil is used to make it resonate at 7.1 MHz. Here's a SWR plot of the antenna (simulated):

I was wondering if it would be possible to replace the loading coil for a trap, for example at 8.5MHz, so the antenna would work in both the 30 and 40M band. Here's my idea:

- At below 8.5MHz, the capacitor will present a high impedance, and the RF would flow through the coil, and will resonate at 7.1MHz
- At above 8.5MHz, the capacitor will present a low impedance, and RF would bypass the coil, making the antenna also resonate at 10MHz

I don't know the exact value of my loading coil. It was calculated around 18uH but I had to remove one turn to raise the frequency to 7.1MHz. 4NEC2 is happy with a 16uH loading coil (as shown by the previous SWR plot). So I calculated a LC network for 8.5MHz with a 16uH inductance. The resulting value is 21.9pF. Here's the plot of said LC network:

Definitely not good I did not find any capacitance values that will satisfy my requirements, so instead I used a coaxial trap calculator to calculate a 8.5MHz trap.

The problem with this is that the values seem to become extremely critical. When testing the different frequencies, the required inductance was within 2.8 to 3uH, and the capacitance between 120 and 130pf. Every picofarad matters, which makes me think thermal expansion effects will alter the trap.

Here's a SWR plot of the same antenna with a trap made with 3uH and 131pf, instead of the 16uH coil:

Definitely much more promising. Let's add a matching network with 4NEC2 and try to take the impedance to 50+0j:

The concept seems to be working, but the SWR bandwidth at the 7MHz section is extrmely narrow. Let's zoom in into the 7 MHz band:

We can see the 1.5 to 1.5 SWR bandwidth goes from 7.18 to 7.22MHz. Only 40KHz! This is unusable and most likely will shift wildly with weather, and will be a nightmare to tune. So to recap:

**Is it possible to replace my loading coil for a trap, and make my 7.2M vertical resonate both "naturally" (for the 30M band at 10.1MHz) and "loaded" (for the 40M band at 7.1MHz)?**

The lower portion of my vertical I'd prefer to stay 6M as not to cut the alu tubing (this is both radiator and structural support. The upper part I can shorten or extend as needed.

## Accepted answer (score 4, by Brian K1LI)

While your specific implementation will include numerous variables which are difficult to account for, I ran a NEC-2 model to illustrate the direction of a solution:

- Vertical element: 8.5-m tall 2-in diameter conductor, elevated 0.1-m above ground
- Radials: 8 x #14 wires, elevated 0.1-m above ground, that are $\frac{\lambda}{4}$-wave on 40m (10.5-m)
- Trap: 5uH in parallel with 50pF placed 85% of the way to the top of the conductor
- Ground: Sommerfeld-Norton model with "medium" conductivity (.005-S/m, $\epsilon_r$=13)

Varying any of these parameters will affect the driving point impedance. Here's a picture of the model:

This produces a 50-$\Omega$ SWR curve that should be a reasonable starting point for further optimization:

The resonant frequencies are:

- 7.375-MHz with 300-kHz of 2:1 SWR bandwidth
- 9.75-MHz with 250-kHz of 2:1 SWR bandwidth

Adding a broadband transformer to match 35-$\Omega$ improves the SWR:

I observed that increasing trap capacitance and reducing inductance tended to produce more SWR bandwidth on 40m, so the L/C ratio is an important parameter to vary as you search for your solution. You may well have to spend hours or days tuning your model and more hours or days tuning your implementation, but it's a time-honored solution.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16673/using-a-trap-out-of-its-resonance-frequency, by hjf, Brian K1LI. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
