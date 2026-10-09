# Why are germanium diodes specified in amateur radio designs?

*Tags: electronics · score 10*

## Question

It's somewhat common to find a schematic that calls for a germanium diode in amateur radio contexts. For example:

This is a QSK circuit from the Fldigi manual.

And yet, purchasing a germanium diode is a relatively difficult task. For example, Mouser's offerings from 600 manufacturers doesn't seem to include a germanium diode:

(Although, they do have a few germanium BJTs)

Germanium diodes can be found elsewhere, mostly from surplus or specialty stores, for a cost orders of magnitude higher than most other discrete semiconductors.

Why is it so common for amateur designs which do not appear to have any particularly stringent performance requirements to call for a relatively expensive diode not available through commodity channels?

## Accepted answer (score 6, by Mike Waters)

The lower forward voltage drop (0.3 volts or even less), compared to silicon diodes (0.7 volts or more).

Having said that, there are some schottky diodes with a low forward voltage drop, too.

## Answer (score 7, by user3486184)

A lot of designs that include germanium diodes are older, or based on older designs, when germanium diodes were commonly available.

On the page for Germanium, Wikipedia says, "From 1950 through the early 1970s, this area provided an increasing market for germanium, but then high-purity silicon began replacing germanium in transistors, diodes, and rectifiers".

When germanium diodes started getting replaced with silicon diodes, there was lot of old stock that could be had relatively cheaply. Hams took advantage of that in their designs.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9133/why-are-germanium-diodes-specified-in-amateur-radio-designs, by Phil Frost - W8II, Mike Waters, user3486184. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
