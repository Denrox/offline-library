# How are DTMF tones sent through a mic?

*Tags: microphone · score 8*

## Question

In the following diagrams, a microphone pinout is shown for several radios which have DTMF mics that work with them.

How is DTMF sent to the radio without a pin designated "DTMF"? Is it through the microphone audio, or is it through the up/down pins, which are used only when the radio is not transmitting? Or is there some other way to send DTMF?

## Answer (score 9, by mtrberzi)

DTMF is an **audio-frequency based** signaling system that sends tone pairs as audible frequencies,. Most DTMF microphones send the tones as though they were ordinary **microphone audio** to be transmitted, so in the diagrams you have shown, the tones will use the same "MIC AUDIO" or "TX AUDIO" path as when you are talking into the mic.

(And if you're interested in *what* those audio frequencies are, Wikipedia's page on DTMF shows the full tone matrix and a few other details about the signaling system.)

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2286/how-are-dtmf-tones-sent-through-a-mic, by Skyler 440, mtrberzi. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
