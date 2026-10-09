# Two Antenna Tuners in Series

*Tags: antenna-tuner · score 8*

## Question

My radio has an internal antenna tuner that can be activated to rapidly tune for the frequency in use.

My antenna has a disgusting SWR for the band I want to use (as measured with an AA-54 antenna analyzer). When activating the internal antenna tuner, it reports multiple occurrences of "Bad SWR" (or something like that). I don't know what the radio does with that information i.e. maybe it refuses to transmit?!? (I'd have to look that up in the manual).

Because of this "Bad SWR" report from the radio, I am fearful of burning out my radio by attempting to transmit on this problem band.

If I connected an external antenna tuner between the antenna feed and my radio, would/could the external tuner get the signal into "the ballpark" for a more tolerable SWR and then let the internal antenna tuner fine tune that ballpark SWR for a final SWR that would be acceptable to the radio? Or would it not be of any help?

## Accepted answer (score 5, by Phil Frost - W8II)

A simple tuner might be just a capacitor and an inductor:

For more flexibility, many tuners add a 2nd capacitor to make a pi network:

If you were to have two such tuners:

Well, now you just have more elements which can be adjusted. There's nothing inherently wrong here. In fact it gives you additional tuning range.

Internal tuners usually do not have much range, and it's likely with an external tuner you won't even need the internal tuner. You might consider simply disabling the internal tuner. Or if your external tuner is manual, you could adjust it for a good match at the middle of the band, then enable the internal tuner to compensate for the slight mismatch as you move within the band. If the external tuner is automatic, I can't really think of a reason you'd need both.

Another possibility given your situation: skip the external tuner, and instead just pick some fixed component(s) to make a matching network. It's cheaper than buying an adjustable tuner if you don't already have one, in fact you can probably build it from scrap you already have. And you can then mount it outside at the antenna feedpoint to reduce feedline losses.

## Answer (score 2, by K7PEH)

Often internal tuners are automatic -- that is, they initiate a retune sequence when the SWR drifts too high, usually above some settable threshold or something like above 2:1.

If you are using an internal tuner with an external tuner (which is OK if done right) then you could have problems if the internal tuner is enabled for automatic mode. What may happen is that as you adjust the external manual tuner, you may affect the SWR that the internal tuner sees and it will change automatically as a result. This change though on the internal tuner can affect the external tuner as well. It is even worse if the external tuner is also an automatic tuner. Thus, internal tuners can battle with external tuners in an never ending war of attempting to get a good match.

Usually, a tuner expects input side to be 50 ohms and therefore you should present a 50-ohm impedance to the external tuner by disabling your internal tuner. This is the smart thing to do. Life is simpler with only one tuner being active.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7866/two-antenna-tuners-in-series, by Steve, Phil Frost - W8II, K7PEH. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
