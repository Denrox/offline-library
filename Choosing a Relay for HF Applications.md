# Choosing a Relay for HF Applications

*Tags: hf, electronics, equipment-design · score 5*

## Question

As part of my 20m transceiver build I'm looking for a relay to by-pass an RF amplifier in the front-end board. So, to be clear, that's after the 20m broad bandpass filter and before the RF mixer (it's a single-conversion superhet design).

Being the enterprising individual I am, I would normally scavenge for relays from old scraped radio gear. But, on this occasion I feel the need to invest in a few newly purchased relays to have on-hand. Specialized RF relays can be quite expensive, so I'm wondering if there are specifications to watch out for to help choose a relay from the general herd.

In my case, the coil voltage and contact voltage will be low, say 5 or 6 volts for the coil and a tiny voltage on the contacts. The required current handling capability will also be low. So, these parameters are a given.

However, beyond that I'm wondering what I should be watching out for? For example, my local parts supplier has a class of relays called "Signal Relays", which I assume are aimed primarily at the telco market. Here's one I pulled at random (sort of): https://www.farnell.com/datasheets/1683386.pdf. Are there any aspects or specifications of this particular relay that would make it a bad candidate for HF RF applications? Regards!

## Answer (score 3, by tomnexus)

Antenna tuners use fairly standard 250 V relays, so this would be a good place to start.

The SGC-230 is an example I know. This post has some nice photos of its relays. Smaller tuners use little black relays, if you scratch around for photos you might be able to read the specifications printed on the relays.

The SGC-235 is a claimed 400 watt tuner. If I recall correctly, in its output section, they used four relays in series for each switching element, to increase the breakdown voltage.

In a transceiver you have the advantage that the line is mostly well matched so the voltages are much lower than in a tuner. 20 watts in 50 ohms at 2:1 SWR is a peak voltage of about 60 V, or an RMS current of 0.9 A, so any mains rated relay should be able to handle that, and possibly small automotive relays too. You could always experiment to confirm that the breakdown voltage is high enough.

You may find a small reed relay that meets your needs. Here's an example at Digikey:  
  
It has 1 Amp contacts, 200 volts, and the coil takes 10 mA at 5 V! I see they recommend 10 watts total power, so you might need a larger one. If it matters to you, a reed relay should have less capacitance to ground, and definitely less series inductance than a regular relay, because of its geometry. It is SPST so you need two of them to switch T/R etc.

It will always be important not to switch the relay while the high power RF is turned on, but you can take care of that in software.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18512/choosing-a-relay-for-hf-applications, by Buck8pe, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
