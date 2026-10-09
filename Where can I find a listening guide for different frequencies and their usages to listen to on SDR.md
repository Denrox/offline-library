# Where can I find a listening guide for different frequencies and their usages to listen to on SDR?

*Tags: software-defined-radio, frequency, rtl-sdr · score 6*

## Question

I just got an RTL-SDR dongle by Nooelec and am using CubicSDR on Mac (which supports AM, FM, and SSB), and I'm in Canada. I'm able to easily find FM radio stations, but outside of that I'm not sure where to look for interesting frequencies to listen to. (total newbie)

What frequencies should I try tuning into to find various types of signals I can listen to?

## Answer (score 3, by Rowan Hawkins)

I agree that what is interesting is very subjective. You can listen to anything within the frequency range of your device. If another device uses radio frequency within that range you can listen to it. You may not understand it, but that is where learning starts.

In general, anything below 30MHZ will most likely be AM or SSB and above will be FM though there are several exceptions to that. You could start on the low side and work your way up scanning and trying different modes.

As you have mentioned you've already listened to to the easy services.

Every nation has a frequency coordination service usually run by the government which allocates frequencies for users within that country. The US has the FCC, and Canada has Industry Canada. That service says what power and what type of range each frequency can be used with.

Because of the shared border between the Canada and the US, we have rules about what Frequency and how much power we can use for Amateur Radio, but those rules extend to frequencies well beyond the Amateur Radio Bands.

In the United States and Canada. Radio devices have an ID listing which allow you to look the device up in the country's database. That is one place to start searching for things to listen to.

Anything that receives or communicates with a remote device uses some portion of radio spectrum all the way up through and beyond light are listed in those services. unless it uses too low a power to be regulated or uses an unregulated section of spectrum.

There are also websites dedicated to SIGnal IDentification where people share and post waveforms from their SDR's and discuss the technology surrounding the different communication processes.

As for what you find interesting your best way to find that is to Google for

*"Thing you find interesting"* radio frequency.

That will provide you with not only the frequency but usually some information like signal power, modulation type and expected range which can be used to listen or decode it.

I'm not sure about Canada specifically, but the UK has laws about what you can and can't listen to legally. The US does as well, but mostly limited to voice telecommunication.

## Answer (score 3, by hotpaw2)

If you are near any airports, the AM VHF airband or aviation band (roughly between 108 and 137 MHz) is standard throughout most developed countries, and within the frequency range of most generic RTL-SDR dongles.

Another possibility, if you are near any navigable waters, is the VHF marine band, where many countries broadcast weather and/or sea conditions constantly or often. Often narrow-band FM. A web search for Canada marine radio turns up many sites, such as: http://www.offshoreblue.com/communications/vhf-ca.php

Your national government's radio licensing agency likely has a band plan for amateur radio use. Many of those amateur bands are in the VHF and higher region, in the range of an RTL-SDR.

If you have a suitable antenna with a good clear view of the sky, your RTL-SDR can often pick up satellite signals as various orbital objects pass overhead.

Many countries use VHF bands for police and fire dispatch (there are probably online scanner frequency lists for your locale in various search databases); but make sure your country's laws allow reception of such.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7350/where-can-i-find-a-listening-guide-for-different-frequencies-and-their-usages-, by Rowan Hawkins, hotpaw2. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
