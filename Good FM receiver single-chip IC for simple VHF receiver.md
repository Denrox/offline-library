# Good FM receiver single-chip IC for simple VHF receiver?

*Tags: receiver, vhf, electronics · score 5*

## Question

Is there an IC out there that implements all, or most all, of a simple FM receiver in the VHF range? I'm interested in doing some experiments with using DTMF over the air for tele-commands and the like, and I'd like to keep the receiver electronics as simple as possible. The idea is to have a very simple receiver from which I can pipe the audio output to a DTMF decoder IC and then send signals to an Arduino or Raspberry Pi or something of that nature.

I think I may be looking for something like the TDA7000 chip but I'm not clear on what frequency range it can support. It also appears that it may be obsolete / hard to source? I seem to mostly only see ebay vendors selling these. Is there perhaps a more modern successor this this chip that I should be looking at?

This Silicon Labs chip also looks promising and the frequency range is clearly spec'd, and should work for what I want to do, but the problem is that it's only available in a surface mount QFN package, and I'm really not familiar with soldering SMT devices. Something in a good old fashioned DIP package would be great if something like that exists.

Edit: the more I look at this stuff, the more confused I get. It looks like a lot of the IC's that are out there that are billed as "RF receivers" assume you're encoding data in FSK or something, and they want to give you decoded data. Sadly, that's not what I want. I just want the audio demodulated from FM. On that front, it appears that there are "receiver" IC's that will demodulate FM and give you audio, but from what I can tell, they all expect to receive as input, an "IF" (Intermediate Frequency) of 10.7mhz or 45mhz or something... which if I'm reading this right, implies you need another circuit - a mixer - in front of the receiver to downconvert the RF.

This is starting to seem overly complicated, so I may just drop the idea of looking for an IC to do this stuff and just roll it the old fashioned way. That said, if somebody reading this can point to a nice, simple IC based way (using no more than 2 or 3 IC's preferably, 1 would be better) to go from RF -> demodulated audio, it would be appreciated.

## Accepted answer (score 1, by rclocher3)

I don't know much about receiver-on-a-chip devices, although both of the chips you mention look promising. I'd be very surprised if the TDA7000 couldn't handle VHF frequencies.

The TDA7000 is almost certainly not being manufactured, but I wouldn't let that bother you. octopart.com shows two resellers that have the parts in stock, which means that they will be available for a few more years yet in small quantities. I wouldn't design a product to be manufactured around the chip, but if you're just experimenting then you can expect eBay sellers to have them for a few years longer.

The Si4362 is carried by the usual distributors, so it's likely still being manufactured.

You could attach the Si4362 to a DIP adapter, which would allow you to plug the chip into a 20-pin DIP socket, but you'd still need to solder the chip to the adapter. Soldering SMT parts by hand is easier than it looks; Adafruit has some great advice.

Good luck, and let us know how you do with a comment.

## Answer (score 2, by Manawyrm)

another way to do it would be to use a cheaply available RTL-SDR device (like a 5$ DVB-T receiver), and then go software-defined from there.

rtl_fm can do FM demodulation in the needed frequency bands and multimon-ng can demodulate DTMF tones and signaling and give you the data.

A simple Raspberry Pi has enough processing power to do something like this.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6625/good-fm-receiver-single-chip-ic-for-simple-vhf-receiver, by mindcrime, rclocher3, Manawyrm. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
