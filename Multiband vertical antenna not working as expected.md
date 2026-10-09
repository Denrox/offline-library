# Multiband vertical antenna not working as expected

*Tags: antenna, vertical-antenna · score 6*

## Question

I built a vertical out of a 5M aluminium pipe. It tunes fine (and wide!) on 20M. I decided to add a loading coil to operate it on 40M, and it also worked fine, albeit not so wide. While I was at it, I extended the coil for operation on 80M as well. It became super narrow! But it worked.

To test this, I used crocodile wires to bite into the coil. I decided make a remote switch out of relays. But it's not working as expected when operating 80M. The SWR jumps around like crazy on my meter, and at some point it just stays inifinite.

This is what I built:

What I suspect is that when both relays are off, there is a very high voltage across the relays and an arc forms, due to the high Q of the coil. This does not happen when the 40 or 20M relays are activated. The antenna works more or less as expected when the 40 or 20M relays are active.

Could this be the problem? Could it be solved somehow?

I thought of using traps instead of relays to make the antenna "auto switching", but I'm not sure if traps would add more loss than the relays, or if they would whitstand the high voltages appearing on the coil.

## Answer (score 5, by Mike Waters)

It may very well be that the open contacts are arcing, and I'm betting that's what is happening.

Here are some possible solutions. How about using different relays that have less tendency to arc:

1. Open-frame relays with much wider contact spacing
2. Vacuum relays
3. Multiple relays in series

Another *possibility* might be that RF on the control lines may be activating the relays. Suitable RF chokes and bypass capacitors might help that.

**It's a myth that all traps are lossy**. If they don't get hot to the touch at sustained 100W or higher, then their loss is insignificant. Scroll to the bottom of https://www.w8ji.com/traps.htm:

3.) Do traps create noticeable loss, perhaps one dB per trap typically?

NO! Even the worst traps (coaxial traps) in the worse possible condition of operation are only 1.6dB loss for BOTH traps!

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/14682/multiband-vertical-antenna-not-working-as-expected, by hjf, Mike Waters. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
