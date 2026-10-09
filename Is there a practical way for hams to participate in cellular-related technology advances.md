# Is there a practical way for hams to participate in cellular-related technology advances?

*Tags: legal, wifi, history · score 8*

## Question

My understanding is that there used to be more timely overlap between commercial and amateur radio technology — e.g. helping study ionospheric propagation, relatively early adoption of SSB technology, up through re-purposing business equipment for voice and packet use on 2m/70cm bands.

But now as a ham I feel like knowing about Baudot and "varicode", setting up an APRS bridge, WinLink and EchoLink…? These might be interesting from a historical/cultural perspective, but hardly overlaps what I might learn from a wireless engineering curriculum nowadays. I guess I could buy a shiny D-STAR/WIRES-X setup and send lo-res pictures of the sunset through a local repeater — but given that the underlying AMBE patent *expired* last year, I'm not sure how much that does to "advance the state of the radio art"!

My impression is that the ham world lost its connection with the commercial wireless "side" when that market largely shifted from business bands over to cellular service providers and standards. I know hams are able to re-purpose Wi-Fi equipment and some ham groups have worked on interesting projects like HSMM-Mesh — is there any similar effort using cellular specifications and equipment?

I guess this would entail things like:

- Are there any cellular bands that are close enough to amateur allocation for off-the-shelf cellular modems/filters/antennas to work?
- Does any relatively modern generation of cell technology have enough public datasheets for home/hobby use?
- Can baseband chips be configured sufficiently to e.g. disable encryption and enable identification as usually required by amateur licensing?

For example, I have an old Firefox phone where most of the OS is open source, and I know the SDR/security/open-source crowds have been playing with base station deployments for a while (e.g. OpenBTS) but I am unsure what licensing regime if any they are working under. Is the underlying phone hardware flexible enough that hams could convert it for use under amateur radio guidelines?

## Accepted answer (score 5, by Marcus Müller)

Are there any cellular bands that are close enough to amateur allocation for off-the-shelf cellular modems/filters/antennas to work?

Yep, thanks to the fact that what is a GSM band in Europe is the American 33cm band.

Does any relatively modern generation of cell technology have enough public datasheets for home/hobby use?

Well, 2G and later standards are all accessible, and far as I can tell, at least from a physical layer perspective for free.

Can baseband chips be configured sufficiently to e.g. disable encryption and enable identification as usually required by amateur licensing?

Yes! Or, well, all these features are defined and/or negiotiated by/with the mobile network operator. So, you might need a custom SIM card to work with your modified/custom GSM base station.

I can heartily recommend visiting the osmocom project, which is a forerunner in FOSS cellular infrastructure – not only with respect to developing SDR-based and building commercial hardware-based base stations, but also with respect to building a whole backend network, so that one can make and route actual phone calls, data, messages …

To little surprise, cellular networks are complex beasts, and there's a lot of network components that have to play along with each other.

So, as said, you can use an SDR as your cellular base station, or integrate commercially available base station hardware into an infrastructure of your own. Frankly, from a development point of view, going the SDR route might be more sensible. (Of course, this is all a bit of a point of view: 4G base stations are 100% SDR, but with very application specific design (filters, rates, accelerators for certain operations…))

Emphasis mine:

For example, I have an old Firefox phone where **most of the OS** is open source,

**most** of it, aside from the firmware running on the baseband chip e.g. from qualcomm. You won't get to meddle with that. Anyway, you don't need to, usually, as these things are really flexible and are typically controlled in a lot of parameters via negotiation and setup by software.

and I know the SDR/security/open-source crowds have been playing with base station deployments for a while (e.g. OpenBTS) but I am unsure what licensing regime if any they are working under.

I'll venture to say that most "playing around" doesn't happen with ham licenses (impossible in commercial settings completely, not very useful elsewhere) but by requesting temporary/experimental/… licenses from the respective authority. Terms of that really depend.

Is the underlying phone hardware flexible enough that hams could convert it for use under amateur radio guidelines?

these being? I mean, we're getting *very* country-specific here. But, for example, there's the requirement to not use encryption. Check – that's just something that the handset chooses itself based on what the basestation and communication with the SIM module tell it. Identification with Call Sign? You're running with custom SIM cards, anyway, so there's a direct mapping between any IMSI or IMEI and call sign, if you want so, but if you actually want to transmit the call sign: you're sending unencrypted data, so just stuff it in some regularly sent data frames going nowhere. I've seen people actually pulse their GSM base station's output power, so that to an AM receiver, it sounded like Morse. worst case resort, but works; these technologies can deal with fading, and turning your power down looks just like that.

Other requirements might be bandwidth; and here, again, it really depends on jurisdiction. Some countries allow maximum data rates, other don't restrict that (much better idea, obviously); that precludes a few cellular standards, but not others (you can have very narrowband LTE, for example).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10554/is-there-a-practical-way-for-hams-to-participate-in-cellular-related-technolog, by natevw - AF7TB, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
