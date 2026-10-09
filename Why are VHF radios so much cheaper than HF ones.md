# Why are VHF radios so much cheaper than HF ones?

*Tags: hf, vhf, transceiver · score 3*

## Question

Why do VHF-UHF radios tend to be cheaper than HF ones? There are expensive VHF radios and relatively cheap HF ones, but finding a cheap VHF radio is much easier than finding a cheap HF radio. Why? Aren't HF radios simpler?

## Accepted answer (score 5, by user10489)

I think the premise of the question is actually incorrect.

The things that make a radio expensive are receive sensitivity, output power, frequency agility, and modulation/demodulation circuit complexity. VHF and higher frequency generation use to be a big cost in the radio, but there are now integrated circuits that can do this cheaply, and the cost of an off the shelf VHF vfo is now lower than a hand built HF vfo.

HF radios can be found or built for under \$150 easily. The catch is that they are simple, single band, low power, and have low sensitivity, just like the cheap VHF radios of the same price range. The super cheap VHF ham radios (under $50) cut a lot of corners and have dramatically lower sensitivity as well as corresponding spectrum impurities and splattering.

Additionally, expensive VHF radios exist that are multi-band, multi-mode, higher power, and have higher sensitivity designed for use in weak signal receiption.

And just to add a bit of economics to this, cheap HF radios are not in high demand, and so typically end up as kits. Cheap VHF radios are mass produced with a high level of industrial design and surface mount components, which dramatically decreases per unit production cost.

Also, to some extent, frequency agility and mod/demod can now be done cheaply in SDR, so this is now less of an issue than it use to be. Sensitivity can also be increased with SDR, but this is not yet cheap. (It's cheaper than doing it with analog components, but still more expensive than leaving it out.)

So, to summarize, expensive HF and VHF radios with feature parity will have a similar price. Cheap VHF radios might beat cheap HF radios purely due to mass production economy of scale. The final irony in this is that some modern cheap HF designs upconvert the signal to take advantage of cheap mass produced VHF components.

As an extreme example of this, you can get a complete broadcast AM/FM receiver in a single chip for under $2. Catch is, it is receive only, and it doesn't need any sensitivity because it is receiving a 20KW+ broadcast station 50 miles away instead of a 100W HF ham station 1000 miles away. (And broadcast AM is between ham HF bands and ham LF bands anyway, so HF/VHF not a factor in this.)

## Answer (score 4)

Most VHF radios are relatively low power. They need to reach the closest repeater or just a few miles to another radio in simplex. They are not used or long distance. They typically are only VHF or VHF/UHF. Most are restricted to FM modulation. Also many VHF HAM radios are variations of commercial VHF radio which are produced in relatively large quantities.

HF radio tend to be higher power, cover many different bands, have several different types of modulation (FM, SSB, AM, CW, and so on). They are also produced in far smaller quantities as they are only used by HAMs.

## Answer (score 3, by Marcus Müller)

Why do VHF-UHF radios tend to be cheaper than HF ones?

That's an economic question, not a radio technology one. How many radios of either type are sold per year? For which of the two types will hence cheap mass-produced devices exist?

Who is more likely to spend more than a device is worth: Someone who needs a handheld radio, or someone with space for a HF antenna system?

Aren't HF radios simpler?

No. (Why should they?)

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21403/why-are-vhf-radios-so-much-cheaper-than-hf-ones, by Someone, user10489, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
