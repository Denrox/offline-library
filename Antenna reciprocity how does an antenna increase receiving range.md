# Antenna reciprocity how does an antenna increase receiving range?

*Tags: antenna, antenna-theory, receiver, transceiver, wifi · score 3*

## Question

According to Wikipedia antennas are reciprocal unless they're constructed of nonreciprocal materials.

There are a multitude of mathematical formulas which unfortunately I'm unable to understand due to my lack of knowledge, that prove this.

Various resources (1)(2) confirm that antennas are indeed reciprocal

WokFi gains are typically 10+ dB, with range boosts, thus can be 16-32 times over the antenna of a bare USB adapter. Ranges (LoS) are typically 3–5 km (2 to 3 miles)

When transmitting, a high-gain antenna allows more of the transmitted power to be sent in the direction of the receiver, increasing the received signal strength. When receiving, a high gain antenna captures more of the signal, again increasing signal strength. Due to reciprocity, these two effects are equal—an antenna that makes a transmitted signal 100 times stronger (compared to an isotropic radiator) will also capture 100 times as much energy as the isotropic antenna when used as a receiving antenna. As a consequence of their directivity, directional antennas also send less (and receive less) signal from directions other than the main beam. This property may be used to reduce interference.

When using a high gain directional antenna it's logical that transmitted waves are able to travel further, since they're reflected of a surface in a narrow beamwidth.

Although it's a lot harder to visualize with reception.

I know that electromagnetic waves travel through the air and in a vacuum they'd travel indefinitely, since there's no noise nor obstructions.

However practically there will always be always be obstructions even ever so slightly.

Suppose you're trying to connect to a distant network at the client side you have a USB WiFi adapter with a high gain external antenna, the other side being a generic WiFi router with a stock omni-directional antenna.

Using the USB WiFi adapter with a stock omni-directional antenna I would be able to connect to the network with a distance of 100m.

With a directional antenna and a LoS we might be able to achieve a link at a 1 mile distance.

But how does the antenna manage to "catch" the transmitted waves at the RF end?

How are the "electrons" able to be "pulled back" to the antenna?

I understand that high gain directional antennas are able to make sense of weaker signals because they are more sensitive having multiple elements.

Similar to a dogs ears, they're able to hear sounds from further away because they have more sensitivity.

But do you need to have somewhat of a signal, even if it's incredibly weak at the client side in order to establish a bidirectional connection? Or does the antenna manage to "pull back" those electrons.

## Answer (score 3, by Marcus Müller)

So to start off: I (an electrical engineer who had to take classes on that stuff) regularly get sad when I read the packaging of Wifi equipment, because the marketing speech on that is so wrong it hurts.

For example, you have a picture of a wifi access point with 4 antennas. I have a similar one. package says "4×4 MIMO with high gain antennas". Nope. None of these four antennas is highly directive, has high gain, *individually*. You can get directivity or gain by combining them in very particular ways, but it's not a property of the antenna as is.

We'll see how that happens!

Let me first address a few misconceptions, or maybe just imprecise choice of words, to make discussion afterwords a bit easier, otherwise my explanation might make no sense, as it would contradict the wording of your question.

I understand that high gain directional antennas are able to make sense of weaker signals because they are more sensitive having multiple elements.

nope! That's a fallacy; having more elements is not the key to being able to pick up more. Think about this: assume I have say, 10000 dipole antennas, connected to a coax cable each, and finally merged through splitters. I just throw them on a giant pile.

That's incredibly many elements, but still on expectation (this being very random) a shoddy antenna!

When using a high gain directional antenna […] they're reflected of a surface in a narrow beamwidth.

Not all high-gain antennas have reflectors! Satellite dishes do, but there's very many high-gain antenna designs that don't. *Gain* just says "there's a direction in which this antenna emits more power (if used as a transmit antenna) than the average of all direction"; *high-gain* is a bit of a vague term, but basically means there's a direction where you see most power being emitted, which "suggests" it gives you a beam.

transmitted waves are able to travel further

Ah, that one I'll have to veto. Waves travel infinitely long, until something absorbs them. It's however clear what you meant: The signal strength is stronger at a larger distance. And that's just the effect of having *gain*: if I put in some power $P$ and it's emitted in all directions evenly (so, gain is 1 = 0dBi, "decibel compared to an *i*sotropic antenna") by my antenna, then it doesn't matter in which direction my receiver (of some effective surface area $A$) is: the amount of power it catches only depends on the distance, not the direction. If I, instead, have gain, then less power goes in my direction if I'm not standing in the "main" direction, but more if I stand there.

Important message here is, by the way, that gain just "redistributes" power from all to one direction. No free lunch, an antenna that has high gain means that one direction gets more power, at the expense of the other directions, which receive less.

Now, that's all very "high-level" looks at antennas. You were wondering about a low-level fact of antennas. And, sadly, for that, this abstraction level does not suffice. We'll need to understand how electromagnetic (EM) waves actually work, what they actually are.

So. You know capacitors, I'll assume:

Symbol is pretty descriptive of a plate capacitor: you apply a voltage across the two terminals, you get a potential difference between the left and the right plate. In between, there's an electric field, which goes from the positive to the negative potential, *it has an end and a start*:  
Homogenic electric field. Author: Phatency on creative commons

