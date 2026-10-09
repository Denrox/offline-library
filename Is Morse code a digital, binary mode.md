# Is Morse code a digital, binary mode?

*Tags: digital-modes, cw · score 15*

## Question

At first glance Morse code looks like a digital mode - there are dits and dahs, two values which contain the information of the transmission. Alternatively, at any point in time there either is a signal, or there isn't.

Morse code follows the following pattern:

- dit: tone for one unit (1)
- dah: tone for three units (111)
- separation between elements: silence for one unit (0)
- separation between letters: silence for three units (000)
- separation between words: silence for seven units (0000000)

As mentioned in a Vsauce video, however, Morse code doesn't actually require only two different values, but actually three: dits, dahs and spaces. He goes on to explain that any Morse transmission can be broken up into three components: a dit with one unit space (10 in his notation), dah with a space (1110) and a separator character (00, two dits in length). From this he argues that it is actually a trinary, rather than a binary code.

But is it?

After all, any transmission can be represented as either a high or low signal voltage at the receiver, sent in a pattern of one bit per dit. The information is encoded entirely in two separate, discrete values. How this information is afterwards decoded is a matter of choice I would argue.

It seems similar to the ASCII scheme - the information to what letter corresponds to what bit sequence is just a matter of definition, but the information is still binary. Analogous to that, Morse code is nothing more than an encoding with variable-length 'bytes'.

**From a strict definition (what is it?), is Morse code (CW) a binary mode? Or is it trinary, or something else entirely?**

## Accepted answer (score 21, by Jamie Hanrahan)

According to Shannon (in *A Mathematical Theory of Communication* - and who's going to argue with Shannon?) there are really only four symbols in Morse, not five:

- "dit" (defined as one unit time on followed by one unit time off)
- "dah" (three unit times on followed by one unit time off)
- "letter space" (two unit times off) (should follow a dit or dah symbol)
- "word space" (four unit times off) (should follow a dit or dah symbol)

You don't need a fifth symbol for the intra-letter space because you can't represent a "dit" or a "dah" without *some* space following it. So by defining the dit and dah symbols as above, you get the intra-letter spaces without adding to the symbol count.

Aside from that, I believe we are dancing around the distinction between *line states* and the *channel code*. The line state in Morse usage is binary but the channel code is not. Per Shannon, the channel code has four different symbols.

Another example of a channel code is EFM, eight-to-fourteen modulation, which encodes every eight bits of end-user data as a 14-bit word. The allowable 14-bit words are chosen so that each has zero DC offset (same number of 0's and 1's) and to limit the number of successive 1's and of successive 0's. It is used on Compact Discs and other optical digital media.

## Answer (score 7, by Brian K1LI)

The mode hams call "CW" is also called "on-off keying" (OOK) - a hint to the fact that it *is* a binary code. Dots, dashes and spaces are usually sized in multiples of the "dot time": one dot time *on* for a "dot," one dot time *off* for the "space" between dots and dashes within a given character, three dot times *on* for a "dash". Spaces between letters and words comprise other dot time multiples. These multiples can be adjusted for purposes of readability or "personality."

An earlier [Ham Stack Exchange](Coherent%20CW%20synchronization.md) answer described how these properties are exploited to improve the signal-to-noise ratio of CW signals.

## Answer (score 2, by Tasos Papastylianou)

I believe the question is confusing the difference between something *being* a natural basis for a language, versus whether something could be adequately *represented* by one in a mathematical / encoding sense.

It is clear that morse code can be represented adequately using a binary representation / encoding. This is not surprising, since a binary representation can be created to represent much more complex bases anyway, such as the latin alphabet (e.g. ASCII).

However, you would probably agree that this doesn't make the latin alphabet a binary one in nature. Rather, the alphabet's elementary particles (the letters) can be used to form more complex constructs (the words). So in this sense, the English language is most naturally regarded as a 26-base system (because there are 26 elementary letters-particles).

Similarly, while it is possible to represent morse code using binary encoding, one would be hard pressed to argue that this is the most natural representation for it, or that this makes it a binary 'alphabet'. It is rather intuitive to consider the 'dit', 'dah', and 'separator' as the elementary particles that combine to form more complex constructs ('morse code').

You could of course try to argue that the 'dah' is not a well-suited, natural atomic particle for the morse code language, hence you can accept the 'binary' representation of '10', '1110', '00' etc, but I would argue that this is not really a good interpretation of the nature of morse code words; it is far more intuitive to conceive of morse code letters as composed by elementary dits, dahs, and separators as the elementary particles. If you need three bits to express a 'dah', then you're using essentially using four 'atomic particles' in your chosen representation, to express what is essentially a single natural atomic particle in the morse language, which seems like a rather inefficient way of expressing the language. Remember that binary is the choice of digital signals because of the electrical nature of transistors which deal with such signals most efficiently. But there's no reason for morse code to abide by that requirement, so a more efficient representation which is more natural to morse code (and its transmission by telegraph) would presumably have been preferable to such a binary encoding among telegraphers.

As to the separate question of whether it should be possible to consider the dit and dah itself as a sufficient number of elementary particles to fully express the morse code language, the answer to this is no (and hence it is not a naturally binary 'alphabet'). You can confirm this by attempting to express morse code in the absence of spaces. The reason telegraphers could rely on only dits and dahs is because they also had the added element of time, which could simulate word separation. When these need to be written down on paper as symbols, however, the word separator needs to be made explicit, thus making morse code a ternary system.

Another way to see why time in itself is not a trivial aspect, but actually adds information is to treat it as if it's a separate signal transmitted in parallel with your dits and dahs. You now have two signals to consider at each time point, one in the dit-dah dimension which tells you whether you're dealing with a dit or a dah at that timepoint, and one in the time dimension, which tells you if you're dealing with a dit-dah particle, or not (i.e. a separator). Since these are two independent binary signals, your receiver at the other end would have to process a 4-bit signal. However, this can be encoded more efficiently as a 3-bit signal, since when the time series has a separator, the ditdah series is ignored. Thus the most efficient and natural representation for morse code is a ternary one.

PS. I forgot about the distinction between a 'letter separator' and a 'word separator', but the above arguments still apply. You could make the case for a quaternary base instead of a ternary one incorporating a bespoke 'word separator' particle, or accept the ternary one and accept the inefficiency that comes with always having to represent a 'word separator' using a slightly less efficient representation using a 'diphthong'.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12142/is-morse-code-a-digital-binary-mode, by DK2AX, Jamie Hanrahan, Brian K1LI, Tasos Papastylianou. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
