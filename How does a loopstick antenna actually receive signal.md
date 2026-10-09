# How does a loopstick antenna actually receive signal?

*Tags: antenna, ferrite · score 6*

## Question

Around 1970, I acquired a little transistor radio (powered by 4xAA cells, 6V) that had no external antenna. Inside the back panel (which opened to allow replacing the battery cells) one could see the loopstick antenna, just a ferrite rod with a lot of turns of fine wire that connected to the circuit board. I used to get KGO AM (IIRC around 800 kHz), from San Francisco, in central Washington state at night with this little receiver.

I've always wondered how a loopstick like this can act as an antenna. The wire is wrapped tight (the coil length I recall from this radio was around half an inch, close wound; others I've seen that were coming apart seemed to be wound in layers, suggesting hundreds of turns) on a paper sleeve around the ferrite. The antenna is only slightly directional; the weakest of stations would fade when the radio was rotated 90 degrees from where they were strongest.

What I picture in my head is that the ferrite permeates with the magnetic component of the signal to be received, and its fluctuating field induces a voltage in the wire coil which is then amplified before going into the IF stage.

Am I understanding this correctly?

## Accepted answer (score 8, by Phil Frost - W8II)

The basic operation can be understood by Faraday's law of induction. Any loop of wire will exhibit an electromotive force proportional to the rate of change of magnetic flux encircled by it. Since any electromagnetic radiation consists of both a time-varying electric and magnetic field, any loop of wire can theoretically be used as an antenna. The trouble is getting the EMF to be large enough to be feasibly detected.

To maximize the EMF, the ferrite rod collects and concentrates the magnetic flux from nearby areas. Just as a copper rod concentrates the electric field because it has high conductivity, the ferrite rod concentrates the magnetic field because it has high permeability.

Each turn of wire around the core then exhibits an electromotive force (EMF) according to Faraday's law. One turn would work, but considering the entire coil is many turns in series, the EMF of each adds together.

So between the high permeability of the core and the many turns around it, the antenna has a much higher effective aperture than its small size would suggest.

This seems like a great deal, so why then are these antennas seen pretty much only on broadcast AM receivers? A loopstick antenna works well at relatively low frequencies, perhaps up to a few MHz. Above that, and hysteresis losses in the ferrite become significant enough to offset the advantages of the design.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18564/how-does-a-loopstick-antenna-actually-receive-signal, by Zeiss Ikon, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
