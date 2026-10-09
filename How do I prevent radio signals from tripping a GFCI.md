# How do I prevent radio signals from tripping a GFCI?

*Tags: rfi, grounding, gfci · score 13*

## Question

My wife woke up several nights by a metallic "thunk". It happened to be while I was talking on 10 meters and turned out to be the ground fault circuit interrupter (GFCI) on her hair dryer cord. Apart from the obvious answer of leaving it unplugged, I'm looking for a solution to preventing this because I'm concerned there are other effects of which I'm not aware.

At the time, I had not completed the grounding of my newly set up shack. I've since established an earth ground using a backup water well point pipe in my basement (it's electrically isolated from the pump by a PVC connect pipe and is hardly used so I'm not worried about regular interference from that). Unfortunately, the 12v supply for the HF radio doesn't seem to have a ground stud on it so I can't ground that apart from the regular mains cord ground. The antenna mast is grounded to a typical 8ft ground rod using a 6AWG wire. But despite my efforts at proper grounding, the problem still occurs.

Is the GFCI tripping due to improper grounding or possibly due to RFI (which additional or better grounding wouldn't necessarily fix)? And how could this tripping be prevented? I'm concerned that whatever is causing this could be affecting other more sensitive (and expensive) devices in the house.

(Note that this is an older house - 1960s - and doesn't have any GFCI breakers or outlets where I'd expect there to be any such as the outside, garage or kitchen. So I can't report on similar behavior in other GFCIs.)

## Accepted answer (score 10, by Bill - K5WL)

Some older GFCI circuits were known to be susceptible to stray RF. The ARRL recommends replacing these older breakers with new ones that they have listed at the link I provided.

## Answer (score 8, by Phil Frost - W8II)

It's true, some GFCIs are just abnormally fussy, and you can attenuate RF on a conductor with ferrites.

However, *a lot* of amateur setups have improperly designed or installed antennas. Common-mode RF currents in the antenna feed system will travel right down the feedline, to your transmitter, down its power cord, and into every other device in your house which is connected by the mains wiring, including all your GFCI outlets. Your house, and all the wiring in it, is essentially an oddly shaped radial, and RF currents will use it, if you don't do something to stop them.

A GFCI is effectively a common-mode current detector. When an electrical device isn't electrocuting someone, the current on the hot conductor is exactly balanced by current on the neutral conductor. That is, there is no common-mode current. When you are holding a cold water pipe with one hand, and a faulty hair dryer with another, now some of that current can return to ground through the water pipe. Now the currents on the hot and neutral conductors aren't balanced: there is a common-mode current. The GFCI concludes someone is being electrocuted, and opens the circuit.

Of course, a GFCI can't tell if the common-mode currents are due to you being electrocuted, or exist because your antenna finds your house's wiring as a favorable RF return. It pops either way.

So, before you go off replacing your GFCIs, or getting crazy with ferrite beads behind the walls in all the rooms, I suggest you look at your antenna feed. See [Using a balun with a resonant dipole](Using%20a%20balun%20with%20a%20resonant%20dipole.md). The problem is equally applicable to verticals also: if your antenna isn't on an ideal, infinite ground plane, you might need a balun anyway. Same goes for loops, or any other kind of antenna. Eliminate (to the extent possible) the common-mode currents at the source (your antenna) first.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/63/how-do-i-prevent-radio-signals-from-tripping-a-gfci, by Peter KB1AVL, Bill - K5WL, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
