# What do you connect antenna Radials to?

*Tags: antenna, antenna-theory, grounding, radial · score 3*

## Question

I am trying to communicate between two arduino microcontrollers using radio. For this purpose I am building a whip antenna with 4 ¼ wave radials. I've done a bit of reading and have got most of it, but all guides I've found are a bit vague on the topic of radials.

So my question is: When it says that Radials should be grounded, does that mean they have to be connected to the actual ground, or is the ground Pin on the arduino (the "minus pole") ok too? As my project is mobile, actual ground is pretty tough...

## Accepted answer (score 2, by Mike Waters)

The radials are not connected to the earth. Here's a photo of a ground plane antenna. They are connected together as shown to the coax shield. This shield should be connected to the common on the board that can serve as an RF ground.

## Answer (score 2, by SDsolar)

Radials are grounded to the feedpoint.

For instance, the shield of the coax feeding the quarter-wave antenna. For AM radio broadcasting stations, there are radials every 3 degrees (120 of them) and they are generally buried (enough so you can still mow the lawn above them), so they are at ground potential their entire length.

If the radials are not themselves grounded then that is called a counterpoise, like if you install a radial system on a rooftop. In that case the true ground is at your transmitter, then the feedline shield is the connection to the counterpoise on the roof.

In terms of Amateur Radio usage, there are a lot of great antennas like the Hustler 5BTV that require professional-quality ground systems.

Another example is if you use a magnetic mount for your antenna on the car, it couples into the metal of your car as the ground plane.

I think the best answer to your question can be found HERE - the basic concept is shown in this diagram:

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7467/what-do-you-connect-antenna-radials-to, by user5227744, Mike Waters, SDsolar. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
