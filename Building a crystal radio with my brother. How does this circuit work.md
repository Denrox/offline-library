# Building a crystal radio with my brother. How does this circuit work?

*Tags: am, crystal-radio · score 5*

## Question

I'll be visiting home soon after school lets out, and I want to build an AM crystal radio with my little brother. This is the design we'll use:

http://crystalradio.net/beginners/

I'll be doing my best to explain to him how this works. I understand that when a radio ray passes over an antenna, it generates an alternating electrical field in the antenna wire. If the antenna wire is the correct length for the given radio ray, the electrons in the wire will bounce back and forth in sync with the alternating field, moving faster and faster with each oscillation (resonance). I also understand how audio can be embedded in an AM signal using amplitude modulation.

However, I do not understand the diagram in the diy linked above.

- Where do the electrons flow?
- Doesn't splitting the circuit in the middle of the coil create two "antennas", each with a different resonant frequency?
- What is the purpose of the resistor? I have looked up the internal design of piezoelectric earpieces, and it does not appear that current flows all the way through them.

The circuit I've chosen is similar to, but different from, the circuit shown here:

https://en.wikipedia.org/wiki/Crystal_radio#Design

I was able to find some helpful material on the howstuffworks pages for AM radios, but it is not a one-to-one mapping of the design proposed in the first diagram.

## Accepted answer (score 5, by Marcus Müller)

I'll try to address your concerns a bit! I'll be simplifying here and there, but I think you'll notice where I'm doing that.

I'll be doing my best to explain to him how this works. I understand that when a radio ray passes over an antenna, it generates an alternating electrical field in the antenna wire.

Close, but not quite :) I'll correct you here, because it makes things easier to explain below.

We talk of radio *waves*, not *rays*. The point is that the wave actually *is* the alternating electrical field *in the air*. It induces a *current* in the antenna. So, any piece of metal that you have lying around is an antenna, and there's electricity flowing through it, because there's radio waves of all kinds of sources (some natural, some man-made, some intentional, some accidental) everywhere! But: these antennas don't work overly well, and also, there's not much power at most wavelengths (see below).

If the antenna wire is the correct length for the given radio ray,

Here's why I mentioned the wave naming: If the wave's *wavelength* happens to be such that the antenna connects a "deep" and a "high" point in the electrical field, you get an especially strong current. So, the length of your antenna has to be in a specific relation to the wavelength of the radio signal you want to capture. If it's a bit "off", that's not too bad. But you can't properly receive, for example, a 3 MHz (wavelength: 100 m) signal with an antenna that's meant to receive a 2.4 GHz (wavelength: 1/8 m).

the electrons in the wire will bounce back and forth in sync with the alternating field,

Exactly! The electrical field that is the wave "pulls" and "pushes" the electrons in the antenna. If we make sure the antenna is sized and shaped just right to push and pull the electrons with the most force possible, we get the strongest reception!

moving faster and faster with each oscillation (resonance).

The speed is fixed (it's given by the frequency of the radio wave, which is just the speed of light divided by the wave length), but with resonance, we can make much stronger currents.

I think this calls for an analogy: get a (maybe just in your head) bucket of water. Hold it between your hands.

Slightly push it back and forth. For some amounts of times pushing the bucket back and forth per second, the ripples on the water aren't really big. But for others, the water gets really troubled and starts making extremely high peaks! You've hit the *resonant frequency* of your water/bucket system.

With electrons, antennas and a tuned receiver, the same happens: a specific wave frequency (that is, a specific wavelength) is able to rock the electrons *just* at the right rate so that the peaks get really high.

Now, in your bucket experiment, the bucket is fixed, and you find the frequency that resonates well.

Unlike you with your bucket, the frequency is fixed (because you want to receive a specific station!), so you have to vary your bucket: Essentially, tuning your receiver is the same as shrinking or growing your bucket. The bigger the bucket, the lower the resonant frequency becomes.

I also understand how audio can be embedded in an AM signal using amplitude modulation.

Great! In essence, staying in the bucket picture: The audio signal would just be how high the peaks got, which is just a result of how strongly you pushed (maintaining the same frequency, of course, that's where it gets difficult with the bucket).

However, I do not understand the diagram in the diy linked above. Where do the electrons flow?

So, the electrical field pushes and pulls the electrons in the antenna back and forth – that push/pull extends down the antenna wire up into the coil – which basically acts like a reservoir of water. You push in a little current, the next moment you pull it back out, and so on.

Now, the size of that reservoir determines at which frequencies we are in resonance. Which means, the amount of windings that are effective in the coil determines how much current can flow into the coil, get its energy stored in the magnetic field of that coil, and then flow back.

By selecting less or more windings with the alligator clip, you get less or more reservoir – thus, you change the resonant frequency of the antenna/coil system!

Doesn't splitting the circuit in the middle of the coil create two "antennas", each with a different resonant frequency?

Kind of, yes! But the other half (not attached to the antenna) is attached to ground, so nothing is received there. Keen observation!

What is the purpose of the resistor? I have looked up the internal design of piezoelectric earpieces, and it does not appear that current flows all the way through them.

Exactly. Piezoelectrics react to *changes* in voltage, and other than that, basically isolate. To allow net current flow from the diode to ground, you'll need something that always passes current.

Now, using this resistor means that you won't get all energy that you've received to drive your ear piece, but that's not all that bad.

I hope that gave you a start :) Would love to hear your feedback, and see you back around here :)

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7487/building-a-crystal-radio-with-my-brother-how-does-this-circuit-work, by BitPusher16, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
