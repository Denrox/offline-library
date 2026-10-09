# SDR set up that will TX & RX on CB, UHF and VHF

*Tags: software-defined-radio, equipment, united-kingdom · score 4*

## Question

I would like to use SDR to receive **and** transmit on CB, UHF and VHF. Is this possible and if so what type of equipment will I need (antennae, dongle etc)? I currently have both UHF/VHF and CB but atm have separate antennae for each rig. Reading about SDR I think I can have one single antenna and use the computer magic to allow me to work with all frequencies that antennae receives, am I mistaken?

## Accepted answer (score 5, by rclocher3)

You didn't mention which country you're in, but in the US, it is only legal to transmit on CB with a "type-accepted" radio. In other words, the manufacturer of the radio must apply to the FCC for permission to sell the model. It's not legal to build your own CB transmitter.

Regarding using a single antenna for multiple bands, a transmitter typically expects the antenna to have a certain impedance. It is possible to use a single antenna for multiple bands, but in that case a simple antenna will have quite a wide variety of impedances across the multiple bands. For a very low-powered transmitter this may not pose a problem. For higher-powered transmitters, a mismatched load can cause very high voltages that can easily damage the transmitter. (Modern high-powered transmitters often include a circuit to automatically reduce power when a mismatch is detected, to protect the electronics.) Another problem is that the efficiency of the transmitter and the feedline can vary considerably if the frequency strays far from the optimal range.

How to design an antenna and feedline system for a wide range of frequencies deserves to be a separate question here, but let me say that the most economical solution to the problem is often to have separate antennas and a coaxial switch to choose between them.

## Answer (score 4, by Marcus Müller)

Reading about SDR I think I can have one single antenna and use the computer magic to allow me to work with all frequencies that antennae receives, am I mistaken?

Well, I always explain it that way:

An SDR is like a soundcard on speed. Usually, with a mixer.

So, what the SDR does (in Receive direction) is take a spectrum of bandwidth $B$ (for example, 10 MHz) around a center frequency $f_c$. So, all signals between $f_c - \frac B2$ and $f_c + \frac B2$. It then mixes them down, usually to baseband, which means that these frequencies all get shifted by $f_c$, so that the same $B$ wide swath of spectrum ends up around 0 Hz, that means in $-\frac B2$ to $+\frac B2$.

Then, it uses, just like a sound card, a fast (dual) ADC to digitize the full $B$.

Now, flexibility comes from two things:

1. You now got a digital signal. FM? AM? SSB? PSK? APRS? Doesn't matter, it's in your computer, you just pick the right software to demodulate that. Also, you can have a digital filter in software that is much sharper than any physical filter and select exactly one channel.
2. The $f_c$ is usually pretty freely choosable. So, you can tune your SDR to receive e.g. 20 MHz to 30 MHz, or you can tune it to 140 to 150 MHz. In the end, the original center frequency doesn't matter for the processing of the signal.

So much for theory. In practice, of course, a couple of things must still work out:

- your SDR must actually be able to tune to all frequencies you want. If it doesn't, this can often be compensated with an external up- or downconverter, but that'd basically not achieve your single device goal
- As you might know, mixers aren't inherently perfect. They tend to not only mix down the intended frequency, but also harmonics of that (amongst doing other interesting things). Hence, an SDR must include some sort of selection filter that avoids unwanted intermodulation products. Now, the more flexible a device is, the less fixed and the less great these filters can be. Not a problem if your antenna only works well for the frequency band you're interested in. Not as cool if your antenna actually works for multiple bands. So, you **might** need preselection filters. Details can really only be discussed if we know what SDR you're considering.

 - A commonly overrated problem is deafening by stronger transmitters in the same band. Whilst this might be a problem in extreme situations (and you can only remedy that with analog filtering), it's astonishingly easy to avoid (offset tuning, oversampling, predistortion).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9651/sdr-set-up-that-will-tx-rx-on-cb-uhf-and-vhf, by welfare, rclocher3, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
