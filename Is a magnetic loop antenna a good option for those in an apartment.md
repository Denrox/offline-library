# Is a magnetic loop antenna a good option for those in an apartment?

*Tags: antenna, magnetic-loop · score 3*

## Question

Are magnetic loops a good choice for those living in apartments or condos where a permanent installation is often not an option and the operator still wants access to the HF bands? Why or Why not?

Edit: Building is from the 1800's, the roof of this building is sheets of steel and the walls are just brick, I am just under the roof, walls are brick, I am on the 4th (top) floor.

Edit2: I have enough options for portable stations i am only looking for an apartment solution at this time.

## Accepted answer (score 9, by hobbs - KC2G)

If you're talking about placing the antenna indoors, there are no *good* options. A magloop might be your *best* option, but:

1.

It's still going to receive plenty of noise (stuff you may have heard about them being insensitive to E-field noise is overblown; it's only true for a specific range of distances, and in any case isn't enough of an effect to override the fact that a noise source ten feet away is orders of magnitude louder than the signal you're trying to receive).

2.

Modern construction apartment buildings often make good approximations of Faraday cages at HF frequencies. Practically no signal makes it in or out. I once played around with operating from a waterfront penthouse (19th floor) apartment on the east coast of the US (sounds like pretty good conditions!), with 100W into a coil-loaded dipole. The result: I could hear very little, and I couldn't even get a single spot on FT8. I could have gotten more signal out operating with 1W from the roof than I did with 100W indoors.

3.

Unless you're willing to go very expensive, loops tend to be limited in power to significantly less than 100W, and they also tend to be pretty inefficient. Probably you're looking at a radiated power equivalent to what you would get from putting 10W or less into a full-size dipole. This isn't impossible, but it does compound with issue #2.

4.

If you *do* go all-out on a large, heavy loop with a high-voltage vacuum capacitor so that you can get more power output, your new problem is that the high voltages and high field strengths near the antenna make it unsafe to get within a few feet of it. Not very easy to reconcile with apartment life.

Again, my opinion is that an indoor apartment antenna for HF is a lose-lose proposition. If you have some kind of outdoor space (like a balcony) then you might be able to put a magloop there without too much trouble, and it might work to some extent (#1 becomes less of an issue if you move it away from the noise and on the other side of a wall, #2 becomes less of an issue for at least one direction, #4 becomes less of an issue, #3 doesn't really change). However if I was stuck in that situation I would probably look for alternatives like a loaded vertical (with a downspout or fire escape as counterpoise), a loaded dipole, or a "throw it out the window" end-fed, all of which might be more tractable than a magloop.

## Answer (score 5, by hotpaw2)

In, meaning Inside an apartment, a magnetic loop may not be a good idea for transmit, as the RF magnetic field can couple very strongly to any household wiring or appliances inside, window frames, etc., possibly causing hazards as well as severe pattern distortions and losses. For receive it might be Ok if the walls (stucco wire, metal siding, etc.) do not approximate a Faraday cage.

Outside on an apartment balcony or small yard, a magnetic loop is likely fairly efficient compared to anything else of similar height and spherical volume, and there are reports of this working for both Rx and Tx. A mag loop on an extended horizontal flagpole off a balcony railing might be a workable placement, if safe. But as with any antenna placement, YMMV... by a lot.

If you can get roof or attic access over your apartment, you may have more options.

## Answer (score 3, by webmarc)

Definitely read Hobbs's answer re ins-and-outs of mag loops, spot on... I don't have anything to add on that part.

Another option is to make friends with the building super. Depending on his/her disposition, you may be able to get permission to drop a line from the roof to your window. I had GREAT luck with this in one of the buildings I lived in (Washington DC) and also struck out in another building... it just depends.

Finally, if your window opens and you're on a high enough floor, you may have great success with a dangling EFHW or OCFD (whip up, long wire down) or other similar options.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17665/is-a-magnetic-loop-antenna-a-good-option-for-those-in-an-apartment, by hehe3301, hobbs - KC2G, hotpaw2, webmarc. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
