# Looking for criticisms on my VNA-like SWR meter I am designing

*Tags: diy, impedance-matching, impedance, equipment-design, swr-meter · score 4*

## Question

I am in the process of building a SWR meter with VNA-like features. I'd be really interested to hear from fellow hams any input, suggestions, or tips they have regarding this before I go get it mass produces. I'll share the schematic and technical details but I am also looking for feedback just in terms of usability or features or any criticism really

So basically I'm building an Arduino shield where the primary use case is to be a SWR meter with an LCD display (not depicted here as that is a separate shield). But it provides all the functions of a Vector Network Analyzer (VNA) and as such goes well beyond your typical SWR meter.

Because the primary use case here is to act as an inline meter on a transmission line with an existing transmitter its not designed as a typical VNA would be using mixers. The only thing it doesn't have that a VNA would have is a function generator, as it relies on the transmitter to do that, and the directional coupler would be external. However I have designed it in a modular way so not only can the directional coupler be swapped out for one the user prefers or more suited for their setup, but it can also be configured to work more like a traditional VNA as well. With the additional of an additional shield with an in-built low power directional coupler and a sine wave generator it would be possible to also pop on this other shield and effectively have a handheld VNA instead. Being modular there are also several other possibilities for how this device can be configured including as a remote SWR meter so you can have a meter at both the transmitter and the antenna to properly calculate feedline loss, or to understand how the complex impedance of your antenna changes with frequency.

Because of its role as an in-line meter in an existing antenna system it also provides functions a traditional VNA would not, specifically the ability to analyze properties of the transmitter such as accurately determining the true RMS under modulation or precisely determining the frequency the transmitter is transmitting on. Perhaps in the future I may add other features as well either in software of hardware.

Some specifications:


Operates 1 MHz to 500 MHz


Can measure input signals from -52dBm to 0dBm (adjust external directional coupler and attenuator to handle any power transmitter).


Inputs are 50 ohm matched but if building yourself you can switch out different resistors to match different impedances

Note: This is an open-source project and free for anyone else to replicate my work. At some point I may sell kits and/or the printed PCB to people to make it cheaper than needing to pay to get your own PCB printed. So I'd like to make sure if I provide PCBs they have been scrutinized and tested first.

The link to the projects source can be found here for anyone who wants to access the actual files.

https://git.qoto.org/roes/roes-hardware/

Here is a picture of the schematic:

Here is an older picture of the UI in demo mode. The data on the screen is intentionally bogus, and the glitches in the rendering have since been fixed.

This is a four-layer board so you'll have to see the GIT repository if you want to pick apart my layout in detail. But for now I will share the front side and back side so you can at least get a sense of my placement of the chips and my use of shielding.

Front:

Back:

## Accepted answer (score 3, by pgibbons)

I think the problem you will run into is that people will want this to be plug and play. They may not have a directional coupler, or know or feel like to calibrate it and all that other stuff. Even if they do it, they may wonder if they did it right and if the reading will be accurate or not. I think you will need to handle this part in your design and support much greater power handling. Make it a pass-through, one connector on each side and that's it.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17271/looking-for-criticisms-on-my-vna-like-swr-meter-i-am-designing, by Jeffrey Phillips Freeman, pgibbons. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
