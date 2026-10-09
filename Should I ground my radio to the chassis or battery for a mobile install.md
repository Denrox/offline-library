# Should I ground my radio to the chassis or battery for a mobile install?

*Tags: mobile, grounding, dc-power · score 11*

## Question

From what I've seen, there are generally two ways to power a mobile radio:

- Positive lead to battery, negative lead grounded to chassis
- Both positive and negative leads to battery

I know that antennas should be grounded to the chassis, but what about the radio itself? There must be some electrical difference, but I'm not sure what it is and I've seen a lot of contradictory information.

What is the "correct" way to do this? The vehicle is a 2012 Honda Accord.

## Accepted answer (score 7, by Kevin Reid AG6YO)

There are two reasons for the advice to run direct to the battery:

1.

Minimize the *area enclosed by the power connections*. This reduces both interference picked up by the wiring, and inductance (which is undesirable in power supply connections).

2.

Minimize resistance. A radio can be a fairly heavy load as car *accessories* go, so you want to avoid any voltage drop you can, and the chassis may not give you the best conduction to the battery.

Neither of these is a reason to wire specifically to the battery per se, only to avoid using a completely different conductor (the chassis). According to K0BG.com, a site dedicated to mobile amateur radio, some modern cars have electrical systems in which you shouldn't wire direct to the battery terminals, for example:

The use of these sophisticated subsystems have necessitated the relocation of the ELD to the negative lead of the SLI battery as shown at right (surrounding the battery ground lead), and below right (incorporated in the battery negative connector). The photos are of a 2014 Nissan Titan, and 2013 Honda Accord respectively, but other makes are similar such as Ford's F150 shown below at left.

Ford's Battery Monitoring SystemIt should be obvious that transceiver ground connections cannot be made directly to the battery as recommended in the past, as doing so would bypass the BMS. Thus in the examples shown, the negative lead would be attached to the battery's chassis connection point (Titan), or on the ground side of the ELD (Honda).

(Note that the reference to connecting to the chassis is to the point at which the *battery* is connected to the chassis, not elsewhere on the chassis.)

The article goes on to say, after discussing other possible complications:

The bottom line here is, if in doubt, read your Service Manual, or contact your dealer's service department before undertaking your installation.

To summarize:

1.

Learn how your vehicle's electrical system works — specifically, where it is safe to tap for a high-current accessory.

2.

Run a dedicated, fused 2-conductor power cable between that connection point and your transceiver.

## Answer (score 2, by Danny W. Burdick)

Have a 2018 Subaru Forester Has a heavy 2nd wire from negative batter terminal going to an ELD sensor...the wire from the sensor to the chassis ground is enclosed within aluminum tubing and cannot be easily accessed. The head tech for Subaru in my location went to my car opened the hood and pointed to the main chassis ground bolt between the fuse box and the shock mount...good enough for me..

## Answer (score 2, by Dereck Campbell)

Very simple. Never connect Negative directly to battery and never fuse the Negative as doing so is extremely dangerous. Doing so puts your radio in Parallel with the Battery Bonding Strap to the chassis. That means a portion of all the automobile electronics systems current is flowing through your radio including the Starter. Secondly will bypass the vehicle HFE current sensor in the vehicle battery bonding jumper.

If anything were to happen to the vehicle bonding jumper, means your radio is now the bonding jumper. Put your key in the ignition, all the lights, bells, and whistles come as normal. Turn the key to crank your engine, and your car fills with smoke and fire. All that starter current flowed right down the Radio Negative Battery lead, through radio chassis and circuitry, and out the coax shield completing the circuit burning it all up along the way.

Not only is it dangerous, with a portion of all vehicle current flowing through you radio is called Common Mode Noise, Can be bad enough to render your radio useless.

The proper termination points for Positive and Ground. For Positive directly to the Battery Term post with a fuse as close as possible to battery.

For the Ground aka negative circuit conductor, locate the factory Battery Bonding Jumper to chassis. Cannot miss it, it is the cable on the Battery Negative Term Post. Typically bonded to Wheel Well, or Fire Wall. Remove factory bolt. Clean any paint, grease, dirt off and make sure you have bright shinny metal. Use an anti-oxidant. Place your radio negative cable Ring Terminal on TOP, not below Factory Rind Terminal. Replace factory bolt and Locking hardware. Same effect as directly to battery post with respect to low voltage loss, but takes your radio out of a Nasty Nasty Ground Loop. Anyone tells you different, tell them to pound rocks, they do not know what they are talking about.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/4951/should-i-ground-my-radio-to-the-chassis-or-battery-for-a-mobile-install, by Ben, Kevin Reid AG6YO, Danny W. Burdick, Dereck Campbell. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
