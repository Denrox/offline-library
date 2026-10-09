# Is it possible to comply with FCC regulations using a mode that takes over ten minutes to send a call sign?

*Tags: legal, fcc · score 4*

## Question

Is there any legal way to use an extremely slow mode that takes over ten minutes to send a call sign?

## Accepted answer (score 7, by Marcus Müller)

Sec. 97.119 Station identification

(a) Each amateur station, except a space station or telecommand station, must transmit its assigned call sign on its transmitting channel at the end of each communication, and at least every 10 minutes during a communication, for the purpose of clearly making the source of the transmissions from the station known to those receiving the transmissions.

There's nothing said in there about the identification having to be in the same slow mode, it just says it needs to be on the same channel.

**Relatively technical talk below**. This was written with in the mindset of someone who's had formal education in designing transmission schemes and systems. I don't know whether that applies to you – if not, feel free to ask! There's a *conclusion* below, which I'll try to make more generally accessible.

And I'll argue that's not a big deal. Your slow mode is going to be of a nature that is designed to deal with noise having more power at the receiver, anyways. That means that the "stupidest possible" solution to having to send your identification in the middle of your transmission is to actually just… sending that ID in a less robust mode (your pick of §97.119 (b): (1), (2) or (3)) replacing what you would have transmitted in the same time in data. To your receiver this will just look like interference, and the error correcting capabilities of the system will have to deal with it. If it can't, you just need to add more redundancy (or increase interleaver length to make that burst error into a bunch of more isolated errors that can be more easily corrected).

Of course, instead of just playing interferer with yourself, it'd be smarter to just specify a so and so many milliseconds gap every 10 minutes into your mode for identification purposes, which gets ignored by a compatible receiver. Your transmission of course gets even longer that way – but I'll argue that if you go with §97.119 (b)(1), so, morsing your callsign, you can always do that within 80 "morse time slots"¹, i.e. 80 channel accesses or symbol durations or spread-sequence chips, depending on how you think of your transmission scheme. That way, your identification stays in your system's bandwidth.

Depending on your slow mode, you could also combine data signal and identification. For example, if your mode is based on FSK, you could just increase/decrease the power to emulate a CW keying without stopping to transmit. Of course, the FSK symbols with decreased power will have worse symbol error probabilities, but your error correction scheme could be designed to account for that. (Or, you say, fuck it, and just let the existing error correction deal with it).

From a slightly higher-up perspective:

You're designing an extremely slow mode, which means you're designing for a high-loss channel. You asking here and about FCC regulation means your channel is high loss due to long distance (and not because it's a submarine communicating through saltwater and ice, or because it's an exvacator in a salt mine communicating with mining operations on the surface).

Your channel being long distance operations means that *a lot* of things can happen in 10 minutes. Chances are your channel is not coherent for 10 minutes, and even oscillators are not going to be stable for so long. So, you'd go for incoherent detection (something like PPM, or FSK) - but even for that, you'd have to start tracking SNR during your transmission to set correct decision boundaries (or, rather, scale the input to your soft-decoder appropriately). That *is* a complication that also does cost your mutual information, because you need to ensure signal statistics or use pilots to make that possible.

It would be worth investigating whether building independently decodable packets of up to 10 minutes duration would mean too much of a loss in terms of decoding gain – I don't know the specifics of your proposed mode, but we don't have great decoders for extremely low-rate (as in R=k/n) codes, burst errors probably don't last longer than 10 minutes so that longer interleaver intervals scarcely make sense, and there's only so much gain you get by using longer codes in that regime. In other words: other than thinking about how to insert identification into a transmission that is multiple 10 minute intervals long, ask yourself whether you don't want to think about splitting up the overall data to be transmitted into independent 10 minute transmission pieces.  
That would especially make sense if ARQ is technically feasible.

### Conclusion

Your options include:

- Just morse out your call sign every 10 minutes, "over" your actual transmission. Let the receiver deal with the additional noise that represents to the system.
- Just leave a gap for transmitting your call sign in your transmission scheme.
- If the slow mode allows for that, modulate its power to "sound like" a morsed call sign.
- Or, don't have the problem at all by chopping up your transmission into independent 10 minute pieces and ending each of them with a classically transmitted call sign.

¹ I hate Morse, because it's impossible to elegantly fit into sensible timing schemes, without converting. So convert: dah= on on on off, dit = on off, inter-letter space = off off off

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21989/is-it-possible-to-comply-with-fcc-regulations-using-a-mode-that-takes-over-ten, by Someone, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
