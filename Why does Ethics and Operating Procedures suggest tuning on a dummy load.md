# Why does "Ethics and Operating Procedures" suggest tuning on a dummy load?

*Tags: antenna, procedure, equipment-operation · score 9*

## Question

The seminal work "Ethics and Operating Procedures for the Radio Amateur" suggests in subsection II.8.1 to perform tuning only on a dummy load.

Sometimes before transmitting it is necessary to tune (adjust) the transmitter (or antenna tuner). Tuning should in the first instance be done on a dummy load. If necessary, fine tuning can be done on a clear frequency with reduced power, after having asked if the frequency is in use.

My understanding is that a dummy load matches the transceiver impedance so tuning is probably a) not necessary and b) without any predictive value for how the actual antenna will work with the tuning parameters. What am I missing?

## Accepted answer (score 11, by Kevin Reid AG6YO)

The text you refer to seems to be (emphasis mine):

Sometimes before transmitting it is necessary to tune (adjust) the transmitter (or antenna tuner). Tuning should **in the first instance** be done on a dummy load.

This is not referring to the use of an antenna tuner, whether integral or external. Rather, it is referring to tuning the final output stage ("finals") of a vacuum-tube-based transmitter (or external power amplifier). These are also impedance-matching adjustments, but involve elements internal to the transmitter/amplifier rather than exclusively the transmitter to the antenna. (The antenna impedance is also involved, so in some cases there could be some amount of antenna matching, if not as much as a dedicated antenna tuner. Or so I understand — I'm not an expert on this part of the technology.)

Solid-state radios operate differently and do not require these adjustments, so the recommendation you read does not apply. However, there are other uses for transmitting into a dummy load — for example, checking if your microphone is working, you're not over-modulating, or even that a computer-controlled transmission is correctly controlling your radio's frequency and PTT.

## Answer (score 5, by Mike Waters)

We use a non-radiating dummy load at first *so that we minimize the chance of interfering with others*.

When our tuning adjustments are as close as they can be using that, **then** we can switch over to our antenna and make any needed adjustments.

The HF bands are full of annoying carriers because hams perform their entire tuneup procedure into their antennas.

## Answer (score 2, by Phil Frost - W8II)

There are two ways the text could be interpreted:

1. First tune to a dummy load. Then, switch to the antenna and tune again.
2. First tune your transmitter for a 50 ohm load, using a dummy load. Then tune your (separate) antenna tuner to present a 50 ohm load to the transmitter.

The first case, which is how I first understood it, doesn't make any sense unless you know the antenna is 50 ohms.

In the case where you have a transmitter that requires tuning (common for tube equipment) *and* an antenna tuner, then the second sense makes sense.

Though in either case I have a better solution: make a mark where the knobs should be set for a 50 ohm load: then you can return to this setting without any dummy load at all.

Here's what you need to know about tuning:

- Try to do it on a clear frequency. Avoid doing it on recognized calling frequencies.
- Do it at low power, if possible.
- Keep it short by writing down the approximate settings for each band beforehand.

More generally, I think half that document is absurd, and I wouldn't take anything it says too seriously. Consider the first sentence of http://www.hamradio-operating-ethics.org/:

Over the past decades, and not surprisingly together with the introduction and growth of the Internet, the behavior of the radio amateurs on the bands has significantly deteriorated.

Kids these days, am I right?

I would call it not so much a "seminal work", rather than an overbearing, 68 page tirade by a couple people upset that not everyone does everything exactly how the authors do it. Half the work has legitimate information on basic procedure, but the other half is common sense or just the author's particular operating habits presented as authoritative procedure.

For example:

Some subjects which are a **no no** in amateur radio conversations on the air are:

- religion
- politics
- business (you can talk about your profession, but you cannot advertise for your business);
- derogatory remarks directed at any group (ethnic, religious, racial, sexual etc.).
- bathroom humor: if you wouldn't tell the joke to your ten year old child, don't tell it on the radio;
- any subject that has no relation whatsoever with the ham radio hobby.

People use ham radio to talk about the weather, their health problems, or to make plans to meet friends. I don't know what these things have to do with the ham radio hobby.

Another example:

Saying 'CQ from Victor Romeo two Oscar Portable' is not very clear. Either VR2OP calls SQ using an incorrect spelling phonetic, or VR2O/p calls CQ and omits to add the expression 'stroke' while calling CQ. This can lead to a lot of confusion.

This is what's called a false dilemma. There's a 3rd possibility: VR2O is portable. That's how I understand it, anyway. Sometimes people even say "mobile" instead of "portable", but I don't find it confusing at all.

Call CQ: ‘CQ from G3ZZZ, G3ZZZ calling CQ, golf three zulu zulu zulu calling CQ and listening’. At the end you may say ‘...calling CQ and standing by’, instead of ‘...and listening’. One could also say: ‘...and standing by for any call’.

I just assume anyone calling CQ is standing by for any call. I just end with "calling CQ", but reading this document makes me feel like I must be "doing it wrong" and the ham radio procedure police are probably going to arrest me.

If signals are not very strong and if the readability is not perfect, you can spell out your name etc. Example: 'My name is John, spelled juliett, oscar, hotel, november ...' Do NOT say '...juliett juliett, oscar oscar, hotel hotel, november november'. This is **not** the way you spell the name **John**.

I have never once heard anyone doing this. Reminds me of four shalt thou not count...

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12539/why-does-ethics-and-operating-procedures-suggest-tuning-on-a-dummy-load, by xmjx, Kevin Reid AG6YO, Mike Waters, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
