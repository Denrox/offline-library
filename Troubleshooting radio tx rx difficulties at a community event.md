# Troubleshooting radio tx/rx difficulties at a community event

*Tags: ht, equipment-troubleshooting, equipment-operation, frs · score 3*

## Question

I volunteered at a community event recently. The event organizers provided a few HTs of unknown provenance but didn't have enough for all teams to use. Several volunteers brought FRS HTs. We were all told to use "channel 3." As you'd expect, the event radios could tx/rx with each other and none of the volunteer FRS radios could tx/rx with the event radios.

I'd like to avoid this problem in the future when community groups work together. Typically no one is licensed in any way, so we should be sticking to FRS or MURS, and the ready availability of FRS HTs makes FRS the most accessible.

My thoughts immediately go to checking

- are the various radios actually using the same band/standard?
- were the event radios using DCS or CTCS?
- were the squelch settings somehow incompatible?

but what else should I be thinking about?

Come to find out the event radios are Ansoko 888S. DCS, CTS, and squelch settings are not seemingly available through the buttons on the radio, so I'm waiting for my CHIRP cable to arrive now that I've secured one of the event radios. Meanwhile it's not clear to me what compatibility the 888S might have with your garden-variety bubble pack FRS radio, and I'm not sure how to investigate that.

Thanks in advance, yes I'm a total noob, and I'm very happy to take pointers to previous questions that I somehow didn't find. WSIX524

## Accepted answer (score 1, by WSIX524)

Come to find out these Ansoko ASK-888S (same equipment, factory, and FCC ID as Baofeng BF-888S) commonly ship with a variety of channels configured, only two of which overlap with GMRS or FRS channels (and don't have the same channel numbers). On those two channels a tone squelch is preconfigured.

(Comparing the radio's settings to the factory image for BF-888S suggests that these ASK-888S are still in their factory configuration.)

All that plus the removable antenna, transmit power, and configurability make them unlawful for unlicensed use, though they can be programmed to use the usual FRS channel settings. So the organizers are going to need to make some decisions about what to do with these.

Oddly enough, Ansoko is also selling these same radios as FRS radios, likely with FRS channels pre-configured, but in the product shots they still have the removable antennas so even if they've locked down the configuration they would still not be legal for unlicensed use. Baofeng lists an FRS version of this radio with a fixed antenna. Most configuration of these radios is done via CHIRP, so if they've locked things down they would be pretty under-capable as FRS radios go.

Anyhow, this brings my "what should I be thinking about" list for general tx/rx compatibility troubleshooting (the core of the original question) to

Settings

- frequency being used
- tone squelch or digital coded squelch settings
- squelch settings
- bandwidth

Equipment

- power issues
- antenna issues
- brokenness

Site

- interference
- obstacles
- distance

…but I'm sure there is more.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/23611/troubleshooting-radio-tx-rx-difficulties-at-a-community-event, by WSIX524. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
