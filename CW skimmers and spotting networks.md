# CW skimmers and spotting networks?

*Tags: cw · score 4*

## Question

What are CW skimmers, especially with regard to spotting networks? Are there more than one (of each)? How do the skimmers interface with spotting networks? (Or are they combined into a single application?) Is there an open protocol?

Is there a controversy regarding the use of CW skimmers and/or spotting networks for certain purposes? (e.g. contests, DX pile-ups, SKCC, etc.) If so, what is the controversy?

## Accepted answer (score 4, by rclocher3)

Computerized Morse decoders have been around for quite a while, but until recently they had many limitations. The original style of decoder, what one might call the "first generation", listens to a very narrow frequency range of a few hertz at most, and tries to interpret whether a single signal's carrier is present or not. Such decoders work fairly well for well-formed code when conditions on the bands are good and there is no man-made interference (QRM). Noise on the bands (QRN), fading (QSB), interference, or badly-formed code from a straight key or a "bug" tends to quickly destroy the intelligibility of the decoded text from such a first-generation decoder.

Please note that deciding if a signal is present or not is a difficult problem for a simple decoder circuit or algorithm. Radioteletype, RTTY, is much, much easier for such a circuit or algorithm to decode: instead of deciding whether a weak signal in a noisy environment is present or not, the algorithm has only to decide if the signal at one particular frequency is louder than the signal at another frequency, because an RTTY signal constantly alternates between two different tones at a 100% duty cycle.

Hams used such first-generation Morse decoders in contests, but their use wasn't very controversial, because such decoders work on only a single signal, and are easily out-performed by the ear of a skilled operator, especially in typical HF contest conditions where QRN, QRM, and QSB are rife.

Then Alex Shovkoplyas VE3NEA changed everything, when he released his software CW Skimmer. CW Skimmer uses DSP (digital signal processing) techniques and more advanced algorithms to decode every Morse signal in a receiver's entire passband. And because the software can be passed the receiver's entire passband in I and Q format, simple and inexpensive SDR receivers can be used that have enough bandwidth to cover the entire Morse code part of an HF band. The decoding isn't perfect, but it's very good, an enormous improvement over first-generation decoders. The software also estimates the signal-to-noise ratio, which gives a fairly good estimate of how accurate the decoding might be, which is important when an operator is trying to decide if CW Skimmer really did hear the incredibly-rare DX prefix in a call sign or not.

I should mention that CW Skimmer has a built-in telnet spotting server, so it interfaces with contesting software just like a spotting network. Really, it *is* a built-in spotting network.

To answer another question that was asked, no, there is no public CW Skimmer protocol, other than the well-known telnet protocol used by internet spotting networks. CW Skimmer is closed-source proprietary software. It's shareware, which allows users to try the software for free for 30 days before deciding whether or not to buy it.

This revolutionary improvement in machine decoding quickly became controversial in the contesting community, which was just settling down after a long public discussion about how contests should handle hams using spotting networks. (Should there be separate categories for operators using spotting networks? How should the inevitable cheaters be caught? And so on.)

Fortunately, the controversy over spotting networks that had recently been largely resolved lead to guidelines that could be applied to the new controversy. Most contest committees quickly decided that using CW Skimmer during a contest meant that the operator or operators are in the "assisted" category, the same category that operators using spotting networks are in.

However, there's one particularly controversial technique: operators can monitor the output of a CW Skimmer connected to a remote receiver at a different location. Some contests, like the CQ WW CW contest, simply don't allow remote receivers, which makes that technique cheating in that contest. Other contests, like the ARRL DX CW, allow operators to listen to remote receivers as long as they are *public*; it's not cheating unless the operator is listening to a *private* remote CW Skimmer.

CW Skimmer isn't controversial for DXing, because there's no way to police whether operators use it or not. Operators use it and they can't be stopped, so it has changed DXing forever, like it or not, and has generally been grudgingly accepted.

You didn't ask about the Reverse Beacon Network, but no discussion of CW Skimmer is complete without talking about the RBN. What is the reverse beacon network, and why is it "reverse"? Well a normal beacon "network" consists of several beacons transmitting from different locations. An operator can tune in to the beacons, and which beacons can be heard gives a good idea of where the band may be open to.

The Reverse Beacon Network is simply a network of stations running receivers connected to computers running CW Skimmer in different places. To test the RBN, one transmits a quick CQ, and then checks to see which RBN locations heard the signal. Using a typical beacon involves listening, but using the RBN involves transmitting, which is why it's the "reverse" beacon network.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15074/cw-skimmers-and-spotting-networks, by hotpaw2, rclocher3. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
