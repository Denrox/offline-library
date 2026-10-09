# Does an antenna pick up signals of all frequencies or only its resonant frequency?

*Tags: antenna, antenna-theory, antenna-tuner, resonance · score 4*

## Question

I heard that an antenna picks up signals of all frequencies, and then these signals are filtered by a circuit using an inductor and capacitor, and that this is how a radio is tuned.

However, I also heard that an antenna has a resonant frequency, and that this is determined by its length.

- Does this mean that it will only pick up signals at or near to its resonant frequency?
- What then is the point of a tuning circuit?
- And what about transmitting antennas? Will they naturally transmit signals at their resonant frequency without the need of a tuner?
- If antennas can receive signals of any frequency, and the tuning  
circuit filters out all the unwanted frequencies, why is it  
necessary to design antennas with a specific resonant frequency? Couldn't we use an antenna of any resonant frequency and just use  
the tuning circuit to get the frequency we want?

## Answer (score 4, by hotpaw2)

All frequencies.

**But**, there's a big difference between "picking up" a signal, and how well an antenna will "pick up" a signal.

Any metal object will pick up almost any RF signal at almost any frequency (I've used unbent paperclips for a wide range of Rx testing.) But the problem in that certain antenna geometries might pick up a signal too weakly, when compared to receiver noise or the local ambient RF noise floor, to detect. Other antenna's have better gain and directionality towards the frequencies and signals of interest.

But lots of people use random length wires to SWL (short wave listen) all the way from MF (and lower) to VHF, even though the length might be far from resonance at the shortwave frequencies received.

With transmit antennas, there is a similar problem regarding efficiency and providing a proper output load for the transmitter. But people have accomplished DX contacts using old incandescent lightbulbs for antenna's (possibly also radiating RF off of the random lengths of feed lines, power cords, and ground lines connected to the transmitter.) Or accomplished QSOs with poorly shielded dummy loads. But a proper half-wave dipole well above ground level will probably radiate a signal even farther with less power.

## Answer (score 2, by user10489)

It depends on the antenna. Some antennas are very broad band and do more or less pick up every frequency, but may have more sensitivity on some than others. Typically, it would pick up more on its resonant frequency and harmonics of that, but there may not be a lot of difference across the spectrum.

Some antennas act like RLC circuits themselves, and act like filters. As a rule of thumb the more complicated the antenna, the more narrow band it is, but there are many factors that affect antenna bandwidth. Most antennas are a compromise between factors, and bandwidth is one of those.

The point of an antenna tuner is in part to enhance this effect, but more typically it is used to impedance match the antenna for transmission where it is more critical, mostly to keep reflections from impedance mismatches from overheating the radio. But the radio itself has a completely different "tuning circuit" whose purpose is to narrow the bandwidth down to a single channel and frequently shift it to a new frequency (heterodyne) to make further processing easier.

The small loop antenna has a bandwidth so narrow (~100KHz maybe) that it would be nearly useless without the tuning capacitor integrated into the antenna. This is an extreme case of the antenna acting like a filter.

## Answer (score 2, by rclocher3)

Your question is similar to others that have been asked here before. Here are a few:

- Does a resonant antenna work better than a non-resonant antenna?
- What exactly makes an antenna resonant?
- [What is the advantage of making an antenna resonant?](What%20is%20the%20advantage%20of%20making%20an%20antenna%20resonant.md)
- [What is the relationship between SWR and receive performance?](What%20is%20the%20relationship%20between%20SWR%20and%20receive%20performance.md)
- [Why do I need to tune an antenna?](Why%20do%20I%20need%20to%20tune%20an%20antenna.md)
- [What is an antenna tuner? Why bother with resonant antennas in the first place?](What%20is%20an%20antenna%20tuner%20Why%20bother%20with%20resonant%20antennas%20in%20the%20first%20place.md)

An antenna being resonant means that its impedance is purely resistive, and has no reactance. This happens when the antenna is a half-wavelength long electrically for dipole antennas, or a quarter-wave long for vertical antennas. Typically antennas are designed to have low SWR near the point of resonance, but not always. Whether an antenna is resonant or not really isn't important to hams most of the time; what's usually more important is the SWR of the antenna at the bands or frequencies you're interested in.

If the antenna has a low SWR, that means that it will be easy to couple to the transmitter. Most HF transmitters can handle a mismatch of 2:1 or better without the need for a transmatch (antenna tuner). Receivers typically don't much care about the antenna being resonant. Most ham receivers hear better when the SWR is low, but usually that's a small effect because receivers have plenty of gain. Because the effect is usually small, antennas typically don't do much receive filtering of their own.

The point of a tuning circuit is typically to keep the SWR low on a coaxial feed line for transmitting, because coaxial cable tends to be very lossy at high SWRs. Also, most solid-state transmitters are sensitive to SWR, and will automatically reduce power if the SWR is too high. A tuning circuit is typically not needed if the SWR is lower than 2:1. Many antennas are designed to have an SWR in that range for all the frequencies of interest. A transmatch (antenna tuner) can extend the useful frequency range for an antenna, or it can make a multi-band HF wire antenna practical.

Transmatches (antenna tuners) can be great problem-solvers, but it's important to note that just because the SWR at the transmitter is 1:1 doesn't mean that power isn't being lost in the feed line or in the transmatch, or that the antenna is working efficiently. My HF transmatch can tune up a 3' (1 m) piece of coax with nothing connected to the other end, but that piece of coax is a terrible antenna!

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20525/does-an-antenna-pick-up-signals-of-all-frequencies-or-only-its-resonant-freque, by Urthona26, hotpaw2, user10489, rclocher3. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
