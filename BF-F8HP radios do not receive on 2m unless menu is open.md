# BF-F8HP radios do not receive on 2m unless menu is open

*Tags: baofeng, equipment-troubleshooting, squelch · score 3*

## Question

I just got 4 BF-F8HP radios, 2 knockoffs, and 2 "legits"; definitions of knockoff and legit come from a website I found. All 4 of them are having this issue.

I can transmit fine on both 2m and 70cm, and I can receive on 70cm fine, but I can only receive short distances of around a mile on 2m. Unless I open up the menu while listening, as long as the menu is open I can hear just fine for long distances picking up local repeaters in the area.

I have tried a Menu 40 reset, and i've tried using CHIRP to reload the firmware. So far nothing has had any affect in altering this issue.

I am completely stumped, I have submitted a support request, but i've heard that baofeng only responds to those if you ordered off their site directly. Is this a fundamental flaw in this line of their radios? Is there any way to resolve it?

A local ham brought over his UV-5R, and using my antenna system he was able to transmit and receive just fine to the local repeaters. So I know it is an issue with my radios. He went over all the settings in my radios and we compared them to the settings in his in case I messed something up. In fact, he was able to hit the local repeater using low power on the UV-5R, while mine can't receive even if someone a few miles away is putting out 50 watts.

He is able to hear me transmit on 2m. And I am able to hear him on 2m when he drives to within a mile or so of me. Again, his baofeng (the older model) does not have this issue.

**Edit:** N5R340B & F8HP-1 are the firmware messages on two of my radios. The Knockoff ones come up with a blank Settings page in CHIRP, but when trying to upload an image to them I get the message at the end of the upload that "Other Settings" could not be sent due to a firmware miss match, and that the radio is model HN5RV011(bunch of weird symbols)

My ham friend took one of my radios to run tests on it. At two other transmit locations it worked fine for him and he was able to hit repeaters even further away than the one I was trying to reach in addition to the one I was going for. He ran a power output test on it and discovered that the "8 watt" radio was not even putting out 6 watts, so they appear to be falsely advertised. The tests showed the older UV-5R radios putting out 4.75 watts, while the F8HP models put out 5.75 watts.

**Edit2:** We hooked my baofeng up to a 50 ohm cable on a short antenna outside my house and it worked correctly. So there might be something with the 70 ohm 50 ft cable I am running inside the house that is tripping the issue on this model of baofeng.

I'm starting to wonder if it could be some sort of safety measure built into the newer models that the older ones don't have. That doesn't make a lot of sense to me, but it is so weird that the issue only occurs on all new baofeng models and only on the 70 ohm cable.

**Edit3 (Details from comments):** For clarification. When I first discovered this problem it was during on-the-air testing with a ham friend. Since then, the majority of my tests have been transmitting static to the repeater and seeing if it will open my squelch immediately after the brief transmit. I was shown this method by my ham friend on his older baofeng while he was at my house; we were proving that his radio worked fine on my antenna setup.

I have tried both frequency and channel mode. Channel mode I loaded with CHIRP from a local repeater library. From a ham friends house I have no problems, my radio can send and receive to a repeater even further away using a worse antenna. I have also tried adjusting the squelch several times; My friends baofeng at 3 works, mine at 1 does not without the menu hack.

I tried multiple manual configurations with and without tones and adjusting squelch and comparing my settings to my ham friends working older baofeng before ever even downloading CHIRP. With CHIRP I tried "flashing" (I've heard you can't truly flash just configure) an image off the Internet for the model of radio I was using.

I haven't been able to truly test the MONI button also fixing the issue because the repeater is not very active. I'm working on scheduling a time for that. Looking on the Internet, it seems like this is a pretty common issue with the newer baofengs, one repeated solution I have seen is re-flashing the correct firmware/config. If so, then the one I found wasn't the right one.

**Edit 4:** After more testing I discovered the following.

- All 4 radios work with a mag mount car antenna and a short 50 ohm cable.
- The "official" radios respond to both the MONI and menu buttons to get them working on the longer cables.
- A 50' cable of either 70ohm or 50ohm does not work without the MONI or menu hacks.
- The "knock-off" radios only respond to the menu button to get them working on the longer cables.
- Config uploads and configurations made using CHIRP do not fix or even alter the issue.
- Channel vs Frequency mode does not make a difference.
- Configuring the radio by hand does not make a difference.
- Different squelch settings do not have an affect, other than high settings prevent the radio from receiving at all.
- High, Medium, and Low power all work and can hit the repeater both using the mag mount, and using the menu hack with the longer cable.

**Conclusion:** At this point, I think there is a firmware bug that is unfixable by the user. There's still a remote chance that there is a config out there that could fix it. However, all my research on the Internet has shown that this is a common issue at various levels for these radios; especially first few batches of new models. My best bet at this point seems to be to try and return my radios and get and older model that has had more of its bugs worked out.

**Edit 5 (Solution?):** I finished doing another extensive round of testing, and made a few more discoveries I will document here. I don't want to get rid of the prior testing as it was all part of the road of discovery getting here.

