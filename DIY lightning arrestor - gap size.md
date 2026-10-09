# DIY lightning arrestor - gap size?

*Tags: antenna, grounding, safety, lightning, equipment-protection · score 6*

## Question

I have an antenna that's well above the treeline, and I've heard I can add some small amount of protection by placing two bolt heads a short distance from each other, one connected to the antenna, the other connected to the ground rod.

What distance should I have the bolt heads apart to induce spark over on lightning strikes, but not interfere with my normal transmissions? I won't be using more than 100W in the HF bands with this antenna.

## Accepted answer (score 3, by Adam Davis)

One enthusiast reports, "*.029" spacing for a KW station, and .045" spacing for 2.5 KWs*"

Keep in mind that a lightning arrestor doesn't stop an electrical discharge event, it merely shunts most of the energy to ground. There's still a lot of damaging current that ends up in the wire which will damage attached equipment. See [How can I protect equipment against a lightning strike?](How%20can%20I%20protect%20equipment%20against%20a%20lightning%20strike.md) for a better overview of all aspects of lightning protection.

## Answer (score 2, by Bumbal)

Get a two terminal GDT and call it a day, use very short low inductance leads to attach it between the center conductor and earth ground. GDT (Gas Discharge Tube), Bourns make them, Digikey or Mouser may have them. GDTs are high-impedance, very fast-acting, very high-energy devices for surge protection. MOV (Metal Oxide Varistor) devices may have low enough off-state leakage to parallel the GDT - pick a 600VDC device. These two together should really nail down any spikes. You will find lots of application information at the Bourns and Little Fuse web sites.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/984/diy-lightning-arrestor-gap-size, by Adam Davis, Bumbal. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
