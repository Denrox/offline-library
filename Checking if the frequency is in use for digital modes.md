# Checking if the frequency is in use for digital modes

*Tags: digital-modes · score 5*

## Question

On CW and phone, we are taught to ask if the frequency is in use before calling CQ. Is it correct to say that with digital modes, that is impractical, and you should just listen (over the bandwidth you plan to use) and if you hear nothing, just go?

It was interesting to me to see, during RTTY contests, several RTTY QSOs occurring on top of some wide-band digital mode signal. I expect that both modes employ some degree of forward error correction and retries, so maybe it worked out for both (of course, on RTTY the "forward error correction" and retry mechanism is done by the operator).

## Answer (score 2, by Marcus Müller)

Is it correct to say that with digital modes, that is impractical, and you should just listen (over the bandwidth you plan to use) and if you hear nothing, just go?

Well, that really depends; "listen before talk" is not an unreasonable thing, yes. In fact, for non ham licensees, it's the only way you're allowed to operate any device with a duty cycle of > 1% at all in the 2.4 GHz band! (i.e., if you want to operate a wifi or whatever device, which is on for 1/100 of the time or more, that device must first check whether someone else can be observed, before starting to transmit).

I'm sure the rules there differ from country to country, so I don't think general advice can be given. However, being excellent to each other: always a good idea.

Asking whether a channel is clear to send makes – honestly – very little sense in congested scenarios. Imagine a room full of 50 people, barely understanding each other because so many people are talking, and now in addition to the things people actually want to say, they have to go, loud and clearly "HELLO. I'D LIKE TO SAY SOMETHING. IS THAT OK?". You'd be making the problem worse!

Now, another thing, however comes into play with digital modes: There's digital modes *designed* to be talked atop of each other! In fact, things like the hugely popular FT8 make sure that everyone starts talking at the same time slots!

Thing is easy to explain: these modes are *code-division multiple access* (CDMA). Most hams are inherently comfortable with the concepts of

- *frequency-division multiple access* (FDMA) ("if the channel is used, use a different channel", and schemes that pre-define who uses what channel. FM broadcast, 1G cellular phones generally fall under that), and
- *time-division multiple access* (TDMA) ("There's times when I talk, and I yield times for when the others talk", and schemes that predefine that. 2G (GSM), and most western incarnations of 3G, 4G, 5G fall under that)

But there's also other methods of dividing spectrum access across multiple users; the interesting one, CDMA, employs a *code* to tell users' signals apart. It's not hard to explain in principle!

Say you want to have two users who should be able to send a signal at the same time, on the same frequency. Say, they do Phase Keying, and transmit 1 bit, so one of the digital "0"s and "1"s that make up cat pictures; they do that by either sending a signal with phase 0 (that's a +1) or phase $\pi$ (that's a -1). But instead of just multiplying their carrier with +1 or -1 to give the carrier the phase they want, they "*spread*" the bit.

User A uses the rule "send the desired phase, and repeat it once", so if they want to send a +1, they send +1, +1 (and if they want to send a -1, they send -1, -1). (one symbol gets sent after the other, so we make our transmission twice as long.)

User B uses the rule "send the desired phase, then send the opposite", so if they want to send a +1, they send a +1, -1 (and if they want to send a -1, they send a -1, +1).

So far, so slightly confusing but possible to take at face value. We just send twice as many phase symbols, and have a strange method of converting what we actually wanted to send to these.

Now, what the receiver that wants to receive what User A sent does, is that they sum up both symbols they received, and divide by two. Clever, because A's signal is either +1, +1, so the receiver calculates +1 + +1 = 2, divides it by 2, and gets the original +1. Or A sends -1, -1, so the receiver does (-1 + -1) / 2 = -1. Check!

But what about User B's signal? These can be +1, -1, or -1, +1. Ok, +1 + -1 = 0, divided by 2 is still 0. Oh!  
Other option as -1, +1, so the sum is -1 + +1 = 0, so that's also 0!

Now that happens even when we add the signals from User A and User B: User B's signal always cancels itself out in the receiver for User A, and does not make the reception of User A's signal any worse.

