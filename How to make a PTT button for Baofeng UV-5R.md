# How to make a PTT button for Baofeng UV-5R

*Tags: baofeng · score 8*

## Question

I use the radio for paragliding and the radio is mounted on a "cockpit" in front of me when flying.

When in flight my hands are busy. I can hear the radio fine (don't need an earpiece) and I can transmit fine too (others can hear me, don't need a better/closer mic).

However transmitting can be problematic because I have to take one of my hands off the controls to press and hold the PTT button on the side of the radio.

My idea was to use a kenwood type cable and connecting a button/switch to the correct terminals so that I can put effectively the PTT switch about 50cm away from the radio where I can push and transmit without taking my hands off the controls.

If this is possible, which two terminals would I be shorting?

As a bonus question, would the UV-5R support dual PTT (A and B) like the UV82 described in the link?

Many thanks for the help

## Accepted answer (score 8, by MoTLD)

You want your switch to short the shield of each of the connectors to each other, strange as that sounds. These plugs are commonly known as TRS, or tip-ring-shield, so the shield is the part closest to the body of the plug. The ones you want are both marked PTT in this image (don't let the other stuff confuse you, these pins do multiple things when connected with mic or speaker to other pins, but they transmit when connected to each other):

The Miklor page you linked to, in the fine print under the dual PTT picture, does have the answer to your other question, which is unfortunately no, the UV-82 style dual PTT only works with dual-PTT radios like the UV-82. Honestly, they're cheap and dual remote PTTs might be useful enough in your circumstance to get one just for that feature. My mom has a UV-82 and likes it very much, so I can personally recommend it.

In the case that you do have a dual PTT radio, shorting both shields as above will transmit on the lower display channel, and shorting the tip of the 3.5mm plug (marked +V above) to the shield of the 2.5mm plug gets you the upper channel.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7398/how-to-make-a-ptt-button-for-baofeng-uv-5r, by Andre, MoTLD. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
