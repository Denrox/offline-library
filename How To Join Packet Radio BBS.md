# How To Join Packet Radio BBS

*Tags: united-states, receiver, transmitter, packet · score 13*

## Question

I'm a complete newbie here, and on the Southeast Coast of the USA. I don't even own a ham radio yet. Some *preppers* and I got to talking about a dystopian time of Internet collapse where shortwave radio might be an important factor of survival. This led me to consider joining or starting a packet radio BBS (bulletin board system), unless of course there is something better by now.

My question is what kind of equipment and licenses would I need in order to join and communicate with a packet radio bulletin board system (unless of course something is better/faster now)? Ideally it would be great to interact with other preppers on this system in case some ill-fated dystopian future arrives.

*Note my background -- I'm a PHP, C++, Objective C++ coder and a former computer networking engineer who's well aware of the OSI model of several protocols, although not this AX.25 protocol that's used in packet radio. So, feel free to speak technically to me.*

## Answer (score 11, by JSH)

#### A summary of requirements:

1. Licensing: Technician - very minimal requirements
2. Equipment: Transceiver, Terminal Node Controller and terminal

 - Transceiver - traditionally a VHF/UHF FM radio
 - Terminal Node Controller - Partly a modem, partly an AX.25 layer manager
 - Terminal - Any serial terminal will do, but most likely you will use a personal computer
3. A bulletin board system to connect with.

Let's break these down a bit.

#### Licensing

You're in luck here as the technician class license is easy to obtain only requiring minimal study, no code, and learning the basic rules of how to transmit without going outside the allocated frequency privileges.

#### Transceiver

There are a growing number of ways to pass a digital message or two around, but the traditional meat and potatoes way for AX.25 packet is with a 2m or 440 FM transceiver. The audio connections marry with the modem IO of the terminal node controller.

#### Terminal Node Controller (TNC)

You're in luck here as well as in addition to a fairly large used market, new makes and models of packet ready modems are coming online. I think we have the APRS system to thank for these recent development efforts. Some TNCs have both the modem component along with the AX.25 management firmware. For these all you need is something that can connect to an EIA232 style serial port.

Another kind of TNC is the KISS (keep it simple) version that omits some or all of the AX.25 network firmware leaving a much simpler and much cheaper modem in place. There is still a serial port, but the expectation is a program running on the other end of that serial line will perform the necessary AX.25 network management features.

A modern approach is to skip the standalone TNC and connect the transceiver audio directly to a computer soundcard port. Numerous programs exist that will perform all packet functions (modem and AX.25) within the PC and make the resulting "terminal" text available on some TCP/IP port or virtual serial port. This is likely an excellent way to initially explore packet radio.

#### Terminal

At the user end of the above, you have a simple text entry screen with responses typed on your display. What you actually type here is a learning exercise and a really good resource to learn the basics may be found on this very old, but nonetheless excellent resource...

http://www.choisser.com/packet/

#### Bulletin Board System (BBS)

Here is where things get a bit difficult. In the old days, numerous BBS systems were available for hams to connect with and leave messages to each other. Some are still around, but packet radio fell out of favor after excessive traffic proved too much for AX.25 and the relatively slow data speeds to handle with any practical utility. You may be in luck and have a local BBS you can connect with and I'm sure the sysop may well allow access for want of users.

Several of us in our area are in the planning stages of rolling out a BBS available on a variety of frequencies including HF (shortwave)...

Virginia Packet Network

We have not made it through a feasibility study yet, but the prepper community is one target "market" for such a system and your very question gives us hope.

Note that ham BBS users may interact with the typical BBS system entirely on the command line, sending, receiving and listing, BBS "mail" not unlike modern email concepts. There are also programs you can run on your local PC that will interact with the BBS behind the scenes, but organize the display and management of the messages on your machine much like a modern email program. Once such example is Outpost Packet Message Manager (PMM). I, for one, love the convenience of Outpost, but relish the fact the straight terminal interaction with the BBS is still possible if a terminal is all you have at the moment.

I will add that some of the more expensive standalone TNCs have BBS functionality built in or available as an option. PBBS is what I believe it is called. Storage is limited by the amount of memory space and we are talking about values under 100 kbytes or so. It is, however, an almost plug and play BBS that you and your friends can access and use to store messages.

#### Caveats

A few good points to know include:

