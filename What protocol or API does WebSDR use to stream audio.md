# What protocol or API does WebSDR use to stream audio?

*Tags: software-defined-radio, software · score 6*

## Question

What documented protocol or API does WebSDR use to stream audio over the internet?

I'm interested in capturing a WebSDR audio stream using a small embedded device which has lots of audio DSP capability, good internet access (TCP/UDP network sockets, raw http, etc.), but no (HTML/JS) browser or Java/JVM runtime.

## Answer (score 5, by Kevin Reid AG6YO)

The "HTML5"-compatible (not using Java applets) audio interface for WebSDR uses audio samples streamed over a WebSocket connection — this can be seen from the JS client files it downloads.

However, the author of WebSDR has indicated that they do not wish the software used in ways other than via the provided web client (in their FAQ and even in a comment in the very JS file I'm speaking of!) so I recommend that you do not pursue this project without asking the author, as they might well consider it abuse of their service for you to connect with an alternate client.

If you merely want a remote radio receiver and not specifically to use the hardware of existing WebSDR installations, there are several open-source possibilities. If you're interested in that option, I suggest asking about it as a separate question.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2272/what-protocol-or-api-does-websdr-use-to-stream-audio, by hotpaw2, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
