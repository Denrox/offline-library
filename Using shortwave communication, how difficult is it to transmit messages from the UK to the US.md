# Using shortwave communication, how difficult is it to transmit messages from the UK to the US?

*Tags: hf, propagation · score 6*

## Question

Is it possible to transmit a short message via shortwave from the UK to the US, across the Atlantic ocean? From what I understand, long-distance shortwave communication has lower bandwidth requirements than other forms of communication, such as microwave, which also requires line-of-sight. When I say "short message," I mean maybe around three bytes.

**Some questions:**

1.

Would sending a three byte message over such a long distance require an antenna that uses a great deal of power?

2.

Are there any companies that allow users to rent time on antennas that would be capable of transmitting messages over such long distances? Or would this require a completely custom infrastructure -- buying land and building a tower(s) with the necessary antennas?

3.

How reliable would this be? I am aware that messages transmitted via shortwave may be subject to scrambling/interference due to sunspot activity/ionosphere conditions and poor weather.

If there are any other things to consider for this theoretical scenario (e.g. licensing, costs etc), I would appreciate any information on them.

## Accepted answer (score 11, by hobbs - KC2G)

1. To send a message of around three bytes over such a long distance, would this require an antenna that uses a lot of power?

No. There's a huge variety of tradeoffs here, but as a quick calibration, WSPR sends 50-bit messages (so, a bit more than twice what you're asking) all around the world using power levels usually ranging from several milliwatts to ten watts. Its main disadvantage is that it takes almost two minutes to send such a message. There are digital modes that are quite a bit faster, that can still do the job with less than 100 watts (which is considered an "ordinary" amount of power for an amateur).

Are there companies that enable users to rent space on antennas that would be capable of transmitting messages over such long distances? Or would this require a completely custom infrastructure (e.g. buying land and building a tower(s) with the necessary antennas)?

Hmm, maybe? I'm not familiar with rental, but I imagine it's possible. However, you might need far less in the way of land and antennas than you think, and no towers at all. It's hard to get into specifics without knowing details of your situation, but a simple wire antenna on a rooftop or a "small transmitting loop" antenna could potentially get the job done.

How reliable would this be? I am aware that messages transmitted via shortwave may be subject to scrambling/interference due to sunspot activity/ionosphere conditions and poor weather.

Less than 100% reliable — sometimes solar flares and the like make HF pretty close to completely unusable. But on *most* days, there will be at least several hours when there is at least a 90%-reliability path from the UK to a given part of the US. When those hours occur and which bands they occur on depend on solar cycle, time of year, and location (the US is a big place).

If there are any other things to consider for this theoretical scenario (e.g. licensing, costs etc), I would appreciate any information on them.

Licensing is probably the sticking point. I imagine the communications you want to do are probably *not* within the rules of amateur radio, so another form of licensing will be necessary. I'm not especially familiar with the UK but it seems like there's no out-of-the-box license type for this kind of use, and requests are handled case-by-case by Ofcom. In this regard, working with a third party is probably to your benefit.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15827/using-shortwave-communication-how-difficult-is-it-to-transmit-messages-from-th, by p.luck, hobbs - KC2G. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
