# APRS: what is with stations clustered in the middle of a lake?

*Tags: aprs, equipment-operation · score 3*

## Question

I just recently started using APRSdroid, and I've been just looking at maps, and I've noticed that in my area there are spots with just a cluster of stations on top of each other (in this specific case, in the middle of a lake??). I'm the car icon SW of the cluster.

What is going on? I've noticed a similar behavior another town over, but on land. Are people all just saying that's their location for personal reasons or is there another reason?

## Answer (score 5, by Kevin Reid AG6YO)

Two relevant facts about APRS:

- APRS stations are not obligated to get their location from GPS. And in practice, many fixed stations have manually entered locations.
- It is possible to transmit an explicitly coarse location (removing digits from the right).

I do not think that this can be a coarse location because I cannot reproduce that center of lake point by dropping digits (from a latitude and longitude expressed as degrees and decimal minutes, as APRS does). Nor is it the center (or corner) of a Maidenhead grid square.

Therefore, my best hypothesis so far is that it is FOR SOME REASON a deliberately entered location for those stations. Perhaps there is a local group which did not want to reveal their home addresses and they agreed they'd all use the lake as their location, as an obviously-not-real location.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9584/aprs-what-is-with-stations-clustered-in-the-middle-of-a-lake, by J. Polfer, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
