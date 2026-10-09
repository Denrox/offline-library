# Conventional or electron current

*Tags: electronics, theory · score 3*

## Question

I’m reading a radio theory book, Radio Theory Handbook by Ron Bertrand VK2DQ, which suggests that electron flow (ie current flowing from negative to positive) is used in radio theory and design.

In the electrical trades it is common to hear of current flow from positive to negative. This is called the conventional direction of current flow. This is just what it says, a convention. Current flow is electron flow and it is from negative to positive. Conventional current flow is mostly used in Electrical Engineering. In Radio there is a greater tendency to do what I have done in this book and that is to use electron flow; current flows from negative to positive.

The author then says that one should think of current travelling the opposite way to the arrow in a diode or transistor, which seems like a bad idea to me. I know conventional current flow from positive to negative is technically ‘wrong’, but it’s the convention that is used pretty much everywhere. Is this author right, in saying that electron flow is used in radio theory, rather than conventional current flow?

## Accepted answer (score 4, by Marcus Müller)

Current flow is electron flow and it is from negative to positive.

This is what we call class A hogwash.

Current notation is just a convention. Going by electron flow is not righter than going the other way around.

Conventional current flow is mostly used in Electrical Engineering.

As an EE, can confirm.

In Radio there is a greater tendency to do what I have done in this book and that is to use electron flow; current flows from negative to positive".

As an EE with a bit of focus on communications I can say:

This is simply not true. The standard literature on radio theory, wave propagation and the like all use currents and current densities that are coherent with the electrical field. And that goes from positive to negative potential. That implies that current should flow in the same direction.

Of you don't do that, you end up with a set of Maxwell's equations that might still work, but have different signs as the ones you meet everywhere.

So, get another book. This one doesn't stick to nearly 150 years of conventions, and there's really no good reason for making the things you learn harder to compare to what basically everyone else does.

## Answer (score 2, by Glenn W9IQ)

In general, you will find that the electrical engineering field uses conventional current flow (current flows from positive to negative connections). This is re-enforced by some of the symbology used in electrical engineering - a notable example of this being a solid state diode with the arrow showing the direction of conventional current flow. With that being said, you will find some electrical engineering professors and engineering texts that prefer to discuss current flow in the sense of electron travel - even though they don't really "travel" very far. But this approach is clearly in the far minority within the electrical engineering community.

On the other hand, the physics majors will more often prefer to discuss current flow in the "electron flow" manner since this allows a more convenient description of some of the underlying mechanisms of physics. So if you are in a broader research organization or in an academic setting, you will find it necessary to be able to freely switch between the two concepts.

So the suggestion that describing radio wave mechanics on the basis of electron flow is more likely symptomatic of someone who's background or training comes from the physics side rather than the electrical engineering side. Radio wave theory is easily explained using either approach. Most electrical engineers will stick with conventional flow even when describing radio wave theory.

To underscore the somewhat debatable nature of this topic, consider that even the notion of electrons being negative is agreed upon only by a matter of convention as well.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9647/conventional-or-electron-current, by jford, Marcus Müller, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
