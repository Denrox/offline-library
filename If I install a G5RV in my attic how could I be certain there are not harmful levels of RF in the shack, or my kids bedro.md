# If I install a G5RV in my attic how could I be certain there are not harmful levels of RF in the shack, or my kids bedroom?

*Tags: antenna, safety · score 15*

## Question

I assume that anyone who has a G5RV or G5RV junior in their attic has done so with ceramic spacers, and has zigzag or dog-leg installations, or otherwise has contorted the antenna to fit up there.

My worry is how can I satisfy my own and my XYL (wife)'s concerns about RF in our house, especially in the bedrooms immediately below the attic, where all of us sleep?

What do I need to know, and what do I need to measure to know if any harmful RF levels would exist in the area 12 feet below the attic?

Assuming that other questions here cover using radios or Oscilliscopes to measure and observe decreases in RF in the shack, how can I establish reasonably easily that levels not more than 1/10th of the level that could cause harm, are present in my house?

For example, if high levels can cause GFCI breakers in my outlets to trip, how high would such levels be, compared to the levels that could cause damage to people? Is there any way to know?

## Accepted answer (score 14, by Phil Frost - W8II)

If you want to be *certain*, you will need calibrated electric and magnetic field probes and a spectrum analyzer. If you had that equipment, I doubt you would ask this question, so let's assume you *don't* have it, and you don't care to drop thousands of dollars to get it. How can you be *pretty sure* that exposure is safe, without expensive test equipment?

First we have to define *safe*. Since this forum is about Amateur Radio, and not medical research, let's use the FCC's definition of safe.

The FCC has determined that amateur operators need not give any special consideration to RF safety if the transmitter power is below a certain level. At these relatively low transmitter powers, it's just really hard to encounter a dangerous field, no matter how close you get. The ARRL gives a full table, but all bands 15m and below are good at 100W PEP or less (limits are even higher on lower bands). The limit for 12m is 75W, and 10m is 50W PEP. That covers the usual operating range for a G5RV.

If you exceed those limits, you may very will still be safe, but you have to do some analysis. Here's a simple way to do it: the maximum power density for 3MHz to 30MHz is 180mW per square centimeter, divided by the frequency in MHz squared.

We can estimate the power density by making some simplifying assumptions. If we leave a big margin, we can still be pretty sure we are within safe limits despite our gross simplifications. First, let's assume that power is radiated equally along the antenna's length, and that you are close enough that we should consider it as a line source, not a point source. If you put 100W into it, then for any cylinder centered on that antenna, there is 100W passing through it.

The half-size G5RV, being smaller, will have higher power density. It's 15.5m long. Let's say you are 3m away from it, and you are feeding it with 100W. The area of a cylinder (without the ends) 15.5m in length and 3m in radius is:

$$ 2 \pi \cdot 3\mathrm m \cdot 15.5m = 292 \mathrm m^2 $$

Your 100W of transmitter power is spread over this cylinder, so the power density is:

$$ \require{cancel} \frac{100\cancel{\mathrm W}}{292 \cancel{\mathrm m^2}} \frac{1 \cancel{\mathrm m}}{100 \mathrm{cm}} \frac{1 \cancel{\mathrm m}}{100 \mathrm{cm}} \frac{1000\mathrm{mW}}{1\cancel{\mathrm W}} = 0.0342 \mathrm{mW}/\mathrm{cm} $$

Let's call the top end of 10m an even 30MHz. The maximum safe power density is:

$$ \frac{180}{30^2} = 0.2\mathrm{mW}/\mathrm{cm}^2 $$

So, you are 7.6dB below the FCC limit for uncontrolled exposure. I'd call it safe.

Remember that this is a gross simplification. Factors that make our estimation less safe include:

- power isn't actually radiated equally all over the antenna. There will be hot spots, and cold spots.
- with the antenna in your attic, you aren't even in the far field of the antenna. Calculating the actual fields is really hard.
- ground reflections, and also any wiring in your house, may reflect, distort, or focus the field, making more hot spots.

Factors that provide additional safety margin to our estimate include:

- the antenna doesn't radiate like the worst-case cylinder: some power goes towards the sides also.
- exposure limits are higher for lower frequencies (at 7 MHz: 3.6 milliwatt per square centimeter).
- SSB power is usually measured in PEP, while exposure limits are set by average power over 30 minutes. SSB has a duty cycle around 20%.
- Regardless of the mode you use, you probably don't transmit all the time, further reducing duty cycle.

## Answer (score 3, by imabug)

The ARRL RF Exposure page has a lot of useful resources. It has links to a number of articles and external websites that provide some good info. If you happen to have a copy of the ARRL Handbook, the Safety chapter has a section that covers RF safety.

Between 1.34-30MHz, the FCC maximum permissible exposure (uncontrolled exposures/general population) for power density is 180/f mW/cm and 0.2 mW/cm between 30-300 MHz, where f is the frequency in MHz.

As for measuring the field strengths, it's probably not something you'll be able to do yourself without some specialized equipment. There are companies that can do this for you, but if you're not running more than 100 W, it's probably not worth the expense. This RF safety calculator looks like it would be useful to see how close you might be to any limits.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1524/if-i-install-a-g5rv-in-my-attic-how-could-i-be-certain-there-are-not-harmful-l, by Warren  VA7WPX, Phil Frost - W8II, imabug. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
