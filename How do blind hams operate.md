# How do blind hams operate?

*Tags: software, equipment-operation, software-development, disability · score 4*

## Question

In an earlier question, there seemed to be some surprise when I (indirectly) asked about radio modes accessible to a blind operator.

First question: So how do blind hams operate?

If I were to be blind-folded, I could not operate any of my radios, HF or VHF, as I could not even tell if the rig was tuned to a proper legal frequency, as all the radio info is only output via LEDs or LCD displays. I can use a few iPhone apps blindfolded (I've actually written a couple iOS apps for just that use case); the macOS command-line Terminal is usable via VoiceOver; but all of my Mac and Linux SDR apps (and thus digital modes) would be completely unusable, AFAIK.

Second question: If one were to design radios or SDR applications or digital modes or an operating station targeted for vision impaired amateur radio operators, what would be a good set of requirements to optimize for that use case?

For instance: perhaps voice (or Morse Code?) readout for all "front panel" information displays, and some form of feedback for all radio control settings; connector ports that could all be identified by touch.

Any other necessary or beneficial requirements?

## Answer (score 4, by Mike Waters)

I'll answer the first part of your question, Ronald.

I once witnessed a blind ham (WD8PIC) operate. His solid-state transceiver had a speech synthesizer that audibly spoke the frequency when the front-panel SPEECH button was pressed. What is more, he had everything on the front and back panels memorized.

It was simply amazing how much he was able to do for himself. I built him a custom crystal calibrator, and handed him the power plug. He had that plugged in and connected faster than I could. It did not have Braille on the rotary selector switch, but he quickly memorized its different positions before I left.

Many blind hams are helped to erect antennas and set up their station by other hams that can see, and he was no exception. There are also automatic antenna tuners, either built-in or external.

Although he lost his sight at an early age, he attended a school for the blind. They taught him how to do many things for himself.

## Answer (score 3)

There are accessories for some radios that provide a speech capability. Here is a link to a web site, HamRadioAndVision, that has some information.

https://www.hamradioandvision.com/accessible-transceivers-vision/

Also keep in mind that a person can be legally blind but still have some sight. I believe that a person with 20/100 vision is considered to be blind. 20/100 sight means they see at 20 feet the same amount of detail that someone with normal vision sees at 100 feet. Often with magnify aids they can read dials and displays.

Also by using remote control software on a PC with a large monitor they can more easily see.

I cannot find a link, but I remember reading about some small QRP homebrew or kit CW radios that announced the frequency with Morse code as they were tuned.

## Answer (score 3, by blind man)

the only radios that came close to complete accessibbility without third party intervension, was the kenwood brand radios. a few of them needed the VGS-1 board, where as the TS-2000 required the VS-3 board. both boards made the radio fully accessible. the Icom and Yaesu brands, however, have yet to catch up. yes most Icom shack-in-a-box radios have a UT-102 speech board built in, but that's about the extent of it. without third party software, most blind hams would be SOL when it comes to radio operation, in this day and age of direct conversion radios like the 7300 and other SDR radios. as a white stick myself, I appreciate how frustingly annoying it is to have to borrow a pair of eyes to change a setting or three.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15654/how-do-blind-hams-operate, by hotpaw2, Mike Waters, blind man. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
