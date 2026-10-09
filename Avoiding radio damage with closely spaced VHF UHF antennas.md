# Avoiding radio damage with closely spaced VHF/UHF antennas

*Tags: antenna-theory, vertical-antenna · score 3*

## Question

I've mostly been using a discone in the attic so far, but now I want to get proper antennas up for 2m/70cm and gmrs. I'll probably get common commercial vertical antennas. I'm not sure how much I really need to be worrying about them interacting, and since changing placement changes what sort of support system I need, which could change which antenna sizes I can use, I'm unsure about where to start.

So far I've been looking at:

- GMRS (50W) looks like most antennas are about 5dbi
- 2m/70cm (100W) - maybe comet gp-6 ? 6.5dbi on 2m, 9dbi on 70cm

How should I arrange these to avoid damaging one radio when transmitting in another?

## Answer (score 2, by Nuclear Chemist)

A lot will depend on the type of radio gear you are using, on my old Alinco DJ1FE 2 m handheld there was no relay to switch between TX and RX. Instead on that rig it had two diodes to protect the front end from its own RF.

This was not a good thing under some conditions, I found if I was close to VHF PMR transmitters that the intermodulation products from the different transmitters caused lots of strange signals to appear within the 144-146 MHz band.

You have to ask what you want the other equipment to be able to do while you are in transmit, are you hoping to be able to use full duplex going cross band where you will need to operate a RX and a TX at the same time. I think that this is the greatest challenge.

You could try to harden your system using band pass filters on all the rigs, if you are trying to use the GMRS rig at the same time as 70 cm then it could be rather hard. I would suggest that you consider making cavity filters to notch out the unwanted signal. I would consider as an alternative to cavity filters a strip line design. This could be used to decrease the coupling between the two rigs.

If you are willing to give up the ability to use both rigs at the same time. I would like to make a suggestion. You would need to change the PTT arrangements for the rigs. I would suggest the following timing sequence. Rig 1 Rig 2 PTT line rig 1 PTT rig 2 PTT on mike for rig 1

Aerial Aerial OFF OFF OFF

Aerial Aerial OFF OFF ON

Aerial Dummy load OFF OFF ON

Aerial Dummy load ON OFF ON

Chatter Chatter etc etc

Aerial Dummy load OFF OFF OFF

Aerial Aerial OFF OFF OFF

73 DE G7LSZ / SA6BID

## Answer (score 2, by John)

I have a rover with many antennas and amplifiers very close together and this is a real problem.

What I do is to connect an antenna to one rig at a time and transmit with it at max power, and use a power meter to make sure none of the other antennas have more than about a milliwatt (0dbm) coming out of them that would be going into the receiver.

Various strategies can be used if you find too much power. I use back-to-back diplexers and triplexers to inject a little more band isolation for each antenna. Sometimes moving the antennas apart or limiting power is the only reasonable option. With transverters you can modify the PTT relay so they sit in the transmit position when not powered, instead of in the receive position.

Stacking vertical antennas vertically maximizes their isolation.

Basically, you don't want more than a milliwatt (0dBm) at any frequency on the antenna jack of a receiver to minimize the risk of damage.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18263/avoiding-radio-damage-with-closely-spaced-vhf-uhf-antennas, by Brad Mace, Nuclear Chemist, John. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
