# How far do radio waves travel?

*Tags: propagation, physics · score 6*

## Question

I have read that radio waves just keep traveling but the signal gets weaker because of how the wave spreads. OK, I get this, but what confuses me is that satellites emit signals from space that our phones and GPS modules pick up regardless of distance, versus walkie-talkies and WiFi routers whose signals don't travel nearly as far relative to GPS and phones. If GPS modules can pick up waves from space, why can't my laptop reach my WiFi Signal from far away? And why are walkie-talkies not able to transmit and receive at much further distances? Do all radio waves potentially travel the same distance? Or does the distance depend on the power of the signal? What determines the power of signal, wavelength or frequency?

## Answer (score 15, by Kevin Reid AG6YO)

Radio waves don't stop at a distance, they just get weaker; you've read this correctly. The reason that communications stop working at some distance is that *the signals are too weak to be understood.*

Besides distance (and being absorbed or reflected by objects in the path) causing the signal to be weak in an absolute sense (how much power there is), there is also the question of *signal-to-noise ratio*. That is, there are other radio waves, from other transmitters, natural sources, and even unintentional noise sources inside the receiver itself, all of which “drown out” the desired signal just like acoustic noise can make it hard to hold a conversation.

Ok i get this but what confuses me is that satellites emit signals from space that our phones and GPS modules pick up regardless of distance versus; Walkie-talkies and WiFi routers whos siganls don't travel nearly as far relative to GPS and phones

There are several factors here, including:

- The GPS system is *predictable* by the receivers. If you've ever used a dedicated GPS receiver, you may notice that it takes longer to get a location fix the first time it's turned on or if it's been off for a while. This is because it's using the information about *where it last was*, and what time it is, and the last satellite-orbit information it copied from the transmissions, to make good guesses about what it expects to receive. This allows GPS to work with a very poor signal-to-noise ratio.
- (Almost) nobody else is transmitting on the GPS frequencies, because that's illegal. They're reserved for the purpose. In WiFi, there are lots and lots of devices all using the same few channels; if two transmit at the same time on the same channel (and distance/obstacles don't make one significantly stronger) then neither will get through, for that one packet.
- GPS is sending a lot less information per second than WiFi. The Shannon-Hartley theorem tells us that there is a maximum rate of information transfer across any channel (here, a limited range of radio frequencies) depending on the signal-to-noise ratio. So WiFi is doing a harder task.
- Your phone does not just use GPS to obtain its location; it also detects nearby WiFi devices and cell towers, and constructs a best guess from all of these information sources.

Do all radio waves potentially travel the same distance?

There is no limit on distance. In a vacuum, with nothing else around, a wave simply loses power with distance. On Earth, with atmosphere and trees and buildings and so on, different wavelengths/frequencies will be reflected and absorbed differently. Generally, longer wavelengths (lower frequencies) can be used at greater distances, because absorption generally tends to increase with frequency.

Also, in the "HF" regions of the spectrum, below 30 MHz, signals are actually refracted off the ionosphere allowing them to propagate around the curve of the earth, whereas higher frequencies usually pass through the ionosphere — which is better if you want to talk to satellites!

Or does the distance depend on the power of signal?

If you increase power from the transmitter, then any receiver receives proportionally more power. Therefore, the signal-to-noise ratio improves (unless the power is so high as to cause overload). So more power means a larger *usable* range.

What determines the power of signal, wavelength or frequency?

Neither; they're completely independent. If you have a transmitter that can produce a power of $x$ watts at a frequency of $y$ MHz, then you can always reduce its power output to some lesser value. This is done routinely for any non-broadcast communication; reducing output power saves battery and lets other users use the same frequency at a distance without "overhearing" each other as much (just the same whether these are 'walkie-talkie' voice communications or several WiFi networks or anything else).

If you get into fundamental physics, you may hear that the energy of a *photon* is proportional to its frequency, and that radio waves are made of photons. This is all true, but practically useful radio transmissions are made up of *many* photons. So changing the transmitter power changes the number of photons emitted per second, but each photon still has the same energy.

(Also note that wavelength and frequency *are the same thing* just measured reciprocally: you can convert one to the other using $\lambda = \frac{c}{f}$, where $\lambda$ is the wavelength, $f$ is the frequency, and $c$ is the constant speed of light.)

## Answer (score 3, by hotpaw2)

The curvature of the Earth also makes a difference between how a signal will propagate near the ground versus in outer space.

And at a large enough distance, the random quantum behavior of the atoms and electrons in your receiver radio will drown out their reaction to any incoming radio waves.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12690/how-far-do-radio-waves-travel, by sirshakir, Kevin Reid AG6YO, hotpaw2. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
