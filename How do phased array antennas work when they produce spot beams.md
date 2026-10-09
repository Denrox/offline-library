# How do phased array antennas work when they produce spot beams?

*Tags: antenna, antenna-theory, satellites, phased-array · score 4*

## Question

## Background

In a lot of literature regarding satellite communications with phased arrays, you'd see this kind of image:

Conceptually, I get the basic concept of how this works - a bunch of small antennas work together to direct a stronger signal to a certain location (the spot beam). One thing that I'm not very clear on though: is how is the scalability issue solved?

## Question

So let's say you have a phased array in space that's capable of producing the 19 spot beams from the above image. How *exactly* is the satellite generating those beams?

Does it have to effectively "scan" and transmit each beam one-by-one? Or are spot beams far apart from each other with the same frequency able to be transmitted at the same time? What about the frequency problem? Surely, one phased array can't transmit at say, 2000MHz for one spot beam, and simultaneously transmit a 3000MHz signal for the spot beam right next to it, right? Or is the phased array actually transmitting to all the spots beams simultaneously?

Finally, how is the receiving side of the problem solved? Let's say you have end-user A that's transmitting at 2500MHz to the satellite in one of the "Beam 1" spot beams. But then thousands of kilometers away you have end-user B transmitting at 2500MHz in another "Beam 1". When receiving the signals, would it be possible for the phased array to distinguish between the 2500MHz signals of users A and B?

This part isn't very intuitive for me. My common sense is telling me "how can you tell which signal is which if they arrive at the same time," but maybe there's a trick behind it? Is it like pointing a powerful camera down at Earth and being able to tell one red object from another red object hundreds of kilometers away if you take a picture? After all, it doesn't make sense to me to have all these spot beams to increase down-link scalability, but have your upload speed be crippled if you can't tell a 2500MHz incoming signal from one spot beam from another and being forced to timeshare each incoming signal.

If someone can help me understand how the satellites accomplishes these scalability challenges, that'd be great. Thank you!

## Accepted answer (score 7, by Marcus Müller)

I'm doing this from a transmit direction, first, I find that easier to explain. You know that antennas work in transmit as in receive, so what you'll (maybe?) learn will work for reception as well.

Does it have to effectively "scan" and transmit each beam one-by-one? Or are spot beams far apart from each other with the same frequency able to be transmitted at the same time?

At the same time.

It's a large "combination antenna", with (at least) 19 inputs. And you can either build a complicated array of 19 highly directional antennas, or you make an array of 19 not very directional antennas, and use math to "pre-mix" the signals in exactly a way that this whole array is a *different* directive antenna for each of the 19 individual signals.

How exactly is the satellite generating those beams?

See "digital beamforming": big, mature topic :) My apologies, I'm not going to throw the linear algebra and trigonometrics at you here; books can do that much better, whilst introducing the math and a consistent notation... this is just an answer on a stackexchange site.

1. think about just one beam for a second. Think of your antenna as a system of many antennas, let's actually take 25 in an array of 5×5 patch antennas.
2. you take the signal that you want that beam to transport, and divide it into 25 different identical sigbnals. Then you add a phase shift to each, and send the resulting signals to a different antenna element each.
3. Because you shifted the phase differently, there are directions in which the signal from different elements add up constructively, and others, where it cancels. Yay! Due to these adjustable phases, you've built a system that can point a beam in pretty much arbitrary directions. Note that a beam isn't necessarily just one direction, but typically more like a grid of directions (convenient for both frequency planning and for the fact that the math underlying the phase shifts leads to "side lobes" in regular patterns).
4. choose the 25 phase shifts such that the antenna array points its beam in the direction you want.
5. Do the same for the 18 other satellite signals. Add the results. You get 19 different beams, carrying 19 different signals in 19 different directions.

What about the frequency problem? Surely, one phased array can't transmit at say, 2000MHz for one spot beam, and simultaneously transmit a 3000MHz signal for the spot beam right next to it, right?

The spots typically don't have frequencies that are different by a factor of 1.5; it's more like "10.000 GHz – 10.600 GHz for the first beam, 10.600 – 11.200 GHZ for the next beam" and so on; a popular result from graph theory is that you don't need to have more than four different bands to not have to use the same band for neighboring spots ("Four Color Problem").

But even if so, the individual array elements don't have crazy gain, so building them somewhat broadband is not inherently impossible. And because you calculate the phase shifts *per beam*, you can take the different properties of the patches at different frequencies into account - separately. So, yes, that would work.

My common sense is telling me "how can you tell which signal is which if they arrive at the same time," but maybe there's a trick behind it?

Your assumption is wrong! They don't arrive with the same phase (because a different angle means that they arrive *later* at some antenna elements than at others, not at the same time).

Is it like pointing a powerful camera down at Earth and being able to tell one red object from another red object hundreds of kilometers away if you take a picture?

not quite sure what you mean here, but... I don't think this is comparable.

After all, it doesn't make sense to me to have all these spot beams to increase down-link scalability, but have your upload speed be crippled if you can't tell a 2500MHz incoming signal from one spot beam from another and being forced to timeshare each incoming signal.

1. completely different topic,
2. what works in transmit works exactly the same in receive, so this is not really a problem: The satellite has the same beam characteristic in receive as in transmit direction if you just choose the right phase shifts to combine your antenna elements' received signals
3. many systems are *not* symmetrical in up- and downlink, or they have one uplink station with a separate antenna.

Let's say you have end-user A that's transmitting at 2500MHz to the satellite in one of the "Beam 1" spot beams. But then thousands of kilometers away you have end-user B transmitting at 2500MHz in another "Beam 1". When receiving the signals, would it be possible for the phased array to distinguish between the 2500MHz signals of users A and B?

Yes, it would be possible, if using different phasing than to generate the original beams. But that would just lead to different users now sharing the same frequency.

So, usually this is solved by putting different users on different subbands, or time slots, or codes, or combination of these.

After all, it doesn't make sense to me to have all these spot beams to increase down-link scalability, but have your upload speed be crippled if you can't tell a 2500MHz incoming signal from one spot beam from another and being forced to timeshare each incoming signal.

Well, you can't cheat physics! Just as the downlink bandwidth in each beam is divided among all users in that beam, so is the uplink bandwidth.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20629/how-do-phased-array-antennas-work-when-they-produce-spot-beams, by 0xbad1d3a5, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
