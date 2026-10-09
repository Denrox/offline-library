# What are the regulation requirements for running a repeater?

*Tags: united-states, legal, license, repeater, callsign · score 7*

## Question

When I try to find information on the requirements to run a repeater, I just see a lot of results related to building one. But I'm wondering about USA regulations.


Does one need a particular license?


Which frequencies are allowed?


Can/should the station have its own call sign, or the call sign of the owner? How does one get another callsign?


What is required of a station that is not being monitored by the owner (Automated by a controller)? Does it have to broadcast its call sign every X minutes?


What other limitations/requirements are there?

## Accepted answer (score 13, by WA9ZZZ)

The regulations for an amateur radio repeater are fairly minimal. To answer your specific questions:

"Does one need a particular license?" Your license must permit transmissions on the repeater output frequency. That is, general or higher for 10m, technician or higher for higher frequency bands. There is no special repeater license. (There used to be.)

"Which frequencies are allowed?" Repeaters are only allowed on the 10m and higher frequency bands. Within those bands there are subranges where repeaters are not allowed (neither receive nor transmit). These are spelled out in 97.205(b) of the regulations.

"What other limitations are there?" Not much. For the most part the regulations for power, modes, etc. are the same for repeaters as for other stations. You should get coordinated with your local repeater coordination council. That is not an FCC requirement, but if you don't you might have to protect a coordinated repeater from interference.

Most of the rules are fairly simple and can be found in Part 97 of the FCC regulations. The ARRL web site has a link to the official rules website plus it has a PDF. Just search for "repeater" and you'll find the information you need.

## Answer (score 10, by rclocher3)

WA9ZZZ's answer missed the issue of control of the repeater. The repeater must be under control of one or more control operators, or under automatic control, at all times when the repeater is on. There are three types of control:

- Primary control, where a control operator is physically near the equipment and monitoring the repeater, ready to intervene as necessary, the whole time it's on.
- Remote control, where the control operator(s) is/are monitoring the repeater remotely and also controlling it remotely through a control link, typically a telephone line or a radio link.
- Automatic control, where devices and procedures are used to ensure that the repeater is operating in compliance with FCC rules. For instance, a repeater controller can time out and stop transmitting if someone has been talking continuously through the repeater for too long.

Most repeaters in the US have a repeater controller, which is a device that provides automatic control. Typically the repeater controller also allows some remote control to turn functions of the repeater on and off; for instance, a sequence of DTMF tones can be sent to turn the repeater off if someone is transmitting profanity through the repeater.

If remote control and not automatic control is used (no repeater controller), then the control link has to be usable 100% of the time the repeater is running. In my opinion this rule would preclude DTMF tones on the repeater input frequency being used for control, because a malicious operator with a bigger signal could block out the control operator.

To sum up, if you're not planning on babysitting your repeater locally or remotely, then you'll need a repeater controller so your repeater will legally be under automatic control.

I found much of this information on the ARRL's Auxiliary Station FAQ page.

Also, the repeater must identify itself periodically, like any other station. Repeater controllers can typically be programmed to do this, or I suppose a control operator could identify for the repeater.

Someone asked if a repeater needs its own call sign, because the owner of the call sign, the licensee, might be operating on a different frequency at the same time. As I understand, a repeater doesn't need its own call sign. Furthermore, an operator can be on several frequencies at once, from several different physical locations, as long as he or she is exercising control over all the stations. (Hat tip to @hobbs-KC2G.) Many repeaters identify using Morse code, and the nearly-universal practice is to put the suffix "/R" on the end of the call sign, which identifies that the call sign is for a repeater. If the identification is by voice, either by a recording or a live control operator, then I'd think the identification would be something like "this is W1AW, repeater". So the "/R" or "repeater" suffix on the call sign clearly identifies the call sign as being for a repeater, so there should be no need for a separate call sign.

In the United States, the only way that I know of to get a new separate call sign for a repeater is to use a club call sign. This process apparently was frequently abused in the past, because the rules have been tightened down considerably. First, there must be a club with at least four members, and the club must have a document of organization (typically a charter) and several officers, and it must have regular meetings. The club must designate a person to serve as trustee for the club call sign in a document signed by club officers. A person can serve as trustee for only one club call sign. A club can have multiple club call signs (and therefore multiple trustees), but only one call sign can be a "vanity" call sign. More information about club call signs can be found on the ARRL's Club Call Signs page.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16354/what-are-the-regulation-requirements-for-running-a-repeater, by Bort, WA9ZZZ, rclocher3. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
