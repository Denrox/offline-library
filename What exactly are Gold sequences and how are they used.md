# What exactly are Gold sequences and how are they used?

*Tags: digital-modes, jargon, ax.25 · score 4*

## Question

I recently became familiar with the FX.25 protocol extension for AX.25. Within the protocol is what they call a "correlation tag", which is a Gold sequence or Gold code. I've heard that Gold sequences are used when there are multiple signals using the same frequency, but what exactly is a Gold code and how exactly are they implemented in order to differentiate multiple signals on the same frequency?

## Accepted answer (score 7, by Marcus Müller)

**Table of contents**

1. But what exactly *generally* is a Gold code?
2. How exactly are they implemented in order to differentiate multiple signals on the same frequency?

 1. What Gold Codes are and aren't
 2. How they can be used to find the beginning (and presence) of a transmission
 3. What's a Correlation, and is it delicious?
 4. Great. What to Do with a Correlation?
 5. Cross-correlation: Telling transmitters apart
3. What **exactly** is a Gold code?

## But what exactly *generally* is a Gold code?

A Gold Code is a *pseudorandom bit sequence*, i.e., a sequence of bits that *looks* random, but is reproducible.

## How exactly are they implemented in order to differentiate multiple signals on the same frequency?

### What Gold Codes are and aren't

Ah, the Gold Code is just the pseuodrandom bit-sequence, not the mechanism to pick apart multiple signals on the same frequency.

What they *are* used for is actually *Code-Division Multiple Access* (CDMA), which is an elegant math trick to allow different transmission to happen on the same frequency, at the same time, while *not* interfering with each other. But that's not what's actually happening in AX.25 or an extension to it.

All that Gold code is used for is *finding the beginning (in time) of a transmission*. How?

### How they can be used to find the beginning (and presence) of a transmission

For that, two properties of any well-designed Gold code are important:

1. They can be reproduced easily – so, the receiver of a message can calculate, on the fly, the exact bit sequence that the transmitter used, to look for it, and
2. the have very low *auto-correlation* for any non-zero shift.

I think the first thing is relatively easy to understand. If we both are going to a crowded place, and I want to be able to hear out of the chattering when you shout at me, then we should both agree on a word for you to shout, and I should know how it sounds when you shout that word. In the digital communications sense, that would be the same as knowing what to *correlate* for.

### What's a Correlation, and is it delicious?

Quick excursion: what's a *correlation*?

Pretty simple; you take two sequences, e.g., your received values from the air and the reference bit sequence (that you map to -1, +1, e.g. "1" becomes -1, "0" becomes -1) that you and the transmitter agreed upon, and you multiply them "point-wise", then add up the result:

- name  pos.1  pos.2  pos.3  pos.4  pos.5  pos.6  …
- **received sequence**  0.8  0.3  -0.2  -0.1  +0.4  0.0  …
- **reference sequence**  +1  +1  +1  -1  +1  -1  …
- **element-wise product**  +0.8  +0.3  -0.2  -0.1  +0.4  0.0  …

Note that the received values are smaller and also not "stable" - they are attenuated and noise. Well, it's a radio reception!

We can see that for any element of that sequence where the *sign* of the reference and of the received value agree, we get a positive entry in the last row (because + times + = +, and - times - = +, as well), and if the signs differ, we get a negative element-wise product.

Summing these things up, $0.8+0.3-0.2-0.1+0.4+0.0=1.2$, we were "mostly right on". We call that sum the "correlation coefficient".

Now maybe that means we found the sequence that the transmitter and our receiver agree on in the noisy reception! But there might also be a point in time where our sequences agree better. Let's try! Let's forget about the first received value, and shift the whole upper row left by one (we receive a new value, instead, -0.7):

- name (shift 1)  pos.1  pos.2  pos.3  pos.4  pos.5  pos.6  …
- **received sequence**  0.3  -0.2  -0.1  +0.4  0.0  -0.7  …
- **reference sequence**  +1  +1  +1  -1  +1  -1  …
- **element-wise product**  +0.3  -0.2  -0.1  -0.4  0.0  +0.7  …

