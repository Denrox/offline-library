# Build a HamRadio Friendly UMTS Module

*Tags: software-defined-radio, digital-modes · score 3*

## Question

I would like to play around with openBTS/yateBTS (experimental, no 24/7 run). What I would like to do is to modify a UMTS/GSM module or mobile phone so it operates in a frequency that can be used with a HAM license.

I looked around and think in my location, Austria, I can use this frequency because in my area there are no active hams that use ATV: 1272,0 – 1290,994 MHz. Has anybody ever done this before? Does anybody know a good module or phone where this can be archived?

I first thought about just replacing the crystal and bypassing the filters, but i can't access them all, because some of them are in the chip. Another idea was to use a mixer to offset the output frequency and place filters behind this.

So the questions are:

- Is it okay to use an ATV frequency when I am sure no other ham gets disturbed?
- How should i modify an existing chip/mobile phone?
- Is one of the ideas above good enough for experimental usage?

## Accepted answer (score 1, by Marcus Müller)

… to modify a UMTS/GSM module or mobile phone so it operates in a frequency that can be used with a HAM license.

That means you'll need external mixers – mobile chipsets are very well designed to filter exactly the frequencies relevant to exactly one standard, and you won't be able to change that.

With LTE, there's support for ISM-band operation in some newer chipsets (I'm not 100% about the specifics), and that also means that the Ham/ISM overlap might be usable here; also, there's LTE allocations in what's called *digitale dividende* in the German-speaking regions – the spectrum that was freed by shutting down the analog commercial TV stations.

But for GSM (where that filtering is even much more fine-granular) and UMTS, I'm afraid your only option is to use external down/upconverters to transform the downlink and uplink band of the chipset to whatever you want to use.

- How should i modify an existing chip/mobile phone?

Not at all, add external uplink/downlink frequency transverters.

- Is it okay to use an ATV frequency when I am sure no other ham gets disturbed?

Probably not; I'm not an expert for legal details, but I think that usually these bands are meant for video communication, and doing something else on there isn't OK for the others.

Also note that GSM hops (or at least, the base station can configure itself and the mobiles to do so) over a large bandwidth – potentially much wider than a TV channel. UMTS channel widths are also configurable to exceed TV channel widths. I'd strongly recommend you do your first experiments within the confines of cabling!

- Is one of the ideas above good enough for experimental usage?

Experimentation is always fun!

I don't know how much use it'll be, however. If you need to run around with a handset that is twice as large because you had to remove its original antenna, add two mixers and a diplexer and another antenna, and uses additional battery, you might really be better off with looking into getting an SDR-based LTE basestation running in the ISM bands to work with your handset.

Also note that cell phone and cellular infrastructure manufacturers have implemented standards that are *meant* to push the edge of "state of the art". That means that these devices' receivers are heavily optimized for a specific channel model – and channel models are frequency-dependent! You get very different problems when you do something e.g. on 1.8 GHz vs doing the same transmission on 146 MHz; however, 1272 MHz is probably a channel that "might be similar enough" and just work (make sure the analog parts of your cellular hardware aren't hit by TV broadcast powers – cell phones are easily a couple billion times more sensitive than TV sets).

Timing in cellular networks is also optimized so that a lot of people can participate in one cell. Thus, building e.g. a GSM network where maximum distances aren't really what you'd expect (a couple of kilometers), but signals are "in flight" for a lot longer, then you'd need to tweak parameters of that network – and it might happen that at some point, the hardware involved simply won't be able to accomodate a setting, or that the way the network operates makes no sense anymore.

UMTS might be an especially bad choice – it depends on code orthogonality, and that actually isn't the nicest assumption for wide-spanning networks or fast-moving communication partners, or reflectors (and that's one of the technical reasons it got superseeded by LTE). Also, I think there's more mature LTE than UMTS SDR implementations out there – have a look at https://github.com/srsLTE/srsLTE

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6926/build-a-hamradio-friendly-umts-module, by maxbit89, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
