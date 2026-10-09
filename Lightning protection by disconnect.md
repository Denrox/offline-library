# Lightning protection by disconnect

*Tags: grounding, lightning · score 3*

## Question

Currently I am evaluating options for my antenna's in regards to lightning protection.

My setup is a physical disconnect of all my antennas using an outside "patch panel". So every time I power up my station, I have to go outside and physically connect the antenna feeds to a patch panel which brings the feed inside.

**Theoretically this is probably the best protection**, however **it is getting a bit of a nuisance**. So I am looking at alternatives. [emphasis added, due to comments]

One of the obvious choices would be a lightning protector, there are various models and types, and there is plenty of information available.

However I have found an Antenna Disconnect product which seems to be a good fit as well.

The link provided is only an example, there are others. Or even "home brew" circuitry which can be found by searching using a search engine.

My question: what would be the theoretical disadvantages of such a disconnect system ?

[edit 1] I am not in a high-risk strike area, however we do have 2-3 lightning storms annually. Direct strikes have not occurred in a 10-km radius for the last 10-years (which is obviously not a guarantee that they can not occur)

[edit 2] I am aware of electrical code.

Any comments welcome.

## Accepted answer (score 7, by Phil Frost - W8II)

what would be the theoretical disadvantages of such a disconnect system?

Firstly, keep in mind that antennas don't cause lightning damage: grounds do. It's not clear from your description if your patch panel is grounded at the same point as your electrical service or not.

If it's not, you have two separate grounds. This doesn't comply with the NEC, and it increases the risk of lightning damage since lowest impedance path from one ground (electrical service entry) to the other (patch panel) involves going through your equipment. See [How can I protect equipment against a lightning strike?](How%20can%20I%20protect%20equipment%20against%20a%20lightning%20strike.md) and an excellent example from W8JI where a strike on a tree 20 feet away arced back out of the ground to travel down a beverage antenna which was grounded on the far end.

Assuming you have a good single point ground, the purpose of the disconnect, surge protector, or any other device you might put at that point is not to handle the surge current, but rather to keep all the conductors at about the same voltage. Lightning is common-mode, so fortunately most of that energy will be flowing on the shield, leaving whatever protection device you choose with a relatively small amount of energy to deal with.

Just any method of disconnecting may not be effective: the voltages involved may still be high enough to arc across gaps. They are certainly high enough to blow past any solid state devices. W8JI recommends a double-make double-break relay, with the reasoning being that any arcs will most likely go to ground. He does not use coaxial surge protectors, and has never had a radio damaged.

Commercial installations operate continuously and don't disconnect the antennas. Most use a DC block surge protector like the Polyphaser IS-50 series. I don't have any relay control system so I use this approach. My first one I bought new, but I recently decided [used units are probably fine too](Are%20used%20PolyPhaser%20IS-50%20RF%20surge%20protectors%20likely%20to%20work.md). Used they go for about $25 USD, which is about as much as I'd expect to pay for a disconnect device or the parts to build one. I like that there's no chance of forgetting to disconnect something.

Both these systems work, which I think shows that it's not the protectors or the disconnects, but rather the ground system that makes it work.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9074/lightning-protection-by-disconnect, by Edwin van Mierlo, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