Now, our sum is $0.3-0.2-0.1-0.4+0.0+0.7= 0.3$. Since 0.3 is much smaller in magnitude than our 1.2, we can still assume that the original point in time was the "righter" detection of the sequence. Let's do that with another shift, just for illustration; our new receive value us -0.5:

- name (shift 2)  pos.1  pos.2  pos.3  pos.4  pos.5  pos.6  …
- **received sequence**  -0.2  -0.1  +0.4  0.0  -0.7  +0.5  …
- **reference sequence**  +1  +1  +1  -1  +1  -1  …
- **element-wise product**  -0.2  -0.1  +0.4  0.0  -0.7  -0.5  …

We end up with a sum of $-0.2 -0.1+0.4+0.0-0.7-0.5=-1.1$. This is *nearly* as good as our 1.2, in magnitude, but not as good. That means it's still more likely that the signal was 0-shifted (instead of 1- or 2-shifted).

Last shift of today:

- name (shift 3)  pos.1  pos.2  pos.3  pos.4  pos.5  pos.6  …
- **received sequence**  -0.1  +0.4  0.0  -0.7  +0.5  -0.3  …
- **reference sequence**  +1  +1  +1  -1  +1  -1  …
- **element-wise product**  -0.1  +0.4  0.0  +0.7  +0.5  +0.3  …

Now, $-0.1 +0.4 + 0.0 +0.7 +0.5 +0.3 = 1.8$. What an excellently high value! It would assume most likely that the right thing to do is to wait three values for the agreed-upon sequence to appear.

We can write that all down a table:

- Shift  0  1  2  3  …
- Correlation Coefficient  +1.2  +0.3  -1.1  +1.8  …

We call the "shift-dependent correlation coefficient" sequence from the lower row of that table the "discrete correlation". Tadah!

### Great. What to Do with a Correlation?

Here's the reasoning why that's good:

Assuming we'd receive **exactly** what was transmitted (so the same $\pm 1$s), each element in our point-wise multiplication table would be a $1$, and our sum would simply be identical to the length of the sequence.

Now, we have attenuation, so that, say our beautiful +1 on transmit become +0.4 on receive, and -1 becomes -0.4 (i.e., we have an attenuation factor of 0.4). Then, however, our sum would simply still be the length of the sequence, times the attenuation (because we can "extract" the common attenuation factor from the sum).

With a bit of imagination, we can see that if there's just a single "+" being flipped to a "-" in the transmitter, that would always reduce our sum. So, we get an unambiguous, strongly standing out maximum with the "correct" shift.

If, and only if, no parts of the sequence "repeat", so that for some shift, you get a relatively high correlation coefficient.

That's what the second property above is about: A Gold Code is designed such that for any non-zero shift, it has a low correlation coefficient, so that it's easy to look for the a clear maximum.

### Cross-correlation: Telling transmitters apart

There's a third property:

1. Gold Codes from the same family have very low cross-correlation

What that means is that the way you generate a single Gold Code sequence, you can generate a whole bunch of them. We call these a family. And they share the property that if you do that "point-wise product and sum" trick, the correlation, as shown above, with two different codes, you end up with very low correlation coefficients, so that if two different transmitters have different Gold codes, and I only "compare" with the one of "my" transmitter, I can basically ignore the other one. That's handy if you need to tell many transmitters apart!

## What **exactly** is a Gold code?

I'll assume you can imagine a shift register. If you can't: it's like a bucket-brigade of small 1-bit memory cells:

```
+----+----+----+----+----+----+----+
| x1 | x2 | x3 | x4 | x5 | x6 | x7 |
+----+----+----+----+----+----+----+

```

Each value x1, x2 and so on is a bit, so either 0 or 1.

It's called shift register, because on an external (so-called clock) signal, they can all shift, to the left or right; let this shift register, which is just an example, to the right:

