# Antenna options

*Tags: antenna, antenna-construction, wire-antenna · score 6*

## Question

I am considering a new ham station in a relatively urban environment on the South coast of England, and would like like some ideas / feedback on antenna options.

Aim is to get reasonable performance for 40/20/15/10m bands with 100W TX power from an ICOM 7300 using the internal tuner (ie SWR <= 3). Aim is to get contact around Europe (note compass orientation of SatImage below).

Trying to avoid putting up large structures on roof, and utilise nearby Chestnut tree on edge of property. My current simplest idea is a fan dipole, with some concerns/buts (see below)... Some sketches:

Side view looking towards ENE:

Top View:

SatView to give impression of urban environment. Note that north is up on this image. Note the large "block" of flats about 20m to the ENE. This block is uphill from house and their top floor is about 5m(?) above where the diploe would be (ie 15m off "my ground")

I have only shown some end-insulators on a single dipole with coax centre feed into a 1:1 balun. Basic plan is currently for a fan dipole to get reasonable resonance in each of the bands.

1.

Unless I butt right up to the tree and the roof, I probably won't have room for a 40m band half-wavelength dipole. The length from end of roof ridge to fork in tree is just over 20m. There might a possibility of attaching to the other top ridge running ENE (ref sat image), which would give me the extra length but put a significant part of the antenna length over the roof.

2.

The neighbours.... The top floors is 20m away horizontally and 5m above vertically. Broadside to the dipole. Bad idea?

3.

"False ground" where the dipole overhangs the roof. And plenty of "foliage" above the dipole in chestnut tree (total height 20m+ above ground). Also the metal roofed garage to the right of dipole in SatImage, it's only 2.5m high, so probably 7-8m from dipole. How serious are these effects likely to be? Suck it and see?

4.

Other Antenna types other than fan dipole which include 40m band? Perhaps something like this: http://www.m0pzt.com/fan-dipole/.

5.

If above can't work, is there anything that could? Happy to go for external tuner or external amp for matching and more power up to UK legal limit of 400W. Central tower to "drape" inverted V dipole over the house? Or throw money and install a tower with a Yagi Beam. Or give up on 40m and stick to <=30m?

Many thanks

## Accepted answer (score 4, by Phil Frost - W8II)

Unless I butt right up to the tree and the roof, I probably won't have room for a 40m band half-wavelength dipole.

Then butt up to the tree and the roof. Of course it would be better if you had an enormous pair of towers in the middle of nowhere. It will still work.

The neighbours.... The top floors is 20m away horizontally and 5m above vertically. Broadside to the dipole. Bad idea?

It will be fine. And there's nothing you can do about it anyway, besides move to a location where you have more land.

"False ground" where the dipole overhangs the roof. And plenty of "foliage" above the dipole in chestnut tree

I wouldn't worry about it. Perhaps if you had a metal roof it would be somewhat significant, but it's just one of many things you can compensate for when tuning the antenna. If you wanted to run much higher power you might start to worry about arcing off the ends of the antenna, but at 100W that won't happen.

Other Antenna types other than fan dipole which include 40m band?

A trap vertical is another option to get multiple bands in one antenna with a small footprint. You could possibly mount it in the middle of your roof, with radials extending to the edges of the house. But the fan dipole probably works better and is cheaper to build.

If above can't work, is there anything that could? Happy to go for external tuner or external amp for matching and more power up to UK legal limit of 400W. Central tower to "drape" inverted V dipole over the house? Or throw money and install a tower with a Yagi Beam. Or give up on 40m and stick to <=30m?

More power will make it easier for other people to hear you, but it won't make it any easier for you to hear other people over the noise, which is going to be significant due to all the houses nearby.

Getting the antenna higher with a tower could be an improvement, but definitely not necessary. The improvement would probably be most significant on 40 meters, since 10 meters is only a 1/4 wavelength high there.

A directional antenna is likely the biggest improvement you could make, especially if you can also put it up higher. This is because the antenna directivity will also eliminate the noise you receive. But again, by no means necessary.

Overall, your plan sounds fine. My advice would be to get an antenna in the air and see how it works.

## Answer (score 3, by Brian K1LI)

Here's the SWR curve for a half-sized "Slightly Off-Center Fed Dipole" described in the September 2019 issue of *QST* magazine:

The antenna provides an SWR on your bands of interest that any rig's built-in matching network should handle with ease and mismatch losses in a modest run of coax should be minimal.

Notice that the SWR is calculated for 200-$\Omega$ characteristic impedance. The wire is 20.9-m long and is fed 40% from one end through a 200-$\Omega$:50-$\Omega$ balun for convenient coax feed. (Note: not a typo, this feedpoint is slightly different from the article.) As the author of the original article I received dozens of letters, some of which claimed success with a variety of balun designs, but I recommend a two-core Guanella type "current balun":

with a choke of coax turns on a ferrite ring below but near the balun to prevent common-mode current on the outside of the coax shield.

Because the feedpoint is not far off center, it's possible this balun is somewhat over-designed, but the parts are relatively inexpensive and readily available. I wound the balun for the article with two-conductor speaker wire to illustrate the utility of low-cost, everyday items one might find lying around the house:

It's abundantly possible that, with sag, the entire wire will just fit in the 20-m space between your house and tree. But, if it doesn't, "drooping" the far end of the wire will have very little effect on the antenna's behavior.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18132/antenna-options, by Oliver Schönrock, Phil Frost - W8II, Brian K1LI. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
