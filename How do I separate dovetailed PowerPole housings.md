# How do I separate dovetailed PowerPole housings?

*Tags: connectors, dc-power · score 4*

## Question

Anderson PowerPole connector housings can be joined side-to-side using dovetail joints molded into the plastic to make a multi-conductor connector, as seen in the conventional amateur radio 12V power positive/negative configuration.

**How does one *separate* the joined connectors, particularly if they have wires attached?** When experimenting, I found it impossible to separate them by hand. I can think of solutions involving a specifically shaped jig and a vise or hammer, but I'd like to know if there's a way to do this that's more practical.

The reason I'm asking is that I plan to make up a wiring harness which is not strictly symmetric but has something inserted in one half and not the other (e.g. a switch or ammeter). I'd like to be able to later change the wire length, termination, etc. of one side without also replacing the other side.

## Accepted answer (score 3, by Kevin Reid AG6YO)

Individual PowerPole housings are in fact easy to separate by hand, assuming they are not locked together in some way.

The reason I found it hard is that the first time I experimented with using the dovetail joint, what I used was actually the outer sides of two pre-assembled ultrasonically welded red/black pairs. Apparently the welding process also affects the outside surfaces of the connectors, because the individual housings slide together and apart easily whereas the welded ones have rougher, harder-to-slide surfaces.

If one *were* starting with housings that are jammed or bonded together, then another approach to reusing the parts as described in the question is to remove one or both *contacts* (terminals) from the paired housings (which requires a specialized tool or careful use of a tiny screwdriver or such), which does the same job of allowing the two wires to be separated.

## Answer (score 13, by Phil Frost - W8II)

Firstly, there's a hole for a locking pin in the connectors. The pin prevents the connectors from sliding apart. If there's a pin in there, you'll need to push it out with a punch.

If there isn't a pin, it's possible the connector was assembled with cyanoacrylate glue. Since the roll pin can sometimes fall out, Anderson recommends glue in applications where this would be a problem. In this case you may not be able to get the connectors apart without damage.

With the roll pin removed, the connectors slide apart. Each side of the connector will have either a groove or a tongue. If one side has a groove, the opposite side will always have a tongue, so you should be able to determine the necessary sliding direction by looking at the connector. An image helps:

If there are wires attached to the connector it might be hard to slide connector apart. If the wire is zipline, it may be possible to separate the wires for a few inches so there's enough flexibility to move the connectors.

If that's not possible, then you may be able to get the contacts out of the housing. There's a tool for doing this. If you don't have or don't care to purchase the tool, then you may be able to improvise something similar with a bent piece of metal.

The contacts are held in place by an internal spring.

You need to get something around and behind the contact to push up the spring. The spring is what retains the contact: by lifting the spring the contact will be free to slide out.

Take care to avoid bending the contact when doing this: if the contact is bent it may no longer make solid contact with the mating connector. Where possible I'd advise discarding the old contacts and attaching new contacts.

## Answer (score 3, by Fred)

The Anderson power pole connectors I had to dismantle were not easy to disassemble by hand. (They were not glued, nor did they have a roll pin.) Using the instructions provided by this website (black goes forward, red goes backwards), I set the bottom of the black connector on top of the edge of a table with the red connector hanging off the table unsupported. I then gently tapped the top of the red connector with a tack hammer, and it moved! From there I gently tapped some more and was able to successfully separate the connectors.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6065/how-do-i-separate-dovetailed-powerpole-housings, by Kevin Reid AG6YO, Phil Frost - W8II, Fred. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
