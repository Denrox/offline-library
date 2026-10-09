# Can I use electrical ground / earth as my RF ground?

*Tags: antenna, vertical-antenna, grounding, lightning, earth · score 3*

## Question

I live on a high floor in an apartment block and have a radial-free multi-band vertical antenna attached to my terrace railing. This is the antenna :

https://www.thunderpole.co.uk/amateur-radio-homebase-antennas/se-hf-x80-vertical-hf-antenna.html

It actually works quite well surprisingly, but of course noisy on receive. I guess it would be better to ground the outer coax shield somehow? However, being so high up, it's not so easy.

Two questions. Feel free to ridicule them. I am still learning here:)

1.

What would happen if I tried to use my electrical ground / earth from the apartment as my RF ground. Hence connect the other coax shield to the earth pin of an electrical plug as it enters the apartment?

2.

I'm of course also worried about lightning striking the antenna and damaging my equipment. What if I use a lightning surge protector and connect the ground terminal to the electrical ground / earth pin of an electrical plug?

Are there any problems with this? Dangerous? Pointless? Please explain.

Thanks in advance

## Answer (score 3, by Phil Frost - W8II)

"RF ground" usually means "something that is at the same potential as the soil". This is important because if you have a wire (such as your feedline, for example) which is *not* at ground potential, then there exists a non-zero electromagnetic field between that wire and the soil. That means the feedline is radiating/receiving, which is usually undesirable.

Simply attaching the coax to your electrical ground probably won't do much. For one thing, the electrical ground is not a low impedance connection to the soil at RF: since you're on a high floor in an apartment building the electrical ground in your apartment and the soil are separated by a wire of significant (relative to wavelength) length, which means it will radiate and receive just like an antenna.

Furthermore the electrical ground is extremely noisy since it's very near all kinds of digital electronics. If your objective is reducing received noise then you need to get this kind of stuff further *away* from your antenna system, not directly connected to it!

Unfortunately, if you want to continue using that antenna you will need to install some radials. What's happening now is without any radials the common mode of your feedline is serving that function, so your feedline is part of the antenna. And the feedline runs inside, near noisy electronics.

A surge protector is unlikely to provide any significant protection to a lightning strike on the antenna, either. See [How can I protect equipment against a lightning strike?](How%20can%20I%20protect%20equipment%20against%20a%20lightning%20strike.md)

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18641/can-i-use-electrical-ground-earth-as-my-rf-ground, by Engineer999, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
