# Are satellites Left or Right hand circularly polarized?

*Tags: antenna, satellites, circular-polarization · score 9*

## Question

I'm thinking of building some helical antennas for satellite work. I want to know which way to wind them.

If satellites are spinning randomly, how can we know if they are left hand or right hand polarized or

*Which way do I wind my antenna*

## Answer (score 4, by Rory Alsop)

Circular polarisation is not caused by the spin of the satellite. The reason for circular polarisation is to make the orientation of the satellite irrelevant. If you were running a linearly polarised antenna and the orientation of the satellite was 90 degrees off, you could get end up with an effectively infinite loss whereas you can always pick up a circular polarised signal with a circular polarised antenna of the same direction.

If you have a clockwise polarisation but the satellite is sending an anticlockwise signal (both as viewed from the same end) you will need to change polarisation - which you can do with a crossed yagi setup (you effectively reverse 90 degree phase by feeding to one side or other of one yagi set)

You can't do that with a helical antenna - so you would need two if you want to pick up clockwise and anticlockwise signals.

## Answer (score 4, by Phil Frost - W8II)

It is not the spinning of the satellite that polarizes the signal. Rather, it is that a circularly polarized signal can be rotated without affecting the signal which makes circular polarization desirable.

This is not the case with linearly polarized signals: if the two are cross-polarized (one is vertical, the other is horizontal, for example), then the link will be extremely poor. As the satellite spins through aligned polarization and cross-polarization, you get deep spin fading.

There is no standard for which way satellites are polarized. Some are right-handed, some are left-handed. Sometimes the difference comes down to which was easier to build. Some satellites aren't circularly polarized at all.

If you build a right-hand antenna, this will work with circularly polarized satellites of the same sense, and also with linearly polarized signals with a 3dB loss. It won't work very well at all with an opposite-sense circular polarization on the other end. If you wanted to work left-hand circular polarization, you either need another antenna, or you need a different kind of antenna where the polarization can be switched. Helical antennas can't do this, but crossed yagis can.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1551/are-satellites-left-or-right-hand-circularly-polarized, by Skyler 440, Rory Alsop, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
