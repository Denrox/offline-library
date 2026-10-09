# SSB Transceiver Architecture - USB with Crystal Filter

*Tags: transceiver, equipment-design, filter, ssb, mixer · score 3*

## Question

I'm planning to build a 20m SSB transceiver and I want to get the overall architecture straight in my head first. Here's what I'm thinking so far, a single conversion superhet design with a 9MHz IF and a homemade crystal filter. The problem I'm struggling with is in relation to mixers and inversion.

Because it's 20m and conventionally broadcasts are USB, lets say we're tuned to 14.1MHz and there is a USB signal from 14.1 to 14.103 MHz. 14.1 equates to 0Hz audio and 14.103 is the highest audio frequency. My filter has a BW of 3KHz and a centre frequency of 9 MHz. If I tune my VFO to 23.1015 MHz then I end up with an inverted USB signal through my filter. Do I have that correct?

So, 23.1015 - 14.1 = 9.0015 (i.e., the lowest audio frequency in my signal ends up at the highest frequency through my filter) Likewise, 23.1015 - 14.103 = 8.9985 (highest audio is lowest through filter) But, it's often said that a crystal filter favours LSB, is this setup going to cause any issues?

So, if I set my BFO to 9.0015 MHz, I get: 9.0015 - 9.0015 = 0 Hz and 9.0015 - 8.9985 = 3 KHz. So, the highest filtered signal becomes the lowest audio signal and vice-versa.. Do I have that right?

I'm not sure if this is the standard way to build a simple SSB transceiver, are there any pitfalls in this approach?

## Answer (score 4)

All OK. Pitfall for 14 MHz RX and 9 MHz crystal filter is choice of oscillator frequency. 5 MHz is possible but a bad choice, because the harmonics of the oscillator give unwanted spurious reception.

By the way: I did identical things. See pictures. In my opinion there is no preference for LSB or USB based on such passband characteristics.

## Answer (score 3, by Phil Frost - W8II)

Using an example from Crystal Ladder Filters for All, a crystal filter response might look like this:

Indeed, this filter might "prefer" LSB, because that would place the carrier near the right side of the passband which has a steeper attenuation. That would mean you'd design your IF like this:

When the IF is subsequently heterodyned down to baseband, there are two bands that will be audible: the desired signal in green, and the image frequencies in red. Designing the IF in this way is good because it maximizes attenuation of the image frequencies.

Insufficient attenuation to the left of the green area maps to audible frequencies above 3400 Hz. The filter between your ears is very good at removing this interference because its frequency does not overlap with the signal.

But insufficient attenuation to the right maps to audible frequencies that overlap with the signal. Your brain can not filter out this interference.

If the IF were designed the other way, then attenuation of the image frequencies (in red) would not be as good:

Of course, whether this particular issue is more relevant than other concerns, and if your particular filter response is like this example is a different matter. If you look at F. Sessink's image for example, it looks like the filter response is essentially symmetrical. And even in the example here with the carrier to the left of the passband, the attenuation of the image frequencies is still at worst 50 dB, which isn't terrible. As F. Sessink notes in the comments and other answer, other concerns such as phase noise and other spurious reception may likely be more significant.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17706/ssb-transceiver-architecture-usb-with-crystal-filter, by Buck8pe, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
