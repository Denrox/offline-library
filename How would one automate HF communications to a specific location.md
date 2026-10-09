# How would one automate HF communications to a specific location?

*Tags: united-states, hf, emergency, phone, automation · score 4*

## Question

There appears to be some significant [interest](What%20bands%20and%20modes%20will%20give%20me%20voice%20at%203%2C000%20miles.md) in establishing a fool-proof HF communications method for location to location communication regardless of current propagation conditions.

Given that there's a beacon network which provides good information about how signals are traveling in various bands, it seems like it should be possible to create a transceiver that listens for the beacons, then chooses a suitable band for communication to a user-specified location. If the receiver has a similar radio, it too would see similar conditions, and assuming it was set up knowing the location of the first transceiver it could probably choose the same band.

With some additional pre-setup (agreed on specific frequencies inside each band) and a few attempts at communicating, it seems like one could design such a radio that would essentially automate the process an operator would go through, trying to contact a specific station, and have good chances of making it on one of the available HF frequencies.

Is this possible, or are there problems that would prevent such an approach working? Assuming proper identification is used, and probably using digital modes to do the searching are there legal problems to having the radio perform a quick automated search, or does the operator have to have more direct control over the transmissions?

Essentially what I'd like is an automated station that, given a few minutes, can often find a path to a distant receiver to provide the desired long-distance, always available communications without advanced training and significant effort each contact would normally require.

*Of course there is no guarantee that any band will be open, but if there's an opening an automated system to find it would be the bee's knees.

## Accepted answer (score 4, by KC0ZMX)

You might already know about this, but the Automatic Link Establishment (ALE) system has similar goals and might be what you're looking for.

## Answer (score 3, by K7AAY)

Your automated system would require a PC of some kind to evaluate the beacon reception so SDR, especially cognitive radio, looks like the way to go. I'd suggest getting familiar with GNU Radio and Kali Linux as well as SDR-Radio and SoftRock to work out the band-and-frequency selection process, using the aforementioned beacons as a starting point.

Once you have a strong beacon signal, then evaluate it to see if it's good enough for phone and in a phone-permitted band; perhaps even consider digital modes as well.

Then, start looking for testing partners in multiple locales.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1024/how-would-one-automate-hf-communications-to-a-specific-location, by Adam Davis, KC0ZMX, K7AAY. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
