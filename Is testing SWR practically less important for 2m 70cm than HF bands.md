# Is testing SWR *practically* less important for 2m/70cm than HF bands?

*Tags: hf, vhf, uhf, impedance-matching · score 4*

## Question

Totally new amateur operator and I've noticed that a lot of material e.g. Your Tube videos, blogs, forums when discussing metering VSWR mainkly seem to be talking about HF bands. I also see fewer VSWR meters that cover the VHF/UHF bands in stores.

In PRACTICE is metering and adjustimg VSWR less of an issue for the higher frequencies?

I understand that for optimal performance you're going to want to meter and tune your antennae for each frequency, but it appears to this obsever that measuring VSWR and tuning antennas or matching impedance is less common on the VHF/UHF bands and from this I infer that VHF/UHF bands may be less sensitive to VSWR issues or perhaps there are fewer VSWR issues in those bands?

## Accepted answer (score 6, by tomnexus)

I would say in practice it is less important because hams use different types of antennas for HF and for VUHF.

At HF, the same antenna is often used for many bands. The bands have large fractional bandwidth. Antennas are often simple wire, very thin compared to wavelength. And finally, because the wavelength is quite long, they are often too short for the band of interest, and very close to the ground. All of these factors mean we can't buy an antenna that simply works, or tune it once. We often have to use an antenna tuner to adjust the antenna impedance at a particular operating frequency, and we need an SWR meter to see how we're doing.

At VUHF, the antennas are more often full size, single band, tuned once, parhaps at the factory (base collinears or yagis) or during installation (whips on cars), and then working well after that. If they do need tuning, it's done occasionally by adjusting the antenna dimensions, not with a tuner. This means we don't need to regularly measure the SWR of VUHF antennas. It is useful to check it though, as high SWR might indicate a problem with the antenna or feed.

One counter-example would be an HF single or multi-band beam, designed and tuned for a few specific frequencies. These will have consistent, low SWR at these frequencies, no need for a tuner or to check SWR regularly.

## Answer (score 2, by Brian K1LI)

Welcome to hamSE, Jason.

Assuming you can match your rig to the load at the shack end of the transmission line, the importance of SWR depends primarily on how much transmission line loss affects your operations and how much money you're willing to spend on transmit power amplifiers, receive preamplifiers and lower-loss transmission lines to compensate for it.

AC6LA describes the calculation of transmission line losses, including a thorough analysis of why the assumptions built into some of the available tools may produce inaccurate results. His program Transmission Line Details breaks losses down into contributions from conductor, dielectric and reflection. This detailed picture tells you exactly how important SWR will be to your operation.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18146/is-testing-swr-practically-less-important-for-2m-70cm-than-hf-bands, by Jason Tan, tomnexus, Brian K1LI. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
