# Fresnel zone

A **Fresnel zone** (English: /freɪˈnɛl/ *fray-NEL*), named after physicist Augustin-Jean Fresnel, is one of a series of confocal prolate ellipsoidal regions of space between and around a transmitter and a receiver. The size of the calculated Fresnel zone at any particular distance from the transmitter and receiver predicts whether obstructions or discontinuities along the path will cause significant interference.

### Background

The primary wave will travel in a relatively straight line from the transmitter to the receiver. Aberrant transmitted radio, sound, or light waves which are transmitted at the same time [can follow slightly different paths before reaching a receiver](Multipath%20propagation.md), especially if there are obstructions or deflecting objects between the two. The two waves can arrive at the receiver at slightly different times and the aberrant wave may arrive out of phase with the primary wave due to the different path lengths. Depending on the magnitude of the phase difference between the two waves, the waves can interfere constructively or destructively.

### Significance

In any wave-propagated transmission between a transmitter and receiver, some amount of the radiated wave propagates off-axis (not on the line-of-sight path between transmitter and receiver). This can then deflect off objects and then radiate to the receiver. However, the direct-path wave and the deflected-path wave may arrive out of phase, leading to destructive interference when the phase difference is half an odd integer ($${(2z+1)/2, z \in \mathbb Z}$$) multiple of the period. The n-th Fresnel zone is defined as the locus of points in 3D space such that a 2-segment path from the transmitter to the receiver that deflects off a point on that surface will be between n-1 and n half-wavelengths out of phase with the straight-line path. The boundaries of these zones will be ellipsoids with foci at the transmitter and receiver. In order to ensure limited interference, such transmission paths are designed with a certain clearance distance determined by a Fresnel-zone analysis.

The dependence on the interference on clearance is the cause of the picket-fencing effect when either the radio transmitter or receiver is moving, and the high and low signal strength zones are above and below the receiver's cut-off threshold. The extreme variations of signal strength at the receiver can cause interruptions in the communications link, or even prevent a signal from being received at all.

Fresnel zones are seen in optics, radio communications, electrodynamics, seismology, acoustics, gravitational radiation, and other situations involving the radiation of waves and [multipath propagation](Multipath%20propagation.md). Fresnel zone computations are used to anticipate obstacle clearances required when designing highly directive systems such as microwave parabolic antenna systems. Although intuitively, clear line-of-sight between transmitter and receiver may seem to be all that is required for a strong antenna system, but because of the complex nature of radio waves, obstructions within the first Fresnel zone can cause significant weakness, even if those obstructions are not blocking the apparent line-of-sight signal path. For this reason, it is valuable to do a calculation of the size of the 1st, or primary, Fresnel zone for a given antenna system. Doing this will enable the antenna installer to decide if an obstacle, such as a tree, is going to make a significant impact on signal strength. The rule of thumb is that the primary Fresnel zone would ideally be 80% clear of obstacles, but must be at least 60% clear.

### Spatial structure

Fresnel zones are confocal prolate ellipsoidal shaped regions in space (e.g. 1, 2, 3), centered around the line of the direct transmission path (path AB on the diagram). The first region includes the ellipsoidal space which the direct line-of-sight signal passes through. If a stray component of the transmitted signal bounces off an object within this region and then arrives at the receiving antenna, the phase shift will be something less than a quarter-length wave, or less than a 90º shift (path ACB on the diagram). The effect regarding phase-shift alone will be minimal. Therefore, this bounced signal can potentially result in having a positive impact on the receiver, as it is receiving a stronger signal than it would have without the deflection, and the additional signal will potentially be mostly in-phase. However, the positive attributes of this deflection also depends on the polarization of the signal relative to the object.

The second region surrounds the first region but excludes it. If a reflective object is located in the second region, the stray sine-wave which has bounced from this object and has been captured by the receiver will be shifted more than 90º but less than 270º because of the increased path length, and will potentially be received out-of-phase. Generally this is unfavorable. But again, this depends on polarization. Use of same circular polarization (e.g. right) in both ends, will eliminate odd number of reflections (including one).

The third region surrounds the second region and deflected waves captured by the receiver will have the same effect as a wave in the first region. That is, the sine wave will have shifted more than 270º but less than 450º (ideally it would be a 360º shift) and will therefore arrive at the receiver with the same shift as a signal might arrive from the first region. A wave deflected from this region has the potential to be shifted precisely one wavelength so that it is exactly in sync with the line-of-sight wave when it arrives at the receiving antenna.

If unobstructed and in a perfect environment, radio waves will travel in a straight line from the transmitter to the receiver. But if there are reflective surfaces that interact with a stray transmitted wave, such as bodies of water, smooth terrain, roof tops, sides of buildings, etc., the radio waves deflecting off those surfaces may arrive either out-of-phase or in-phase with the signals that travel directly to the receiver. Sometimes this results in the counter-intuitive finding that reducing the height of an antenna increases the signal-to-noise ratio at the receiver.

Although radio waves generally travel in a relative straight line, fog and even humidity can cause some of the signal in certain frequencies to scatter or bend before reaching the receiver. This means objects which are clear of the line of sight path will still potentially block parts of the signal. To maximize signal strength, one needs to minimize the effect of obstruction loss by removing obstacles from both the direct radio frequency [line of sight](Line-of-sight%20propagation.md) (RF LoS) line and also the area around it within the primary Fresnel zone. The strongest signals are on the direct line between transmitter and receiver and always lie in the first Fresnel zone.

