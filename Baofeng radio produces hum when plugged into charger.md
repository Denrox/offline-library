# Baofeng radio produces hum when plugged into charger

*Tags: mobile, baofeng, grounding · score 3*

## Question

So I am working on a low cost ham radio beacon using my Baofeng UV-5R radio because it is easy to use and portable. I built a simple PTT interface for a Raspberry Pi and wrote some python to transmit the information I want. However, there is one problem. I want the option to have to radio plugged in to its charger to be able to transmit for long periods of time without dying but when I plug the radio into the wall and use Raspberry Pi to transmit audio it produces a very loud hum over the radio signal and it is completely unusable. This does not happen when I plug a battery operated audio source (such as a phone) into the radio, only when I use a wall powered source such as the Pi or a computer. it also does no occur when the radio is using battery power and the Pi is plugged into the wall. It does happen when using a simple male to male aux cable and VOX PTT. I can't seem to find the problem however I suspect it to be an issue with common grounds or something of the like but I have no idea how to solve it if that is the case. Please help!

Thanks,

Mr. Schmuck

## Answer (score 3, by imabug)

Probably the charger you're using. I ran into a similar issue with a QRP receiver I was running off a wall wart. Try with a different wall wart, or maybe a few windings through a toroid.

## Answer (score 2, by Glenn W9IQ)

The symptoms you related sound like a classic ground loop problem. One solution is to galvanically isolate the PI circuit from the radio. This technique allows the signals to pass but not stray currents. Here is a simple circuit containing only three parts that can be built for under $10 with new parts.

The audio transformer isolates the audio signal while the optoisolator isolates the push to talk (PTT) signal. There should be no other direct connections between the PI and the radio (or its power supply).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9683/baofeng-radio-produces-hum-when-plugged-into-charger, by MrSchmuck, imabug, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
