# Is a ground plane necessary for transmitting and receiving with a vertical (monopole) antenna?

*Tags: hf, vhf · score 6*

## Question

I've read the post here:

https://electronics.stackexchange.com/questions/77256/why-do-some-radio-antennas-require-a-path-to-ground-and-some-do-not

which says

The antenna system requires a "ground plane" for the radio wave to form. With dipoles, one half of the antenna is your ground. In verticals, something below must provide ground to complete the RF wave. This is usually achieved with radials, either attached to the base of the vertical, or buried below a ground mounted antenna. The presence of a metal mast/tower (which is lightning grounded) may contribute/interfere with the ground plane but it is not considered the antenna ground.

But, for example, 2m verticals on boats don't have ground planes. Two questions.

1.

Am I right in saying that a ground plane results in optimal radiation, but that radiation will still take place without one e.g. boats antennas still reach the horizon, though likely height and more power are required.

2.

Is a ground plane necessary for receiving?

Thanks for reading

## Accepted answer (score 4, by Kevin Reid AG6YO)

Every antenna has two halves, meeting at the feed point (where the coax or other transmission line is attached). Both halves affect the properties of the antenna (radiation pattern, efficiency, etc.).

A vertical element and a ground plane is **just one possibility** for what those two halves can be. If you omit the ground plane from a ground plane antenna, then there are only two possibilities for what happens:

- You have an ineffective antenna — it does not radiate/receive well.
- Something else is serving as the ‘second half’.

In most designs of coax-fed antennas, what ends up being that second half is the shield of the coax cable and (if applicable) the conductive metal structure the antenna is mounted to. I don't know how antennas on boats usually are, but I bet there's a metal structure there.

This *can* work fine, but there are two potential problems:

- This conductive shape wasn't particularly designed to be an antenna, so it may not have the best characteristics for that (irregular radiation pattern, lossy, wrong impedance, etc.).
- It may be closer to other electronic equipment, the operator, etc. and thus (for receiving) pick up extra noise or (for transmitting) deliver significant RF energy where it is not wanted.

If you're interested only in receiving for now, put up whatever antenna you can and don't worry too much. If you find you need better performance from your antenna, install a proper ground plane or other design of antenna.

## Answer (score 3, by Mike Waters)

Any vertical that you may have seen mounted on a nonmetallic surface **should** have something like a metallic sheet or λ/4 copper tape radials (of proper dimensions) underneath it (and the coax shield connected to that). Otherwise, the outside of the shield will try and act as the return and have common-mode currents on it. How well that works depends on many factors, **but that's not the proper way to do it to maximize communication range.**

Of all the physical laws that there are, none are more well-established than the fact that a bottom-fed vertical (vertical monopole) or an inverted-L needs something to "push against" to be most effective. Call that 'something' a counterpoise, radials, or whatever you want to; but to be effective, it's got to be there. Period.

K5UJ put it nicely when he said "The reason for radials is to collect RF currents and return them to the feedpoint since you don't have the other half of the antenna to do that, the part that would make it a dipole."

If we make the statement that adding a counterpoise to a λ/4 vertical (for example) is not really necessary, then we might as well say that opening the window blinds won't make the room any brighter. Sure, maybe we can see our way around, but when we let the sun in, life is so much better. Or, someone could say that we don't really need tires on a car. Sure, with enough ground clearance we can drive around on the rims, but isn't the car much more fun to drive with the rubber attached? *Likewise, a proper RF ground makes the radiated signal stronger while preventing unwanted common-mode currents on the outside of the coax shield.*

From this web page.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7089/is-a-ground-plane-necessary-for-transmitting-and-receiving-with-a-vertical-mon, by Steve, Kevin Reid AG6YO, Mike Waters. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
