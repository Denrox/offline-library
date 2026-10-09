# Why don't J-Poles need to be grounded?

*Tags: antenna, antenna-construction, j-pole · score 5*

## Question

I'm building my first J-Pole and the different projects and articles I read about differ slightly but one commonility is a J-Pole does not need to be grounded. Why is that?

I read that it is optional to ground the J-Pole antenna to deal against lightning strikes but does not add benefit to the quality of transmission.

Please feel free to correct my current knowledge or add what you do for your J-Pole as I am a newbie to building these. Thanks!

## Accepted answer (score 3, by T.Bren)

The ground you are referring to is a slight misunderstanding. True, some antennas require a ground to function correctly but the reason for that is the ground is the other half of the antenna, such as a marconi or ground mounted vertical, the ground is the other half of the 1/4 wave vertical.

Horizontal dipoles don't require a 'ground' because both 1/4 wave sections are already there and there is no need for any more connections to make an antenna.

A J-pole is a end-fed vertical which is already 1/2 wavelength long (or longer) with a matching stub at the bottom to meet SWR requirements for the coax. No ground is required because it's 1/2 wave or longer to start with. You can ground a J-pole for lightning protection simply by mounting it to a metal grounded mast.

A basic law of almost all antennas is that they form a complete circuit, that is, a minimum of an electrical 1/2 wavelength to be efficient. A dipole meets this by using 2 quarter wave sections joined in the middle. Most car antennas require the metal body of the car to complete the other half of the antenna to complete a full 1/2 wave.

The loop antenna is an exception to this rule as its a complete circuit tuned to a particular frequency. There are others too. But most people use antennas based upon 1/2 wavelength total with 2 quarter wavelengths jointed. All yagi antennas are built this way. The J-pole is similar to the bazooka antenna but its length is still a 1/2 wave or 5/8th wave or even 3/4 wave and the U-shaped joint at the bottom is a 1/4 wave tuning stub and thus no outside ground is required.

## Answer (score 8, by user10489)

There are 3 kinds of ground in radio:

- Lightning ground
- Electrical ground
- Antenna ground

Electrical ground is irrelevant for antennas.

Antenna ground is a misnomer, it's really just the other half of the dipole when working with a quarter wave monopole.

J-pole antennas don't need to be "grounded" because they are a half wave end fed dipole instead of a quarter wave monopole.

Anything below the short of the parallel matching section is technically not part of the antenna. Put a lightning ground there if you feel you need to, but it shouldn't affect performance either way.

## Answer (score 2, by Ryuji AB1WX)

### The Misconception: Grounding and Efficiency

The J-Pole antenna is a curious piece of equipment in amateur radio. Often misunderstood due to its design, which resembles an end-fed half-wave antenna with a matching stub, many enthusiasts believe it can function efficiently and stably without grounding. However, this perception is quite misleading.

This misconception arises because people incorrectly assume the transmission line at the bottom functions perfectly as an isolating impedance transformer without an RF ground reference. In reality, even when placed in free space, the coax feed line will have some common mode current and participate in radiation. In real life, the conductive support or the environment can easily detune the antenna.

#### The Role of Grounding

Attaching **a radial at the shorted end of the stub—typically the bottom end of the matching stub**—is crucial to making a J-Pole antenna stable and reducing common mode current. Since the coax braid is placed off the ground, a common mode choke is still useful in this setup.

Another approach involves adding a few radials to the coax braid, which feeds across the parallel matching stub. In this configuration, the shorted end of the stub must be isolated and floating from the support. This approach requires more radials for stability.

The same discussion applies to end-fed half-wavelength antennas typically used in HF bands. Here, the matching stub is replaced by a conventional transformer. Many believe radials at the feed point are optional or unnecessary due to the coax braid. However, ground potential is shared with the high-impedance antenna feed.

In the vicinity of the feedpoint and the "antenna ground," **the reactive near field is very high, especially the electric field.** To ensure stability and performance, minimizing unwanted environmental interactions is crucial, such as the ground or other conductive materials nearby. One practical approach is using an elevated radial.

Compared to quarter-wavelength monopole antennas, a radial is less critical because the antenna doesn't need it to function somewhat. However, it remains an efficient approach to maximize antenna efficiency.

#### Why Major Manufacturers Avoid J-Pole Antennas

Major manufacturers do not commonly supply the J-Pole antenna due to its sensitivity to environmental factors, which makes it difficult to tune. This would create a customer support nightmare for large companies. However, this does not mean the J-Pole cannot be made to work well with proper grounding, radials, and chokes.

#### Alternatives to J-Pole Antennas

Folded dipoles are extensively used in commercial and professional applications for those seeking more reliable and stable alternatives. They require the feed line to be routed perpendicularly to the radiating elements, but otherwise, they have a number of desirable properties.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21813/why-don-t-j-poles-need-to-be-grounded, by john_ham_radio, T.Bren, user10489, Ryuji AB1WX. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
