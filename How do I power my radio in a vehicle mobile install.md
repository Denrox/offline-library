# How do I power my radio in a vehicle mobile install?

*Tags: rf-power, mobile · score 6*

## Question

I want to install a 30W mobile UHF radio in my car. I already have an antenna and mounting bracket - but how do I get power to this radio? It has an SAE bullet connector on the back - do I just need a cigarette lighter adapter, or do I have to wire it in somewhere else? Do I need a fuse?

## Accepted answer (score 6, by Dan KD2EE)

While many transceivers and scanners can be powered by a cigarette lighter adapter, you typically want to run at most one transceiver in this way, and should make absolutely certain that you know where that lighter is getting powered from. Most car fuseboxes are relatively easy to access, and most owners manuals will tell you what fuse is associated with each cigarette lighter - if the fuse is anything less than 10 Amps, do not use it. Absolutely do not change the fuse to something higher.

Some possible concerns include the fact that your radio will likely start drawing it's full current only occasionally, but suddenly. Intermittent current draws like that are less likely to pop fuses than constant draws, even if the current is greater than the fuse's rating. On the other hand, you may experience voltage drops when you key up due to the resistance in the wire between your radio and battery. In the worst case, your cigarette lighter may be wired for "chassis ground return", where that 10 amp current is not being returned through a copper ground wire, but through the car's steel chassis. This is OK for stuff like an AM/FM radio or the cabin lighting, but that same resistance equates to a higher voltage drop with your 10 amp radio, which can distort your output signal or even cause devices to sense an "undervolt" condition and shut down.

And as an added bonus, guess what else is connected to your vehicle chassis? Yep, that's right, your antenna ground! So now you may have three different actual grounds all connected together, but at different voltages because of the resistance in the chassis: Your power supply ground at the radio, your RF ground at the antenna, and the actual negative post of the battery. This situation can mess with the bias of your final RF amplifier causing signal distortion or overheating.

The best way, and the ways the pros do it, is to run a separate pair of wires from the battery to the radio. These wires must be rated for the maximum current draw of the radio (and then some, since every ham initially plans to install one radio and then winds up with 5) and both positive and negative leads must be fused at the battery. If they aren't, and come into contact with anything, you may short your car battery causing a fire.

There's another bonus of connecting directly to the battery - some cars shut off the cigarette lighter when the car is off, but if you connect straight to the battery, you have control over how the power is controlled. There are low voltage disconnects intended for this purpose which will detect when the car is turned off and shut off the radio a fixed amount of time later, but which can be overriden to allow you to operate the radio without turning on the car if needed.

## Answer (score 2, by Adam Davis)

A 30W UHF radio should consume less than 10A, which is the limit of most cigarette lighter outlets. You can try it out, and if it blows the fuse, replace the fuse and choose a different option for powering it. Since the outlet is fused, you don't need to add an additional fuse inline with the radio power.

Beyond that, I suggest you check your user manual and the manufacturer's suggestions for installation. It'll vary based on the vehicle and whether you want it to work with the engine off or not. You may be able to find an automotive radio/alarm installer that could perform the install for you as well, if not talk to your mechanic.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/300/how-do-i-power-my-radio-in-a-vehicle-mobile-install, by Dan KD2EE, Adam Davis. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
