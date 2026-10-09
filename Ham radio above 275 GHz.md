# Ham radio above 275 GHz

*Tags: ehf · score 19*

## Question

I see on the allocation chart all modes and frequencies are allowed above 275 gigahertz. Has anybody experimented with this? Are there interesting things you can do on these extremely high frequencies?

The bandwidth must be amazing here; maybe someone could make something like wifi but faster!

How is it even possible to make the electronic circuits operate at these frequencies?

## Accepted answer (score 10, by Adam Davis)

Occasionally you'll find researchers and amateur radio enthusiasts who have created transmitters and receivers that operate in the EHF band. This band goes from 30GHz to 300GHz, and covers the frequencies you are interested in.

At these frequencies, conventional electronics and oscillators aren't very useful, and typically oscillators are built by using resonant cavities. This is akin to a pipe organ, but at radio frequencies. One example is the magnetron in the typical microwave oven - while it operates at a much lower frequency, it uses the same principle. At higher frequencies you might use a Klystron, which is a special tube that contains the parts needed to create an EHF oscillator while controlling the amplitude, frequency and phase. The Klystron may be used as the antenna itself as well, directing what you might consider a microwave beam of radio energy, or the energy might be coupled into suitable coaxial cables as in a typical radio setup. The Klystron and Magnetron technically operate on different principles, but they are both examples of ways to generate EHF waves.

Note that the next band up, running from 300GHz to 3,000GHz, referred to as terahertz, is the same band that newer airport scanners run at, imaging human bodies below their clothing. Many frequencies in EHF and THF bands will not travel very far through many materials, and so aren't very useful for general radio use. But there are specialized uses where these frequencies are used, such as airport security scanners and particle accelerators.

If you are looking for faster wifi, keep in mind that we haven't fully exploited the spectrum we're already using. MIMO is being used to double and triple throughput, for instance. Channel bonding and wider channels are being used it increase throughput. Going another 10 GHz higher isn't going to buy us much with our current technology, but will further limit transmission range and penetration.

## Answer (score 2, by user9694)

Any amateurs working all the way up at 440 to 475 THz ? aka your typical red LED aka 650nm, red laser

20W sector transmitters are pretty cheep and readily available on Amazon. http://a.co/bMHXMgJ

100mW high gain transmitters are also pretty cheep and readily available on Amazon. http://a.co/2r47axc

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/516/ham-radio-above-275-ghz, by Skyler 440, Adam Davis, user9694. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
