# I just can't get out on my car mounted HF

*Tags: antenna, hf · score 4*

## Question

Would love some advice from you seasoned vets. I have an FT857D in my car which I tend to only use (and really want to use) when I'm stopped and setup camping. I bought a portable Windom antenna which I've been mounting horizontally (about 65cm/2ft from the ground) and i have a 15M/45ft lead line which connects staight to the radio.

I'm just not getting out and I don't know why. My radio is putting out power, low SWR on the antenna and eveything seems ok. Yesterday I ran a sanity test where I continuously broadcasted a recording on FM at 100W on 40M, 20M and 10M and listened to a number of KiwiSDRs near me. Nothing - not a peep. I tried different distances, different states - not a peep. Where's all this energy going?!

The only thing I can think of is that I've a grounding issue - but with the Windom or similar is it reliant on a ground given it's not balanced? Do I need an earth stake connected to my vehicle ground? Perhaps the radio isn't well enough grounded to the chassis - It's only attached to the battery earth at the moment.

I'd love some advice and help here as I'm incredibly keen to start playing with some digital modes like PSK and Winlink but don't seem to be able to get out.

## Accepted answer (score 4, by K7PEH)

Advice on antennas for portable operation. First suggestion: get rid of the windom. Instead, consider end-fed antenna with a counterpoise wire that is laying on the ground. The end-fed antenna can be different lengths but I have been successful with 40 to about 60 feet depending on the band I am operating.

My procedure is to use a nearby tree -- hopefully there is a nearby tree, if not there are some other solutions. Get yourself a sling-shot and some fishing line and a fishing lead weight (not too heavy). Run out about 50 to 75 feet of fishing line, laying on the ground in a way that it will not get tangled when you launch one end of the line up into a tree or over a tree using the sling shot and lead weight. Practice doing this at home -- I am pretty good, normally takes one shot, rarely more than two.

Using the fishing line, now attached at one end to your antenna wire, haul up the antenna wire to a good height. Branches are usually not a problem with most trees as the wire just sits on top of them. Attach the antenna wire at your transceiver to the adapter using a convenient method. I modified a PL-259 to connect the antenna wire to the center pin and a ground counterpoise wire to the ground side of the PL-259. The counterpoise merely lays on the ground stretched out in a direction that works best for the direction you want. Experiment. I use a length of counterpoise wire of about 28 to 30 feet and sometimes more. I have lots of little homemade spools of counterpoise wire of varying lengths.

If you have no trees available, you can do something I did a few times although it costs a little. A telescoping fiberglass pole. I usually had my pickup truck with me and I could put the bottom of the telescoping pole in the stake hole in the back. I have used such a pole for center fed 20-meter V-dipole and for end-Fed antennas. Unfortunately, I broke the fiberglass pole and never replaced it.

I bought a Buddipole Delux antenna with an additional 18 foot telescoping pole that I use most of the time now. I use Dacron lines to guy the extended 18 foot pole though most of the time I do not go all the way to 18 feet, usually about 15 feet but it is sitting in a tripod which lifts it off the ground about 2 feet. The Buddipole works great and I have the most contacts on that antenna -- usually near the ocean on the Oregon coast or Washington coast.

All my QSOs are CW QRP with a variety of transceivers (Norcal 40A on 40-meters, Elecraft KX1, Elecraft KX3 and KX2 on 40/20/17/15. I always use an antenna tuner but with the Buddipole I can usually get a good match at under 2:1 SWR, in fact on 20 usually 1.5:1. I just recently sold the KX2 so my next portable ops will be with the KX3.

I typically use antennas that are easy and fast to setup and take down. After arriving at a site, I am usually operating with the Buddipole in 30 minutes or less.

## Answer (score 6, by Phil Frost - W8II)

An HF antenna only 2 feet from the ground is mostly a device for making warm soil. With such close proximity to the ground, the RF current in the soil will be very high, and ground losses will be very significant.

A low SWR is not indicative of an effective antenna. Consider a dummy load: great SWR, abysmal radiation. In fact, a way to make an antenna with good SWR over a largee bandwidth is to make the antenna lossy. I suspect you will find the SWR bandwidth of your antenna is very good: that implies it's very lossy.

If you want to stick with a wire antenna, try getting it higher, as high as possible. You'll need a portable mast or a big tree on at least one end, ideally both.

If you can't get the antenna higher, try some kind of shortened vertical mounted on a metal vehicle. The MFJ Ham Stick is an inexpensive example.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17153/i-just-can-t-get-out-on-my-car-mounted-hf, by Alex Turner, K7PEH, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
