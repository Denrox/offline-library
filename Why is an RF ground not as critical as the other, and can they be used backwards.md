# Why is an RF ground not as critical as the other, and can they be used backwards?

*Tags: grounding · score 9*

## Question

I will give the magmount antenna as an example:

The vertical element to the antenna is very critical, cut to a certain wavelength, often added with some loading coils, or a little spiral to make everything perfect for the specific frequency.

The other part of the antenna is a random car, just a chunk of metal.

On a dipole, both elements are equally important, both acting together to make the antenna.

Why on the magmount, and other antennas like AM towers is the ground or counterpoise not as important?

Can this be switched around, lets say I used the center coax as the RF ground, and the exterior coax as the vertical element, would this work equivalently?

## Answer (score 4, by Phil Frost - W8II)

Why on the magmount, and other antennas like AM towers is the ground or counterpoise not as important?

It *is* important. For example, if you try to put a magmount on a fiberglass car, it won't work very well. It won't work well on a bicycle, either.

For the ground plane (roof of car, radials under antenna, etc) to work well, it must approximate an infinite plane of perfectly conductive material. Of course, we don't have infinitely conductive materials, but any reasonably conductive metal is a good enough approximation.

We also don't have infinite planes. However, as the distance away from the feedpoint increases, the electric and magnetic field strengths decrease. Rule of thumb: the ground plane should extend at least a quarter-wavelength in all directions. Beyond this distance there isn't much current or voltage, so the ground plane becomes less significant. You can extend it farther if you want, but you get diminishing returns in efficiency and only small changes to antenna parameters like feedpoint impedance and resonant frequency.

Can this be switched around, lets say I used the center coax as the RF ground, and the exterior coax as the vertical element, would this work equivalently?

Yes and no, depending on the details of the situation. Voltage is a relative measurement between two points, and electrically what we choose to call "ground" is arbitrary.

In the case of a magmount antenna on a car, were you to switch the center and shield connections, nothing much changes. The vertical element still oscillates at an AC voltage relative to the body of the car, which is the other half of the antenna. However, this mostly works because the car is floating. It runs on a battery and is on insulating tires, and is not connected to anything else except through some small, mostly negligible capacitance.

If you were to try this at a station where the ground plane is not a floating car body but rather radials firmly connected to Earth, then maybe bad things would happen, depending on how things are connected. For example, it's common to have the chassis connected to Earth. If you flip the shield and center connections where the radio meets the feedline you have a problem: the chassis of the radio is connected to Earth, and the center pin on the radio's antenna connector is also connected to Earth (because it's connected to the shield of the feedline, which goes to the antenna's radials). Thus, the thing between your radio's output isn't the antenna, but two points on the ground. Probably not what you wanted.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1819/why-is-an-rf-ground-not-as-critical-as-the-other-and-can-they-be-used-backward, by Skyler 440, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
