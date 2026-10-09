# Can a FM tuner (receiver) be detected and triangulated?

*Tags: receiver, fm, emergency, location · score 3*

## Question

In movie "6 Below", based on a true history, a lost snowboarder at Mammoth Mountain (California) is located by search and recuse when they detect and triangulate a signal from his MP3 player that also had an FM radio tuner (not a phone nor a two-way-radio, just an FM tuner).

This event forms a essential part of the story, so it doesn't makes sense to me that they just made it up as a part of their theatrical license.

However, I was very confused because in my understanding it should be impossible to detect a receiver.

After some google search I found some info saying that: as the receiver internally amplifies the signal, this creates "unintended emissions", and those emissions could be detected. Also this fairly recent paper refer to such methods.

**Is this possible in practice?** If so. **It is such technology actually used for Search & Rescue in California?**

## Accepted answer (score 4, by Marcus Müller)

Is this [detection of a receiver through its amplification of received signals] possible in practice?

Aaaah, no. Not exactly like described in that thread. In more general terms, yes, it is.

So, first of all: the point of *radio* is that the transmitted energy *radiates* away from the transmitter. That means that you can't know whether something absorbed that energy at the transmitter. The energy is gone either way, and there's no way for information to "flow back".

If we assumed that the receiver had an amplifier for the transmitted frequency (say, a tone of 100 MHz), and it "leaked" energy back out, and we'd need to detect that, we'd be in a bad spot:

Since the original transmitter was meant to transmit, its emission will be much stronger; and being on the exact same frequency, we couldn't reliably tell the leakage from a faint echo, e.g. from a reflection off a rock or metal surface.

There's another way of detecting radio receivers, and rumor has it used to be used in the 20th century by TV companies trying to detect unlicensed TV receivers: Receivers have to *mix down* the RF signal to some fixed intermediate frequency. There was basically one fixed IF that all good ole TVs used – and if you built a sensitive receiver for those, you might have been able to locate *turned on, actively receiving TVs of the 1940s to 70s*; not modern MP3 players. They don't all agree on a single IF, if they use an IF at all; and they won't be as leaky, and they won't be as powerful, and most importantly, probably turned off.

**But:** Everything that actively deals with a signal is some kind of *non-linear* device.

What that means is that math is your friend: Without loss of generality, we can assume our tone to be a cosine of frequency $f$, i.e.

$$s(t) = \cos(2\pi ft)\text.$$

Now, that cosine is picked up by an antenna (which in itself is undetectable from a position of the transmitter), and amplified; amplified means "sent through something that multiplies the signal with a constant $>1$".

Now, such somethings are made from *active components*, typically *transistors*. And all these have a pretty important downside:

They don't actually multiply the signal with a constant. That is technically relatively hard to achieve.

Instead, they have *exponential* behaviour, something like

$$r(t) = e^{\alpha + \beta s(t)}\tag1$$

where $s$ is the horizontal axis (input), and $r$ would be on the vertical axis (output).

Now, that's not very alike to what we want,

$$\hat r(t) = a \cdot s(t),\quad a\gg 1\text, \tag2$$

so how does that work out?

Well, you make sure that the $s(t)$ is relatively small and is offset with a bit of DC voltage so that you pick a region on that curve that is pretty steep and looks "flat enough", so that you land on the rightmost black dot in the below figure when $s=0$, and let $s$ vary just a bit so that the difference between the steep red line and the blue exponential curve is small:

Now, you have something that has *approximately* the linear behaviour from $(2)$ that we wanted.

But only approximately so. Maybe you've had some advanced math – if you did, you might know that the exponential function can be written as a series:

$$e^x = \sum_{k=0}^\infty \frac{x^k}{k!} = 1 + x + \frac{x^2}2 + \frac{x^3}{6} + \cdots$$

Of that, we've only covered the first to terms with our approximation:

$$e^x = \underbrace{1 + x}_{\text{red line approximation}} + \underbrace{\frac{x^2}2 + \frac{x^3}{6} + \cdots}_{\text{error terms}}$$

Now, when you mentally replace $x$ with your $s(t)$ in that error term, you see that you get your signal squared, cubed, …⁵ and so on as error terms, albeit with less amplitude the higher the exponent.

So, let's look at one of these – the strongest, x². What happens to our cosine when we square it?

\begin{align} \cos(2\pi ft)^2 &= \cos(2\pi ft)\cos(2\pi ft)\\ &= \frac12\left(\cos(2\pi ft+ 2\pi ft)+ \cos(2\pi ft-2\pi ft)\right)\\ &= \frac12\left(\cos(2\cdot2\pi ft)+ \cos(0)\right)\\ &= \frac12\left(\cos(2\pi (2f)t)+ 1\right)\\ &= \frac12\cos(2\pi (2f)t)+ \frac12\tag3 \end{align}

Now, $(3)$ is pretty spectacular: that's a *new* cosine with twice the input frequency!

A sensitive receiver can look for signals at that specific double frequency; if you couple that with switching the transmitter of the original frequency on and off to test the hypothesis of energy there not just being random noise, you can make a pretty decent detector.

That's actually used in detection of semiconductor junctions by physicists experimenting with materials, for example.

It's also been used in the past to detect simplistic bugging devices in e.g. embassies, but these are designed to be transmitters, so they are going to be a pretty solid bit easier to detect than just a radio receiver.

So, I'd assume that since being not very close to the device makes the detection harder (actually, the hardness goes with the square of the distance), nope, that's not going to happen in an emergency location situation.

What does work is if you are carrying something that is *meant* to be excited by an external tone, then "save" that energy and continue to transmit for a few microseconds at least after the external tone has been shut off – that's exactly how these cheap anti-theft tags work, and it's how radioresponders in ski clothing work.

If so. It is such technology actually used for Search & Rescue in California?

I don't know, but the passive tags mentioned above stand a high chance of being known to rescue teams and thus, there's a high chance they carry equipment to detect these.

However, the "radiolocation through MP3 player" will not be part of anyone but James Bond's avalanche rescue team, is my technical assessment.

## Answer (score 8, by Phil Frost - W8II)

The story is about Eric LeMarque who got lost after snowboarding out of bounds in the Sierra Nevada mountains.

Radio receivers usually contain some kind of oscillator. Detecting the unintentional radiation from the oscillator or the mixing products in the receiver is technically possible, but in modern receivers the power is so weak this power is so weak it is quite difficult to detect, even knowing the particular model of receiver and where it is. Consider what would happen if receivers produced conspicuous detectable signals: every radio would be a source of interference, and all kinds of radio communication wouldn't work through the noise.

LeMarque unsuccessfully tried using the screen of his MP3 player as a signaling device. He was instead found the usual way: search and rescue teams followed his trail in the snow.

Search and rescue teams don't find people by their MP3 players, but they do use intentional transmitters like avalanche transceivers and personal locator beacons when people have the good sense to carry them. More ordinary radio communication devices like cell phones, portable FRS and amateur radios, etc. also factor into some operations.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12927/can-a-fm-tuner-receiver-be-detected-and-triangulated, by Camilo Rada, Marcus Müller, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