In the early 19th century, French scientist Augustin-Jean Fresnel created a method to calculate where the zones are — that is, whether a given obstacle will cause mostly in-phase or mostly out-of-phase deflections between the transmitter and the receiver.

### Clearance calculation

The concept of Fresnel zone clearance may be used to analyze interference by obstacles near the path of a radio beam. The first zone must be kept largely free from obstructions to avoid interfering with the radio reception. However, some obstruction of the Fresnel zones can often be tolerated. As a rule of thumb the maximum obstruction allowable is 40%, but the recommended obstruction is 20% or less.

For establishing Fresnel zones, first determine the RF line of sight (RF LoS), which in simple terms is a straight line between the transmitting and receiving antennas. Now the zone surrounding the RF LoS is said to be the Fresnel zone. The cross sectional radius of each Fresnel zone is the longest at the midpoint of the RF LoS, shrinking to a point at each vertex, behind the antennas.

#### Formulation

Consider an arbitrary point *P* in the LoS, at a distance $$d_1$$ and $$d_2$$ with respect to each of the two antennas. To obtain the radius $$r_n$$ of zone $$n$$, note that the volume of the zone is delimited by all points for which the difference in distances, between the reflected wave ($$\overline{AP} + \overline{PB}$$) and the direct wave ($$D=d_1+d_2$$) is the constant $$n\frac{\lambda}{2}$$ (multiples of half a wavelength). This effectively defines an ellipsoid with the major axis along $$\overline{AB}$$ and foci at the antennas (points A and B). So:

$$
\overline{AP} + \overline{PB} - D = n\frac{\lambda}{2}
$$

Re-writing the expression with the coordinates of point $$P$$ and the distance between antennas $$D$$, it gives:

$$
\sqrt{d_1^2+r_n^2}+\sqrt{d_2^2+r_n^2}-(d_1+d_2)=n\frac{\lambda}{2}
$$

$$
d_1\left(\sqrt{1+r_n^2/d_1^2}-1\right)+d_2\left(\sqrt{1+r_n^2/d_2^2}-1\right)=n\frac{\lambda}{2}
$$

Assuming the distances between the antennas and the point $$P$$ are much larger than the radius and applying the binomial approximation for the square root, $$\sqrt{1+x} \approx 1+x/2$$ (for *x*≪1), the expression simplifies to:

$$
\frac{r_n^2}{2}\left(\frac{1}{d_1}+\frac{1}{d_2}\right)\approx n\frac{\lambda}{2}
$$

which can be solved for $$r_n$$:

$$
r_n\approx\sqrt{n\frac{d_1\ d_2}{D}\lambda},\quad d_1, d_2 \gg n\lambda,
$$

For a satellite-to-Earth link, it further simplifies to:

$$
r_n\approx \sqrt{n d_1 \lambda},\quad d_1 \gg n\lambda,\quad d_2\approx D
$$

Extended content

Note that when $$d_1=0$$ or $$d_2=0\implies r_n=0$$, which implies that the foci seem to coincide with the vertices of the ellipsoid. This is not correct and it's a consequence of the approximation made.

Setting the point $$P$$ to one of the vertices (behind an antenna), it's possible to obtain the error $$\epsilon$$ of this approximation:

$$
\epsilon + \left(\epsilon+D\right) - D = n\frac{\lambda}{2}\implies\epsilon=n\frac{\lambda}{4}
$$

Since the distance between antennas is generally tens of km and $$\lambda$$ of the order of cm, the error is negligible for a graphical representation.

On the other hand, considering the clearance at the left-hand antenna, with $$d_1=0, d_2=D$$, and applying the binomial approximation only at the right-hand antenna, we find:

$$
\left(\sqrt{d_1^2+r_n^2}-d_1\right)+0.5 r_n^2/d_2=0.5 n \lambda
$$

$$
r_n +0.5 r_n^2/D=0.5 n \lambda
$$

The quadratic polynomial roots are:

$$
r_n=D\left(-1 \pm \sqrt{1+n\lambda/D}\right)
$$

Applying the binomial approximation one last time, we finally find:

$$
r_n=0.5n\lambda,\quad d_1=0
$$

So, there should be at least half a wavelength of clearance at the antenna in the direction perpendicular to the line of sight. The vertical clearance at the antenna in a slant direction inclined at an altitude angle *a* would be:

$$
v_n=r_n \sec(a).
$$

#### Maximum clearance

For practical applications, it is often useful to know the maximum radius of the first Fresnel zone. Using $$n = 1$$, $$d_1 = d_2 = D/2$$, and $$\lambda = c/f$$ in the above formula gives

$$
F_1 = {1 \over 2} \sqrt{\lambda D} = {1 \over 2} \sqrt{c D \over f},
$$

where  
$$D$$ is the distance between the two antennas,  
$$f$$ is the frequency of the transmitted signal,  
$$c$$ ≈ 2.997×10 m/s is the speed of light in the air.

Substitution of the numeric value for $$c$$ followed by a unit conversion results in an easy way to calculate the radius of the first Fresnel zone $$F_1$$, knowing the distance between the two antennas $$D$$ and the frequency of the transmitted signal $$f$$:

- $$F_1 \mathrm{[m]} = 8.656 \sqrt{D \mathrm{[km]} \over f \mathrm{[GHz]}}$$
- $$F_1 \mathrm{[ft]}= 36.03 \sqrt{D \mathrm{[mi]} \over f \mathrm{[GHz]}}$$

---

*Source: Wikipedia, Fresnel zone (https://en.wikipedia.org/wiki/Fresnel_zone), by Wikipedia contributors, CC BY-SA 4.0.*
