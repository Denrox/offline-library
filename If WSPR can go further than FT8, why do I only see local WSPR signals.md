# If WSPR can go further than FT8, why do I only see local WSPR signals?

*Tags: ft8, wsjt-x, wspr · score 4*

## Question

I've been scanning through the bands using WSJT-X to pick up FT8 and WSPR. Using a VHF discone, I decode messages from nearly 10,000 km away, consistently, when listening for FT8. But when switching to WSPR I'm lucky to get anything even 1/10 that distance. This is using the exact same setup, and I've tried a variety of HF bands. Why is that? My understanding of WSPR was that it should be legible at far greater distances than FT8.

## Accepted answer (score 6, by hotpaw2)

My guess, looking at WSPR reports, is that, on average (median), WSPR beacons are transmitted at power levels maybe in the range of 10 to 30 dB lower than the median of FT8 transmissions. e.g. 20 dBm Raspberry Pi hat vs. 37 dBm QRP SDR, or 30 dBm WSPR appliance vs 50+ dBm desktop transceiver and/or QRO amp, as bracketing examples.

So the reported 10 dBm advantage of a WSPR beacon (usually just left running on auto-pilot) is swamped by a typical range of 10 to 30 dBm higher power used by people actively trying to add FT8 contacts (and DX contacts) to their logbooks. Maybe even rotating their antennas in your direction for even higher radiated gains.

And given a constant receiver noise floor and constant propagation attenuation per unit distance (neither of which are actually constants), 20 dB of increased power corresponds to 10X greater communication range (for similar coding). So if you are seeing a 10X range difference, that corresponds finding the Tx power on the FT8 signals you receive to be 30 dB greater that the WSPR signals you receive.

Another possibility is that your RF noise floor is high, as some people get reports for their milliWatt WSPR beacons from 1/4 of the way around the planet, or farther. So, due to your noise floor, you can only hear high powered stations, and not any milliWatt beacons. So your statistical sample set has an artificially truncated bottom end.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17455/if-wspr-can-go-further-than-ft8-why-do-i-only-see-local-wspr-signals, by directedition, hotpaw2. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
