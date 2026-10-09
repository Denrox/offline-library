# What's the difference between "maximum usable" and "critical" frequencies?

*Tags: hf, propagation, map · score 10*

## Question

In discussing HF ionospheric propagation, you hear about both "critical" and "maximum usable" frequencies. For example:

Above the critical frequency, the ionosphere is unable to refract the signal back to Earth and it escapes to space. The critical frequency during the day is in the neighborhood of 6m: depending on the space weather, 6m way work for skywave, or it may not.

(from [https://ham.stackexchange.com/a/1757/1362](Which%20HF%20bands%20are%20best%20during%20the%20day%20and%20which%20are%20better%20at%20night.md).)

I've found maps for both F2-Layer Critical Frequency and Maximum Usable Frequency, and they're quite different — the Maximum Usable Frequency map seems much more "optimistic", that is, the frequencies are much higher at any given location.

What's the difference between the two measures?

## Answer (score 8, by natevw - AF7TB)

The maps are related, but as this excellent posting describes:

The 'critical frequency' is the highest frequency that gets reflected when it is aimed straight up at the ionosphere.

However:

…as the angle decreases from vertical the reflected frequency increases.

And so therefore:

MUF or MOF is a path dependent value. It depends not only on the state of the ionosphere but also the path between the end points. […] What you may see for a MUF map is what is often called M3000, or some similar value which is the MUF calculated using a single 3000km hop with that point as the center.

So basically, the critical frequency *is* the most pessimistic because it's showing what signals will reflect in the very "worst case" (i.e. straight up) above each particular location.

The maximum usable frequency would be estimated based on the expected path the signal would take between two points, and could be significantly better if the expected angle of incidence is more oblique.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6463/what-s-the-difference-between-maximum-usable-and-critical-frequencies, by natevw - AF7TB. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
