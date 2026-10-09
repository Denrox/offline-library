# Receiving the ISS SSTV: dipole antenna configuration and orientation

*Tags: antenna, dipole, satellites, polarization, sstv · score 5*

## Question

### In short

I am trying to receive SSTV Images from the ISS (145.8Mhz) and I all have is a simple "bunny ears" dipole antenna. In what configuration (straight, vee shaped, upside down vee, ...) and orientation should I place the antenna to optimize signal reception? Could you please explain why and/or link to some sources where I can learn how to find the proper orientation myself?

### More details

I've tried answering this question myself but I all found was tutorials that either didn't specify the antenna configuration/orientation or even contradict each other.

While vertically dipoles are widely discussed, there are not many sources (that I could find) that discuss other dipole configurations. Since the radiation pattern of a vertical dipole is shaped like a doughnut (where the dipole is passing through the doughnut hole), I was expecting that rotating the dipole by 90 degrees (so that it lies in the horizontal plane) would also rotate the radiation pattern accordingly. Apparently I was wrong.

Assuming that the information on that website is correct, I can't really find an orientation for good reception of a signal coming almost-vertically from the sky.

Also, I wasn't able to figure out what polarization is being used by the ISS SSTV transmission. This website reports it as "U: linear, V: linear", but there is no explanation of what U and V mean in this context (I assume it's a standard notion but I haven't been able to find an explanation either).

What does this polarization refer to anyway? Since the ISS rotates I assume the polarization will also shift by 90 degrees (twice) from the perspective of the receiver. At what point in the orbit does the apparent polarization match the nominal one?

Finally, to optimize reception I assume I'd need to rotate the antenna along with the ISS pass (to properly direct the radiation pattern and match polarization). What's the correct orientation at any given point in the orbit?

If reorienting the antenna is not possible, are there any tips for choosing a fixed antenna position? Is it better to optimize for reception when the station is directly overhead, for when it's rising/setting, somewhere in-between, ...?

As you can see I'm a little confused, and I would be grateful for any guidance from anyone more expert than me.

## Accepted answer (score 5, by hobbs - KC2G)

reports it as "U: linear, V: linear"

Satellites which transmit and receive at the same time frequently do one on VHF (2m) and the other on UHF (70cm), and they frequently have separate antennas for each (rather than a dual-band antenna). This notation is saying that the ISS's UHF and VHF antennas are both linearly polarized.

What does this polarization refer to anyway? Since the ISS rotates I assume the polarization will also shift by 90 degrees (twice) from the perspective of the receiver. At what point in the orbit does the apparent polarization match the nominal one?

There is no nominal one. It's just linear *something*, as opposed to circular. With satellites you don't really know which way they're pointing. That's the advantage of circular polarization — you don't have to know, you just have to get the correct handedness.

Finally, to optimize reception I assume I'd need to rotate the antenna along with the ISS pass (to properly direct the radiation pattern and match polarization). What's the correct orientation at any given point in the orbit?

With regard to polarization, again, you don't really know. With regard to pattern... whichever way gives you gain in the direction of the ISS :)

If reorienting the antenna is not possible, are there any tips for choosing a fixed antenna position? Is it better to optimize for reception when the station is directly overhead, for when it's rising/setting, somewhere in-between, ...?

A good trick in this case is to orient the dipole horizontally, and perpendicular to the track of the satellite's pass. i.e. if the ISS is going to be coming over from the northwest to the southeast, point the ends of the antenna to the northeast and southwest. This places your nulls roughly on the northeast and southwest horizon, which are the points furthest from where the satellite will be at any point in the pass, so you should enjoy decent reception throughout.

Finally, as Duston mentions in a comment, the ISS is pretty darn loud compared to most amateur satellites... in most cases you can do everything wrong and still hear it fine, so don't worry too hard.

## Answer (score 2, by jp314)

The ionosphere conversion to circular is not particularly good - e.g. see cv.nrao.edu/~demerson/ionosphere/ionopol.html. This means that the circular polarization is very variable (ratio of major:minor axis signal strengths). Conversely the (linear) polarization alignment of most satellite signals is unpredictable from the receiver's point of view - maybe the satellite is tumbling. Because of that, a circularly polarized receiving antenna will work 'least bad' -- it's sensitivity is independent of the actual alignment of the linear polarization, although it is about 3 dB worse than a correctly aligned linear antenna would be (but you'd have to continually rotate it to align with the transmitter).

So a circularly polarized receiving antenna won't have any nulls when receiving a linearly polarize signal (at any angle), while a linearly polarized (e.g. a standard) antenna could have nulls if misaligned by 90°, and will be worse than the circular one for misalignments of between -45° and +45°. Thus, unless you can control or adjust a linearly polarized antenna, on average, 50% of the time, the circular one will be better (all other things being equal), and the circular will never have a null where it receives nothing.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17785/receiving-the-iss-sstv-dipole-antenna-configuration-and-orientation, by Steven, hobbs - KC2G, jp314. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
