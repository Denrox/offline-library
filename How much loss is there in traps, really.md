# How much loss is there in traps, really?

*Tags: antenna · score 4*

## Question

I searched and couldn't find a direct answer so thought I'd ask.

We all know the mantra "traps aren't good as they have losses", but how much loss are we talking about, really?

Am I correct in understanding it is mainly (only?) resistive losses by having more metal to travel through?

I'm guessing there's more to it.

Thanks.

## Accepted answer (score 8, by Phil Frost - W8II)

W8JI has some measurements, and the worst case loss he found for two traps in a dipole was 1.6 dB. These were coaxial traps, operated at their resonant frequency, which is both the worst way to tune a trap, and the worst kind of trap.

The losses are indeed mostly resistive losses, but not just because there is more metal. Losses are highest at resonance because this is where current in the trap is at a maximum. The current circulating in the trap at resonance is much higher than it would be if there were no trap. Since resistive losses are proportional to the square of current, this makes a big difference.

As such, it's a good idea to move the resonant frequency a little out of the band. This will reduce current and consequently loss in the trap significantly while still providing sufficient impedance for the trap to be effective.

Far away from resonance, the trap is effectively a loading coil. Current isn't very high and so losses in the trap itself are negligible, however the shortening of the antenna reduces radiation resistance and thus makes all the other losses in the antenna system more significant. More traps for more bands means more shortening and less efficiency.

It's hard to say generally just how much loss this ends up being: I'd bet in most situations ground losses are the most significant source of loss, and that can vary quite a bit between local ground conductivity, antenna height (for dipoles), and radials installation (for monopoles).

## Answer (score 2, by Scott Earle)

A trap is usually a notch filter, designed to stop frequencies within a certain band from passing. The theory is that if you have a wire dipole that is electrically tuned for 20m, and then you put a pair of traps in there to ‘cut the antenna short’ when a signal at 21MHz is presented, you can effectively have an antenna that is resonant on 20m and 15m.

This cutting short is achieved by having a small LC circuit (inductance and capacitance) that acts as a notch at 15m.

But in order for this to work, the trap needs to have zero impedance at 20m, and infinite impedance at 15m. Of course this is not the case, and so adding the trap affects the overall properties of the dipole. Usually, this means that when the traps are added, the wire dipole needs to be shortened to make it resonant on 20m again. A multi band antenna with traps for 10m, 12m, 15m, 20m and 30m will still work on 40m, it will just not be as effective as a 40m dipole.

This is all to say that there can be losses of a few dB in an antenna with multiple traps when it is used on its lowest bands.

A trap antenna is (as usual with all multi band antennas!) basically a compromise. In an ideal world we would all have the means to put up a resonant antenna for every band we would like to work, but this is not an ideal world.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16984/how-much-loss-is-there-in-traps-really, by t252, Phil Frost - W8II, Scott Earle. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
