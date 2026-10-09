# Why am I hearing FM radio show content on 1.355 MHz? (Using CubicSDR and SDR kit)

*Tags: software-defined-radio, frequency · score 5*

## Question

I am just beginning to learn about SDR. I purchased a "NooElec NESDR Mini 2 SDR & DVB-T USB Stick (RTL2832 + R820T2) with Antenna and Remote Control"

I plugged it into my Mac, downloaded CubicSDR, and was quickly able to listen to local FM radio stations. I also searched around and found a weather station as well. So I know it works, and I know how to identify frequencies in the software interface. For example, a local radio station is 93.3 WMMR and I can easily find it.

While exploring, I found that on 1.355 MHz, using FM modulation, I am hearing a hockey game. At a very nearby frequency I can also find a country music station. But (from what I can tell with some web searches) FM radio is supposed to be located within 87.8 MHz to 108 MHz. Which makes me wonder: Why am I hearing entertainment on 1.355 MHz?

To recap: Why am I hearing these hockey games and music stations at a much lower frequency range than normal FM radio? (I am hearing these things at and near 1.355MHz.) By "why" I mean: what are likely reasons that someone is broadcasting at such a low range? What are helpful resources I could use to figure this out? It's just curiosity. This is tonight's mystery as I explore SDR.

(Please see screenshot to see the frequency on the screen. Am I misunderstanding something? The reason I have taken extra time to explain the tech I am using is that I want to validate I am not misunderstanding something about the interface. Am I for sure listening to 1.355 MHz? It seems I am. But is there something I am not considering? Or, alternately, could sports and radio stations be on this low frequency for some reason?)

UPDATE:

I found a different example with much more detail:

Instead of the 1.355 MHz original signal, I have now found another example. In this example, 21.452 MHz and 88.5 MHz share the same signal. Details follow:

On the advice of comments, I listened for the call letters. I wasn't able to find the station from last night, but I easily found another one this morning where a signal on 21.452 MHz is also on 88.5 MHz. And here is what I found. I heard the call letters WXPN. A web search revealed it is 88.5FM in Philadelphia (where I live.) The announcer said it's a University of Pennsylvania Radio station which is available on these frequencies:

88.5 WXPN HD1 Philadelphia

88.7 WXPH HD1 Middletown

91.9 WXPJ HD1 Hacketstown

90.5 WKHS Wharton

and streaming at xpn.org, "member supported radio from the university of pennsylvania"

So as these two screenshots show, I can hear the same station at both 21.452 MHz and 88.5 MHz. Of course with each, I can move a little up or down and still hear it. The signal is more clear on the 88.5 MHz.

Does this additional information provide additional help or insight?

Screenshot 1 is the station on 21.452 MHz:

Screenshot 2 is the same station on 88.5 MHz:

## Answer (score 4, by hobbs - KC2G)

Don't trust everything you see when using hardware well outside its design specifications. The R820T2 tuner chip inside the NESDR Mini 2 was meant to be a TV receiver, and its datasheet says it works between 42 and 1002 MHz. SDR dongles push it beyond those limits, but even NooElec only claims 25 - 1750 MHz "approximately". The signals you're hearing aren't actually at the frequencies they appear on the waterfall, and you can confirm that by listening for a while until you hear a station ID.

## Answer (score 2, by MTA)

I know next to nothing about amateur radio, but I'd like to float a possible explanation. If someone in your area is broadcasting an unmodulated carrier somewhere in the FM broadcast band, and if the frequency of this carrier is 1.355 MHz above or below the sports station's frequency, won't you detect an FM signal way down at 1.355 MHz due to heterodyning? Heterodyned frequencies give you new signals at the sum and difference of the two frequencies.

For example, if the sport station is at 101.1 and the unmodulated carrier is at 102.355, you'll detect FM sports programming at 1.355 and 203.455 MHz. The fact that you heard other programming near this frequency tends to support this hypothesis.

Unlicensed FM modulators that work in the 88-108 broadcast band are out there, and are recently more common due to churches and similar institutions broadcasting their worship services to cars in their parking lots during the pandemic.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20354/why-am-i-hearing-fm-radio-show-content-on-1-355-mhz-using-cubicsdr-and-sdr-kit, by Jack Amoratis, hobbs - KC2G, MTA. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
