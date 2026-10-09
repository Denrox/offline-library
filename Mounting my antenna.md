# Mounting my antenna

*Tags: antenna, mobile, citizens-band · score 5*

## Question

I just bought a CB and mounted it in my truck. I ran my antenna to the back and was going to stick it to my tool box but it turns out to be aluminum, so I'm thinking of bolting a metal plate to the top so the magnet will stick.

Should I attach a ground wire to my plate so my antenna will be grounded as well?

## Answer (score 3, by rclocher3)

Many hams who do a lot of mobile HF operating (CB is HF also) take the time to bond many different parts of the vehicle together. The theory is that your vertical antenna is 1/4 wavelength long electrically, but it's only half the antenna; the other half is the ground plane, through which current must pass for efficient operation. There's lots of information on Alan K0BG's page about bonding.

I don't think you'd need to bond the steel plate inside the toolbox to the toolbox, because the RF current will be mainly flowing on the surface of the aluminum. (RF currents flow mainly in a thin surface layer of a conductor.) If I were you I would bond the toolbox to the truck, and also bond the bed of the truck to the frame. Have fun!

## Answer (score 3, by K7PEH)

You didn't mention if the antenna was a full-sized quarter wave-length or a shorter antenna with a loading coil. This makes a difference for two different reasons. I will handle the first reason immediately -- no full sized quarter-wave 11-meter (CB in US) antenna should be mounted with a magnetic mount -- although the "wrongness" of this type of mount suggests it is likely a shorter antenna with a loading coil.

Assuming your tool box is mounted just behind the cab of the truck then I believe that your antenna will be below (or mostly below) much of the cab which is a lot of conductive metal. This is not good for having the best performance from your antenna. In fact, you can experiment with this easily (especially for magnetic mount) is to try doing tests (signal strength etc.) with the antenna temporarily placed at different locations on your truck.

Most of the coil loaded CB antennas I have seen have a center mounted loading coil. This means that the higher current part of the antenna which produces your strongest radiation, is between the base of the antenna (at the feed point) and the center loaded coil. This part of the antenna should be clear from as much of the metal of the truck as possible (metal below the antenna is OK).

## Answer (score 2, by Phil Frost - W8II)

Should I attach a ground wire to my plate so my antenna will be grounded as well?

I wouldn't bother. The "grounding" of the antenna at DC like a multimeter would measure is irrelevant. You care about the impedance at 27 MHz which is very different. At 27 MHz, a capacitance which has an infinite impedance at DC can be a very low impedance, and a wire of the right length which has very little impedance at DC can have a large impedance.

The capacitive coupling between the steel plate and the toolbox provides a low impedance at 27 MHz. The same is true when the mag-mount antenna is stuck directly to a steel panel of the vehicle with an insulating layer of paint between.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6701/mounting-my-antenna, by B Wingfield, rclocher3, K7PEH, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
