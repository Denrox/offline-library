# Power connector for a HPA

*Tags: power-supply, dc-power · score 4*

## Question

I've got two Kuhne's HPAs rated at 12V, 10Amps. The HPAs have power connectors circled in blue. Is there a specific jumper with a compatible head that I could plug directly into this connector? I'm trying to avoid soldering if possible.

## Accepted answer (score 2, by tomnexus)

This is a feedthrough capacitor, it helps to filter the power and control lines entering the enclosure. It will have some capacitance to the body, and probably a small ferrite bead around the conductor.

You need to solder a wire to it.

But remember it's just the copper leg of a component, it's not very strong! The ground lug next to it may provide some strain relief, otherwise put a screw into the heatsink below it. If you pull the wire and snap it off, it will be a pain to repair.

Do it like this [own work]:  
and not like this [apologies to [VK6UU]](https://www.vk6uu.id.au/Repeater-Project.html):

## Answer (score 4, by Mike Waters)

I've seen these before, and they need to be soldered.

What you have is a solder-type feedthrough capacitor with a solder-type ground lug next to it.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21244/power-connector-for-a-hpa, by Moses Browne Mwakyanjala, tomnexus, Mike Waters. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
