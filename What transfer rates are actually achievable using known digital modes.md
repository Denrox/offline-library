# What transfer rates are actually achievable using known digital modes?

*Tags: digital-modes · score 12*

## Question

I've found all sorts of info concerning digital modes, sound samples, spectrum samples, but nobody ever cites what speed a given digital mode can reach.

Could anyone tell me more about that, or point me somewhere where I can find this kind of info, possibly in terms of kbps?

Also, what could be the maximum achievable transfer rate on short waves, specifically?

**Edit:** I thought that given the premises in first paragraph, it was clear that the heart of the question was about knowing the actually achievable transfer limits using known and used modes, not just understanding theoretical limits... (which is still a precious contribute though). Since it seems this did not come off so clear to some people, so I'm specifying it here and in title too.

## Accepted answer (score 5, by Phil Frost - W8II)

8VSB, as used ATSC digital television, has a gross bit rate of 32 Mbit/s in a 6 MHz channel.

802.11ac's fastest mode (1024-QAM) is capable of a gross bit rate of 1300 Mbit/s in a 160 MHz channel in each spatial stream, with up to 8 spatial streams. (I don't think any 8x8 MIMO APs are on the market yet, but surely someone's tried it in the lab.)

These are just two examples of ubiquitous digital modes which achieve high bit rates. There are undoubtedly modes used in scientific, military, and experimental applications which are orders of magnitude faster.

There is no upper physical limit besides that provided by the Shannon-Hartley theorem. As long as I can do any of:

- buy more spectrum,
- transmit with a higher power,
- use a more directional antenna to reduce received noise, or
- put the receiver and transmitter closer together,

then I can cram more bits into the æther. The reason it's not done in practice is that at some point there ceases to be a need (do most people have a need for Wi-Fi that's faster than their wired network?) or it becomes more economically feasible to run a wire.

## Answer (score 7, by user)

You are looking for the Shannon-Hartley theorem. Borrowing Wikipedia's summary, because it's better than what I can come up with:

In information theory, the Shannon–Hartley theorem tells the maximum rate at which information can be transmitted over a communications channel of a specified bandwidth in the presence of noise.

The Shannon-Hartley theorem states that the theoretical maximum bandwidth of a communications channel can be stated as:

$$ C = B \log_2{\left( 1 + \frac{S}{N} \right)} $$

where $C$ is the channel capacity in bits per second, $B$ is the bandwidth of the channel in Hz, $S$ is the average received signal power over the bandwidth, $N$ is the average noise power received over the bandwidth, and $S$ and $N$ are in the same unit (here, watts, or a multiple thereof). Notice that no communications channel in practice (not even a crystal-clear FM transmission or studio CD recording) is completely free of noise, so you will always have a $N > 0$. The theorem does *not* state how to achieve this channel capacity.

It follows from this that if you know the bandwidth, the signal strength received and the noise level, you can compute the maximum theoretical data rate. Transmission frequency does not enter into the picture, although it could place a practical limit on the achievable transmission bandwidth because antennas for lower frequencies tend to be more narrow-band due to employing various forms of matching networks which are not needed when antenna sizes are a considerable fraction of a full-sized antenna for the transmission frequency range employed.

Note that this allows you to compute the *maximum theoretical* data rate at which transmission is *somehow possible practically without errors*. This data rate will not always be achievable in practice, and in fact a lot of transmission mode research has gone into getting as close to the theoretical maximum data rate as possible. A transmission actually at the Shannon-Hartley limit would most likely look like white noise across the transmission bandwidth unless you know what to look for; compare ultra-wideband, or the signals used by late-generation dial-up telephone modems.

Since a large factor in the equation is the received signal-to-noise (S/N) ratio, you can increase the achievable transmission rate within a given bandwidth "simply" by increasing transmitter output power, or antenna gain. Conversely, in situations where bandwidth is extremely limited, such as on 136 kHz, the transmission bandwidth is reduced by reducing the data rate. In situations where signal is hard to come by, such as in communication with faraway space probes or again on 136 kHz, the data rate is reduced in order to match the available S/N ratio.

Wikipedia has several examples applying the theorem that you may be interested in.

## Answer (score 3, by JSH)

For what it's worth, I made a graph of a token selection of amateur digital modes with bandwidth vs. frequency (as wavelength) to provide a rough sense of the digital scene.

This came from our feasibility study for a new packet system in the Virginia area.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5240/what-transfer-rates-are-actually-achievable-using-known-digital-modes, by red-o-alf, Phil Frost - W8II, user, JSH. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
