# Colocated three orthogonal wire loops for lightning detection network

*Tags: antenna-theory, lightning, small-loop · score 4*

## Question

I'm considering building multi-turn wire loop receive antennas for a blitzortung.org lightning detection receiver. It has three separate channels for H-field antennas, operating simultaneously.

Typically, only two orthogonal loops in vertical planes are made and co-located, e.g like:

Having enough real estate available this time, I wonder if there could be any advantage in placing loops several meters apart. Aren't directional nulls suffering from the close neighbour - other loop? (*possibly* resulting in a poorer SNR for the given loop, if a near noise source would be otherwise in a deeper directional null)

Same question applies for adding a third, horizontal loop. Are there any advantages in not using the same mechanical frame? When co-locating, is there anything about the feeder routing to consider? (extremely: one could route the feeder of horizontal loop in question right along the side of a vertical loop).

I saw three colocated orthogonal loops elsewhere, but that was quite a different application. There, only one of loops is connected to the receiver, others are open-circuit.

And lastly, would same considerations (from the answers to come) apply if [shielded loops](What%20does%20the%20addition%20of%20a%20shield%20to%20a%20small%20loop%20accomplish.md) are used?

### Mobius loop:

## Accepted answer (score 2, by Glenn W9IQ)

The lightning detection antennas are not used in any sense to triangulate or to direction find through any other method such as phasing. The three antennas are there simply to provide quasi 360° detection of lightning events. The actual direction finding is accomplished by analyzing the timing of detected lightning events from multiple sites using GPS time stamping and calculating time of fight by comparing data from multiple stations. In other words, if there was only one receive site in North America, no direction finding could be done for that region. In fact, it is acceptable to have a station with just one antenna - it simply may not be as sensitive to lightning events from certain directions.

With this as the background, feel free to spread out your loops if that works for you. Many people don't have that luxury which is why they have the creative colocated loops.

The "Blue" receiver version, the latest, has differential preamps so do not use any type of balun between the antenna and the preamp. You could place a wound coax/toroid type balun on the feedline to the receiver but keep in mind that you are dealing with very low frequencies so the typical amateur radio designs will not work well.

The shielded loop antenna is not the type that hides the feedline. They are using the split shield design to form a so called H field antenna (which has nothing to do with receiving only the H field!). If you decide to use such an antenna, follow their construction notes. They are sloppy on the description of where the break in the shield should be. I would recommend it be placed exactly in the center of the circumference in order to provide an optimum differential feed.

## Answer (score 2, by Mike Waters)

FORGET the third **horizontal** (yellow) loop antenna!

I finally disabled mine because it caused me no end of trouble with noise pickup and thousands of spurious signals sent to the BT (Blitzortung) servers in Europe. Although it appears in the official documentation, I have not been able to find *anyone* who is using one. Most are using just two vertically-polarized loops 90 degrees apart. That's all that are needed.

A better way is to have three H-field (magnetic) loops, all vertical, 60 degrees apart. (That's what I intend to do.) Several BT stations are using ferrite rods purchased from the BT people in a delta configuration.

In the forum, the developers have since retracted any recommendations for a horizontal loop. It was one of those "Well, it seemed like a good idea at the time" things.

I now have two Blitzortung lightning receiver stations, 1977 and 2294. If you are a participant you can see the antenna on https://forum.blitzortung.org.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7849/colocated-three-orthogonal-wire-loops-for-lightning-detection-network, by Xpector, Glenn W9IQ, Mike Waters. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
