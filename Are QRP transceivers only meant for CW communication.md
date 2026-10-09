# Are QRP transceivers only meant for CW communication?

*Tags: diy, cw, equipment-design, qrp · score 6*

## Question

I was just thinking about making a QRP transceiver, but are they only used for CW (Morse code) communication?

If it is so, can I modify a QRP for two way audio communication?

## Accepted answer (score 9, by Phil Frost - W8II)

QRP only means low power, often 1W or less.

While you could technically have a 1W SSB transceiver and call it QRP, the practical range of such a radio would be limited. It is much easier to hear a single tone over the noise than it is to hear a voice which has its energy spread over a wide range of frequencies. Thus we say CW is a more *sensitive* mode: it can be detected at a lower power.

Let's try some simulations with VOACAP. In each case, the simulation is for UTC 20:00 for a transmitter in Michigan, USA (marked by the red dot) on 30 meters. The simulated antenna is a dipole 10 meters above ground at both receiver and transmitter, and the transmitter power is 1W. The colors on the map indicate the probability that communication will be possible, depending on conditions.

Here's the simulation for SSB:

Looks like about a 40% chance of some contacts in an approximately 600 mile radius, and no chance of anything outside that. Neat, but not especially thrilling. On some days, it may be impossible to make contacts at all.

Now CW:

Within that primary 600 mile radius, the reliability is 90%. There's now some small chance of much longer range contacts, including Europe, Asia, and the Western US. While these contacts will require some good luck, for many people this is the thrill and challenge of QRP operation.

There are even more sensitive modes than CW. Here's a simulation for FT8:

And WSPR:

While digital modes like FT8 and WSPR are more sensitive than CW, they require a computer to operate. Since CW is simple to implement electronically, and requires no computer, and is still sensitive enough to feasibly complete QRP contacts, many QRP kits are CW. For digital modes there are some QRP kits that are essentially the analog bits of an SDR which then interface to a computer soundcard to perform modulation and demodulation available for under $50 USD.

## Answer (score 5, by Scott Earle)

A QRP transceiver is just a transceiver that operates on low power (usually less than 5 watts). If you look at the international Q Code, you will see that QRP simply means 'low power', and QRO means 'high power'.

However, what you are talking about is a QRP transceiver **kit**. Such kits are usually by necessity a fairly simple design, and the simplest transmitter is a CW transmitter. Transmitting CW is just a matter of keying on and off a signal from an oscillator and putting the signal through a power amplifier.

If you were to build an AM transmitter and receiver, those are also relatively simple - but nobody (I know, *some* people still use it) uses AM these days.

I have seen kits that are based around an SDR design, that do CW/SSB/AM/FM, and cost in the order of \$300-\$400. But when someone says they are thinking of building a QRP kit, this is not usually the first thing that comes to mind. An example of such a device is this one at \$209 for the 'kit' version.

Most CW kits are small, and only do CW because of the simplicity of the design. An example is the QRP Pixie kit at \$15.

Having said all this about the complexity of SSB versus the simplicity of CW (when it comes to transmitting, at least), when it comes to operating the radio the SSB one is obviously much simpler if you don't know Morse code.

If you were to learn Morse code, though ... then you can use the cheapest possible kits, and get all the benefits of a smaller, simpler device - with a lot of the complexity taking place in your own brain as you operate.

## Answer (score 4, by Brian K1LI)

CW is preferred over SSB for low power (QRP) operation because CW delivers better signal-to-noise ratio (S/N or SNR) than SSB. Because a CW signal occupies about an order of magnitude less bandwidth than an SSB signal, a narrower receiving filter can be used, which admits all of the signal and a much smaller amount of noise energy than a wider SSB filter.

While QRP is often considered to be synonymous with CW for the cost and SNR reasons already pointed out, the challenge of QRP SSB is not without its adherents; many "phone" contests attract QRP entrants and QRP may satisfy the needs and constraints of a particular situation. The BitX, KX2/KX3 and QSX transceivers are all fine examples of QRP SSB/CW transceivers. Amplifiers are also available from several suppliers to boost the output power as conditions warrant.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/13379/are-qrp-transceivers-only-meant-for-cw-communication, by Sumithran, Phil Frost - W8II, Scott Earle, Brian K1LI. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