Change the voltage, you change the electric field. Invert the voltage, invert the field.

You also know electromagnets: You apply current flowing through a coil of wire, you get a magnetic field. That magnetic field makes nice, *closed* lines going one time around the coil and closes in the coil. That works with 100 turns of wire, it works with 2 turns of wire. It also works with a single wire, in which case the magnetic field simply circles around the current:  
Drawing of magnetic field around a current carrying wire. Author: Stannered on wikimedia commons.

You change the current, you change the magnetic field. You invert the direction of the current, you invert the direction of the circling. (You might have heard of the right-hand-rule.)

**Now comes the interesting part that has to do with antennas**:  
Physics has fixed some relations between the changes of magnetic fields and the electric field, and changes in the electric field and the magnetic field. These are *Maxwell's Equations*.

These equations say that if you change an electric field, you cause an electrical field that looks as if it could have opposed exactly the current that caused the change in magnetic field.

When you change the electric field, you cause a magnetic field, that looks as if it was caused by a current that causes the change in electric field.

Huh. So changing one causes the other; the way these things are linked over distance limits the speed of change, so that not every change has an immediate effect everywhere.

So, and here's **how antennas actually work**, when you let a current flow through a conductor, and change it periodically, like a sine, then it causes a magnetic field, which also changes sine-like. Which in turn causes a sine-like changing electric field. Uff, complicated, but it turns out the maxima of the magnitude of the magnetic field have a 90° time shift to these of the electric field.

Now, these changing fields have effects on the neighboring places, which now also change sine-like. Congratulations, without actually writing down a formula, we have gotten an idea why a small piece of wire with sinusoidal current through it has field energy propagating away from it, in all directions. It's an antenna! The "thing", the combination of ever-changing electrical and magnetic field, radiating away? That's the electromagnetic wave!

Now, let's talk about **gain**. All these fields, and their derivatives (what I called "change"), are *linear*, that means if you have two capacitors and put one between the plates of another, the field in between the inner one's plates is the sum of the fields that the two capacitors would have in itself, for example.

Now, you put two such elemental antennas next to each other, then depending on how you feed them with current (in phase, anti-phased, something in between) and how far they are apart, you get points where the fields of the waves always add up to become twice as strong, and others, where they always add up to zero and cancel. We call that *interference*. And it's how you can build antennas that have gain. Make it so that parts of the antenna system emit waves with just the right delay so that in one direction you always get the constructive interference, i.e. stronger amplitudes.

You can do that with many individually driven antennas (like the 4 in your Wifi access point!) or you can have one antenna and a big reflector with a very particular shape (like a satellite dish) so that there's a direction where the fields always add up constructively. You can even start by calculating a shape for the conductor so that the conductor through which you let your current flow has gain of its own (like a patch antenna!).

Here's an illustration of these individual (round) wavefronts add up in the arrow-marked direction if the phases between the individually driven antennas are chosen appropiately:  
Animation showing how a phased array works.

That's about how your wifi access point "points" a beam in the direction you have your laptop: it choses the right delay for the signals going to its antennas such that the sum of all waves adds up positively in the direction of your laptop. Or some other far-away station.

So, back to: **Why are these things reciprocal?**

It's simply because if you change the magnetic field around a coil, or a single wire, it induces a current, just working the opposite as if you caused the magnetic field change by changing the current. (That's why motors work as generators, and vice versa). And because an electric field with a conductor running through it causes a current in that conductor.

So, the underlying field/electrical potential/current relationships that you see in everyday circuits have an inverse, and that's why the apply to antennas, too. That's why antennas are always reciprocal (unless they're made of something that is a very strange material, which you basically never encounter, unless you're in the business of building powerful radar systems, or light-amplifying crystals).

## Answer (score 2, by hotpaw2)

I tend to think about receiving gain in terms of capture area.

If you put some dishes out in the rain, the dish with the biggest surface area will capture more raindrops, if aimed upwards, not sideways (unless maybe the rain is blowing sideways).

Same with antennas and their equivalent to raindrops: (photons of) electromagnetic waves. More metal in the air (or vacuum) will usually act like a bigger dish and capture more RF EM signal (if carefully connected so that the energy picked up from the EM waves doesn't cancel out due to being in opposing phase). Two antennas, if phased properly, can send their signals to some point where the signals can be added together into a larger signal. A reflector element in a multi-element Yagi-Uda will pick up some EM energy that the main element would not have on its own. Then the reflector can send some of that energy back to the main element such that, if in phase, it adds up to a bigger signal received.

Where reciprocity often fails is that it only works perfectly in a fictional universe where there is zero noise. Usually signal levels are different in opposing directions between two system very different in size, and noise levels are not the same as well. If the signal level (number of raindrops) at one end is lower than the noise inherent in a physical antenna and receiver (due to quantum and thermal reality, plus any cheap LED lighting in the building), then reciprocity will fail in that direction, where it may work in the other.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21222/antenna-reciprocity-how-does-an-antenna-increase-receiving-range, by icyli2, Marcus Müller, hotpaw2. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
