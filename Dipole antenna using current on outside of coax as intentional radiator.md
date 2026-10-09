# Dipole antenna using current on outside of coax as intentional radiator?

*Tags: antenna, antenna-construction, coaxial-cable, choke-balun · score 3*

## Question

Is there an antenna design somewhat like a coaxial dipole, where the coax ends in a quarter-wave radiator, but instead of an explicit coaxial radiator running back over the coax body, the outer surface of the coax is the radiator, much like common-mode currents arising with some coax-to-dipole antennas? The coax could have a choke at the quarter-wave point along the coax to prevent the remaining coax from radiating. How well does / would this work?

(My internet searches have not identified anything similar to this idea, just current baluns and coax dipoles.)

## Accepted answer (score 4, by natevw - AF7TB)

Yes, for example see "End-Feeding a Center-Fed Vertical Dipole" and iiuc sometimes the concept is called a "bazooka dipole" as well.

While not a fatal flaw, I think the "gotcha" lies with this part of the plan:

The coax could have a choke at the quarter-wave point along the coax to prevent the remaining coax from radiating.

If you look in that first presentation link (by Jim Brown, K9YC) you can see it takes some significant engineering to implement a choke that can handle the requirements placed upon it in this application, and handle them efficiently.

I've mostly only done "armchair" research on this so far; personally I keep circling back to it as an attractive idea. **But** each specific time, a more traditional approach (e.g. a monopole, or perpendicular feeding, or an end-fed, or … etc. etc. …) ends up seeming like a more practical way to accomplish my actual real-world goals in the end.

## Answer (score 3, by webmarc)

Yes. You can google for a "flower pot antenna" to find this design for VHF and UHF bands, so named for the ability to stealthily have an antenna disguised on one's apartment balcony in a flower pot.

This VHF example uses a simple coax-coil as a choke (as you posit in your question), though I suspect it's a good idea to augment this.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/22036/dipole-antenna-using-current-on-outside-of-coax-as-intentional-radiator, by ralph vanhoek, natevw - AF7TB, webmarc. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
