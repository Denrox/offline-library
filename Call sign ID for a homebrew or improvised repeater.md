# Call sign ID for a "homebrew" or improvised repeater?

*Tags: united-states, legal, repeater, callsign · score 6*

## Question

I saw a couple YouTube videos last night about setting up a repeater using a pair of cheap hand-held radios and, at its simplest, an audio patch cable to connect the speaker output of one radio to the mic input on the other. Set frequencies correctly, turn VOX on, and what one HT receives will be retransmitted by the other -- potentially even cross-repeating between 2m and 70cm bands, or whatever bands your radios can use.

There are potential issues with doing this on a non-emergency basis -- protecting the radios from weather, keeping their batteries charged, preventing someone from finding the setup and saying "Hey, free radios!" The one I'm concerned with at the moment, however, is FCC legality. It's my understanding that periodic ID, at least when active, is legally required, but none of the other repeaters I've listened to seem to do this.

Since the cheap HT sets don't have this capability, I'm concerned about the legality of operating a repeater that doesn't identify itself. Just because another repeater doesn't (that I've heard), doesn't mean it's legal to do things that way.

Is there an inexpensive way to insert an ID generator between the receive and transmit HT units in this kind of setup? It would need to detect activity, wait some period of time, and then send an ID, as well as sending periodically if there's no activity. Either voice or Morse is legal, but presuming this will be a digital playback system of some kind, either one is easy to set up.

## Accepted answer (score 7, by hobbs - KC2G)

Are you up to buying a Raspberry Pi, two USB sound cards, some assorted transistors and such, and making your own interface cable? If so, you can run svxlink. It supports all sorts of fancy things related to internet-linking, remote control, and automation, but you don't *need* to use any of that; it will also function just fine as a repeater controller for a standalone repeater, and periodic ID is one of the built-in features.

## Answer (score 3, by Kevin Reid AG6YO)

Many repeaters are not based on radios with built-in ID or any other repeater functions, but rather an ordinary transmitter and receiver (each possibly a transceiver used only for one function, if that's the most economical option) connected by a **repeater controller** through which the audio, PTT, etc. signals pass. The repeater controller knows how to ID (and to do so without interrupting usage of the repeater), generates the "courtesy tone" at the end of repeated transmissions, and may have remotely-controllable special functions (e.g. for repeater linking).

As I haven't built a repeater I can't recommend any specific examples, but I hope that you can find suitable products or project plans now that you know what to call them.

## Answer (score 2, by Reid Crowe)

You're not required to have an independent controller providing an ID.  
As long as you can ensure the repeater does not transmit without IDing. You could ID the repeater yourself by just saying your callsign. When you ID the transmission on the input, the output provides identification as well. Per §97.119, a crossband system would need an ID transmitted on each input (UHF and VHF) since a true crossband repeater is bidirectional and actually has two transmit frequencies.

Edit: Automatic Control

Repeater controllers provide several functions to a repeater system. One is ID. The other is they will implement a system to comply with §97.109(d). Part 97 no longer gives specific direction on how to accomplish automatic control. Alot of the things repeater controllers implement in terms of automatic control are leftovers from past revisions of Part 97. This is detailed in Repeater and Auxiliary Control on the Repeater-Builder website.

It is generally accepted as a best practice to have an alternate means of turning off the system remotely. This could easily be accomplished with a second receiver and a DTMF controller. Alternatively, if your repeater location has internet access, you could use a WiFi controlled outlet.

I should add that this only applies to the United States.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/13146/call-sign-id-for-a-homebrew-or-improvised-repeater, by Zeiss Ikon, hobbs - KC2G, Kevin Reid AG6YO, Reid Crowe. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
