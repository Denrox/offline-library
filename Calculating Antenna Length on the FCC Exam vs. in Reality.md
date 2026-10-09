# Calculating Antenna Length on the FCC Exam vs. in Reality

*Tags: antenna, united-states, antenna-theory, math, physics · score 14*

## Question

I have seen the following formulas for calculating half and quarter wavelength antennas:

Formula for $\frac{1}{2}$-wavelength antenna (in free space):

\begin{equation} \mathrm{Length~(feet)} = \frac{492}{f_{MHz}} \end{equation}

*Or is it...*

\begin{equation} \mathrm{Length~(feet)} = \frac{468}{f_{MHz}} \end{equation}

Formula for $\frac{1}{4}$-wavelength antenna (in free space):

\begin{equation} \mathrm{Length~(feet)} = \frac{246}{f_{MHz}} \end{equation}

*Or is it...*

\begin{equation} \mathrm{Length~(feet)} = \frac{234}{f_{MHz}} \end{equation}

Or is it none of the above? I believe the US FCC Technician class exam requires the use of 468/f. Are any of these equations helpful in calculating antenna length in reality, or is this only in theory for the exam?

What additional factors should be taken into account, if any? What would be a better equation if none of the above?

## Accepted answer (score 20, by Walter Underwood K6WRU)

The $492/f$ formula is for an ideal antenna in free space, the $468/f$ is an estimate for real antennas at a reasonable height over ground.

The $492/f$ formula is a conversion from metric units to English units for the fundamental frequency and wavelength ($\lambda$) formula. $c = 3\times 10^8_{m/s}$ (the velocity of light) and $f =$ frequency --

\begin{equation} \lambda = \frac{c}{f} \end{equation}

This gives the length of a full wavelength in meters. This formula is correct if the conductor is infinitely thin and other objects are infinitely far away from the antenna.

The length of a real, installed antenna is affected by the diameter of the conductor (not a big effect for wire antennas) and the height above ground (a big effect). Capacitance to ground electrically shortens the antenna, so less wire is needed for resonance.

$468/f$ is a good estimate for wire antennas at HF less than a wavelength above ground. This is an empirical formula, so there is no mathematical derivation. The $468/f$ formula was first published in the 1929 *ARRL Handbook*. It is probably based on experience with 40m and 80m antennas at heights of 1/4 to 1/8 wavelength above ground, since those were common antennas at the time.

A November 2009 *QST* article by Ward Silver, N0AX, measured a 20m dipole at heights from 1/8 to 2 wavelengths and found the length varied from $466/f$ to $481/f$ depending on height. He recommends starting with a wire length of $490/f$ and expecting to shorten the antenna to resonance.

Most wire antennas need length adjustment for resonance after installation, because of the capacitance to nearby structures or trees, or local ground conductivity. It is much easier to shorten an antenna than to lengthen it, so it is a good idea to cut the antenna wire a little long.

For more on this publication history of this formula, see this article by N0AX.

For more information about wire antennas, I would start with Chapter 21 of the *ARRL Handbook*. For details, read the *ARRL Antenna Book*.

## Answer (score 6, by PearsonArtPhoto)

For someone who knows how to convert between inches, feet, and meters, it's really quite simple. You only really need to know one formula to do it all, and that formula is $300=f\times wavelength$. If you find the wavelength for the given frequency, then just find the type of antenna (quarter-wave), take the appropriate fraction of the wavelength, and convert said quantity to the appropriate units. For example, the wavelength for a 146 MHz signal is 2.05 m, multiply by 39 and you have 80 inches. If you want a quarter wave whip, then your antenna is 20 inches long.

As to where this applies after the test, it does apply, but there is one huge catch. The antenna needs to have the provided wavelengths electrically, not physically. What does that mean? Basically, there's a quantity known as Velocity Factor which takes into account how fast the waves move in the metal. However, most metals have a permittivity of about 1, making the electric distance equal to the physical distance. Some non-metal antenna materials could be different, however, so be warned. Also, cable is different, etc. Essentially, if the velocity factor of an antenna is 2, then an antenna could be made with half of the length and still be resonant. However, as the velocity factor for most metals is 1, and there are other reasons to use metal as antenna building material, this isn't usually a significant factor. It does make a small difference in certain types of phased antennas, however.

