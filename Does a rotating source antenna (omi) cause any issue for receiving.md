# Does a rotating source antenna (omi) cause any issue for receiving?

*Tags: antenna · score 3*

## Question

Lets say I want to send some data from the London eye. I decide to mount the antenna at the centre of the wheel point out (normal to the circular plane). It's an omnidirectional antenna so I know there wont be any issue of point specifically, but due to the rotation of the wheel (and hence the antenna) does it cause any serious issue for a receiver on the ground (let say at the base of the wheel)? What if the receiver is moving (in a car driving past the base of the wheel)?

Now, my current understand of how this works is since it doesn't matter where you are located relative to the antenna, it shouldn't matter if the antenna is rotating. However my intuition is that this isn't right! That there would be some issue with the received signal (similar to Doppler maybe?).

## Accepted answer (score 3, by Kevin Reid AG6YO)

“Omnidirectional antenna” is a bit of a misnomer; there is no antenna which radiates equally in all directions on the sphere. I'm going to assume you mean some kind of monopole or coaxial antenna, i.e. one that has all of its parts in a straight line.

In that case, if it is, as you say, **on** the axis of rotation, then the rotation makes no difference whatsoever. After all, it's rotationally symmetric about that axis. The radiation pattern is also symmetric (in both amplitude and phase) about that axis.

If you were to mount the antenna in the same orientation, but not at the center of the wheel, then there would be a very small amount of Doppler shift, since the distance from it to the receiving antenna changes. But the velocity is so small that it would not significantly affect reception — after all, it's slower than a radio in a car on a highway.

(For an example of a radio technology which *does* make use of significant Doppler shifts due to (effectively) moving antennas, take a look at VOR (VHF Omnidirectional Range)).

On the other hand, if you were to mount the antenna in the plane of the wheel instead, there would be major effects.

If your receiver is in a direction near the plane of the wheel, then the signal will drop out twice per revolution, as the two nulls of the antenna align with the receiver.

If your receiver is in a direction near the axis of the wheel (e.g. some distance away and looking at it), then it sees the *polarization* of the signal rotate. Using a normal, linearly polarized, antenna, the receiver would observe it fade out twice per revolution (as the polarization difference reaches ±90°). If the receiver instead had a circularly polarized antenna, then the signal would be stable but have a consistent 3 dB loss.

(This last scenario is exactly how communication with amateur satellites, which are usually spinning relative to the earth and have linearly polarized antennas, is best accomplished.)

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5034/does-a-rotating-source-antenna-omi-cause-any-issue-for-receiving, by FraserOfSmeg, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
