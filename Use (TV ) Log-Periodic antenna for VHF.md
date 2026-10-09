# Use (TV?) Log-Periodic antenna for VHF

*Tags: antenna, antenna-theory, vhf · score 3*

## Question

I found this old log periodic antenna that I assume was from a TV. Could I, or how would I, use this on the amateur radio bands? My main focus would be VHF, with UHF being secondary and HF would also be nice. I'd like to keep it as cheap as possible.

Largest: 4' 5" (134.62 cm) - seems to be electrically connected to form a 8' 10" element?

smallest: 5" (12.7 cm) (unfolds to be parallel with another 5" element)

"Other" smallest: 6" (15.24 cm) (by itself)

## Accepted answer (score 6, by tomnexus)

I'm sorry to say that's not a simple log-periodic antenna, it's a hybrid monstrosity to meet some particular need.

Guessing from the element lengths:

- 136 cm each side would work at about 50 MHz, so **low-band TV**. Two-element log-P with a reflector. OK.
- 12 cm each side would work at about 550 MHz, so **mid UHF TV**. Some sort of Yagi
- 15 cm total would be a director for about 900 MHz, so the **top end of UHF TV**.

It doesn't seem to cover the VHF ham band, and it probably only starts working above the 440 MHz ham band.

You could probably re-use the mounting and feed hardware, cut the feed down to work at 145 MHz, and then install new directors to give it some gain. But you are basically building a new yagi, and with very non-ideal director spacing.

If you need a directional antenna (for satellites?) rather build a new yagi from scratch. You can make a nice one in a few hours with some bits of brazing rod and a broomstick.

## Answer (score 5, by niels nielsen)

Those antennas are held together with aluminum pop rivets which are easily drilled out. In less than an hour you can completely disassemble a TV antenna like that and salvage the main mast, all the dipole elements, and the plastic element mounts- and use these and some fresh pop rivets and an electric drill to build yourself a two meter yagi beam with excellent performance, for which there are numerous plans available on the web.

## Answer (score 2, by Mike Waters)

Log-periodic antennas have a very wide bandwidth. One designed for TV would not work at HF, but it may very well work on 2 meters, 6 meters, and some UHF amateur bands.

I suggest that you measure the SWR and see. However, unless its impedance is 50 to 75 ohms, you will need a suitable matching device.

Can you post photos of it? While you're at it, include the minimum and maximum lengths of the elements.

Countless hams have used TV log-periodic antennas on the ham bands, and with little or no modifications.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17621/use-tv-log-periodic-antenna-for-vhf, by Galaxy, tomnexus, niels nielsen, Mike Waters. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
