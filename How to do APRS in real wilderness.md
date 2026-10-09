# How to do APRS in real wilderness?

*Tags: hf, ht, aprs, repeater-coverage · score 12*

## Question

I'm a relatively new ham (licensed a couple of years ago, occasional activity on 70cm and 2m, mostly repeaters). I'm looking to extend my ham experience and am interested in digital and packet modes.

I'm interested in APRS. The main reason is to update my location when I'm off to wilderness, which is often. But outside of Europe and North America, I see that there are not many APRS digipeaters around. Let's say I want hike for days in Central Asia or the Himalayas. What options do I have? Is there some portable HF rig I can carry? When I'm in some deep narrow valleys, is there any hope of updating my location?

Any experience or suggestions will be helpful.

## Accepted answer (score 11, by rclocher3)

So you want to broadcast your location using backpack-portable equipment from deep in a narrow valley hundreds of miles from civilization. I'll assume that you would also like the ability to get a message out when necessary. These are very demanding requirements. I don't think that there is any inexpensive, 100% reliable way to do what you seem to want, but here are some alternatives to consider.

**Option: Morse code QRP (low-power) transceiver**

Pros:

- Radio, battery, and antenna can be under 1.5 lb / 0.75 kg
- Radio can be inexpensive if you're willing to homebrew it
- Simple equipment, therefore hopefully reliable
- Can hold a conversation, rather than just delivering a simple message
- Can normally communicate out to about 1000 miles / 1600 km with ease
- No computer required
- Very power-efficient

Cons:

- Results depend on propagation to some extent
- Morse code knowledge and QRP skill required

**Option: satellite phone**

Pros:

- Theoretically works from anywhere

Cons:

- Expensive
- Fragile equipment
- Battery hog

**Option: PSK31 over HF**

Pros:

- No Morse code experience required
- Easy propagation to about 1000 miles / 1600 km

Cons:

- Results depend on propagation to some extent
- Amateur radio skill required
- Some sort of computer required; computer is fragile and battery-hungry

**Option: APRS via ISS**

I'm talking about APRS using the International Space Station's digipeater (or another satellite's). (more information).

Pros:

- Potentially send APRS messages from anywhere!

Cons:

- Skill required
- Need a fragile gain antenna
- Need some sort of computer for satellite pass information and packet generation
- Difficult for one person to aim the antenna at the satellite and operate the radio at the same time
- Need to get a short packet out during a very brief satellite pass
- Depends on a single digipeater in orbit, which may be hopelessly congested

**Option: Personal Locator Beacon (PLB)**

PLBs are similar to EPIRBs used at sea: a simple, rugged commercially-made transmitter that is designed to transmit an urgent MAYDAY message. When a PLB is activated, generally a Search And Rescue (SAR) team is called out.

Pros:

- Reliable and rugged
- Simple to use
- No subscription required

Cons:

- Can't use it for routine updates
- If a SAR team responds, the user may be liable for the cost of the rescue attempt

**Option: Satellite Messenger device**

A Satellite Messenger is a simple commercially-made device that allows the user to send text messages via the Iridium or Globalstar satellite network.

Pros:

- Reliable and rugged
- Simple to use
- Can send regular non-emergency updates

Cons:

- Subscription is required
- The "jury is still out" on how well they work, according to the REI article

**Other options**

- WSPR: I wouldn't choose this option, because there is no good way to send a MAYDAY / SOS
- Winlink: I wouldn't choose this one either, because it requires a strong signal, which would require a big battery and larger antenna

Personally, I would choose the QRP Morse code transceiver (with a PLB or a Satellite Messenger as a backup), but I already have experience with Morse code QRP. This is a skill, which takes some time to learn, that would need to be acquired and practiced in civilization *before* you head out to the middle of nowhere. But it's the method that uses the simplest equipment and the least power. By the way, for any of these methods to work reliably you would need to hike out of the narrow, deep valley.

## Answer (score 4, by EEd)

Apart from matured and highly reliable commercial satellite-based services, WSPR can be another 'DIY/experimental' alternative for broadcasting your location from wilderness. See examples for balloon, photo and ocean floater, photo.

WSPR is an very low speed mode with 2x to 3x dB SNR advantage over many other digi-modes. Range of a few hundreds to a few thousands km are possible with a few watts, or less, of HF transmission power.

A global network of receiving stations are already setup.

EDIT: If broadcasting position and/or maintaining telecommunication are essential for 'safety' reasons, mature commercial satellite equipment should be used. As said, WSPR is 'DIY/experimental'.

Some satellite system uses a large number of LEO (Low Earth Orbit) satellites (Iridium etc.) and would have better coverage probability for partially sky view obstructed locations. Satellites can appear at higher elevation (near Zenith), multiple and time-varying sky positions. If you wait a while, one of the many satellites may move to a position in sky with direct line-of-sight toward you.

Depending on where you are on Earth, those use equator geo-sync satellites (Inmarsat etc.) demand "much more openness" sky view as satellite may appear at fixed and lower elevation (toward South and toward horizon) positions.

Even LEO satellite may have better coverage, no satellite works at too deep and too narrow valleys.

Examples of mature commercial equipment for 'safety' (non DIY/Hobby) uses 1 2 3

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6645/how-to-do-aprs-in-real-wilderness, by hamster, rclocher3, EEd. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
