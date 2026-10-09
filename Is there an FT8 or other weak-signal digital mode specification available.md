# Is there an FT8 or other weak-signal digital mode specification available?

*Tags: software-defined-radio, digital-modes, software-development · score 3*

## Question

Is there a complete and programming language independent specification available for the FT8 digital mode? Detailed enough to implement both transmit and receive SDR software from scratch in two different programming languages?

If not, for what popular digital modes are full (programming language and computer independent) specifications available?

The goal is to have a target for an advanced SDR programming exercise in an any arbitrary (Turing and computationally complete) programming language (such as Perl or Swift or Basic or ARM m0 assembly, etc.). This would be for the software equivalent of building ones own radio from basic components (L, C, R, FETs, tubes, wires, etc. -> lines-of-code of elementary ops)

Added: A specification for reliable very-weak-signal (below the noise floor) protocol that is legal to use in within the U.S. amateur bands is preferred. A specification that requires advanced programming and DSP knowledge is not a problem. I do not consider code (other than platform-agnostic algorithmic pseudo-code) or precompiled binaries to be a proper specification. It would be desirable to have the specification complete enough that two independent teams using two different programming languages and platforms could interoperate (communicate) using their implementations of the specified protocol.

## Accepted answer (score 0, by hotpaw2)

To answer my own question:

An article titled "The FT4 and FT8 Communications Protocols", by S. Franke K9AN, B. Sommerville G4WJS, and J. Taylor K1JT, in the July/August 2020 edition of QEX magazine, published by the ARRL, appears to be a (nearly?) complete (textual, not code!) specification of the FT8 protocol, including data formatting, forward error correction, framing, and waveform modulation descriptions.

## Answer (score 4, by Michelle Thompson)

The closest I could find to a specification for FT-8 was on the Wikipedia page for WSJT.

In answer to your second question. I lead an open source project that is designing an implementation of the DVB-S2 and DVB-S2X protocols for amateur terrestrial and space use. The uplink is frequency-division-multiple-access. The downlink is the time-division-multiplexed DVB signal. Advanced SDRs are pretty much a requirement here for both development and deployment.

The transport layer is not MPEG, but is another standard from DVB called GSE, for generic stream encapsulation. This allows IP data to be shipped over the DVB-S2/X link at much lower overhead, and allows for the operator to use voice, voice memo, text, image, video, or any other data that the application layer prepares. We will not be building in a low-rate codec. We have not been happy with codec performance in any amateur digital product. We recommend high rate CODEC2 or Opus, decided at the application layer.

We have really liked working with and learning about DVB-S2/X. You can find our project website at https://phase4ground.github.io/

Many amateur television enthusiasts have switched to DVB-T, so that's another substantial and completely specified open standard available to amateur radio experimenters.

All of these specifications (and many more) are open and available at https://www.dvb.org/

Our uplink is ~75kHz channels of M-ary minimum shift keying. The channels are received by a polyphase filter bank, which in and of itself is a wonderful area to work on.

There are channel assignments and we use Adaptive Coding and Modulation (this is included in the specification along with Constant Coding and Modulation and Variable Coding and Modulation modes). Your station will get as much throughput as possible depending on reported signal-to-noise ratios. Adjustments to coding and modulation will be autonomous.

It isn't necessary to limit research consideration to narrowband weak signal modes that I believe would require some reverse engineering to fully specify.

## Answer (score 2, by B. Horn)

I do have the specification for JT9 if that is of interest to you. It is currently in the form of a pdf. Would you like it emailed to you?

Or would you prefer I paste it on this forum as ASCII text (where the formatting is a bit strange, but...

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9962/is-there-an-ft8-or-other-weak-signal-digital-mode-specification-available, by hotpaw2, Michelle Thompson, B. Horn. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
