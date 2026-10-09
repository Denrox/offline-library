# What do the WSJT-X split frequency options actually do under FT8?

*Tags: ft8, wsjt-x, split-frequency · score 3*

## Question

Maybe I have this all wrong, but as I understand FT8, we're all communicating within a slice of the band ~3 kHz wide. Within this slice, we each have our own sub-slice, and the location of my slice is controlled by what I put as the "Tx" frequency in WSJT-X. This number is both 1) a small offset (since it's expressed in mere hertz) from the frequency showing on my radio's dial; and probably also 2) the audio tone you'll hear out of me if you listen to that dial frequency.

If I double-click someone calling "CQ" in the Band Activity panel, WSJT-X will (by default) set my Tx and Rx frequencies to their Tx frequency as shown in that panel. If I've turned on "Hold Tx Freq," then my Tx frequency doesn't change.

Either way, it seems to me that I don't want to be on the same Tx frequency as someone I want to communicate with. I think you'd either want to 1) use "Hold Tx Freq," and manually control the Tx frequency such that it's close to but different from the Tx frequency of the person you're trying to contact; or 2) turn off "Hold Tx Freq," but adjust the Tx frequency slightly after clicking on someone in "Band Activity." In this manner, you get your Rx frequency to equal their Tx frequency, and transmit on a nearby frequency.

I think I may be wrong about some of this, though, because I can't understand where the "Split" setting in WSJT-X comes into play. It seems like there's an inherent split there already, if I operate one of the two ways I described in the last paragraph. I don't understand where "another split" would come into play.

The one theory I have (other than "I just don't get how FT8 works") is that somehow the "Split" setting in WSJT-X controls *how* the split is implemented. That is, does WSJT-X actually use my rig's split feature, or does it just kind of kerchunk my rig manually between the 2 frequencies when it goes to transmit / stop transmitting?

Thanks for any insight you can share with me!

## Accepted answer (score 3, by gschro)

Keep in mind that FT8 works in 15 second periods. After the station calls CQ in one 15 second period, it will be listening on the next 15 second period. So it is OK if you transmit your response on the same frequency (audio tone) as the CQ. There might be strategic reasons you want to respond on another frequency, and WSJT-X allows for that.

Regarding split, the term is a little confusing. The idea is that you don't want your transmitted audio tone near the edge of your SSB audio signal (i.e. down near 300 Hz or up near 3000 Hz). The reason is you may get a cleaner signal trying to stay in the center. So with split, WSJT-X will adjust your transmit VFO, and your audio tone, as necessary, so your actual audio tone is near the middle of your SSB audio signal (in the range 1500-2000 Hz). Because it adjusts both your VFO and your audio tone, as necessary, you will still be transmitting where you expect.

I believe the term "split" is used because WSJT-X will use the split feature of your rig, if available, to accomplish this. If you say "fake it" it will simply adjust the active VFO when transmitting. So if you look carefully, you might see your rig VFO display changing when transmitting. Of course, this depends the CAT control.

One more thing, if you put WSJT-X into fox or hound mode, often for DXpeditions, then operation is more like "normal" split. So WSJT-X tries to keep the DX station (fox) and the chasers (hounds) transmitting on different audio tones. The DX station transmits using lower audio tones, and the hounds respond on higher tones ("up"). Of course, like with "normal" split, there are always operators who don't understand what is going on, and transmit over the DX station lol.

## Answer (score 2, by hobbs - KC2G)

The one theory I have (other than "I just don't get how FT8 works") is that somehow the "Split" setting in WSJT-X controls how the split is implemented. That is, does WSJT-X actually use my rig's split feature, or does it just kind of kerchunk my rig manually between the 2 frequencies when it goes to transmit / stop transmitting?

Yes, it's this. And its operation has *nothing to do* with whether your TX and RX offsets are the same or different.

WSJT-X prefers to keep the transmit audio frequency it sends to the radio somewhere between 1500Hz and 2000Hz because on many radios that's the frequency range least likely to be affected by any filtering or distortion.

If "Split" is set to "Rig", WSJT-X will compute the offset necessary to put your TX signal in the middle of the audio passband, and program the radio in split mode so that that offset is applied when you transmit. So for instance if you're listening on 14.074 MHz and you have a Tx offset of 300Hz, WSJT-X will set the rig to split mode with VFOB set to 14.0725 MHz, and generate audio tones at 1800Hz. That way your signal ends up at 14,074,300Hz just like you expected, but without any actual 300Hz audio. This works best on older radios where the VFO settling time can be quite long, but split mode uses a "real" separate VFO that can be switched in instantaneously.

If "Split" is set to "Fake It", WSJT-X does the same math as it does for "Rig", but it doesn't program the radio in split mode. It just sends a CAT command to change the frequency before it goes into TX, and again when it goes into RX. This is fine on newer (probably mid-90s and later) radios that can process the CAT command quickly and have a short enough VFO settling time, and it doesn't wipe out your second VFO.

If "Split" is set to "None", WSJT-X will ignore the whole thing and generate audio at whatever actual TX offset you selected. Radios with a digital (direct USB or Ethernet) connection to the computer and a "data mode" setting usually have a perfectly flat TX audio path, so they can use this mode with no problem at all, and it's the simplest thing to do.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/22790/what-do-the-wsjt-x-split-frequency-options-actually-do-under-ft8, by user1172763, gschro, hobbs - KC2G. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
