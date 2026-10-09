# What are the most common RF connectors encountered in amateur radio?

*Tags: connectors · score 7*

## Question

SO-239, PL-259, UHF, NMO, SMA male/female, reverse SMA, oh my! Some of these may even refer to the same thing with different names. Can someone list the most common connector types and show a picture of each? Also, please explain common acronyms or slang terms used for various connectors. I could not find a comprehensive list online that included all of this in one place - this will be a helpful reference for new hams.

Please RF connectors only for this question.

## Answer (score 7, by Dan KD2EE)

Connector use varies based on frequency band and also based slightly on power. The most common that I see, I have bolded, and while they are sorted by band, a VHF/UHF connector can be used on HF - it may not be common, but it's OK. On the other hand, an HF connector will be unacceptable at VHF/UHF, and only GHz/microwave connectors will be acceptable at those frequencies.

**HF connectors**

- **UHF connector** - no, that isn't in the wrong category. Also known as **PL-259** (male) or **SO-239** (female). When this connector was first developed, the nomenclature of HF, VHF, and UHF was different than it is now. This connector is commonly found on HF equipment, and is relatively large.
- **Bare wire/twin lead** - certain antennas and feedline, like twin lead (also known as window cable) or random wire or loop antennas on HF use bare wire connections. These may not be insulated, so don't touch unless you're damn sure that the transmitter is off and disconnected.

**VHF and UHF connectors**

- **SMA** and varieties. This is near universal for portable radios, and common on mobiles, at VHF and UHF. The standard configuration has a male with a center pin and threads on the inside, and a female with threads on the outside. The reverse configuration (sometimes known as **RP-SMA**) has a male with a center pin but threads on the outside. There is also a similar connector used only for HTs where there is no center pin - the threads are the same size as an SMA connector, but the antenna side is just solid metal. Since HT antennas are monopoles anyway, there isn't any downside to using this - but be careful: if you use one of the traditional rat tail or tiger tails on this antenna, it will not work properly and will be carrying full antenna current.
- BNC connectors - this is a quick-mate connector. It takes less than a half turn to mate/unmate the connector, which is great for anything that's being replaced often. If I had an HT that I used both as a portable and in my vehicle on a mobile antenna, I'd use the BNC connector because repeated mate/unmate cycles can damage the connectors on both sides, both the crimp and the solder to the circuit board - especially if you overtighten your connectors, which is surprisingly common.

**Microwave connectors**

- **Type N** connectors - while certified often up to 18GHz, these are often also used for UHF. I've seen them more on commercial gear than ham gear, but hams do use them also. This connector has an extra "circle" of metal shielding the center pin on each end. It's larger than even PL-259 - about 0.8" in diameter. You see a lot of these on RF test equipment.
- TNC connectors - a threaded version of BNC. It's about the same side, but is rated up to about 11GHz (BNC is only rated to 4GHz). Not common, but you might see it. There is also a reverse version (like for SMA).
- Type C connectors are another variation on BNC, which are weatherproof and rated up to 11GHz, but are quick-mate.
- Mini-UHF - more confusion abounds here! This connection can be rated well over 20GHz, unlike the UHF connector above that it seems to be based off of. It may appear similar to or slightly larger than a (standard polarity) SMA connector. Whereas SMA uses 1/4" threads, Mini-UHF uses 3/8".

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/858/what-are-the-most-common-rf-connectors-encountered-in-amateur-radio, by Dan, Dan KD2EE. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
