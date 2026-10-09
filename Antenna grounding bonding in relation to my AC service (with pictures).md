# Antenna grounding / bonding in relation to my AC service (with pictures)

*Tags: antenna-system, grounding, lightning, equipment-protection · score 4*

## Question

I'm trying to figure out how to properly connect new ground rods for an antenna to my main panel. Any advice from those who have done this + have great electrical knowledge would be greatly appreciated.

I plan on hanging a dipole from a tree near the electric service side of my house. I need to ground it and want to install two ground rods (one at the base of the dipole, and another where the coax enters my house). The way that my meter/main panel is set up might not be super common. I had an electrician come out and he thought I could just add ground rods for the antenna and not bond them to my AC service. I'm 99% sure he is wrong since everything I have read says the ground rods must be connected back to the AC service with a continuous #6 wire or larger. I want to have a different electrician come out, but wanted to get a better idea of how things should be hooked up first.

Here is my set up (pictures at the bottom):

**Meter**

- My meter is on a post at the street ~300ft from my house
- The meter box has a section that is accessible to me that contains a 200 amp circuit breaker
- The meter is grounded via ground rods located in the ground at the base of the meter
- The ground wire in the meter box is bonded to the neutral in this box
- 3 wires leave the meter box in underground PVC conduit: 2 hots + 1 neutral (no ground wire)

**Main Panel**

- The 3 wires from my meter enter the house through the underground PVC conduit
- My electrical panel in the house is set up like a main panel (not a sub-panel) and does not separate ground/neutral wires for the various circuits
- This panel has a green screw which I think bonds the neutral bus with the panel box and ground lug that I think is normally used for the connection to earth (ground rods)
- Two wires are connected to the ground lug on this panel: 1. My cold water pipe bond (copper service pipe + copper pipes in the house), 2. A wire that goes to a ground lug on my generator automatic transfer switch panel
- There are no ground rods connected to my main panel or my generator transfer switch panel
- My phone and cable service lines also enter the house through underground conduit and are grounded via a clamp on the outside of my main panel (ideally this would be outside, but probably meets code)

**Things I'm Wondering**

- Can I just install my new ground rods + wire them to anywhere on my neutral bus? Or do I need to install a separate ground bus in my main panel + move my water bond & generator ground to it? Perhaps the ground rods could be connected to the same clamp that my cable/phone service are connected to (I think this may be referred to as an inter system bus terminal - IBT?)
- The ground lug on my main panel having TWO large wires on it looks fishy to me. I'm wondering if this isn't code to have two.
- Does anything seem fishy about my electrical system set up?

**Meter by the street ~300 feet from the houseMain panel inside the house**

## Answer (score 3, by Hogstrom)

Grounding is not something where there is a single answer.

First, you should read up on the topic. I found a book entitled "Grounding and Bonding for the Radio Amateur" by H Ward Silver N0AX invaluable as I have several antennas coming into my home and had the same questions as you.

Second, you'll need to understand the code requirements in your area to determine what is acceptable and legal. There is a lot of good information but you want to ensure that you are in compliance for your safety, insurance should something go wrong and avoiding the unexpected.

Third, I'd talk to other hams in your area to pick their brains and see what works and what else you should know.

## Answer (score 2, by rclocher3)

Ideally answer posts should address the entire question post, but the question post posed many questions, so I choose to answer just two of those questions.

Yes, the NEC (National Electric Code, the template electric code that most local electric codes in the US either adopt or adapt) requires that ground rods be bonded together. Most electricians don't seem to know this.

Apparently the minimum size of the GEC (grounding electrode conductor; that's the terminology used in the NEC) depends on the size of the service-entrance conductors. Typical 200 A service requires 00 (2/0) AWG copper or 0000 (4/0) AWG aluminum service conductors, which would require a minimum 4 AWG copper or 2 AWG aluminum GEC to bond the ground rods together.

If lightning should strike close to your house, it would induce enormous voltages in the ground (and everywhere else nearby also, of course) that would then dissipate. The point of bonding the ground rods together is to reduce the voltage differences in the ground in the immediate vicinity of the ground rods, which in turn should reduce the currents induced in every nearby conductor. In other words, bonding the ground rods would reduce the damage caused by a local lightning strike.

The minimum GEC sizes required by the NEC are really recommendations for average buildings across the US, that attempt to balance the risk of lightning damage against the expense of bonding the grounds. You must decide for yourself where to strike the balance. Some hams go much further to protect their stations and their houses against lightning. Tom Rauch W8JI has some great suggestions in this web page.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20353/antenna-grounding-bonding-in-relation-to-my-ac-service-with-pictures, by Bonfire, Hogstrom, rclocher3. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
