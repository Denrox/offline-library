# Easy Digi hum with isolated ground

*Tags: grounding, noise, audio-interface, echolink · score 4*

## Question

I am creating an Echolink simplex link using a Raspberry Pi 3 B+, a Pluggable USB sound adapter, and an "Easy Digi" sound card interface which has 2 - 600ohm isolation transformers for audio in/out as well as an opto isolated interface for the PTT into my Yaesu FT-1900R. The basic hookup is essentially like this:

Even with the isolation transformer, I am getting a terrible hum when receiving transmissions. I finally got it to stop by connecting the ground from the output of the USB sound card to the PTT ground connected to the radio. This is negates the ground isolation and I can't figure out why this fixes it. Any ideas?

## Accepted answer (score 3, by tomnexus)

TLDR: 60 volts AC divided by the transformer CMRR is much greater than 1 mA times the resistance of the wire installed.

--

In the first case - the raspberry Pi was floating at 60 V AC above ground, being powered by a two-pin USB adapter. The radio was earthed by its power supply, coax, etc. So the transformers have 60 volts across them, and even the smallest asymmetry of capacitance will generate a large differential-mode signal.

In the second case, there's a maximum of (say) 1 mA flowing on the ground wire (there's a legal limit for leakage, something like that). A small voltage develops across this resistance, which is added to the audio signal. The transformers are probably still helping.

--

Transformer isolation is much more important in cases like this:  
Imagine you have a *grounded* computer plugged in on one end of the room, and a *grounded* rig plugged in on the other. Your air conditioner is causing a 1 volt drop in the ground/neutral potential between the two sockets, but this 1 volt is at *a very low impedance*. The simple sound-card earth wire is completely overwhelmed by this, and simply drops the 1 volt too, resulting in a 1 volt differential AC signal added to the audio at the rig/PC. In this case, the transformers provide a vital function, breaking the so-called ground loop.

In your first case, you have a high voltage, high impedance voltage difference between the two halves, so the right solution is a heavy ground wire. Then you use the transformer in the USB power supply for ground isolation.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16751/easy-digi-hum-with-isolated-ground, by john8791, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
