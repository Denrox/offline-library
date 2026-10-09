# Do changing sidebands have their own sidebands?

*Tags: ssb, am, physics · score 4*

## Question

An amplitude changing carrier wave causes sidebands to appear next to it when viewed in the frequency domain. But if those sidebands themselves also change with time (because the modulating signal is not constant), shouldn't those themselves behave the same as a carrier wave and produce their own side bands? These secondary sidebands should then also have their own sidebands again, ad infinitum. Although the amplitude of those higher order sidebands will probably diminish exponentially. There are no laws of physics specific to carriers or sidebands, they all just follow the same laws of electromagnetic waves.

I read everywhere that the bandwidth of an AM modulated signal is twice the bandwidth of the modulating input. But according to the above logic, an AM signal should have an infinite bandwidth, in the same way that FM signals have. What am I missing here?

## Answer (score 2, by hobbs - KC2G)

Part of your problem is in thinking that "a changing carrier causes sidebands to appear next to it" is a physical cause and effect. The carrier doesn't *create* the sidebands, the sidebands *are* the changes in the carrier. They're two different mathematical descriptions of the same thing. It's just a mathematical fact that any physical or mathematical object that responds to a 1000Hz sine wave will also respond to a 900Hz sine wave that changes its amplitude with a period of 100Hz.

These secondary sidebands should then also have their own sidebands again, ad infinitum. [...] But according to the above logic, an AM signal should have an infinite bandwidth

Nope. You *could* look at things the way you suggest, with the sidebands viewed as an infinite collection of individual time-varying signals, and calculate the sidebands for each one. Each one would have its own bandwidth, but if you added them all up perfectly, you would find something funny: they would all cancel out! You would get the original signal, with zero energy outside of the original bandwidth. The sidebands don't have "lives of their own" to vary in any other way; they have this strict mathematical relation because of how they're created — or rather what they *are*, which is a signal with a certain center frequency and bandwidth.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20980/do-changing-sidebands-have-their-own-sidebands, by JanKanis, hobbs - KC2G. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
