# Two antennas on different sides of a building

*Tags: antenna-theory, antenna-system, 2m-band · score 6*

## Question

I live in the 4th floor of a building with one side facing south and the other north. I am able to use my 2M mobile base transceiver with a mobile magnet mount antenna placed just outside the window. I get fairly decent coverage of areas on one side of the building with this setup. My question: Is there a simple way to couple two mobile antennas (one on each side of the building) so I have good coverage of both (north and south) sides at the same time?

## Answer (score 9, by Phil Frost - W8II)

As one solution, you can combine the antennas with a power divider. See [How to combine two 50 Ω antennas such that they appear as one 50 Ω load?](How%20to%20combine%20two%2050%20%CE%A9%20antennas%20such%20that%20they%20appear%20as%20one%2050%20%CE%A9%20load.md)

This makes your pair of antennas into a phased array. If there's no overlap between their coverage, you effectively lose half your antenna gain, or 3 dB. This is because on transmit, half your power goes into the other antenna which sends that power in the "wrong" direction. And by reciprocity the same happens on receive.

In practice there will be some overlap in their coverage, you will get areas of constructive and destructive interference between the two antennas depending on their relative phase. The effect will be [grating lobes](What%20does%20multi-path%20sound%20like%20on%20FM.md). I'd guess however it's no worse than all the reflections already present in an urban environment.

Alternately, you could install a switch, and select the antenna which works best for a particular situation. This avoids the 3 dB loss and grating lobes, but of course you have to operate the switch.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10488/two-antennas-on-different-sides-of-a-building, by 4G1BGS Larry, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
