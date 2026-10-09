# Why are some electrical connectors silver plated?

*Tags: connectors · score 6*

## Question

Silver is pretty expensive. [Unlike gold](Why%20are%20some%20electrical%20contacts%20gold%20plated.md), it will tarnish in air. Why then would anyone bother to plate connectors with it? Does it have some unique electrical characteristics that make it useful?

## Accepted answer (score 7, by Phil Frost - W8II)

Silver has the highest conductivity of ordinary metals. It's also soft, which means the mating connectors squish together making a larger contact area, and thus lower contact resistance.

Low, consistent contact resistance is important in RF connectors, because any significant change in contact resistance will change the impedance of the connector, resulting in increased SWR and attendant losses.

Silver is also easy to solder, which makes soldered connections to silver plated connectors likewise reliable and superbly conductive.

Silver plating is not without disadvantages. Its softness also makes it not terribly durable. It's also prone to tarnish. However, in the RF connector applications where it is typically encountered, connectors are mated and unmated infrequently, and protected from water intrusion through an over-wrap of appropriate tape or such.

## Answer (score 5, by PCBonez)

(I'm a retired USN Electronics Tech.) This is what they taught us about why the Navy chooses silver over other options.

The oxides (aka tarnish) that forms on silver in air is nearly as conductive as the unoxidized silver. That is not the case with gold, nickel, tin, and so on. Thus when silver in a connection oxidizes you lose little conductivity and there is little increased resistance. That makes it ideal for corrosion friendly environments such as high humidity and/or salty sea air.

## Answer (score 3, by WPrecht)

It's a whole lot easier to solder silver plated connectors (specifically I am talking about PL-259s and the like) than the white metal used on the cheaper connectors. Some folks have great soldering setups and a lot of experience soldering. The rest of us are better off spending a little more to make assembling coax a lot easier and more reliable.

Electrically, of course, silver is an excellent conductor of both heat and electricity. But it is soft and as @Phil noted, tarnishes. According to one study I read, as long as the tarnish layer is particularly thick, the conduction surface still performs well.

Silver tarnishes in the presence of water if a polar salt or sulfur is available. Staying with the coax theme, protecting the connection from water intrusion (something you would want to do anyway) will probably mitigate the danger of tarnish reducing the current flow before something else happens to the cable (tree branches, squirrels, UV, etc.).

Reference: Overview of the Use of Silver in Connections

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1399/why-are-some-electrical-connectors-silver-plated, by Phil Frost - W8II, PCBonez, WPrecht. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
