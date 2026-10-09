# Baofeng UV 9R Handheld programming

*Tags: baofeng, radio-programming · score 6*

## Question

I have a Baofeng UV 9R Handheld that I just recently bought and received in the mail brand new, however as much as I like this handheld device I am maxed out with frustration as far as manual programming of this device is concerned. Does anyone have any answers to help guide me in manually programming my UV 9R?

## Answer (score 9, by rclocher3)

Almost nobody programs Baofeng and similar radios by hand: too difficult, as you discovered. The thing to do is to get your hands on a programming cable and programming software. If you go to a meeting of a ham radio club, there's a good chance that someone will have the cable and the software right there, and will be able to program your radio for you in five minutes. If however you want to do it yourself, it's not too difficult.

Inexpensive programming cables for sale abound on the internet, but there's a catch. Most of the inexpensive cables contain a USB-to-serial chip that's a close copy of a chip made by Prolific, so much so that Windows identifies them as Prolific chips. Windows Update will try to download the latest Prolific driver for the clone chips. Unfortunately for unsuspecting owners, Prolific responded to the flood of cloned chips by changing their driver to only work with genuine Prolific chips, so if you have the latest driver, a programming cable based on a cloned chip won't work. There is a work-around described here, which involves disabling automatic hardware driver updates, uninstalling any driver that's already installed, and then manually installing an old driver version.

If that sounds like too much hassle, you can get a programming cable based on a chip made by FTDI, or run the software on Linux rather than Windows; the Linux driver "just works". You can also buy the programming cable and software package sold by RT Systems, which also have the reputation of "just working", but are expensive.

If you don't choose the RT Systems route, then you'll need programming software. Baofeng has free software for their radios. (I don't remember, but the software might be specific to particular models.) Their software works fine, but another alternative which I prefer is the free software called CHIRP, which is excellent, and works for just about every ham VHF/UHF radio that can be programmed by a serial cable. There are versions of CHIRP for most every operating system. CHIRP is frequently updated, and there is a lively mailing list that is friendly to newbies.

I'd also like to recommend the site miklor.com, which is chock-full of good information for owners of Baofeng and similar radios.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10329/baofeng-uv-9r-handheld-programming, by Sebastian Masters, rclocher3. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
