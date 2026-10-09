# What kind of antenna has a spiral connected to a reflector like this picture?

*Tags: antenna · score 10*

## Question

The description on the antenna says it is used for satellite communication, but it was taken in 1984. Is this an antenna style that is still in use? What is it called? What kind of gain should be expected? Is this a style used primarily or only for communications in space? It appears to be a Yagi style antenna strapped to a parabolic, but I've never seen anything like this, so that conclusion may be completely wrong. Any information or links would be awesome.

## Accepted answer (score 8, by Juancho)

This is a helical antenna (Wikipedia link).

Configured in *axial mode*, these are commonly used in microwave satellite communications (below a few GHz) where you need high gain and circular polarization.

The circular metal part behind acts as a reflector element.

It is not only used for space communications. You find similar antennas for directional data links (using WiFi or similar modes).

## Answer (score 7, by Paul)

I've built a helical antenna for 430-440MHz receive from mostly ordinary household items. It was sufficient to receive the FO-29 downlink.

The dimensions of the helix are determined by the center frequency. I think the helix you posted is larger in circumference than mine, and thus would have a lower center frequency.

I believe gain is a bit lower than a yagi of the same length, but the helix is circularly polarized and so spin fading in satellite service is not an issue as it would be if a yagi or quad were used.

I chose a center frequency of 436MHz which gives wavelength of 68.8cm. From my notes I see that the design choices were 1.1 wavelengths for the helix circumference (75.7cm), and turn spacing to circumference ratio of ~0.23 (turn spacing 17.5cm). A generalization of Pythagoras' theorem can be used to give the wire length per helix turn as $\sqrt{75.7^2+17.5^2}=77.7\text{cm}$. I used white solid insulated 12 gauge copper wire marked every 1/3 of a turn with a bit of black wire tape to assist in attaching to the 3 supports.

These choices were influenced by various articles I had read on-line, but unfortunately I did not keep these links and the design notes are on notebook paper.

For the reflector you need a circular metal plate, such as a pizza pan and to support the wire helix of radius ~12cm I used three bamboo poles arranged in an equilateral triangle with ~21cm side length. Turn spacing is about ~17.5cm.

Bamboo is an irregular material. It is not straight, although you can find "approximately straight" pieces. The bandwidth of the helix is wide and the design fairly tolerant of error, allowing for somewhat imprecise construction. To increase the strength and rigidity of the support it is necessary to form some triangles with additional bamboo pieces. It becomes almost like making bamboo triangular tower.

A helix antenna does not present 50 ohms without a tuning or matching section. I remember reading somewhere that other builders had successfully used 1" copper strap, 1/4 wavelength, at an adjustable (but close) height above the reflector. Create a few threaded holes in the reflector using a tap and then you can use plastic bolts and scrap plastic (like a consumer discount card) to hold the copper strap at an adjustable height.

See also the QRZ page for KI6CQ

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1706/what-kind-of-antenna-has-a-spiral-connected-to-a-reflector-like-this-picture, by Jason Petrilla, Juancho, Paul. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
