# Home-brew 10 meter walkie talkies?

*Tags: diy · score 9*

## Question

"When I was in high school, we had 8 hams at once. (Probably rare) 4 of us built little 10 meter walkie-talkies and had great fun using them on Field Day, hiking or around town. It was especially fun because this was pre-cellphone and ordinary non-ham folks could not buy any kind of walkie-talkie. We were hi-tech and really cool. Now the average kid has unused Radio shack talkies in his dresser and couldn't care less about them."

That is from the author of Crystal Sets to Sideband.

Now I'm in the generation of the "radio shack unused walkie talkies" and I want to build myself a 10 meter walkie talkie. I have fairly descent soldering skills and I have been building electronics for about 5 years (I probably started when I was 10)

How can I build a 10 meter handheld, and what parts do I need. I would like getting transistors, inductors, etc and building the whole thing with discrete components (no IC's)

## Answer (score 8, by WPrecht)

I am not sure if you are asking about converting a CB walkie-talkie to 10m or building one from scratch so I will address both, not feeling like working at the moment:

### Converting a CB walkie-talkie

What it will take to Convert a CB walkie-talkie is going to depend on how it's contructed, of course. It can be as simple as replacing one or more crystals. A cheap one will have one offset crystal to move the channels up into the CB range. Fancier ones might have several crystals. Basically you want to move it "up" 2MHz to get you into about 29MHz. You'll be stuck with the channel concept on the frequencies of the crystals, of course, but that can be OK.

A newer CB will probably have some sort of DDS which would make it much much harder to convert.

As a note, CB radios are (usually) AM, and while this is fine on 10m, that's something to remember. Newer ones support SSB as well, but might be much more difficult to mod.

If you want to get crazy you can figure out how to supress the carrier and do DSB or supress both the carrier and the lower sideband. Even more adventurous would be to disconnect the AM modulator, add an FM detector chip (I know you want discrete, but this is just blue sky stuff) and modulating the VCO, then you'd be doing FM. Although these days most repeaters have a PL, which makes this mod a lot less useful.

### Homebrew 10m walkie-talkie

Poking around on the net, there are a bunch of QRP 10m transceivers that could be built into a walkie-talkie form factor. This one looks pretty doable:

The only IC is a small op-amp for the audio out. Looking the schematic over, it's setup for 220V AC power (the author is Australian, but he's probably OK despite that :) ). Since you are going to want to run on battery, you can axe that whole section and wire the DC source right in.

Another option is a 14MHz SSB transceiver. This page details an all discrete component version that will run on battery power. You can either roll with it on 20m or convert it up to 10m.

Happy Soldering.

## Answer (score 5, by Zachary McGrew)

The *only* HT kit I've ever seen in my searches was the "TJ2B MK2 5 Band SSB Handheld Transceiver" from Youkits.

**From Youkits themselves:**

TX/RX: *5-21MHz*, covering 60m, 40m, 20m,17m and 15m band (No TX on 30m)

So it won't work on the 10m band, but it will work on 5 other bands.

***However* WB8YQJ's eHam review says this:**

The new TJ2B "Kit B" seemed ideal, offering *14Mhz to 30Mhz* SSB +(CW Receive) in a handheld case and $269 plus ship.

## Answer (score 2, by L. Wm. Roberts)

About as simple as a half-watt can get.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/749/home-brew-10-meter-walkie-talkies, by Skyler 440, WPrecht, Zachary McGrew, L. Wm. Roberts. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
