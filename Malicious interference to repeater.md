# Malicious interference to repeater

*Tags: vhf, uhf, repeater · score 4*

## Question

Our local repeater is severely sabotaged by unknown parties. For example, broadcast radio transmissions are repeated. Other times someone will send a transmission, when a qso is in progress. Local authorities were informed but they apparently are ignoring this.

- What can be done?
- Could they be triangulated?

## Accepted answer (score 4, by rclocher3)

The first thing to do is to listen on the repeater's input frequency. If you hear the interfering signal on the input frequency, then you're probably dealing with deliberate interference; otherwise, you most likely have a technical problem.

If your problem is deliberate interference, then if I were in your shoes I would absolutely use radio direction finding (RDF) techniques to locate the source of the interfering transmission. I've done a few fox hunts, and the best simple technique technique is to travel around with a directional antenna (a yagi is nice but the antenna doesn't have to be that directional), an attenuator (your body in between the transmitter and your antenna sometimes works well enough for a weak signal), and a radio that ideally has a signal strength meter. An offset attenuator, containing an oscillator running at a few MHz and a mixer, offers better attenuation for this purpose much more cheaply than a typical laboratory attenuator.

Triangulation doesn't seem to work very well for precise location because of reflected signals, at least in the mountainous area where I live; it might work better in flat lands, but I'd think it's still not accurate enough to positively identify the building or vehicle with the antenna. With a directional antenna and a good attenuator, you could walk or drive a loop completely around the suspected location of the transmitter and prove that the transmission comes from inside the looped area.

Document your results thoroughly, hopefully with video, and turn your results over to the relevant government officials, which in the US are the FCC and Official Observers like @ZeissIcon says, and then you'll have done all that you can.

## Answer (score 3, by hotpaw2)

In the U.S., if you can foxhunt the interfering transmitter's location, then you might try sending this information to the ARRL: http://www.arrl.org/amateur-auxiliary

The ARRL has access to lawyers who can send a polite letter informing the source of the potential Federal law violation, and the potential monetary penalties for such. This kind of letter from a lawyer can often get the attention of the RFI source’s operator.

## Answer (score 2, by Zeiss Ikon)

One of my local repeaters has a sound bleed from the (very high power) TV transmission on the same tower, and all the repeaters I use exhibit signal problems and interference that might or might not be intentional. For instance, the same one that has the TV bleed also sometimes (re)transmits a Morse code station ID for another station. My Morse is pretty bad, so I'm not certain what the other ID is, and I can't depend on it to record or concentrate on it.

All of this is just part of using the 2 meter band. The FCC has limited funding and personnel for enforcement on individual repeater interference, and even if they're actively investigating, it sometimes takes *years* to trace down *intentional* interference, never mind something accidental.

Best I can suggest is either try to work around it, move to another repeater, or listen carefully for identifying information when the interference occurs and pass that information to your local FCC and Official Observer(s).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15939/malicious-interference-to-repeater, by mike, rclocher3, hotpaw2, Zeiss Ikon. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
