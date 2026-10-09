# What should I consider when choosing a coaxial cable?

*Tags: feed-line, coaxial-cable · score 15*

## Question

Given a middling-power rig (up to 100 W) requiring a 50 Ω antenna, a few options for the coaxial cable with a 50 Ω impedance are

- RG-174
- RG-58A/U
- RG-8
- RG-213

Apart from cost, what factors are relevant in deciding which coaxial cable to use?

## Accepted answer (score 8, by PearsonArtPhoto)

The most important thing about the cable is how much loss are you willing to accept in the feed line. Figure out how much cable you will need, and then determine what the loss on said cable will be. As I mentioned on my website, here's a few good rules of thumb:

- Keep the power loss to no more than 3 db in the cable.
- If you can, use the same impedance as your antenna/transmitter, but always keep the impedance to within a factor of 1.5 of your antenna/transmitter. But really, match them, it's not worth the hassle of mis-matched cable.
- If you can, use only a single strand of cable. Also, use the right connectors for both ends.
- Buy for the largest frequency that you think you will be using.
- Get a cable that is slightly larger than you need, but not excessively larger.
- The velocity factor only matters if you are trying to build a phase changing antenna.

Longer cable equals more loss. Higher frequency is also more loss. Here's a few websites that talk about what the loss is per length and frequency of each cable:

- http://www.pcs-electronics.com/guide_coax.php?osCsid=600b648260d42af6d62fe29eb5c9053d
- http://www.hamuniverse.com/coaxdata.html
- http://www.thewireman.com/coaxdatacurrent2.pdf

## Answer (score 3, by Bryan Leenheer)

Your question is missing an important item; the frequency at which you're operating.

I work a lot of VHF+ contests, and all four of the varieties of coax you mention pose far too much loss of signal to be viable for those frequencies. I use LMR-400 Ultraflex for 6 meter, and 3/8" Andrews Heliax hardline for 2 meter, 222, and 440 bands.

http://www.w4rp.com/ref/coax.html is a great resource for tracking how much loss coax presents at various frequencies.

Another point you don't mention is where you're intending to use the coax. Tower applications require different coax considerations than a mobile installation, and SOTA requirements are different still.

## Answer (score 2, by Bill - K5WL)

In addition to characteristic impedance (such as 50 ohms) and cost, which you've already considered, the two main factors for coax feed line types are line loss at a particular frequency, and velocity factor. The line loss varies depending on operating frequency, so it depends on your application. For line loss, the main factors are what frequency bands you're going to use over the feedline, and how long the distance is between the transmitter and the antenna. For VHF and above, line loss is a much bigger consideration. Velocity factor comes into play if you are going to create matching stubs or if you are working with non-resonant antennas like the G5RV and need to avoid certain lengths.

Other factors include how flexible the line is (braided vs. solid wire), how much motion it will endure (rotors, portable operations), how waterproof it is (permanent or underground installation), how hard it is to work with (LMR-100 is notoriously hard to attach connectors to), etc.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16/what-should-i-consider-when-choosing-a-coaxial-cable, by VU2NHW, PearsonArtPhoto, Bryan Leenheer, Bill - K5WL. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