As to your specific question, the half-wave formula is $(3.28/2)(300/f)$, or $492/f$, and the quarter wave is similarly $(3.28/4)(300/f)$ or $246/f$. This applies if the velocity factor is 1, which only holds true if the antenna is far away from conductive surfaces, including the ground. The distance required is at least 1 wavelength away typically.

## Answer (score 3, by Dan)

**Legend**

- $c$ = velocity of propogation = speed of light (299,792,458 meters/second)
- $f$ = frequency
- $\lambda $ = wavelength

**Formulas**

The basic formula for calculating wavelength is:

\begin{equation} \lambda = \frac{c}{f} \end{equation}

To make the math simpler, frequency ($f$) is expressed in megahertz (MHz) and the velocity of propogation in free space ($c$) for frequencies above 30 MHz is expressed as and rounded to 300 megameters (Mm). This will return a wavelength ($\lambda$) in meters. So for 1 wavelength *above* 30 MHz:

\begin{equation} \lambda_{m} = \frac{300}{f_{MHz}} \end{equation}

However, when $f < 30_{MHz}$, the velocity of propogation ($c$) is expressed as and rounded to 286 Mm because

"[e]lectrical wave propagation in wire is about 95% to 97% the speed of light. Since wavelength is most commonly used for building antennas which involve conducting the wave from air into the wire and vice versa, the calculation is adjusted assuming the slower propagation in an unshielded conductor.

"However, this 3% to 5% discrepancy is small enough at frequencies above 30 MHz that it is usually ignored for simplicity, and 300 Mm is used instead" ([Adam Davis, KD8OAS](Why%20is%20the%20speed%20of%20light%20rounded%20to%20286%20Mm%20in%20calculations%20involving%20frequencies%20below%2030MHz.md)).

When $f < 30_{MHz}$ the discrepancy becomes more significant and the adjusted value, approximately 95% of 300 Mm, is used instead, which is approximately 286Mm (which would actually be $0.95\overline{3}$). This results in the following formula for 1 wavelength *below* 30 MHz:

\begin{equation} \lambda_{m} = \frac{286}{f_{MHz}} \end{equation}

To convert this into feet, multiply $c$ by 3.28084, which results in the following formula for receiving an answer in feet when $f > 30_{MHz}$:

\begin{equation} \lambda_{ft} = \frac{(3.28084)300}{f_{MHz}} = \frac{984.252}{f_{MHz}} \end{equation}

This is rounded down to $984/f$ for the sake of simplicity. However, recall that when $f < 30_{MHz}$, the velocity of propogation ($c$) is expressed as and rounded to 286 Mm. Applying this formula results in the following for converting this into feet *below* 30 MHz:

\begin{equation} \lambda_{ft} = \frac{(3.28084)286}{f_{MHz}} = \frac{938.32024}{f_{MHz}} \end{equation}

This is also rounded down to $938/f$ for the sake of simplicity.

Calculating for half and quarter waves is just a manner of of dividing $c/2$ or $c/4$, respectively. So we end up with the following calculation for calculating the length of half wave antennas in feet when $f > 30_{MHz}$:

\begin{equation} \lambda_{ft} = \frac{(3.28084)(300/2)}{f_{MHz}} = \frac{492.126}{f_{MHz}} \end{equation}

When calculating the length of half wave antennas in feet where $f < 30_{MHz}$, we have the following formula:

\begin{equation} \lambda_{ft} = \frac{(3.28084)(286/2)}{f_{MHz}} = \frac{469.16012}{f_{MHz}} \end{equation}

But this is generally expressed as $468/f$, not as 469. Why is this? First of all, remember that the velocity factor is *approximately* 95-97% of the speed of light, so adjusting this value results in slightly different results. Also, whether we use the adjusted value of $c$ when $f < 30_{MHz}$ (286 Mm) or apply the velocity factor directly to $c$ will slightly alter our result. So for instance, the following calculation will get us closer to $468/f$:

\begin{equation} \lambda_{ft} = \frac{(3.28084)((300/2)(0.95))}{f_{MHz}} = \frac{467.5197}{f_{MHz}} \end{equation}

This would round up easily to $468/f$ when $f < 30_{MHz}$, and it is slightly more accurate.

This shows why there are different equations and when each should be used.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/283/calculating-antenna-length-on-the-fcc-exam-vs-in-reality, by Dan, Walter Underwood K6WRU, PearsonArtPhoto. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