```
+----+----+----+----+----+----+----+
| ?? | x1 | x2 | x3 | x4 | x5 | x6 | --\
+----+----+----+----+----+----+----+   |
V
Trash

```

Two things: we shifted the whole shift register to the right, so, what used to hold x2 now holds x1, what used to hold x3 now holds x2 and so on; but we haven't said what the new value of the left-most cell is! Also, we've just "forgotten" x7: it was shifted out of the shift register.

Ahaa. What about this instead:

```
+----+----+----+----+----+----+----+
/-> | x7 | x1 | x2 | x3 | x4 | x5 | x6 | --\
|   +----+----+----+----+----+----+----+   |
\------------------------------------------/

```

A *feed-back shift register*! Now the bits go in a merry go round.

Instead of rotating back our right-most bit, lets instead combine different entries:

```
+----+----+----+----+----+----+----+
/-> | XX | x1 | x2 | x3 | x4 | x5 | x6 | --\
|   +----+----+----+----+----+----+----+   |
|           |              |               |
|           V              V               |
\----------(+)<-----------(+)<-------------/

```

Due to the pecularity of bit-math, we choose "XOR" as the combining operation "(+)" in our *linear feed-back shift register*.

Nice! Our shift register feeds back the second, fifth and seventh position of the current shift register's content for the new leftest value next clock.

If we choose these "taps" in the right positions, we can make it that the specific combination of bits in the first to seventh position "internally" never repeat, until all the possible seven-bit numbers have been seen (aside from the all-0 word). We then call the sequence produced by these states a *maximum length sequence of 7 bits* or just *7-bit M-sequence*. (And because there's 2⁷ different internal states, which is 128, but we never encounter the 0000000, that 7-bit M-Sequence is 127 elements long. It's always a $2^N-1$ length.)

That's already an interesting way to generate seemingly random sequences, that in fact aren't really random, but reproducible!

Now, a Gold Code is cleverer: It uses *two* such shift M-sequence shift registers of different length, and produces an even longer sequence (long in the sense that it takes very long until it repeates, it repeats only after (length of the first sequence) × (length of the second sequence)! And that sequence has the aforementioned excellent cross- and autocorrelation properties.

## Answer (score 2, by natevw - AF7TB)

To quote the Wikipedia article:

A Gold code, also known as Gold sequence, is a type of binary sequence, used in telecommunication (CDMA) and satellite navigation (GPS). Gold codes are named after Robert Gold.

The math of "how exactly are they implemented" is summarized in that same article or would be found most authoritatively in the original publication:

Gold, Robert (October 1967). "Optimal binary sequences for spread spectrum multiplexing". IEEE Transactions on Information Theory (Correspondence). IT-13 (4): 619–621. doi:10.1109/TIT.1967.1054048.

(The paper itself as it gets going ends up being quite mathematical/theoretical. A more practical introduction might be found in this archived Gold Code Generators in Virtex Devices PDF also via the same Wikipedia article.)

At a high level, they have to do with finding and/or picking a particular signal out of the "noise" (which would include other competing signals as well).

Sort of like how spread spectrum (which Gold even mentions in the intro to his paper) hops between frequencies in a way that would make little sense if you didn't know the pattern, a sequence of numbers can be used to control any aspect of the signal at a fine- or coarse-grained level. A receiver then "correlates" the overall signal(s) + noise against the sequence(s) it expects, to extract just the desired signal(s).

What makes Gold codes particularly useful compared to other sequences in general is that:

Gold codes have bounded small cross-correlations within a set, which is useful when multiple devices are broadcasting in the same frequency range.

i.e. a set of Gold codes are good at not interfering with **each other**. So if hundreds of cell phones or dozens of GPS satellites are all using the same general Gold code *system* but with a different *key* for each it is (relatively) easy to separate the signals for all of those different keys individually — even when they're all transmitting their individual patterns simultaneously.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21599/what-exactly-are-gold-sequences-and-how-are-they-used, by Steve Mucci, Marcus Müller, natevw - AF7TB. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
