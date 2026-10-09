# How to keep a disconnected coaxial connector weatherproof?

*Tags: coaxial-cable, weather, safety, equipment-protection, lightning · score 8*

## Question

The advice I have seen on lightning safety is that if you don't have high-quality lightning protection (and associated grounding) installed on your feed line, it is advisable to, during a storm and preferably whenever you are not using your station, is to disconnect the antenna feed line from your equipment and **“throw it out the window”**, to separate it from the interior of the house.

This seems like a perfectly reasonable idea to me, except for the fact that “out the window” is likely to be wet, especially under the circumstances. **How can I protect the free end of the coaxial cable (a PL-259 connector in this case) from water and other environmental damage?** Permanent connections can be wrapped with amalgamating tape, but this is temporary and recurring.

It is possible I could arrange to hang the cable right under the eaves of the roof so as to avoid actual rain, but it would still be exposed to damp, windblown crud, bugs, and so on. I do have a rubber dust-cap the cable came with but it doesn't fully enclose the connector — would that be sufficient, assuming there isn't actually rain running down the cable?

Or alternatively, what **other approaches** should I consider for the safety of myself and my equipment, besides the above two? Note I am in a rented space and all of my current equipment is specifically installed “temporarily”. (Taking down the antenna itself is quite easy and I would probably do it in the event of a predicted storm, but even then the feed line is still a conductor outside of the building, and partly on the roof.)

## Accepted answer (score 5, by Phil Frost - W8II)

I'd recommend one of two solutions:

#### 1. Don't throw it out the window.

Most lightning damage comes not from direct strikes but nearby strikes, which can still induce large-ish voltages on the feedline: not enough to make lightning, but enough to damage things. A couple feet of air between the feedline and the tranciever will protect against this. If you do get a direct strike, you will probably have a lot of problems, feedline out the window, or not. Sure, you are taking an additional risk, but it's a small one, and maybe acceptable. Unless you have a very large tower, it's probably nearly as likely that lighting will strike your home's wiring, so unless you are unplugging that also, the additional risk of feedline-not-out-the-window is negligible.

#### 2. Don't throw it out the window, but ground it really well, inside.

If you can arrange for a good Earth ground, and put a connector on it, you can detach your feedline and connect it to this ground. This is as good as throwing it out the window, without the difficulties of protecting the feedline's end from the elements. It still wouldn't hurt to have this grounding point be physically away from your valuable equipment, where possible.

Note that in this case, it's important that the ground you use for the feedline when it's disconnected is used *only* for that purpose. It exists to reduces the chances that current from a strike traveling on the feedline will arc into your house wiring, ductwork, pipes, or desk.

If you were to say, connect a radio chassis to this ground, you have now created a real problem, even if you disconnect the feedline, because you *haven't actually disconnected it*. Should lightning strike the power lines, or even strike somewhere close to your house, there could be hundreds or maybe thousands of volts difference between the utility ground at the electric distribution panel, and the extra one you added for the feedline. Your radio is sitting between these two points, a lot of current will flow through it, and you might be sad. Lightning current from a strike on the antenna will likewise go through your radio, to the electric distribution panel. Bad.

## Answer (score 4, by Adam Davis)

There's no easy way to weatherproof it, but only you can know how bad the weather is likely to get, and balance the effort and cost of providing protection against the actual needed protection.

If you do want to throw it outside and protect it, though, one method that works fairly well is to take a piece of capped PVC mounted so the cap is up, forming a tube with the open end down. Mount it to the side of the house within reach of the window or access point, with a little dowel or notched section of the PVC extending from the bottom an inch or two.

When you need to put it away, shove the cable end up into the PVC, then secure it on the dowel with a clip (clothespin, binder clip, etc), or rubber bands, velcro tie, etc.

Taking it out is simply reversing the process. Leave the clip/velcro/etc in place so you aren't scrounging for one when you need to deal with it next time.

This isn't meant to be weather proof, only to provide temporary short term protection for brief storage periods. If you want to store your cable end outdoors for more than a day or two, humidity, bugs, and other issues will arise that this solution isn't meant to solve.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1451/how-to-keep-a-disconnected-coaxial-connector-weatherproof, by Kevin Reid AG6YO, Phil Frost - W8II, Adam Davis. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
