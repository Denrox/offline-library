# Using Earth as an RF ground

*Tags: grounding, earth · score 7*

## Question

I have built a simple ground plane antenna for 70cm with a connector, 4 radials, and one vertical element.

The RF ground is connected to the radials, and the RF is connected to the vertical.

It got me thinking, can the actual earth be used, because AM towers use it? IF I went outside, connected one end to a deep ground rod, and the other end to the vertical element, would the radiation be the same?

Is using the earth as an RF ground frequency specific, for example, don't use it above 30MHz?

## Answer (score 4, by Phil Frost - W8II)

AM broadcast stations do *not* use the Earth as ground for the antenna. To the contrary, they go through great expense laying huge radial fields precisely to avoid ground currents in the Earth. See these pictures of WTMJ on qsl.net. Here's one of them:

If you look closely, there is a copper mesh all around the antenna base. Around the base perimeter, there is a wide copper strap. You can't see the radials directly in this picture, but there are *a lot* of them: typically 120. They are attached to the copper strap around the perimeter. You can see a couple empty spools on which the radial wire was probably delivered (and by my estimation, there are many more such spools not in this picture).

Broadcast stations don't want antenna currents in the ground because the ground is not a great conductor. Resistive and magnetic losses in the ground would divert a significant fraction of electrical energy into warming the ground, but that energy would better be spent radiating a signal. When broadcasting at tens or hundreds of kilowatts, the associated currents can be quite huge, and the losses can get really big, really fast according to Joule's law: $P = I^2 R$.

An AM broadcast station will also have ground rods, but these are not for the operation of the antenna, and under normal operating conditions carry only negligible, ideally zero current. Their purpose is [lightning protection](How%20can%20I%20protect%20equipment%20against%20a%20lightning%20strike.md).

You *can* operate a vertical antenna without radials, and it is sometimes expedient to do so. It is however quite inefficient. Keep your radials, or use an antenna such as a dipole or loop which does not require a ground plane to operate.

## Answer (score 2, by Scott Earle)

Be aware that connecting your antenna to a good solid earth, and then connecting your radio gear to that antenna, and to the mains electricity supply *can* be a hazard in the event of a mains electrical fault.

Some properties in some parts of the world are wired using a 'protective multiple earth' (PME) system, and bringing a 'real' earth into the shack can provide a hazard if there is a mains electrical fault. (Basically, if the neutral wire becomes loose *and* there is a live-to-chassis type of short, then full mains current would flow through your antenna cable. Not likely to happen, but potentially very dangerous if it did. What WERE they thinking?!? My old house in the UK used to be wired like this until I rewired it myself.)

Check out this page http://en.wikipedia.org/wiki/Earthing_system and find out (really find out) how your property is wired, before bringing an earth into your shack.

I gather from your user profile that you are in the US, and I don't know if PME has ever been common practice in the US - but where safety is involved I would always recommend checking first.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1820/using-earth-as-an-rf-ground, by Skyler 440, Phil Frost - W8II, Scott Earle. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
