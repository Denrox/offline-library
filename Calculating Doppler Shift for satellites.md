# Calculating Doppler Shift for satellites

*Tags: satellites, doppler · score 11*

## Question

If I know how fast a satellite is moving through space, how can I calculate the doppler shift for the pass?

## Accepted answer (score 8, by Joao Encarnacao)

The doppler shift $\Delta f$ is function of the relative velocity $\Delta v$ (a scalar quantity) and the emitted frequency $f_0$, see the relevant wikipedia page.

If you know how the relative velocity (either at one instant in time or as a function of time), it's just a matter of using the formula:

If you don't known the relative velocity, then you need to calculate it. For that you need the ingredients Adam Davis KD8OAS enumerated in his comment.

You need much more than the speed to find this. The orbital elements of a satellite, your location, and the time and date, plugged into a satellite tracking program will do the work for you. Doing it by hand may be interesting, once, but it isn't trivial.

Note that usually we measure $\Delta f$ with a radio, an SDR and an accurate clock, compute $\Delta v$ and then try to figure out the satellites' orbit by guessing which one fits best the observed $\Delta v$.

## Answer (score 3, by KillaKem)

I want to add to and correct the previous answer.

The velocity $v$ is a **vector quantity**, the scalar quantity is the magnitude of $v$ which is the speed.Also note that the equation is commonly simplified to:

$$ \Delta f = \frac{\Delta v}{c} f_{carrier} = \frac{\Delta v}{\lambda} = \frac{|| \Delta v|| }{\lambda} \cos \theta = f_m \cos \theta $$

where $\theta$ is the angle of arrival at the transmitter, $f_m$ is the maximum doppler shift (commonly called the doppler spread) and ||$v$|| is the scalar speed the receiver is traveling relative to a stationary transmitter (or vice versa).

The equation shows that $\Delta f$ will vary from $-f_m$ to +$f_m$ as $\theta$ varies making the received frequency vary (this is called frequency dispersion) and contributing to fast fading. If the only thing you know is the speed the satellite is travelling then all you can calculate is $f_m$ which the worst case scenario for $\Delta f$ so if your system is resistant to frequency shifts of up to $f_m$ then your system will operate well.

## Answer (score 3, by Phil Karn)

To obtain the Doppler shift you need to know the actual emitted frequency and the *range rate* (the first derivative of range, the distance between you and the satellite).

To compute the range rate you need two 3D vector quantities: the satellite's position **P** and velocity **V** relative to you. The range rate is then given by the dot product of **P** and **V** divided by the magnitude of **P**. The vector **P** divided by its magnitude is the *unit position vector*, so what you're really computing is that component of spacecraft velocity along the direction to you; how fast it moves perpendicular to that direction doesn't really matter.

Although most satellite programs seem to compute range rate by finite differencing range, it can be computed analytically for more precise results. Standard orbit models like SGP produce velocity as well as position as functions of time, and it is also fairly straightforward to compute the position and velocity of a ground station on the rotating earth in inertial space.

Note: this discussion ignores relativistic effects. At relativistic speeds, there will be an additional red shift (downward Doppler shift) due to time dilation making the spacecraft oscillator appear to run more slowly. For details, see the Wikipedia article on the Relativistic Doppler Effect.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1509/calculating-doppler-shift-for-satellites, by Skyler 440, Joao Encarnacao, KillaKem, Phil Karn. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
