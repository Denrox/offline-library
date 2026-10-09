# WIFI Antenna Design

*Tags: antenna, antenna-construction, wifi · score 3*

## Question

I have designed a dual band WIFI antenna (2.4-2.5GHz and 5.1-5.7GHz). In 2.4GHz it's completely omnidirectional but with negative gain and in 5.6GHz it's somehow directional but with very good positive gain. why is this?? Where have I been wrong?

## Accepted answer (score 1, by victorbg)

Just to make it clear - if you're wondering why the directivity changes from one configuration to the other, there is no clear answer. The directivity of an antenna varies a lot, depending mostly on the shape of the antenna.

If you're wondering why you have this particular link between directivity and gain, it is actually logical that you would find this:

$G = E_{antenna} D$

Where $E_{antenna}$ is the antenna efficiency (you can look it up on wikipedia). If you have an omnidirectional antenna, you have a lower directivity, and thus a lower gain than for a directive antenna.

This being said, you might also have a different antenna efficiency for those two frequencies, explaining a bigger gap than what you would obtain with only the directivity thing.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/3855/wifi-antenna-design, by user4621, victorbg. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
