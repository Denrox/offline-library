# Attic Dipole - Impact of Ethernet over CAT5/6

*Tags: rfi, antenna-system, transmission-line · score 9*

## Question

I've been thinking about putting 20m and 10m dipoles up in my attic (HOA), but I also intend to soon put some Ethernet cable to a WAP (with PoE) through the attic.

I was intending to feed this with CAT5e cable because I have lots of it and it's cheap, but I recently started thinking about the problems that the two might cause for each other in a proximity of 4-6 feet.

Should I worry about the data on the CAT5 being affected by CW/Data/SSB at 100 W on a resonant dipole whose elements are only a few feet away? Will activity on the CAT5 be noticeable on my dipoles? Does using shielded cable make a significant difference here?

## Accepted answer (score 11, by Glenn W9IQ)

Having Ethernet and your antenna co-located is not an ideal situation. But then most amateur antenna situations involve compromises. The general idea of the following recommendations is to take as many precautions as practical to minimize the interference possibilities.

I recommend that your Ethernet cable to your WAP be a CAT6 *shielded* cable (STP). While obviously not needed for your Ethernet environment, the improved twists of the CAT6 cable along with the foil shield will improve the immunity of the Ethernet cable to ingress from your antenna while transmitting as well as increase the attenuation of leakage from the Ethernet cable to your antenna while receiving.

Your Ethernet cable should also have a few toroid cores of type 43 material spaced along its length to further improve the performance of the shield. Wrap 4 to 6 turns of the cable around each toroid. This attenuates common mode currents that may be flowing along the exterior of the Ethernet shield.

Your transmission line to the antenna should be a double shielded type coax (braid plus foil). This helps to minimize ingress / egress from your transmission line.

Use a high quality, ferrite 1:1 balun at the feedpoint of the antenna. This helps to reduce common mode currents on the cable that can cause interference to your Ethernet from your transmitter or cause interference from the Ethernet to your receiver.

Ensure that your coax length is not close to an odd multiple of 1/4 wavelength (electrical length) for the bands on which you wish to operate. An ideal length is an odd multiple of 1/2 electrical wavelength as this presents the highest impedance for common mode currents. Note that this electrical wavelength relates to the outside of the shield and is influenced by the type of jacket that is on the exterior of the coax cable.

Pay attention to the layout of the cables and antenna. To the greatest extent possible, have cables cross in a perpendicular fashion instead of running or meeting in a parallel fashion. Similarly have the antenna in a perpendicular orientation to the Ethernet cable. This helps to minimize the coupling between the two systems.

## Answer (score 4, by user10489)

Ethernet cable has a minimum bending radius (check the specs of your cable). When feeding it through toroids, don't wind it tighter than that. Exceeding the bending radius causes the twists in the twisted pair to come undone somewhat, and will make the cable leak.

## Answer (score 2, by Edwin van Mierlo)

I have multiple antenna's, feedlines and Ethernet cables in close proximity.

To add to the great answer already given:

I have used STP in stead of UTP for all my Ethernet connections. This reduced cross interference greatly.

I did not have an affect on RX by activity of the Ethernet connections, but I certainly had "unexpected network behaviour" when TX-ing.

You can get STP in Cat5e and Cat6. I would recommend Cat6-STP, but it is more expensive than Cat5e and/or UTP variants.

I understand that you have Cat5e already at hand, so maybe this is not an option for you.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9730/attic-dipole-impact-of-ethernet-over-cat5-6, by William, Glenn W9IQ, user10489, Edwin van Mierlo. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
