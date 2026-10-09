# Receive directionality of a sub-optimal Yagi

*Tags: antenna-theory, yagi, direction-finding · score 4*

## Question

How do I build the best antenna for a given VHF frequency given that an optimal design is too large?

I am trying to understand the properties of a directional antenna of sub-optimal design. All the discussions of directional antennas assume optimally sized elements for a specific frequency. I need to design a directional antenna (Yagi) that is *as good as it can be* for a given VHF frequency (say 144 MHz)directional, but approximately 50% of the usual size. This is a receive-only, direction finding situation.

Obviously my antenna needs to be a good SWR match. I presume that it needs to be resonant at the target frequency, and I want to preserve as much efficiency and forward gain as possible. But the references I consult (ARRL Antenna Book, antenna-theory.com, RGSB publications) generally do not seem to approach the question from this direction.

## Answer (score 5, by Hamsterdave)

A few things to start off with:

1.

You don't care about efficiency, unless the antenna efficiency is truly abysmal, or your receiver is of very poor quality. Efficiency on the receive side is a measure of how effectively the antenna can couple with the ambient RF field and get that energy to the receiver. Even a receiver of very poor quality will have an extremely large dynamic range, 10s of decibels, and a circuit called an Automatic Gain Control, or AGC. The AGC's job is to increase the amplification in the receiver to make incoming signals strong enough to be effectively received. The AGC typically works by taking the strongest signal on a given frequency, and dialing up the gain until that signal has a specified amplitude at the receiver output. So long as the antenna is efficient enough to couple with the desired frequency sufficiently to bring in a signal that is above the receiver's internal noise floor, the receiver should be able to compensate. This is how a Beverage Receiving Antenna works. While they are highly directional, they are abysmally efficient, <1%, and peak gain can be as low as -20dBi because of this poor efficiency. The receiver compensates, however.

2.

You don't care about SWR, so long as it isn't incredibly high, like >20:1, for the same reason.

So, what you care about is **directionality**, which means how well it 'hears' in a given direction compared to how it hears in other or all directions. You *don't* care about **directivity**, meaning how well it hears in a given direction compared to an isotropic radiator.

With that out of the way, it might be easier to see where you can cut corners here. The physical aperture of the antenna, meaning it's size compared to the size of the wavelength it is receiving, is a big player in antenna efficiency, especially when you're trying to get seriously tiny. Since you don't care about efficiency nearly so much, you can sacrifice aperture and accept the reduction in overall gain and efficiency, in exchange for a small package and good directionality.

Depending on your design limitations, you might consider inductive loading of the yagi elements. Just like a dipole or monopole, a yagi can be shortened by adding capacitance or inductance to it's elements to make them electrically longer. You can google for "hamstick yagi" and see an example of this for HF using inductively loaded monopole antennas to create loaded dipole arrays.

In this case, the one thing you won't be able to reduce very much will be the optimal spacing between the elements. In a typical yagi, maximum front to back and front to side ratio is achieved with the antenna elements spaced out a certain amount, and best SWR is achieved at a different spacing. This is why many yagis use gamma matches or the like to achieve a good match at maximum gain. Since you don't care about the SWR, you should stick with the spacing that would give maximum front to back ratio.

You might also consider deviating from the typical yagi shape and use a design that still functions as a yagi, but has a smaller overall footprint. The SteppIR "trombone yagi", as seen here is an example of this. That design yields a roughly 50% reduction in element length, but with no reduction in boom length. Front to back and side rejection are slightly degraded, but not severely, generally <25% with careful design.

Another option would be to consider other directional antenna designs, which would yield a more compact overall package, but resulting in a more 3 dimensional shape.

Examples of this would include the Cubical Quad Array, Delta Loop Arrays, or a circular loop array. Like the yagi, however, they will not provide a dramatic reduction in boom length.

Finally there are antennas that work opposite the typical directional array. Rather than having high gain in one direction and low gain in all others, you can use an antenna with 'average' gain all the way around, but with a steep attenuating null in a single direction. Then, rather than trying to find what direction the signal is strongest in, you attempt to put the signal in the null of the antenna so it as weak as possible. These designs can be quite handy for DF work on strong local radiators that would otherwise overwhelm the receiver's AGC circuit. Small "magnetic" loop antennas exhibit this behavior (though they have 2 nulls), as can Moxon antennas when oriented vertically and relatively close to the ground (below 1 wavelength).

A magnetic loop in particular may work well for you, as they can be absolutely tiny, just 1/10th of a wavelength in circumference, on the desired frequency, however they can be quite tricky to design, particularly when they are electrically very small, and when they are operating above 50MHz.

"Small receiving array" and "Small directional receiving antenna" would be good terms to google for, as they should give you additional designs I didn't include above.

## Answer (score 3, by Phil Frost - W8II)

If a full-sized VHF antenna is too big, then look at how people do direction finding on HF. A longer wavelengh means bigger antennas, so HF direction finders have been dealing with the "too big" problem for a long time.

The canonical HF direction finding antenna is a small loop. This antenna is vertically polarized and gives two nulls when the plane of the loop is perpendicular to the source. The nulls are pretty sharp and deep. So instead of finding the direction where the signal strength is strongest, the operator finds the direction where the strength is weakest.

Here's a US Navy radio direction finder. Of course if you scale this down to VHF sizes and build it with modern electronics it will be much smaller.

See the source for many more examples.

Of course this gives two directions. One way to deal with this taking measurements from two locations and triangulating. In one direction the lines implied by the two measurements intersect, and that's where the source is. In the other direction the lines don't intersect so it doesn't matter.

Another solution to the two-direction problem is to add an omnidirectional antenna, making a phased array. The directionality of this array isn't great, but it's enough to figure out in which of the two directions is the source. You can see such a thing as the vertical rod on the right of the direction finder above.

If your source is horizontally polarized, a vertically polarized antenna won't work especially well. You'll still receive something, but it will be weaker. And much of what you receive will be reflections off objects that rotate the polarization, which will make localizing the source more difficult.

The solution is simple, albeit not obvious: use a dipole. Loops are historically more common because in the day they were developed, technology for high frequency radio didn't exist. Low frequencies propagate as ground waves, and ground waves work work much better in vertical polarization.

VHF doesn't propagate as ground waves so this isn't a problem. If your source is horizontally polarized then use a dipole (short, if you like) instead of a loop. The directionality is identical: only the polarization is different. The nulls are in the directions of the ends of the antenna.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6035/receive-directionality-of-a-sub-optimal-yagi, by dwitten, Hamsterdave, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
