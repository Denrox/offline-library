# How can I decode SSTV with only macOS software?

*Tags: software, sstv, macos · score 6*

## Question

Have you used an SSTV decoding application on an up-to-date version of macOS? Which one, and if you built from source, can you share the steps you took to do so?

I do not know of a single working macOS application for SSTV decoding. I've been playing SSTV signals over my Mac's speakers, captured with my RTL-SDR dongle, and using Robo36 on an Android phone to decode the image, as has everyone else I know, but this comes with additional problems. There have been instances of engine-noise (or even the occasional donkey bray) introducing unwanted artifacts in the decoded image.

## Accepted answer (score 4, by Aleksander Alekseev - R2AUK)

MultiScan 3B works fine in terms of decoding. This being said I had some issues making it work with my external sound card for *transmitting* SSTV. For some reason transmitted images turned out to be cropped. I accidentally figured this out using cqsstv.com.

Eventually I ended up using a Linux laptop and QSSTV software. Still if you are interested only in decoding, MultiScan 3B should be OK.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15035/how-can-i-decode-sstv-with-only-macos-software, by Amin Shah Gilani, Aleksander Alekseev - R2AUK. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
