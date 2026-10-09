# Can I use old TV FM card as SDR?

*Tags: software-defined-radio, wire-antenna · score 5*

## Question

I tried searching a lot before, but couldn't find anything about it; I have an old TV/FM card from an old computer, I wish to know if it can be used as an Software Defined Radio, and if yes, how?

The one I have is the same as this one: http://www.itwinkle.com/51askotvfmnt.html  
It does even have that wire-antenna shown in the photo.

I just found out that Stack Exchange had a site for Amateur Radio, so I wanted to ask here, I know someone might answer xD

## Accepted answer (score 4, by B.Lawrence)

With the limited information provided on that link you posted, I am guessing that the answer would be no. The DVB-T Dongles from nooelec or RTL-SDR are set up to **receive only** on a pretty large portion of the radio spectrum. There is also the option of getting one of the more expensive cards and then purchasing the "ham it up kit" so you would be able to cover the HF channels as well. I have one of the RTL-SDR dongles and it does a pretty amazing job with just the little whips that come with it. I have regular reception from the public safety channels in my area that are up to 30 miles away. Pretty amazing for a $20-30 piece of usb ware. You can research more on SDR and these dongles by going to RTL-SDR.com

Hope that helps

## Answer (score 2, by Marcus Müller)

Can I use old TV FM card as SDR?

Without loss of generality, no.

Old TV cards typically have dedicated analog demodulators to give you a video signal that then is digitized and sent to the PC. No reconstruction of the original signal can be done, usually.

Seriously, though, DVB-T sticks that *don't* do that specific TV signal demodulation can be had for a couple of Euros (you're in Brazil, right? Don't know who imports them there, but I'm pretty sure you can directly buy them somewhere), and they will do a pretty decent job :)

By the way: not every new PC (since ca. 2007) even has a PCI interface anymore, that's one of the reasons these TV cards are cheap/for free this often. I, myself, have two cards I've never used for anything.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6532/can-i-use-old-tv-fm-card-as-sdr, by Miguel Vieira, B.Lawrence, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
