# How would you get an "I'm alive" message to family in another state using amateur radio?

*Tags: mobile, wire-antenna, emergency · score 7*

## Question

I'm researching options for getting an "I'm alive" message during a disaster response out to family in another state that aren't HAMs.

There are likely to be a lot of possible answers that are art and style rather than one "right" answer, so some possible parameters. Let me know if this still ends up too vague.

- Technician or General class.
- Voice (aka phone), rather than CW highly preferred.
- Without a repeater, or at least not one for at least several hundred miles. e.g. Western Washington to California (800+) or Idaho. (500-600)
- Any suggested bands/frequencies where I might find someone willing to call a landline on my behalf? I'm familiar with UHF and VHF calling frequencies - I can look up calling equivalent freqs once I settle on a band.
- Portable. Something I can pack up and take, rather than needing a permanent or very bulky antenna installation or base station. I'm wondering if, matching the other constraints, there's an option for a coiled wire antenna that I can effectively throw up a tree. Ultra portable station - car mobile size would be ideal. I'd likely have a lot of other stuff with me.
- Common battery types - ideally 12v off the car. I'm unclear on the wattage I'd need for, say 500-600 miles simplex. 100-150w seems like starting to stretch the limits on a car inverter, so I may have to look for a generator based solution.
- Economical. I may be just into the realm of pipe-dreams here, but at some point the cost would make satellite phone solutions more practical. I'm okay with low-end solutions (aka 'junk brands') - a disposable solution means I'm more likely to have it with me when I need it, rather than sitting at home in a padded case.
- My focus is mainly on CERT short-term solutions during an event like the Cascadia subduction fault, rather than "end of the world" long term "find the survivors."

This is a bit of a companion question to the [short-range family communication question](Options%20for%20family%20short%20range%20communication%20in%20an%20emergency.md).

I've talked with some locals with base stations and fixed antennas - but they're mostly focused on contesting at significantly further distances. The local ARES team does have satellite phone and bulkier base-station setups - but that's focused on more continuous and varied operation.

Satellite phones are certainly the most purpose built option here, but pricey. Ideally I'd like a solution that I might use for other things - possibly as an excuse to start getting into HF...

Thanks in advance - WE7MOR.

## Accepted answer (score 8, by rclocher3)

When establishing emergency communications in a disaster, the natural choice of band is one that will allow you to communicate out of the disaster zone. Given the scenario you describe, a massive earthquake affecting the West Coast of North America from Northern California to British Columbia, that probably means HF. HF privileges with a US Technician license are limited, so Technician-class licensees preparing for this scenario would do well to upgrade.

There are many fine HF radios that are very portable. Almost all of the more-portable HF rigs are powered by 12 VDC, so no need for an inverter (unless you need one for a computer). The smallest and most portable HF radios are meant for QRP operation, 5 – 10 W, but for emergency communications 100 W would be better. There are several radios that are sized to be installed in a vehicle that cover HF to UHF; one of those radios would be excellent for your purpose. There are also many fine HF radios, some of which include VHF and UHF, that are a little larger but still quite portable.

The antenna is more problematic; generally speaking, your goals of being very portable and easy to set up conflict with the goal of being an efficient radiator. I assume that you also want a multi-band antenna, because you would probably prefer 20m – 10m in the daytime, and 40m – 80m at night. (Many of the regional HF nets are on 80m.) Here are some antennas to consider:


Long wire: a long wire, typically at least 40 m / 130 ft, up high in the trees, connected to an antenna tuner. Advantages: inexpensive; easy to build from whatever wire is on hand; multi-band. Disadvantages: needs lots of wire, must be up high, RF in the shack problems, external antenna tuner required, may not tune on all bands.


G5RV / ZS6BKW: a popular but often-misunderstood wire antenna that includes a section of ladder-line feed. Can be homebrewed or purchased. Advantages: inexpensive; multi-band. Disadvantages: works very poorly on some bands; needs to be up high for best performance; requires a balun and an antenna tuner.


Off-center-fed "Windom": another popular but misunderstood wire antenna. Advantages: inexpensive; multi-band. Disadvantages: performance varies, quality of the balun is crucial; requires a balun and an antenna tuner; needs to be up high for best performance.


Loop: a wire antenna that makes a big horizontal loop, supported by trees. Advantages: inexpensive; multi-band. Disadvantages: requires an antenna tuner; needs to be up high for best performance; may not tune up on all bands.


Commercially-made vertical: I'm speaking of commercially-made multi-band vertical antennas that when assembled are 8 – 12 m / 26 – 40 ft long. Generally comes in a box that's about 1.5 m / 5 ft long. Advantages: no need for trees; multi-band; often doesn't require a tuner. Disadvantages: not as portable; more expensive; requires wire radials laid on the ground; low angle of radiation, which is generally better for long-range communications than intermediate-range.


Car-mounted vertical. Advantages: if your solution is a mobile radio, than a car-mounted antenna is probably already connected. Disadvantages: efficiency ranges from bad to terrible, depending on the band, how large the antenna is, and how much you're willing to spend; some models are quite expensive.


Backpacker vertical (my term): a vertical antenna that is meant to be as portable as possible. Homebrew designs and commercial varieties exist. Advantages: no trees required; very portable; antenna tuner generally not needed. Disadvantages: flimsy; radials required; may not be able to handle 100 W; efficiency is generally low; some of the commercial models are surprisingly expensive.

