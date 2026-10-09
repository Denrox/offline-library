# Using standard headphones with the Yaesu FT-60?

*Tags: ht, equipment-design, yaesu, equipment, audio-interface · score 6*

## Question

I just got a Yaesu FT-60R handheld, along with the MH-37A4B earpiece. After having it around for a couple days, I think I'd like to be able to connect standard headphones to it, so as to be able to listen privately without carrying around an extra accessory.

I see that the pinout for the 4-contact combined "MIC/SP" jack is known, though not in the manual, and there is a a first-party adapter cable (CT-44). However, this doesn't tell me without buying/building whether it's possible to use it in the way I want; specifically:

**If I connect only headphones to the FT-60, using an appropriately wired adapter, can I still use the *internal* microphone and PTT switch to transmit**, or will just having a plug inserted cut out the internal mic?

(I haven't tested this out because I don't have a bare 4-contact plug to experiment, and I hear that plugging in headphones with a standard 3-contact plug results in misbehavior.)

## Accepted answer (score 6, by Kevin Reid AG6YO)

I've done some tests with what I have available (now including the CT-44 adapter).

With the MH-37A4B Earpiece/Microphone connected, the internal microphone can still be used: whichever mic has its PTT switch pressed will provide transmit audio and the other will not. Furthermore, the external microphone is open-circuit when its PTT is not pressed. Therefore, **yes, given an appropriate adapter** one can use headphones without a microphone plugged into the FT-60.

Connecting stereo headphones (64Ω impedance) into the jack directly did indeed result in misbehavior as reported elsewhere on the Internet, including a nonfunctional keypad or being stuck in transmit mode; presumably due to mis-connection of the mic line. Using an appropriately wired cable such as the CT-44 solves this problem, but produces mono (left channel only) audio since it has a mono jack.

Furthermore, loud thumps were heard when the radio is switched on or when it unmutes (due to an offset of 3 V DC when unmuted, 0 V when muted). These are also present but considerably milder on the internal speaker or earpiece accessory presumably due to their frequency response.

I have solved the above problems by building an adapter to stack onto the CT-44, which provides stereo audio and a blocking capacitor (which is an adequate but not ideal fix for the thumps). It could also be built together with a 4-pole plug and no CT-44, but the FT-60's 4-pole jack has slightly different dimensions than the standard smartphone-headset-style 4-pole plug and will not make proper contact with one.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1933/using-standard-headphones-with-the-yaesu-ft-60, by Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
