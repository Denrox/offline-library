# Why is Morse code still in use?

*Tags: modes, cw · score 64*

## Question

Why do people still use Morse code?

What are its advantages over newer *voice* or *data* communication modes?

## Accepted answer (score 81, by scruss)

- because there are a large number of operators who had to learn it to get their licence
- because there is a large (but slowly diminishing) number of operators who learned it while serving in the armed forces
- because the transmitters and receivers can be extremely simple and inexpensive, not needing much more than a key and headphones along with the rig, antenna and battery to send and receive
- because (in theory) it has a very tiny bandwidth, allowing small QRP transmitters to send a very effective signal. This also allows a large number of contesters to cram into a few kilohertz of bandwidth, each (with suitable filtering) able to be picked out individually
- because it's a point of pride for some operators that they know this thing that the young 'uns don't.

CW can be sent exceptionally well by computer (with software like fldigi) or by any number of USB/serial keyers (such as the WinKeyer or K3NG Arduino keyer). It can be copied reasonably well in software (fldigi again, or CW Skimmer). The Reverse Beacon Network relies on multiple stations worldwide running CW Skimmer to report on propagation, and will show you where your CQ has been copied.

It can be thought of as a digital mode, but one that can be copied by ear with sufficient training. It's typically a little slower that PSK-31 or RTTY, and CW only supports a very limited single-case character set. Although it is no longer used commercially or by the military, it's likely to stick around in ham radio for a long time.

## Answer (score 39, by Evan Fosmark)

The advantage? **Efficiency!** You get to put all of that power of your rig into a very small bandwidth, whereas voice modes need to spread the power out much more (for example, SSB uses roughly 2.8kHz of bandwidth).

Quote from: http://home.windstream.net/johnshan/cw_ss.html :

Going a little bit further, assuming a SSB signal takes up 2000 Hz., and comparing a 100 watt 25 WPM CW signal with a 100 watt SSB signal, we have the following. The average power density for CW is 100W / 100 Hz. or 1 w/Hz. For SSB it's 100W / 2000 Hz. or .05 w/Hz. Follow closely now, it gets interesting although a little more technical. We could say that the gain in using CW over SSB is Gain(db) = 10*log(1/.05) which is about 13db. **That means that a 5 watt CW signal packs an equivalent punch to a SSB signal at 100 watts.**

## Answer (score 24, by nc4pk)

One of the reasons it's still in use is because of its inherent simplicity - no real signal processing is needed. Thus, CW transmitters and receivers are very simple and thus inexpensive.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/135/why-is-morse-code-still-in-use, by Timtech, scruss, Evan Fosmark, nc4pk. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
