# High 40m noise floor during the evening but quiet in the afternoon

*Tags: noise · score 9*

## Question

I've been dealing with S7 static on 40 meters ever since I got started a few weeks ago. It's so bad that I have to use my RF ATT so that the static is not deafening.

I did some research about finding noise sources (mostly wall warts) and common mode noise as well as the benefits of ferrite chokes. I have tried choking the antenna feedpoint as well as the point before entering the house- to no avail.

My current setup is a TS-830S with coax going out the window to a dipole up in some trees. At the dipole feed point is 8 loops of RG-8x clamped by a 1" ID mix 31 ferrite bead. That coax runs to a T connector right next to my house. The T connector is clamped onto a ground rod. The bottom of the T has a Palomar Engineering bleeder resistor. The other end of the T has 8 loops of LMR-240 in another clamp on 1" ID 31 bead before entering the house. Just at the feed point on my rig, I have another 8 turns into a toroid (#31).

Before the chokes and grounding- it was just a run of coax straight to the radio from the dipole. It made no difference either way.

Then one day I decided to try 40 meters at 2 o'clock in the afternoon. It was quite dead. In addition to that, there was no noise at all. We're talking less than S1. I turned off the radio and went about the rest of my day. I cam back at 8pm and turn the radio on. This time there was tons of activity and S7 noise. The noise is just static. No hum or buzz. Just snow.

The fact that I had near zero noise in the afternoon leads me to believe my house does not contain the source of this noise. My computer and TV were on at the time and it was still rather quiet. Only once the band opened up did the noise come in. What else can I try? Can I rule out my house or neighbors as the source of noise?

EDIT: Link to sound of the noise https://streamable.com/uiyd4

## Accepted answer (score 2, by mike65535)

Night-time propagation on the low bands is significantly better than that during the day. Static crashes from lightning can be heard from hundreds of miles away on 160m-40m and more so at night. Summer-time noise can be much worse generally than winter-time.

This is NOT to say that you don't have a local radiator from people being home from work - say a plasma TV or other such nonsense.

What does it sound like? Can you record it?

The ARRL website has several noise examples to listen to.

*edit*

Based on your recording I'd say that was normal atmospheric noise.

*/edit*

## Answer (score 2, by Phil Frost - W8II)

Firstly, you can [measure common-mode current](How%20to%20detect%20common-mode%20currents%20or%20RF%20in%20the%20shack.md). That will give you some idea of how effective your choke is.

Also, I suggest getting a battery to power a receiver, and flipping off the main breaker in your house. Does the noise floor go down? If so, turn things back on one circuit at a time, identify the culprits, and replace / relocate / shield / choke them.

If you're friendly with your neighbors, try the same there. Or wait for a power outage.

If testing indicates the antenna choke is effective and there are no obvious noise sources in your house, congratulations: this is about as good as it gets! [Noise is naturally stronger with decreasing frequency](How%20can%20I%20calculate%20the%20effects%20of%20an%20LNA%2C%20antenna%20gain%2C%20etc.%20on%20noise%20performance.md), and S-meters are rarely calibrated to any standard, so a S7 noise floor on 40 meters may just be ordinary. The noise floor will naturally go up as the band opens at night as you are able to hear more distant natural and man-made noise sources.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/11617/high-40m-noise-floor-during-the-evening-but-quiet-in-the-afternoon, by Paul, mike65535, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
