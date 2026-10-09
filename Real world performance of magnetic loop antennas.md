# Real world performance of magnetic loop antennas?

*Tags: antenna, rfi, magnetic-loop · score 11*

## Question

I was investigating about magnetic loop antennas. In a paper about them I found some bold claims:

and

This almost sounds too good to be true, considering a lot of us hams are surronded by city noise and this paper claims the noise would be much lower with this design.

What is the real performance of this kind of antennas, then?

## Answer (score 4, by Ted)

I've been using magnetic loops for 20 years

A magnetic loop can work well if it has two qualities: enough power handling (a 5 kV vacuum variable will handle 100 Watts, 15kV will do a kW); and a decent remote tuning setup. tuning is critical, as Eham reviews show the main dfficulty is getting the SWR properly dipped. Thanks to the popularity of robotics, low cost stepper motors are available, and do the job.

While size isn't critical, efficiency goes rapidly downhill at diameters less than than about a 20th of a wavelength. 1/2" or 3/4" copper tubing is self supporting, low loss, and is easily flattened and drilled for low loss connections. Paint it a dark color for stealth, and to avoid corrosion.

Dealing with high voltages and extreme narrow bandwidth are the price paid for an antenna that makes a magnetic near field, which seems to penetrate nearby conductors, such as trees, the ground, house wiring, powerlines, etc. almost as if they weren't there, because induced currents are in phase with the antenna's field. Near field losses are reduced by an S unit in a typical urban location, when compared with a wire antenna or a vertical whose electrical near field induces out of phase re-radiation.

The statements about quiet receive are approximately correct. In my experience, fixed local terrestrial noise sources (a pole pig with nesting squirrels, an LED streetlight)can be reduced typically by two S units (10 dB) by a vertically hung loop that is tied with a side line to keep the null lined up. Unlike stations using an antenna tuner at the radio, received and transmitted RFI does not come from the loop's feedline because its matched all the way to the antenna, where tuning and matching is done.

Further details are at www.x44.cc, or by googling my ham callsign, K1QAR

## Answer (score 4, by Mike Waters)

Under *some* circumstances, this can be true. What Leigh seems to be talking about is nulling out a **local** noise source, which a rotatable loop excels at.

Between the loop and a vertical or dipole, in my experience the loop will often do what he says. But a loop compared to a beam? Not so much.

I have always respected the author, Leigh Turner VK5KLT for his technical knowledge. However, unless a rotatable beam (such as a tribander) is quite low (say, under 40 or 50 feet), I take exception to his statement that a loop will nearly always hear better than an HF beam.

## Answer (score 3, by skywave dxer)

I use a magnetic loop as my main antenna since I am a renter. It is outdoors about 10 feet from the building and about 10 feet above ground level. It is approximately 1 meter in diameter.

Performance:

usable frequency range: 40 meters through 15 meters.

15 meters similar to dipole you can rotate.

20 meters similar to dipole you can rotate.

30 meters about 3 to 6 db worse than dipole not very directional.

40 meters about 6 to 9 db worse than dipole not very directional.

It is not usable at all on 80 meters , not even for receive of local strong signals.

Overall mag loops have one significant problem: Extremely low usable bandwith (very high Q factor). This is also the reason they work so well so this problem cannot be fixed, you have to work around it. If you want to change frequency more than 1 kHz (not MHz) you will need to re-tune. For this to be practical you will need a remote tuning device of some kind.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/13242/real-world-performance-of-magnetic-loop-antennas, by hjf, Ted, Mike Waters, skywave dxer. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
