# Can I use a 1:1 current balun to feed a 1/4λ vertical?

*Tags: balun, vertical-antenna, choke-balun · score 4*

## Question

I have an LDG RBA-1:1 current balun, and I was wondering if it behaves as a common-mode choke that I can use for a ground-mounted quarter wave vertical w/ 16 radials.

The other choice I have is a 4:1 unun (also LDG), but I think that would cut down my impedance quite a lot.

Unfortunately, I currently do not have an antenna analyzer so that I can properly measure the performance.

## Accepted answer (score 4, by Cecil - W5DXP)

Looking at the pictures of the LDG RBA-1:1, it looks like the answer is yes. It is just a choke that can be used as either a balun or unun. Note that if the vertical has a resonant feedpoint resistance of 35 ohms, a 50 ohm unun will transform the 35 ohms to a slightly inductive impedance which will decrease the resonant frequency at the unun input terminal. Or if you want a perfect SWR, you can use a shunt capacitor at the unun input terminal.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/14459/can-i-use-a-1-1-current-balun-to-feed-a-1-4l-vertical, by Rimio, Cecil - W5DXP. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
