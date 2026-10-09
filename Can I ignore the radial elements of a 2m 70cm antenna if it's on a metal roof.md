# Can I ignore the radial elements of a 2m/70cm antenna if it's on a metal roof?

*Tags: antenna, grounding, vertical-antenna, radial · score 4*

## Question

I'm looking for a dual band base station antenna, and find that many of them have short radials around the base.

Due to the specifics of my installation, I need to remove them. However, it is being mounted in a way that the antenna penetrates the flat metal roof of the structure (a solid, single sheet of metal about 20'x8'). I can mount it so the roof is at the same location as the radials would have been. I might still attach the radials, in fact, and have copper mesh on the lower side of the roofing metal sheet to contact the radials.

Will this impair performance? Do the radials need to be left alone, or are they simply the grounding mirror for the antenna?

Can I get rid of them, or do I need to have the sheet metal contact the antenna at the base where they attach?

The radials would be on the bottom, and are grounded to the mounting point, and presumably to the coax shield. I'm looking at the Diamond X50A at the moment, but there are many with essentially the same design. The instructions don't provide any help.

## Answer (score 2, by webmarc)

You can remove them and instead attach the shield of the transmission line to the actual roof! It will make a great ground-plane, probably much better than the radials that are currently attached.

Alternatively, connecting a copper mesh will work too.

You will definitely want *something* though, as you'll be giving up some power and efficiency if you just leave it off completely.

Example: next time you have a 2 meter HT with a rubber-duck in your hand, grab a 19-inch (doesn't need to be exact) piece of wire and connect it to the shield/outside of the antenna connector with an alligator clip or similar... basically, you've made it a dipole. You can then test just how much the signals improve/degrade with & without that single wire.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2016/can-i-ignore-the-radial-elements-of-a-2m-70cm-antenna-if-it-s-on-a-metal-roof, by Adam Davis, webmarc. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