To summarize the antennas, if the antenna is to be efficient, multi-band, and portable, then we're probably talking about a wire antenna *up high* (generally at least 1/4 λ). Unfortunately, I've found that most hams just can't throw a rock attached to a cord very high, so you may wish to consider a tool to help you get the wire over the tree limb. I use an arborist throw bag and a water-balloon slingshot.

Many of the wire antennas require an antenna tuner. Many radios include antenna tuners, but many built-in antenna tuners have limited range. An external antenna tuner generally has a better tuning range.

Your question is rather open-ended, so I'll stop now, rather than talking about modes, power sources, and other considerations. I will say that if you want to use ham radio in an emergency, you should get your equipment ready and practice the techniques beforehand. Also keep in mind that in a wide-ranging disaster, there will be a very large need for emergency communications; you might want to think about joining your local ARES group so that you can help other people too.

## Answer (score 9, by K7PEH)

The ARRL NTS (National Traffic System) is the method you would use to send messages to anyone anywhere in North America and in concert with other traffic systems to many parts of the world.

NTS has many message passing scheduled times on multiple bands. In the night time hours, 80 meters is so popular that sometimes message trafficking networks are most of the stations you can hear from 5 PM to 8 PM.

You can find any scheduled traffic group in your area. This link will help you get started.

NTS works by dividing North America (USA & Canada) into various levels of traffic handling and areas. The way this works is that you can contact a local (in your area) net on HF or VHF/UHF and then they take the message and relay it up to the next level that routes the message to the local traffic net in the area of the party to receive the message. In almost all cases that I have personally handled traffic for areas in and around the Seattle area I have been given a local phone number to contact the party to pass the message.

I see that you are located in Redmond (via QRZ), I am located in Kirkland, Totem Lake area. I participate in three NTS traffic handling nets each night. They are all on 80 meters and if you are on HF with capabilities on 80 meters you are free to join up. Note that these are not the only ones.

Seattle (Western Washington and greater Northwest) Traffic Nets (a few of them):

- WARTS (Washington Amateur Radio Traffic System), meets at 5:45 PM PDT on 3975 KHz using mode SSB (LSB). Note that these are summer hours a little later than their winter hour at 5:30 PM when the band going long as the evening draws upon us.
- WSN (Washington Section Net), meets at 6:45 PM PDT, on 3563 KHz using CW. Winter hours time is 6:15 PM.
- OSN/1 (Oregon Section Net), meets at 6:30 PM PST, on 3569 KHz using CW. This is the regular scheduled time, OSN/1 does not change for seasonal hours.
- Beaver State Net (Oregon), meets at 5:30 PM PST, on 3920 KHz using SSB.
- Columbia Basin Net (Oregon/Washington), meets on 3960 KHz using SSB, at 6:00 PM PST.

I could list more but will hold off for now. Note that there is also RN7 CW net and PAN (Pacific Area Net) CW which meat also on 80 meters a little later in the evenings. They are the next level up of traffic handling and usually handle cross country messaging.

Give some of these a try. Just dial into the frequency of any of the nets I mention above and listen in. Unfortunately due to the cold dark nights of winter, the short skip almost doesn't exist so sometimes hard to hear net control.

## Answer (score 6, by DK3CW)

Send an HF-E-Mail addressed to your familymembers using a system like ***WinLink 2000*** (http://www.winlink.org). It uses Radio Message Servers (RMS), which provide a bridge between the Central Message Servers (CMS) connected to the Internet and radio clients. Radio modes available for WinLink:

- HF

 - Soundcard modes (requires audio cable between your HF SSB radio and your PC or smartphone and PTT triggering via VOX, serial cable or CAT cable)

 - WINMOR
 - ARDOP (beta, will substitute WINMOR soon)
 - Automatic Link Establishment MIL-STD-188-141
 - TNC modes (requires TNC, e.g. Pactor Controller PTC)

 - PACTOR I
 - PACTOR II
 - PACTOR III
 - PACTOR IV
 - Robust Packet
- VHF/UHF

 - AX.25

 - Packet Radio (using TNC or soundcard modem)
 - APRS using APRSLink
- SHF

 - TCP/IP Networks on SHF, like HamNet in continental europe (Map: http://hamnetdb.net/lsp_map.cgi)

My portable setup:

- FT-817ND
- SCS PTC-II with PACTOR III licence
- homemade soundcard interface (PTT via VOX with minimum VOX delay)
- 5 Ah 12 V battery
- 10m (~33ft) glass fiber reinforced pole (1.3 kgs)
- random wire or dipole
- MFJ-16010 manual tuner
- Netbook running Arch Linux, Debian Linux and Windows 10
- 12V solar panels

As I spent some days in the European Alps, outside of GSM coverage area, I was able to send E-Mails on HF (depending on propagation and time of day, I've used 80, 40, 30, 20, or 17m) not only via some European RMS but also via a Canadian RMS in Nova Scotia (distance was abt 6,000 km) with 5W into 10m end-fed vertical on 40m in PACTOR III and WINMOR).

As I went transalpine on my ham radio bicycle, I've used

- FT-100
- 3m vertical antenna mounted on my mono-wheel bicycle carrier
- MFJ-929 Automatic tuner
- SCS PTC-II with PACTOR III licence
- 12 V 12 Ah battery

instead.

You can use different client software. *WinLink Express* (formerly known as RMS Express) and *Airmail* on Windows machines or a multi-platform solution like *pat*.

I'd like to provide more links, but I can't due to missing reputation on ham.stackexchange

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6946/how-would-you-get-an-i-m-alive-message-to-family-in-another-state-using-amateu, by Matthew Wetmore, rclocher3, K7PEH, DK3CW. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
