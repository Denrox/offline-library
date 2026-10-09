# Low Audio out from Kenwood TM-V71A on cross band repeat

*Tags: ht, kenwood, crossband-repeat, kenwood-tm-v71a · score 3*

## Question

Asking this for a web challenged friend:

He lives in an HOA restricted townhouse, so no external antennas. He only does VHF FM, so it's not a big deal. To participate in the local nets he uses his Kenwood TM-V71A in his car to crossband repeat from a HT in his house. All works as it should if the HT is set to low power (1W). If he runs it at 5W, the audio out of the Kenwood is clear, but low.

He thinks this is the HT's doing, but I am not so sure. Could this be the Kenwood clamping the signal somehow? He's inside a house, true, but it's a crappy plastic house :) and he's no more than 50' away from the car/radio at any given time.

## Accepted answer (score 1, by Adam Davis)

The transmitted audio on the TM-V71A appears to come out of the box setup for particularly sensitive microphones. It can be adjusted, but only using programming software, it's not available via front panel menus:

From the open prgoram

EDIT....Menu.....Select Transmit/Receive

In the *Transmit/Receive* dialogue box, change the microphone sensitivity to the desired setting. (High/Medium/Low).

CLOSE the dialogue box and WRITE back to the Xcvr.

My radio arrived with the setting at the medium level. Some stations said that my audio levels were "clean but low". I hung the rig across a scope and the deviation read +3.8khz and -4.0khz (in the Medium senstivity setting and extreme close talking of the mic). Once the setting was changed to high, the deviation swing was in excess of 4khz both ways and "louder". Since then the reports have been normal. "Sounds fine".

(source)

While this is primarily intended to deal with microphone sensitivity differences, during crossband repeat the audio is fully demodulated, then passed through the same amplifiers prior to modulation as the microphone audio goes through.

This should resolve your low audio issues, but if it doesn't you'll probably have to look at the FM deviation to find out whether it's the HT, the mobile, or an issue with the crossband repeat function.

## Answer (score 2, by KR7L)

TM-V71A firmware update Ver.2.00 (May 16, 2008) added microphone sensitivity to the Menu (No. 111) so that MCP-2A is not needed to change it.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1228/low-audio-out-from-kenwood-tm-v71a-on-cross-band-repeat, by WPrecht, Adam Davis, KR7L. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
