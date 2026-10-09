# What am I responsible for on my link?

*Tags: repeater, echolink · score 4*

## Question

I have set up an AllStar link system to a repeater depicted in the picture below:

The repeater is under NØMHU's call, and my node is under me, KDØWHB. With permission, I service EchoLink and AllStar to the machine for wide coverage access.

I am curious, who is responsible for what if someone who does not ID gets on and potentially performs illegal action?

**Scenario 1)** Illegal transmitter gets on Eldorado, and transmits through my QTH node to another node remotely.

**Scenario 2)** Illegal transmitter gets on a node I am linked to, and it gets aired on Eldorado.

**Scenario 3)** Non-liscensed ham manages to get on an EchoLink account (or the AllStar web transceiver) and transmits to Eldorado, and a remote node I am linked to.

Who is responsible for what? With any of those scenarios, is my call held responsible?

"A control operator needs to be listening at all time to make sure nothing illegal happens where your node is responsible from a local transmission."

Someone told me that. (yes, the same guy from prev. question) Is that true? Will I be responsible for someone getting on my node and doing "bad stuff".

I know all of the repeater rules, but it gets complicated with my weird setup.

## Answer (score 2, by Phil Frost - W8II)

Foremost, remember that the FCC regulates *stations* and their *emissions*. The FCC does not care about the internet or how things work. They care about what comes out of your station, regardless of how that happened.

Further, good amateur practice would dictate that regardless of where the regulations place the responsibility, if your equipment is being used even indirectly for illegal transmissions, you know about it, and you can do something about it, you should. Failure to conform to "good amateur practice" can be in itself illegal (§97.101):

(a) In all respects not specifically covered by FCC Rules each amateur station must be operated in accordance with good engineering and good amateur practice.

This is the "don't be a dick" rule.

## Scenario 1) Illegal Transmitter gets on Eldorado, and transmits through my QTH node to another node remotely.

You are not transmitting anything in this case, so it's hard to imagine how you might be violating anything. You should probably expect a call from other people operating linked stations though, because you are creating the problem of the next scenario for someone else. These internet linking systems work only because everyone participating in them assumes more responsibility for their proper operation than the regulations require. Without that cooperation, the entire system would not work.

## Scenario 2) Illegal transmitter gets on a node I am linked to, and it gets aired on Eldorado

That it gets aired on Eldorado is irrelevant (although, may additionally create problems for Eldorado's control operator): just that you've transmitted it is sufficient. As the control operator of your station, you are responsible for what you transmit.

Presumably, your station qualifies as an *auxiliary station* which is allowed to be *automatically controlled*. Definitions are in (§97.3):

(6) *Automatic control*. The use of devices and procedures for control of a station when it is transmitting so that compliance with the FCC Rules is achieved without the control operator being present at a control point.

(7) *Auxiliary station*. An amateur station, other than in a message forwarding system, that is transmitting communications point-to-point within a system of cooperating amateur stations.

If an illegal transmission made it into the link system and you retransmitted it, automatic control has failed. Fixing it is your responsibility. §97.109 Station control (d) applies:

When a station is being automatically controlled, the control operator need not be at the control point. Only stations specifically designated elsewhere in this part may be automatically controlled. Automatic control must cease upon notification by a District Director that the station is transmitting improperly or causing harmful interference to other stations. Automatic control must not be resumed without prior approval of the District Director.

The widespread adoption of Echolink and Allstar is tacit acknowledgement that the access control mechanisms those systems offer are sufficient to prevent illegal operation. You won't get in any trouble if some guy abuses your transmitter one time, as long as reasonable steps are taken to stop it.

## Scenario 3) Non-Liscensed ham manages to get on an EchoLink account (or the AllStar web transceiver) and transmits to Eldorado, and a remote node I am linked to

This is similar to scenario 2: automatic control has failed and you are responsible. The fact that Eldorado received the illegal transmission from your station doesn't change your responsibility.

In all cases, although an auxiliary station is permitted to be automatically controlled, that doesn't mean you should set it up and forget it. There are social expectations of responsibility above and beyond what the regulations require.

If you can make arrangements to control your station either by radio or by internet, I would suggest doing so. This allows you to *remotely control* the station in the case that automatic control fails. It might also make it possible for you to give other people the authority to shut down the station in the case a problem occurs when you are not around.

Further reading from ARRL:

- VoIP FAQ
- Auxiliary Station FAQ

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2369/what-am-i-responsible-for-on-my-link, by Skyler 440, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
