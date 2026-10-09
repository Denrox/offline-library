# Suggestions for HF antenna for occasional use on my sailboat

*Tags: wire-antenna, end-fed-antenna, marine · score 4*

## Question

I have had a license since I was a kid, but have not touched anything ham radio related in years. I have been thinking about diving back in and combining it with my sailing. I'm looking for thoughts on an HF antenna that I can easily deploy when needed, which will mean at the dock or anchor and not while underway.

My sailboat is a 30 feet long and has a mast that stands 38 feet above the deck. The distance from the mast step to the aft most point is 18 feet, so if this is a right triangle, the length of the hypotenuse is 42 feet.

I am thinking that a half wave, end fed antenna that could be made to work on 20, 15 and 10 meters would be easy to hoist between the stern and the mast head when needed and would appreciate your thoughts. Also, are there end fed quarter wave antennas? If so I could have one for 40 meters as well. I would prefer to avoid a tuner just because it's one more thing on a small boat.

One other consideration is that, being a sail boat there are 1/4 inch stainless steel cables which hold the mast up. I'm really not interested in putting insulators in these cables or trying to load them as antennas, but I am wondering what interference or impact they might create.

UPDATE: The boat is used primarily for racing so this is the cause of my hesitance to modify the rig.

Also, the mast is "deck stepped" which means that it's bottom sits on the deck. On most sailboats, the mast actually does down through the deck and sits just above the keel.

At the top of the mast is an existing small VHF antenna for the marine VHF radio with a feedline inside the mast.

## Answer (score 3, by Phil Frost - W8II)

I'm really not interested in putting insulators in these cables or trying to load them as antennas

That's a shame, because the mast and the cables probably make an excellent antenna. In fact unless you go through some trouble to get the antenna far away from the mast, or oriented orthogonally, the mast and cables are going to end up being a significant part of the antenna whether you like it or not. Remember you don't need a DC connection: mutual inductance and capacitance will couple things together at RF.

You don't need to put insulators on the cables. Finding a good feed arrangement will take some experimentation, but there are plenty of ways to couple into the mast which don't involve any structural modifications, which I guess is your fear.

If the mast, cables, and hull make a closed loop anywhere, you can put a smaller loop within that and feed the small loop. The two loops effectively make a transformer.

Another method is to clamp a ferrite around one of the cables or the mast, and also run several turns of wire through the ferrite, and feed that. Again, a transformer feed. This works even if there's not a loop to feed. That is, you could clamp such a ferrite around a metal pole stuck in the ground (or the water) and make a fine antenna. A mast on a sailboat is not far from this. Might get tricky to find an appropriate ferrite at higher frequencies or higher power levels though, but might be great for QRP operation on 40 meters.

A [gamma match](What%20is%20a%20Gamma%20match%20in%20the%20context%20of%20the%20driven%20element%20of%20a%20Yagi%20antenna.md) is another option which not only solves the problem of coupling into the mast without structural modifications, but also gives a couple variables to provide a decent match.

If you run a wire up the top of the mast like SDsolar suggests, you've effectively made a crude gamma match. The mast and the wire together make a transmission line. By varying the length of that wire you change the length of that transmission line. You can also decide to connect the wire at the top to the mast or not, which will give you an open or shorted transmission line stub which functions as a kind of stub match.

These are just a few options. For further ideas you can research existing methods of coupling into loop antennas or shunt feeding towers, which are similar problems.

## Answer (score 3, by AA1K Jon Zaimes)

I own an O-Day 272LE sloop and have been operating HF on it for the past several years, including serious Field Day operation from along Delaware Bay and Rehoboth Bay in Delaware.

The stainless-steel cockpit railing makes a good mount for vertical antennas on the stern and bow. This allows for maximum separation from the boat's rigging. For serious FD operation, I use a telescoping MFJ 33-foot mast for 40 meters and a 1/4-wave aluminum tubing 20-meter vertical. Also have used 1/4-wave verticals for 10 and 15 meters though found there wasn't enough activity there to warrant the trouble.

I also have used a gamma match on one of the shrouds to get on 80 meters and made a few QSOs with that. This could also be done for 40 meters. For casual operation I just mount a single-band mobile whip on the stern rail, such as the Hamstick or MFJ-1620T using a mount designed for putting an antenna on a truck mirror.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7630/suggestions-for-hf-antenna-for-occasional-use-on-my-sailboat, by Jim Archer, Phil Frost - W8II, AA1K Jon Zaimes. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
