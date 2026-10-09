# Can I connect my station ground to my house's ground rod?

*Tags: antenna, grounding, lightning · score 5*

## Question

I'm setting up my first HF rig and I'm reading a lot of conflicting information regarding station grounding. Can I connect my HF rig/station's ground to my house's ground rod or do I need a stand-alone ground rod for my station?

I was told I need to ground my HF transceiver even if I didn't have an antenna attached to it most of the time. I don't really understand grounding despite reading quite a bit on it and I can't find a clear-cut best practice.

It would be about a 50ft wire run to the house's grounding rod from my shack.

If I do need a second ground rod for my station, does it need to be bonded (connected via 10 AWG wire) to my house's ground rod?

What I'm thinking of doing is running a 10 AWG wire that's clamped/bonded to my house's ground rod into a black 1-gang PVC box. Then attaching that wire run to a 2 terminal aluminum bus that's attached to a blank faceplate (to look nice and meet wifely approval).

Then run a wire from that "outlet bus" to a 10 terminal aluminum insulated bus that all my station kit would be bonded/wired into.

I'll be taking my antenna (just a simple one) down and detaching it when I'm not operating so as I understand it I don't need to ground that.

Am I grounding this correctly?

## Accepted answer (score 4, by rclocher3)

There are lots of existing questions here about grounding, with answers containing lots of good information. Grounding can be a confusing topic, partly because there are different types of grounds. Some grounds are for electrical safety, some are for RF to make an antenna work as designed, and some are for lightning safety.

The ground lug on your transceiver is provided so that the operator can ground the case, which is usually also connected to the shield of the coaxial cable, to an RF ground. The rig is grounded for electrical safety through its power plug, or the external power supply's power plug. In my opinion, the ground lug is provided for hams who are trying to prevent problems related to RF on the shield of the coaxial cable, which is often called "RF in the shack". However an RF ground connection has to be a small fraction of a wavelength long to be useful. Unless you have a good RF ground such as a network of radials within arm's length of the transceiver, connecting your rig's ground lug to some sort of ground is unlikely to be very helpful, in my opinion. Again in my opinion, there are better ways of solving RF-in-the-shack problems, such as a balun. Personally I don't connect anything to the ground lugs on the transceivers in my shack.

If you do provide a separate connection to ground, it must be sized large enough to handle all the current that normally passes through the neutral line to the building, to prevent a fire in the case of a neutral fault. See @ScottEarle's fine answer to this question.

If your house has modern wiring, your outlet in the shack already has a wire connected (indirectly) to the ground rod. That's what the third prong of a (US) three-prong plug, the prong that is sometimes omitted for double-insulated appliances, does. Your extra box would be unlikely to provide any extra benefit.

If you do have multiple ground rods, they should definitely be connected. In the US, the National Electric Code (which is actually not a national code, it's a model for regional electrical codes) requires that ground rods be interconnected, and specifies the size of the interconnection based on the size of the service cables feeding the house. For most houses, 4 AWG solid copper suffices. (There are two reasons for bonding ground rods together. One is that in the case of a nearby lightning strike, the the enormous charges induced in the earth to dissipate through the ground rod connection rather than through conductors in the building. The other reason is that in the event of a failure in the connection of the neutral line to the building, the current that would normally flow through the neutral line would flow to ground instead. See @ScottEarle's fine answer to this question.)

Unfortunately, disconnecting an antenna temporarily is a tricky way to prevent lightning damage. If lightning were to strike nearby, there would be a tremendous voltage surge on your house wiring, which acts like a big antenna to receive power from the lightning strike. The voltage surge in the house wiring is just as likely to damage your transceiver through the power plug (and damage lots of other things also) as a voltage surge in the coaxial cable. So if you're unplugging the antenna, you should also unplug the rig from the wall outlet, and also disconnect it from everything else. Unplugging the rig from everything after operating gets tiresome, and operators, being human, tend to skip doing it after a while. My advice is to disconnect the radio from everything after operating for now, but take stronger measures to protect your house from lightning soon, before disconnecting the rig becomes too tiresome. There's some great advice in answers to the question "[How can I protect equipment against a lightning strike?](How%20can%20I%20protect%20equipment%20against%20a%20lightning%20strike.md)".

## Answer (score 3, by Scott Earle)

Before connecting anything directly to earth ("ground" in the US), you need to be aware how your home is wired. There are several ways a house can be connected to the power network, as detailed in this Wikipedia article.

In some places (for example, the UK), the earthing system TN-C-S (see the Wikipedia article) is used, which makes it potentially dangerous (like, properly dangerous) to bring an external "earth" connection into the property. The reason being that on the rare occasion of a neutral fault, all current brought into the property would be trying to return through that earth connection, which can be a fire hazard if there are several kilowatts in use but the wire connecting your transceiver to earth is not hefty enough to carry that current.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20634/can-i-connect-my-station-ground-to-my-house-s-ground-rod, by SomeGuy1989, rclocher3, Scott Earle. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
