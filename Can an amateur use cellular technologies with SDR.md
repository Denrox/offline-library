# Can an amateur use cellular technologies with SDR?

*Tags: digital-modes, software-defined-radio, rtl-sdr · score 11*

## Question

Software Defined Radio is opening up many new possibilities for amateur digital modes. One family of technologies that interests me is cellular. 2G GSM voice/sms and 2.5G GPRS data has been proven to work with OpenBTS on a USRP SDR using licensed cellular bands. Can this technology be used by amateurs? Could an amateur cellular network be deployed sometime in the future?

Note: I know that there are many small practical considerations to doing this. Cellular technologies are heavily patented, but patents on many older GSM technologies have recently expired. Also, some deployment tweaks will be needed to adhere to amateur regulations, such as disabling encryption. Answers should focus on the fundamentals of amateurs using cellular technologies via sdr and not these small hangups.

## Accepted answer (score 8, by Adam Davis)

Yes it can be done, and there are some huge advantages:

- Better use of bandwidth
- Existing chipsets/support/implementation
- Low power

In fact there's little reason why one couldn't essentially replace DSTAR and competing systems with a standard based on GSM and GPRS technologies. Even for those parts that are patented, the patents running out means we'd be using technology that's advanced well beyond DSTAR and similar systems, and it's completely open.

It would take a few individuals building up an example design and example infrastructure for it to be picked up widely. But once that happened you could build a cellular network over Amatuer Radio frequencies, and you could expand functionality to support specific Amateur Radio needs such as public safety and emergency communications.

## Answer (score 2, by PearsonArtPhoto)

Honestly, the key technology to making this work has been around for quite a while, and that is the phone patch. Essentially, you can get on a repeater and dial a person from said repeater. The area of operations is fairly limited for such, but it has been done. And an SDR might help with this process, but it isn't required.

As far as digital, the key thing to remember is that Amateur bands prohibit encryption. Most of the useful things that one does over a cellular network require encryption of some form. Thus, it isn't likely to be of huge use. But yes, in principal it could be done.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/814/can-an-amateur-use-cellular-technologies-with-sdr, by JC Hulce, Adam Davis, PearsonArtPhoto. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
