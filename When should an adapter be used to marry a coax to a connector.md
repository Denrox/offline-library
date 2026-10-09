# When should an adapter be used to marry a coax to a connector?

*Tags: feed-line, connectors, coaxial-cable · score 5*

## Question

A quick follow-up to [What should I consider when choosing a coaxial cable?](What%20should%20I%20consider%20when%20choosing%20a%20coaxial%20cable.md)

Most commercial rigs come with a PL259/SO239 connector for use with something like the RG8/RG11. In the event the diameter of the cable used is significantly smaller; say RG58/RG59, it may be possible to marry the cable to the connector directly. I've even seen it done, but ...

The alternative, of course, is to use an adapter.

When should I use an adapter to marry an outsized/narrow coax to a connector?

## Answer (score 3, by Dan KD2EE)

Always use a connector intended for the size of coax you are using. Every adapter has a certain insertion loss - a cost, in decibels, of "inserting" it into the line. It's best to use the correct connectors directly on the coax whenever possible.

There are PL-259 connectors available for RG-58. I don't want to endorse any particular vendor, so try your friendly local ham dealer or Google.

## Answer (score 3, by Peter KB1AVL)

Ideally you should use a connect on the cable that matches the radio connector. But obviously, if you are going from say RG8 with a PL259 to an HT with a BNC/TNC/SNA, you are going to have a hard time finding a connector that fits that cable so you'll have to use an adapter. But remember that adapters introduce loss.

If you are going from a small cable to a larger connector, like a PL259 on RG58, there are inserts to resize the outside shield collar to a small diameter to accommodate the cable.

## Answer (score 3, by Phil Frost - W8II)

It's best to simply get the connector sized for the cable. PL-259 connectors are available for any cable size. To put one on RG-58, there are adapters such as Amphenol 182107:

These slide over the cable, and the threads screw into the PL-259 connectors popular among amateurs, which are normally designed to screw on to RG-8.

Alternately, there are connectors designed for direct attachment to RG-58, such as Amphenol 182100:

These require a crimp tool to install. Personally I much prefer crimping: it's easier to get a solid termination, and quicker also.

That said, using an adapter is hardly an issue in practice. The biggest issue I have with adapters is the additional strain on the connectors: the adapters make a longer lever, making for more strain from gravity pulling down on the cable, etc.

An adapter may also be more expensive than replacing the connector.

The insertion loss from an adapter is probably not significant in practice, especially with more modern connectors like BNC or N, and especially on HF. VK3JEG has some emperical data: a PL-259 connector had an insertion loss of 0.2 dB at 145 MHz, and much less at HF. N connector return loss was "almost immeasurable".

Some amount of that insertion loss is due to the non-constant impedance in the PL-259 connector, and thus some of the "lost" power is actually just reflected back at the source. This is equivalent to increasing the SWR, and the [actual losses](What%20is%20the%20actual%20loss%20in%20a%20feed%20line%20with%20high%20SWR.md) in such a situation may end up as less than the insertion loss depending on the particular situation.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/80/when-should-an-adapter-be-used-to-marry-a-coax-to-a-connector, by VU2NHW, Dan KD2EE, Peter KB1AVL, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
