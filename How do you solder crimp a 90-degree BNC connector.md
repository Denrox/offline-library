# How do you solder/crimp a 90-degree BNC connector?

*Tags: feed-line, connectors · score 7*

## Question

I ordered this 90-degree BNC connector, but I'm not sure how to connect the center pin. The back of it looks like this:

The small screw plate threads into the back when you're done connecting the wire.

But how does the wire connect? The hole is quite small, not sure if I can get a solder tip in there. Maybe I can, but it will be a tight squeeze and could end up being a poor solder joint. Also the hole is too small to squeeze with needle-noise pliers, and even if I could I'm not sure it would compress hard enough to make a good connection.

Has anyone ever connected one of these?

## Accepted answer (score 7, by tomnexus)

You strip the coax to fit, and solder the pin to the coax. Don't leave any wire sticking out past the pin. You don't and can't crimp it.

Here's a video I found of a similar connector.

If your iron doesn't fit, its tip is probably too big for connector work in general.  
If you use a bit of flux and some care, you can probably alternate poking the iron and the solder into the hole, it doesn't need to fit both at the same time.

Stripping is always by trial and error - even if your connector comes with detailed instructions, you usually need to adjust them. Go with what feels right, once you've deduced the general principles from the instructions.

The VSWR of these connectors is much worse than the straight ones as the impedance isn't well controlled but at 440 MHz it shouldn't be a problem. In general there are some awful BNC-related things in the world - BNC Tees with little springs for the centre leg of the T, etc.

The all-crimp version of this BNC has a little pin which you crimp onto the inner, this then plugs into an *internal* socket deep inside the connector before you crimp the braid.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21507/how-do-you-solder-crimp-a-90-degree-bnc-connector, by KJ7LNW, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