In this round of testing I discovered that even though the UV-5R radios had their squelch opened when hitting the repeater, no audio was coming through, which pretty much invalidated the majority of the testing I had done until now. Since I could no longer use simply having the squelch opened as a valid test, another ham volunteered to be on the receiving end at his house for some true two way communication testing.

A post I was pointed to was talking about how the Squelch settings on Baofeng radios weren't real, and were just lookup entries that are really mapped to internal squelch values. Chirp has been modified to download a settings page that allows you to modify these internal Squelch mappings; by default they are mapped to some fairly high values.

So using chirp, I modified a UV-5R, and the "official" BF-F8HP (firmware N5R340B F8HP-1) radios to map 0, 1, 2, 3 to true 0, 1, 2, 3 squelch values. The "knockoff" BF-F8HP is running firmware HN5RV011, which from what I have read sounds like it is a version of the UV-5R firmware. Unfortunately, CHIRP is unable to display a settings page for that HN5RV011 firmware (I opened a ticket to see if this could be added to CHIRP); so I took a chance and uploaded the UV-5R (firmware HN5RV01, with modified squelch mapping values) to the knockoff BF-F8HP radio.

In several copies of all three radio models I discovered the following.

- The "nockoff" BF-F8HP radios with a UV-5R squelch mapping modified config uploaded to them actually worked as expected on SQL setting 2. CHIRP claims it was unable to upload the settings portion of the config so I do not know how this worked, but I double checked with a non-modified version of the radio and it did not work, until I uploaded the config to it as well, then it started working.
- The "official" BF-F8HP and the newer UV-5R (HN5RV01 firmware) radios did not work even with SQL setting 1; I think the older UV-5R (firmware BFB293) worked though. They still required the menu button hack to get the receive to come through.
- All the radios performed really well in every other location we tested them in. So my house is simply located in an area with challenging reception path issues. My ham friend did sensitivity testing on the "official" BF-F8HP radios and said they performed perfectly, but added that the testing only tested opening the squelch, not passing audio.

Since the knock-off radios were my original ones and the ones I really wanted to work, this has solved my issue. I do not think it is a good solution. And it sounds like these radios need some better SQL configuration options to deal with issues like this.

**Edit 5 (Details):** After continued use of the BF-F8HP I discovered by accident that the hack described above only works if the radio is set to dual listen mode, so it is receiving on both displayed channels. If it is set to single channel listen mode the hack does not work and the problem still exists. Possibly this is why I was never able to get the UV-5R radios to work with the hack.

## Accepted answer (score 5, by rclocher3)

The most likely scenario is that all four radios have the same problem. It's possible that the problem is a manufacturing defect, but that's unlikely, especially if you got the radios from different sources. It doesn't sound like a hardware problem, because the radios hear fine when the menu is open, so the problem sounds like a firmware or configuration issue. It's possible that you have the same buggy firmware revision with each radio, but that seems unlikely also. It seems to me that the most likely thing is that you somehow misconfigured each radio.

Troubleshooting these problems over the internet is difficult because we have very little information. Your best bet would be to find a helpful local. Every ham club has at least one person who is good at programming VHF/UHF FM radios who would probably find your problem fairly quickly. The ARRL has a helpful ham club search tool, if you don't know what your local clubs are.

You didn't mention how you programmed the radios, but you mentioned CHIRP so my guess is that you used software to program them, which makes sense because Baofengs are notoriously difficult to program from the front panel. By the way, I'm fairly confident that CHIRP is not meant to load firmware into a radio.

I have two troubleshooting suggestions. First, try tuning to a repeater that you currently can't hear, and then hold the MONI (monitor) button, ideally while a buddy talks through the repeater. If you can hear the repeater with the monitor function, but not otherwise, then your radio is probably misconfigured. The other suggestion is that if you are trying to listen to the repeater in channel mode, then try tuning it in frequency mode, without worrying about repeater offset, CTCSS (PL) tone, CDCSS (DCS) code, etc. (Don't try transmitting.) If you can hear the repeater OK in frequency mode, then the problem is probably that you have the channel programmed incorrectly, or your squelch setting is wrong.

If you entered the repeater settings into CHIRP or the Baofeng software yourself, then you probably made a mistake, which is easy to do. In that case my advice would be to find another local ham who knows how to program radios through CHIRP, and have that ham program one or all of your radios for you; his or her channel list is probably better than yours anyway. He or she will probably easily be able to spot what you did wrong.

If you did program the radios yourself using CHIRP, you downloaded the radio settings into CHIRP first, made changes, and then uploaded back to the radio, right? You have to do that for each radio. If you upload a setup that came from one radio into another radio, then you risk "bricking" it.

If I had to guess what your problem is just from the information in your question, I'd guess that you set the radios to use a CTCSS tone or CDCSS code for both transmit and receive for each repeater, which would be incorrect. Repeaters typically require a CTCSS tone or CDCSS code on your transmitted signal to reduce interference, but when a repeater transmits it typically doesn't use a tone or code. If you programmed your radio to expect a tone or code on that channel, then I'm not surprised that the repeater doesn't open the squelch.

Your problem could also be just the squelch setting, so try experimenting with that.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18647/bf-f8hp-radios-do-not-receive-on-2m-unless-menu-is-open, by Jereme, rclocher3. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
