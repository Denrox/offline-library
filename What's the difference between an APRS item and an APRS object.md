# What's the difference between an APRS "item" and an APRS "object"?

*Tags: aprs · score 6*

## Question

What's the difference between an APRS "item" and an APRS "object"?

A kenwood manual says Objects have timestamps, items do not. What does that mean, and how should it be used?

Also in general: What is a good resource for learning about APRS? aprs.org is not one, since it only has angry rants about implementations doing it wrong, and no explanations about what's right.

## Accepted answer (score 9, by hobbs - KC2G)

Per the spec, which unsurprisingly is found at aprs.org, objects are intended for moving or animate objects of the same nature as a station beacon (people, vehicles, storms, etc.) while items are meant for permanent points of interest (they may come and go, but they're not expected to move) such as hospitals. However, there's no real difference between them, other than the fact that, as Kenwood says, object reports contain timestamps. In practice, clients seem to display them and age them out identically.

Both of them are almost completely equivalent to ordinary position beacons (which can have a timestamp or not), except that an object or item has a name which is different from the callsign of the originating station.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16342/what-s-the-difference-between-an-aprs-item-and-an-aprs-object, by Thomas, hobbs - KC2G. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
