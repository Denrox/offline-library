# Can I use a helical ground plane radial in the same way that a loading coil works?

*Tags: antenna, antenna-theory, antenna-construction, wire-antenna · score 8*

## Question

I'm working out the science behind mounting an antenna on a vehicle, and I came across the concept of ground planes. [This answer](How%20to%20calculate%20or%20estimate%20surface%20area%20of%20required%20ground%20plane%20for%20a%20mobile%20antenna.md) says that longer is better but don't worry about it too much, but this article focuses on 1/4 wave ground planes, as do most other articles and products. I'll be mounting a monopole whip antenna like this one.

Can I use a coil for a radial to get a linearly shorter wire and still make a good ground plane? Rubber ducky antennas do this for the main antenna, but I'm interested in using the concept for the ground plane radials. This antenna will primarily be for transmitting on VHF and UHF frequencies, but will receive on many others.

This antenna will be mounted on a tailgate / tire rack, and while there is some room for radials or a sheet of metal for a ground plane or radial, there isn't much more than a foot or so, possibly less. Some directions will have more room than others: the back moreso than in between the tailgates, for example.

I don't want you to get distracted with my particular mounting setup, but here's where I'm planning on mounting it, which is a Smittybilt Atlas bumper and tire carrier. Jeep images are random from a DDG search. There will be some kind of interference with the tire carrier top tube, but I was hoping to mitigate that with a good ground plane. I will cover the tube with some kind of non-conductive material in case the antenna ever makes contact there while I am transmitting.

**NOTE:** The black part is a bolt. The Antenna is mounted on a small piece of angle iron in an L shape. My first idea was to put a piece of sheet metal as a ground plane perpendicular to the antenna, but when I started looking into ground planes, realized that often they use radials instead.

## Answer (score 2, by Cecil - W5DXP)

If all you want to do is achieve a resonant feedpoint impedance, one spiral radial will come close, by acting as a counterpoise. I don't know where the radiation from a single spiral radial would go. If you want to prevent the radials from radiating, the usual method is to use N times two identical horizontal radials pointing in opposite directions. Since the identical currents in each two identical radials are flowing in opposite directions, their horizontal far fields tend to cancel. It seems logical to assume that two identical opposing horizontal spiral radials would not radiate much.

## Answer (score 2, by Glenn W9IQ)

The so called ground plane is there primarily to help feed the antenna in a predictable, controlled manner. In the absence of the ground plane, the coax cable becomes part of the antenna which has an effect on the radiation pattern; the impedance and therefore the SWR; and the efficiency and therefore the gain. As the ground plane design is compromised from "ideal", some of these factors come into play.

As a simple example of the effect of the ground plane, consider that an ideal quarter wave VHF or UHF vertical antenna has an impedance of ~34 ohms. In order to better match this to 50 ohm coax, a common technique is to bend down the ground plane radials so they are 45 degrees below horizontal. While this provides a better match, it also alters the radiation pattern of the antenna - moving it closer to the pattern of a 1/2 wave vertical dipole. The result is that some of the transmitted power is wasted as it is directed below the horizon of the base of the antenna towards the ground.

The best advice for your situation is to simply try your ground plane options to see how they work for you. Try to keep the ground plane in symmetry. Ideally you should test the SWR of the antenna with a more optimum ground plane and then with your compromised ground plane in order to compare SWR and signal strength results. Keep in mind that the radiation pattern of the antenna may be altered by the location of the antenna as well as the compromised ground plane.

[EDIT]

Based on the diagram that you added, a radial (wire) radial system will work for your installation. You will have some issues with directivity due to the metal in the tailgate. It would be better if you could elevate the base of the antenna so that it is even with the lower edge of the rear glass. The roll bar will still interfere with the pattern but it will be better in general.

On my Jeep (YJ Wrangler) I use a lip mount bracket on the front hood positioned on the opposite side of the AM/FM broadcast antenna. The hood and front quarter panel provide a reasonable, albeit asymmetric, ground plane.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12396/can-i-use-a-helical-ground-plane-radial-in-the-same-way-that-a-loading-coil-wo, by YetAnotherRandomUser, Cecil - W5DXP, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
