# What is the frequency range 2300-21950 kHz used for?

*Tags: frequency · score 5*

## Question

I was checking out the gizmo mentioned in this [question](Can%20an%20antenna%20be%20too%20powerful%20for%20certain%20receivers.md), and I see that it can receive "shortwave" in the frequency range 2300-21950 kHz. Most times I see "shortwave" mentioned, it's by sales or nontechnical people to describe any number of things. I've taken it to mean that it covers commercial AM and FM stations in the 87-108 MHz (FM) and 520-1710 kHz(AM) range, and possibly the weather band (~160 MHz).

But the Tecsun also can receive in 2300-21950 kHz. What does this frequency range do? What is it used for? Why would this be useful in a presumably emergency-related receiver?

Searching for that range finds product reviews for this device and similar devices. I was able to find this chart, but it has no explanation.

## Answer (score 11, by Phil Frost - W8II)

"Shortwave" means roughly the same thing as "HF": 3 to 30 MHz.

It definitely does *not* include the FM broadcast (around 90 MHz, too high) or AM broadcast (around 1 MHz, too low) bands received by a typical car radio.

Shortwave frequencies have the unique property of supporting ionospheric propagation, which means under the right conditions they can propagate globally.

3 to 30 MHz is a large chunk of spectrum and it is not all allocated to any one use. Of particular interest may be the shortwave broadcast bands which are several allocations set aside by the ITU (and thus in turn, most national regulatory authorities) for broadcast stations intended to be received by the public.

Due to the potential for global propagation, these broadcasts tend to offer interesting international programming not available on the ordinary AM and FM bands. International news (sometimes propaganda), language lessons, and religious broadcasts are some of the things you might find.

The ITU allocated shortwave broadcast bands are:

- 3200-3400 kHz
- 3900-4000 kHz
- 4750-4995 kHz
- 5900-6200 kHz
- 7200-7450 kHz
- 9400-9900 kHz
- 11600-12100 kHz
- 13570-13870 kHz
- 15100-15800 kHz
- 17480-17900 kHz
- 18900-19020 kHz
- 21450-21850 kHz
- 25670-26100 kHz

Not all of these allocations are permitted globally, nor are all broadcasters following the rules and staying within the allocations. It's not difficult to find stations just tuning around, or use a site like short-wave.info to find known stations.

## Answer (score 4, by rclocher3)

Frequencies are allocated by governments, often in accordance with international treaties. You didn't say what country you're in, but in the United States that broad frequency range has dozens of allocations; see this chart (PDF) published by the US Department of Commerce, and linked to from this Wikipedia article. By the way, I'm not sure what "fixed" means on the chart, but I suspect that those allocations are to the US Government.

Generally speaking, "shortwave" refers to frequencies from 3 – 30 MHz. Signals at those frequencies reflect off the ionosphere, at least some of the time, so those frequencies are useful for long-range communication. The Tecsun receiver you mentioned probably includes those frequencies so that users can tune in the shortwave broadcast and amateur bands contained in that frequency range.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12536/what-is-the-frequency-range-2300-21950-khz-used-for, by YetAnotherRandomUser, Phil Frost - W8II, rclocher3. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
