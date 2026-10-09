# Can my neighbor's ham radio antenna be interfering with my internet signal or is my internet provider just throwing blame elsewhere?

*Tags: rfi · score 36*

## Question

My internet provider is telling me that an antenna on my neighbor's house, which he called a ham radio antenna, is interfering with my DSL internet signal. I'm not tech savvy at all, beyond what's necessary to function in today's world, so I'm clueless as to what this is, what its used for, or if this even a legit accusation.

I am, however, skeptical of this claim due to an ongoing history with my provider. I experience a problem about once a month, I call, they say they'll send someone, then after the call the problem clears up a few minutes later and their "tech" guy never even shows.

But this time its gone on for a week. We've replaced the modem and this is the explanation they're giving me. I feel its more likely that my provider is taking advantage of me, but I can't be sure.

Is it possible that this antenna could be interfering with my internet signal? And if it is the likely factor, is there some way for my neighbor and I to both have what we need? Or is someone going to have to compromise? I don't know this guy, I don't know what he used the antenna for, but it hardly seems fair for me to ask him to take it down or stop using it. He has rights just as I do. But at the same time, this problem is interfering with my livelihood. My job requires that I have internet access at home. If this problem persists, I'm super screwed.

Can anyone here offer up some advice? And please, I'm an idiot when it comes to techie stuff. Please dumb down your language enough for me to grasp what you're talking about. Ya know.. Use laymen's terms for me.

## Answer (score 37, by Kevin Reid AG6YO)

Could be, but likely not. In particular, almost no amateur radio station would be operating *continuously*, so if you have a problem that is not intermittent, that's unlikely to be the source of it.

(If you edit your question to specify what type of internet access ('cable', DSL, microwave link…) you have, and include a picture of the antenna, we can make a more informed guess about whether they might interfere. If they're on completely different frequency bands, well then.)

Talk to your neighbor. Don't lead with a complaint — just tell them that this is what your ISP is claiming and you want to get more facts. Have them tell you *when* they're operating (transmitting), or you tell them when you're experiencing connectivity problems. If the timing doesn't match, then this can't be the cause. (Also ask them what “bands” they are operating on and write down the answer.)

If the timing *does* match then things are more complex, because there could be several different situations:

- Your in-home networking equipment (modem, router, WiFi AP) can't tolerate the nearby signal which it should be able to.
- The ISP's equipment not in your house can't, ditto.
- The electronics are fine but the *cable* is damaged somewhere (for cable-type internet access), letting the interfering signal in.
- Your neighbor's equipment is transmitting excess power on frequencies which it shouldn't.
- Your stuff is legal and functioning correctly, their stuff is legal and functioning correctly, but they're just too close together. In this case you'll just have to see if your neighbor can agree to avoid operating when you're working.

## Answer (score 14, by Floris)

A "ham radio" is typically a transmit/receive system that uses certain frequencies set aside for radio amateurs to communicate with other enthusiasts. If there is a big antenna on your neighbor's roof, he/she is likely enthusiastic and quite knowledgeable in the area of radio interference; I am going to guess he/she would be happy to help you troubleshoot.

Interference between your neighbor's activities and your internet signal can happen if the frequencies of the transmitter and the frequencies used by the internet provider are close enough together; and if there is some way for those signals to "mix". This can be a result of poor shielding, damaged cables, or just plain bad luck in the layout. It can also happen if your internet signals are traveling "over the air": this can be because you have a satellite link, or because you use WiFi inside your house to go from the modem (the device that connects your house to the internet) to your computer.

In my experience, WiFi interference is much more likely between WiFi routers in adjacent homes, than between a WiFi router and a ham radio.

Talk to your neighbor. Bring cookies.

## Answer (score 10, by Dan Mills)

A HF transmitter can interfere with a DSL service if the conditions are right simply by inducing more RF on the drop wire then the DSL modem (Which **always** cheap out on front end electronics) can cope with.

Been there with my own DSL service when running a few hundred watts on 20M, suitable ferrite rings on the power and data wiring can sometimes help, but I would expect such problems to be intermittent (Most Hams do not transmit 24/7).

Go and talk to the neighbour, most hams are well aware of the potential for this kind of thing, and while (at least in the USA) it is not really their responsibility to fix your inadequate networking gear, they will often try to help in order to keep the peace.

Testing to find out if his rig is the problem is easy with your cooperation, and you may well find that his station has nothing to do with it (Convincing the phone company 'technician' of this is left as an exercise in frustration).

This really is the ISPs problem, not the radio operators, but having dealt with ISP support departments, you are more likely to get a fix from the ham (Who, apart from anything else, can sometimes point out to the ISP where their problem is)!

From a legal perspective, the modem is almost certainly a "class B computing device under FCC part 15", which means that it must accept any interference from a licensed radio station. This is to say that a licensed station is allowed to cause it interference. Good networking kit will have better protection, but the stuff most ISPs supply as freebies is 'designed to a price'.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6887/can-my-neighbor-s-ham-radio-antenna-be-interfering-with-my-internet-signal-or-, by Vanessa, Kevin Reid AG6YO, Floris, Dan Mills. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
