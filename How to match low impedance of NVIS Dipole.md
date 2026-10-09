# How to match low impedance of NVIS Dipole?

*Tags: antenna-system, balun, impedance-matching · score 5*

## Question

I want to match a 50-ohm coax feed wire to a 40-meter NVIS half-wave dipole. NVIS antenna examples I've found are usually based on a regular dipole (72 ohms in free air). However the impedance drops by a factor of four (to 12 ohms) when it is lowered to 7 feet (https://www.w9xt.com/page_radio_gadgets_nvis_antenna.html). (Note: the author's numbers seem not to correlate with his factor, but at any rate the impedance drops very low).

Just for reference, a folded dipole in free air is between 200 and 300 ohms (https://www.w8ji.com/folded_dipole.htm). Therefore, its impedance would drop by a factor of four to 50-75 ohms, making it closely match 50 ohm coax.

My idea was for a regular dipole (not a folded dipole) and use a 4:1 balun to raise the antenna impedance by a factor of four from 12.5 ohms to 50) to match the coax and transmitter impedance.

Problem: Maybe some baluns are not designed to be reversed because the side designed to be high impedance balanced antenna would then be on the unbalanced coax, and vice versa with the low impedance side. Furthermore, transferring power the side driving the low impedance antenna might draw more current than the balun wire was designed for.

I have not found answers in any Radio Amateur's Handbook (I have six ranging from 1956 through 2012), or on the Internet.

**So what is the proper way to match 50-ohm unbalanced coax to 12.5 ohm balanced dipole?**

## Accepted answer (score 2, by Mike Waters)

Where did you hear that a 40m center-fed dipole λ/4 high has a feedpoint impedance of only 12.5Ω? It will be 75Ω or more. *A center-fed λ/2 dipole is only 50Ω at one height.*

Here are some graphs. As you can see, you don't need a 4:1 balun.

### Ignore the top graph in this first image.

### The graph below is based on theoretical values

### 75Ω coax will be a better match, and the worst case VSWR mismatch to your rig will be only 1.5:1.

## Answer (score 6, by Phil Frost - W8II)

Many baluns will work just fine in either direction, though there isn't just one kind of "4:1 balun".

This kind is wound on two cores, and works as a common-mode choke:

A common-mode choke works in either direction, so it matters not which end is balanced and which is unbalanced (or if both ends are unbalanced, or both balanced, for that matter.)

However this kind is wound on a single core and relies on ground potential being at the midpoint of the balanced terminals:

This can work OK given a well-balanced load on the right, and an unbalanced load on the left. But flipped the other way (with the balanced load on the left) it will try driving each terminal of the balanced load to different voltages relative to ground, so you'll get quite a lot of common-mode current.

## Answer (score 4, by Aleksander Alekseev - R2AUK)

From personal experience, a good 1:4 balun (50 to 200 Ohm) doesn't necessary work as a good 4:1 balun (50 Ohm to 12.5 Ohm). You can wind just a 4:1 transformer and use it with a 1:1 balun though.

Another simple way to match any impedance is to use an LC-network. There are a lot of online calculators. Personally I particularly like this one. Using this approach I matched my 40m delta loop antenna to all bands from 10m to 80m using a separate LC-network for each band.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15452/how-to-match-low-impedance-of-nvis-dipole, by Peter Buxton, Mike Waters, Phil Frost - W8II, Aleksander Alekseev - R2AUK. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
