# How can I change my "home" registration server for D-STAR?

*Tags: d-star · score 3*

## Question

How do you cancel a D-STAR user registration from one local repeater and re-register with a *different* local repeater?

I can't seem to find any documentation on this.

**Background:**

D-STAR requires that users first register their callsign with a local repeater in order to route traffic across the D-STAR network. This is done via web server, run by the operator of said local repeater.

Once you've registered with any one repeater, that registration becomes valid for every other repeater in the world. The US Trust database is used to share registrations amongst D-STAR repeaters, as well as keep track of the last known repeater for each callsign (so that direct traffic can be routed correctly).

Given this, it's not surprising that there's not much demand for moving a registration; it would seem most folks just register once and leave things as-is.

However, my understanding is that it's still best to register with the repeater used most frequently, since that's the default used for routing messages to you if your radio hasn't been heard for awhile. (For example, if a friend is trying to contact you directly, and you haven't transmitted in a very long time, the message may get routed to your home repeater.)

I just can't find any way to actually do this.

## Accepted answer (score 3, by Dustin Schnabel - KDØQYR)

It has been about a year since I have administered a US Trust System gateway, but I believe you would need to contact the administrator of the old gateway; they would delete you from the gateway, and then you can register with the newer gateway.

Although it is a guideline, I wouldn't think it is a necessity to move your registration. Since we do not run the US Trust system on our gateway locally, I'm registered with a US Trust gateway a few hours away.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/3832/how-can-i-change-my-home-registration-server-for-d-star, by Trevor Johns, Dustin Schnabel - KDØQYR. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
