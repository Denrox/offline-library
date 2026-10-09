# 2 Meter horizontal or vertical dipole polarization?

*Tags: antenna, 2m-band, vertical-antenna, dipole, polarization · score 4*

## Question

When should I use one polarization over the other on 2 meters?

I've looked at the radiation patterns for horizontal dipole and seen how it changes based on mounting height. I haven't been able to find any information on how the vertical dipole radiation pattern changes with mounting height.

## Accepted answer (score 7, by Kevin Reid AG6YO)

For VHF, choice of polarization is not up to your desired radiation pattern, but who you want to be able to communicate with. In HF, the ionosphere causes random rotation of your signal's polarization, but in all line-of-sight communication, VHF or higher, there is no such rotation and a polarization mismatch can result in no signal at all.

You should use vertical polarization if you wish to communicate with existing FM mobile and repeater stations, because they also use vertically polarized antennas (by convention, and because quarter-wave verticals are much more convenient than other types of antennas on vehicles and handhelds).

On the other hand, you should use horizontal polarization if you are attempting 2 meter SSB or other types of DX/weak-signal work. Again by convention, but the convention arises because (if I understand correctly) horizontal dipoles typically have more gain, and because a horizontal dipole is a simple, efficient freestanding antenna.

If you wish to be able to communicate with both types of stations using a single antenna, you *can* use a diagonally or circularly polarized antenna, as a compromise which has a reliable small amount of loss in either case. However, such antennas are more directional than a vertical (at least as much as a horizontal dipole) and thus require pointing.

## Answer (score 2, by Charles Boling)

I've always heard (but am unable offhand to quote authoritative research or provide an explanation of why this is so) that an advantage of horizontal for weak signal work is that a lot of man-made noise tends to be better received with vertical polarization than with horizontal. Thus, all else being equal, you will have better performance (i.e. a better SNR at the receiver) with horizontal. As a side benefit, if you are operating on frequencies that are usually used vertically, interference between you and other users is reduced; thus, not only are you giving yourself an advantage, but you are arguably being a good neighbor at the same time!

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5468/2-meter-horizontal-or-vertical-dipole-polarization, by KM4NTK, Kevin Reid AG6YO, Charles Boling. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
