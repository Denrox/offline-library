# New operator struggling to make a contact

*Tags: qrp · score 8*

## Question

I got licensed a couple of weeks ago and after making 4 attempts on different days, I have made no contacts on SSB, only FT8.

What I have (done):

- Xiegu x6100; tried 5W and 10W
- Par EndFedz® EFT-10/20/40 Trail Friendly antenna
- Antenna deployed as a sloper (about 6m above the ground), inverted V and L
- SWR below 1.5:1
- Located in a park far away from any QRM
- Good conditions for the band

Receiving works very well - I hear dozens of stations from all over Europe.

No matter how much I call CQ, nobody responds. No matter whom I answer, they do not hear me.

I checked web-sdr located 50km away while operating on 20m and my signal was so weak, waterfall barely showed it.

How do I even approach this problem?

## Answer (score 7, by Scott Earle)

The fact that you have made FT8 contacts means that everything is "working". You don't say where you are but say that you can hear signals all over Europe, so I am going to assume that you are probably in Europe. You are fairly lucky in that regard, as there are many countries nearby that you will be able to hear, and once you have sorted out this issue should be able to contact too.

I would start with looking at the antenna. To be honest it sounds like your antenna is better than what I have (I live in a condo in a huge city), and I am also rarely able to make SSB contacts because I just don't put out a good signal. Yesterday I worked DU (Philippines) and YB (Indonesia) on SSB, although both took a little effort. The YB was working Europe (mostly DL), and initially thought I was further away than HS (which is where I am) because my signal is so weak.

If you can find an antenna you can experiment with, you might have more luck. At a QTH away from my condo, I have tried with literally a piece of wire attached to a 10m fibre-glass pole, with a balun and a counterpoise. That worked extremely well compared to the very compact antenna I have on my balcony. I made a few SSB contacts on 40m with that piece of wire.

If you can get yourself a balun, some reasonable wire and a 10m telescopic fibre-glass pole, you will have an absolute blast on 40m and 15m particularly. Just 10W will get you out remarkably far with a quarter-wave vertical on 40m - you will be amazed.

Power is not as relevant as people say it is. Most HF sets fall into two categories: QRP and 100W. If you are running 5W your signal is down 13dB compared to running 100W, and if you are running 10W it's down 10dB from 100W. One S-point is 6dB, so your signal is down only two S-points if you run 5W, compared to 100W. If you have 100W and someone says your signal is 57, then the same person would see you at 55 if you have 5W.

If you can't find a 10m fibre-glass pole (I bought mine from Sotabeams in the UK and they shipped it to Thailand just fine), then try using a catapult and firing your wire into a tall tree. A balun and counterpoises will help you with getting the SWR down and your signal up, and not having any common-mode currents on your coax - less of a problem at 5W but can be bad at 100W.

So I guess what I am saying is - antenna. It's always about the antenna. You could have a Xiegu HF radio, or an IC-7851. But plug it into a bad antenna, and you will be making the same number of contacts.

Also - keep going with the FT8! See which countries you can get on there, and what signal reports you are getting. If someone gives you a report of -21 and you give them a report of +10, then you can see the mismatch between your receive ability and your transmit ability right there. Your sent and received signal reports tell you everything you need to know.

Keep going! It can be very disheartening not to be able to make contacts, so please don't give up.

## Answer (score 5, by natevw - AF7TB)

I think Scott's answer is great, and as much improvement as you can make to your antenna efficiency will be to your advantage. Based on the details you provided it's clear you have a good handle on the variables involved. For others finding this question I'll summarize a bit:

1. For a horizontal half-wave dipole and many similar antennas, typically "the higher, the better" at least for a DX-friendly radiation elevation pattern. In this case efficiency comes from getting more of your signal back to the ground rather than lost in space. (Additional discussion at e.g. [How to determine antenna height for given HF frequency and coverage radius?](How%20to%20determine%20antenna%20height%20for%20given%20HF%20frequency%20and%20coverage%20radius.md)) The azimuth pattern shouldn't be neglected either (stronger to the sides, weakest off the ends of the wire).
2. For a vertical quarter-wave monopole and similar antennas, the elevation pattern tends to naturally favor low take-off angles, and ground losses tend to be the biggest factor for efficiency. Unless you've got seawater or great soil, radials will be key. (e.g. [When and why does the size of a ground plane or radials matter?](When%20and%20why%20does%20the%20size%20of%20a%20ground%20plane%20or%20radials%20matter.md))
3. Horizontal end-feds are a bit of a hybrid case in that most of what applies to other dipoles above still (i.e. **height**) but you also have the question of what I'll call "counterpoise losses" which can either be related to ground loss or just unaccounted-for radiation pattern changes due to the coax becoming part of the antenna (e.g. [Do end-fed dipole antennas need choke baluns?](Do%20end-fed%20dipole%20antennas%20need%20choke%20baluns.md) and Is an off-center fed dipole (and/or doublet) inherently unbalanced?)
4. (Special-case antennas like small loops have their own concerns but some QRP operators have found success.)

But all that said, I wanted to mostly address a different side of the question:

No matter how much I call CQ, nobody responds. No matter whom I answer, they do not hear me.

Even with my 20W rig I have struggled to make SSB contacts. What's helped is:

- making sure my mic audio gain was set fairly aggressively and speaking loudly — not to the point of distortion of course, but to make sure my voice is actually peaking the meter near the radio's full power. Otherwise even at 5W you might be sending out closer to a 500 mW signal effectively.
- hunting for stations that seem likely to answer. I've never gotten anything back from my own CQ calls, and I don't think I've ever been able to break into a 1500W contester blasting across the continent either. But when I've come across other modest stations coming in fairly strong, and I hear them looking for contacts — that's when I seem to have an okay chance of at least exchanging a signal report if I'm lucky. But still far from guaranteed. It helps if *they* are in a quiet location.

From what I've hear the main thing with QRP is patience and persistence. Out of maybe ten times setting up my radio and spending some time trying, I've made only a few SSB contacts total. And only in one case could we hear each other clearly enough to have an actual easy conversation — the rest were very brief and my impression was they could only barely just hear my callsign.

One thing I should have tried was "self-spotting" which is sometimes allowed for games like Parks On The Air. If you post to the right website(s) with what time you'll be calling CQ and your location and frequency and that you'll be QRP, then more people might try to seek your signal specifically and respond. (But note in most formal contests perhaps even other contexts this is considered very bad sport or cheating!)

Long story short I'm sure a better operator could do better on low-powered SSB — but for me I have a lot more fun when I stick with digital modes on QRP.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21083/new-operator-struggling-to-make-a-contact, by Amanda Helgström, Scott Earle, natevw - AF7TB. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
