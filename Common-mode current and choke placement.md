# Common-mode current and choke placement

*Tags: antenna-theory · score 6*

## Question

Why are chokes usually placed at the feedpoint, can't common-mode currents occur below the choke as well?

I understand it's placed at the feedpoint to keep everything balanced by eliminating common-mode currents on the outside of the shield, but i thought they can occur below the choke too (unless i've misunderstood?)

For the purposes of this discussion let's assume the antenna is a dipole and is fed by coax.

Thanks :)

## Accepted answer (score 2, by user10489)

Common mode current occurs due to coupling between the antenna and the coax shield, so if you place the choke at the feedpoint, you break the circuit and most of the common mode current will be blocked. (The circuit is from the antenna, though the coax, and back to the antenna via RF.) You shouldn't get any significant amount of common mode current further down the coax.

However, nothing is perfect, and some common mode current may leak past the choke, especially if it is at a nodal point. If this is the case, placement of a second choke somewhat further down the line (say, 1/8 wavelength velocity factor corrected) may hit a maximum and block more current.

Alternately, if you don't place a balun at the feedpoint, then the coax between the balun and the antenna can become part of the antenna and will radiate. If that length of coax is resonant (say, 1/4 wavelength), then this will have minimal impact on SWR shouldn't cause more common mode current past the balun. It will, however, change your radiation pattern, which could increase or decrease your gain, depending on the direction of interest. This is one way to soften the directionality of a beam where you want to get some omnidirectional radiation, or even add a band to an antenna. (For example, the carolina windom uses a 1/4 wavelength of coax with a choke for 10m.)

Placement of a choke at the transmitter might also help, but it only helps common mode from getting into the transmitter -- it may still be on the coax.

There are two primary reasons why we care about common mode current at all. First, common mode current on the coax in the shack is dangerous -- it means you are radiating in the shack, but also you could get RF burns from touching surfaces carrying that common mode current. Secondly, common mode current sourced from the feedpoint is power that is not going into the antenna, and may be radiating in directions we don't want and causing high swr. Other sources of common mode current should be negligible and inconsequential.

## Answer (score 6, by Phil Frost - W8II)

You are right that common-mode currents can occur elsewhere. A common-mode choke with an ideal infinite impedance essentially "disconnects" the common-mode of the feedline, but common-mode currents can still find their way onto the feedline through mutual coupling through the electromagnetic field.

Fortunately, in most antenna and feedline arrangements this coupling isn't very strong. For example, a dipole is usually symmetrical around the feedline's axis. In this arrangement, there is no electric field along the axis of the feedline, and so there is no coupling. For a monopole, the feedline exits below the ground plane and is thus "hidden" from the antenna fields.

Of course real-world installations are always a little bit away from these ideals, and thus there might be a little coupling between the antenna fields and the feedline common-mode. But in most cases this coupling is negligible.

In cases where it's not negligible, it's certainly possible to install additional chokes on the feedline to break it into segments that won't couple as effectively. This just isn't common practice since it's not a common problem.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16798/common-mode-current-and-choke-placement, by t252, user10489, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
