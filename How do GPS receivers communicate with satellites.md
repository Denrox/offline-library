# How do GPS receivers communicate with satellites?

*Tags: satellites, gnss · score 11*

## Question

I have a Technical Amateur Radio license so I know the basics of wavelengths. What I'm researching is how GPS works.

From what I've read, there are frequencies such as L1, L2, and L5 uses in GPS between the receiver and the satellite. These operate at at a frequency of about 1500 MHz. https://gisresources.com/everything-you-need-to-know-about-gps-l1-l2-and-l5-frequencies

What I'm having trouble understanding is how a receiver can communicate with an object 12,000 miles away at about 1 GHz.

I know my knowledge on GPS is rudimentary but I'm trying to make sense if it, thanks!

https://www.gps.gov/systems/gps/space

## Accepted answer (score 27, by mjt)

The first thing to know is the communication is one-way. There's a satellite-to-receiver transmission, nothing going in the opposite direction. So your cell phone doesn't have to find the radio power to send a signal all the way to space!

(exceptions: The decommissioned Chinese BeiDou-1 system - and any products where the GPS receiver chip is used alongside a satellite transmitter, like a Cospas-Sarsat emergency locator beacon)

The signal from GPS satellites is very faint - each satellite has to broadcast a signal to about half the planet, powered only by some solar panels! So the broadcast signal is modulated using a 'Gold Code' (in the case of the oldest public GPS signal) where part of the signal transmitted by the satellite is already known by the receiver - the GPS receiver can pick out the signal despite how faint it is, by tracking the cross-correlation between the received and expected signals.

This also means multiple satellites can transmit their signals at the same frequency - so long as they use different gold codes, the receiver can track both signals independently.

Newer GNSS signals replace gold codes with newer techniques - like 'multiplexed binary offset carriers' - which perform better, but do basically the same thing.

## Answer (score 13, by David Hoelzer)

The receiver does not communicate with the satellite; it just receives.

Fundamentally, the receiver listens on one or more well-known frequencies. The receiver determines which satellites it can "hear" based on the PRN identifier code and each satellites position based on the ephemeris data that it transmits.

The satellites all broadcast a synchronized time signal. Since the receiver knows the location of the satellites and it can measure the differences in the time signals from the various satellites, it can triangulate its position on the surface of the earth.

## Answer (score 10, by user9123)

The other answers already provide very detailed explanations, so I decided instead to suggest a resource which answers your question, but should also be very helpful with your further research:

GPS - Bartosz Ciechanowski (wayback link)

It's an interactive blog post which starts with the basics, then gradually goes into great detail about the inner workings of GPS.

Your question is answered near the very bottom:

Finally, it’s worth reiterating that the receiver doesn’t need to send anything to the satellites, it just listens to the signals that the satellites restlessly emit without knowing if anyone receives them.

In summary, to answer your question, they don't!

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21314/how-do-gps-receivers-communicate-with-satellites, by john_ham_radio, mjt, David Hoelzer, user9123. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