- A BBS is *infrastructure* and if the SHTF, there is no reason to believe someone's BBS will still be there to serve users. The Virginia Packet Network is focusing a great deal on this important aspect, but it can be hard to predict the harsh circumstances of hard times.
- As stated above we have APRS to thank for a lot of the development of new AX.25 modem products. One thing to keep in mind is the data send and receive buffers are often quite small. APRS packets are short enough to survive this, but practical BBS usage with much larger packets may simply not work with modems designed only for APRS.
- BBS software is in, surprisingly, very active development. BPQ32 is one such example. Yes it is as quirky as the web site design makes it look. It works though. If you decide to try making your own BBS system, BPQ32 is probably the best way to go these days and it is available in both Windows and Linux packages... very cool.

#### Conclusion

Having a way to pass messages between each other in hard times is important. The fact BBS packet radio interactions are no longer very popular may, in fact, be a good thing since traffic to/from such systems may remain manageable. "Infrastructure" concerns aside, I think you are heading in a good direction. It is certainly worth a good long look. We certainly are.

## Answer (score 4, by Tadd KA2DEW)

A Technician Class license or better is required. What equipment you need very much depends on the solution or solutions you pursue.

There exist well-baked schemes for creating relatively long distance vhf/uhf ham-radio-exclusive networks where radios are used to tie stations together over short range, and then many hops are used to pass traffic across longer distances. These schemes include using off-the-shelf commercial WI-FI type gear with and without ham-radio-specific firmware. See Broadband Hamnet/HSMM or ARDEN. Other methods use regular voice FM transceivers, off-the-shelf hardware modems (TNC-PI) or software emulated modems (DireWolf) and a Raspberry PI or other inexpensive computer, to do the links between stations. See TARPN.  
One thing many ham radio operators don't consider as a solution, and your question kind of speaks to this, is that an individual can locate equipment in other locations or sites to boost your ability to 'get out'. A person living in a condo in a valley can take advantage of a hilltop location. Sometimes hams buy hilltop houses and sometimes those hams actually like participating in big projects. Considering how inexpensive, small, and reproducible, packet radio solutions can be, owning and operating two stations is well within the realm of possibility. Having built two stations, you have now developed the expertise to construct a network. Now all you need is participants.

## Answer (score 3, by rclocher3)

I think you're barking up the wrong tree preparing for the possible dystopian future. If the internet is unavailable, short-term or long-term, generally the need is to communicate as widely as circumstances allow to get emergency messages in and out. In times like that, I'd think that you'd want to be able to talk to anybody who can still get on the air. That would mean either 2m/70cm FM for local communications, or HF SSB for longer range. If you restrict yourself to digital protocols, then you'll only be able to reach a small fraction of hams. Also if electricity is scarce, then going analog means that the computer, which generally needs lots more power than the radio, isn't required.

But please don't let me discourage you from checking out ham radio in general, and digital modes in particular. Hams use all sorts of interesting digital technologies. Winlink is a technology used to send email over VHF/UHF or HF, which makes it very valuable for communications in a local or wide-area emergency. If there's a digital mode used in a dystopian future without the internet then Winlink is the one most likely to be it, in my opinion. In order to use Winlink you'll need a "sound card interface" to the radio, which can be home-brewed or purchased.

I've always found AX.25 packet to be an interesting protocol, especially because it runs somewhat parallel to various protocols used on the internet. Unfortunately packet is pretty dead where I live, although it might be alive and well where you are. APRS is a protocol built on top of packet. It's meant to share tactical information and short messages, although in practice it's only used to broadcast weather station data and the locations of hams' cars most of the time. You can see your local APRS activity on aprs.fi. Packet and APRS require a Terminal Node Controller, which is normally a hardware device, although some software can emulate a TNC. As I mentioned in a comment, I don't know how well software TNCs work, so your mileage my vary. Some high-end VHF/UHF radios include a built-in TNC.

In the US, a Technician license is the minimum class of license needed to get on the air; that would get you on VHF and UHF, and a tiny little bit of HF access. That's a great place to start. A ham club near you probably offers a license class. There's lots of information here. Another good way to prepare for the license exam is to buy a book, and take practice tests online. This practice test offers immediate feedback on whether you picked the right answer or not; if you take it frequently, the right answers soon stick in your head. Your local ham club should be quite helpful, so feel free to just drop in on a meeting, whether you have your license or not.

Good luck, and have fun!

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6404/how-to-join-packet-radio-bbs, by Radio1, JSH, Tadd KA2DEW, rclocher3. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