What does a receiver for User B do? It takes the difference of the first minus the second symbol. Assuming B sent +1, -1, that makes +1 - (-1) = 1+1 = +2, divide by 2, get the original +1, assuming B sent -1, +1, that makes -1 - (+1) = -2, divide by 2, get the original -1.

And, the because the difference between the two symbols that A sends is always 0 (because they are by decree always the same!), User A's transmission self-cancels in the User B-specific receiver.

So, User A **does not** have to listen whether User B is also starting to send data, and vice versa! They can coexist perfectly well.

You can extend that scheme to more users by adding more repetitions (and finding clever ways to assign these *spreading sequences*, i.e. the rules how to repeat and invert the symbols, to the users), and that's exactly what things like FT8, IEEE 802.11b (that was the "slow" 11 Mbps Wifi of years long past), UMTS (3G), CDMA2000… (US's attempt at 3G) does.

So, nope, there's not a general rule for how to deal with channels with digital mode usage. Usually, there's a bandplan that indicates *what* kind of modes are on there, and then you'd make sure to be compatible with these in how you share the access to the wireless medium.

I expect that both modes employ some degree of forward error correction and retries, so maybe it worked out for both (of course, on RTTY the "forward error correction" and retry mechanism is done by the operator).

Yeah, RTTY is not a CDMA system; they are just rudely talking over each other; I'd say that's hm, a contesting thing, and something that greatly reduces my interest in contests. What the operator does is actually, as you hint at, called *interference cancellation*, helped with some error correction based on knowing what to expect, roughly, and also, honestly, guessing.

Interference cancellation is fun. Assume you receive two analog FM transmissions. One weak, one strong. Quite naturally, you know your classical receiver gets locked on and hence "captured" by the stronger one.  
Now, if you *don't* just use a physical FM receiver with a PLL or another frequency discriminator, but actually used a receiver capable of recording the received signal, you could first let your FM receiver run on the signal, it gets captured by the strong transmission, you clean up the signal (because you know about the voice bandwidth, for example, and can filter accordingly), *and you used the cleaned-up version to reconstruct a lower-noise version of the original stronger FM signal*, and just subtract that from your recorded signal.  
Lo and behold, suddenly you're left with a signal where the weaker FM signal is the only one (and maybe there's some very weak remnants from the originally stronger FM transmitter, because your subtracted signal was not *quite* perfect); then you let your FM receiver run on that again and get the weaker signal out.

Tada! We just did something that, not too long ago, was as common knowledge would have it, impossible. Have two active FM transmitters in the same band!

This of course only works out if there's one transmitter that's really sufficiently stronger than the other, otherwise you don't get properly captured. And it really works out barely decently with FM, as that is a very analog thing. But with digital modes, you can often be better – because you can have checksums to check whether you decoded the stronger one successfully, and you have forward error correction to correct receiving errors, and you have a set of well-known signals that can possibly be sent, and not an analog continuum! So, with digital modes, *Non-Orthogonal Multiple Access* (NOMA) schemes become feasible. "Non-Orthogonal" as opposed to "Orthogonal", as in the two-length spreading sequence above, where User A had zero effect on the receiver for User B, and vice versa, because the spreading sequences mathematically stood orthogonal to each other.

Orthogonal methods like CDMA, FDMA and TDMA allow every user to use their slice of the spectral pie 100% unimpressed by all the other users, so there's no *multi-user access* (MUA) interference.  
Now, NOMA doesn't *try* to achieve that – there's always going to be a loss of signal quality when you're subtracting a noisy guess at what the stronger signal was. But: it also doesn't have to split everything beforehand.

NOMA is still an active research topic – it comes up when people want to deploy a lot of transmitters in the field, with no chance to assign unique sequences to each and every one, and especially in systems where it's not clear that these transmitters even have to send things regularly, and at a constant rate. So, the system operators wants to take the penalty that they get by doing non-orthogonal multiple access – now the transmitters interfere – but get the freedom to build a system where, say a million little satellite transmitters attached to migratory birds, can send data whenever necessary, and without having to assign a *humongously long* spreading sequence so that every bird transmitter can be code-orthogonal to every other one.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/22367/checking-if-the-frequency-is-in-use-for-digital-modes, by gschro, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
