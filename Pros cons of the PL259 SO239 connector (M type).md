# Pros/cons of the PL259/SO239 connector (M type)?

*Tags: pl259-so239-connector, connectors · score 6*

## Question

What are the pros/cons of the PL259/SO239 connector (M type), and why is it used preferentially on civilian rigs vs military?

## Answer (score 8, by Walter Underwood K6WRU)

UHF connectors are cheap and easy to install. In all other respects, they are inferior to more modern designs like BNC or N connectors. The major uses of UHF connectors are amateur and CB equipment in the US.

BNC and N connectors are constant impedance and weatherproof.

The BNC connector handles as much power as a UHF connector (500V peak) and is easier to connect and disconnect.

http://www.amphenolrf.com/products/bnc.asp

The N connector handles more power (1500V peak).

http://www.amphenolrf.com/products/typen.asp

UHF connector specs:

http://www.amphenolrf.com/products/uhf.asp

This is a good overview of the RF characteristics of average-quality UHF connectors.

http://www.qsl.net/vk3jeg/pl259tst.html

Most of the time, UHF connectors will not cause any problems. If you have lots of connections, low-quality connectors, or are operating above 300 MHz, you should probably consider a more modern connector.

## Answer (score 6, by JSH)

I'm not sure what you mean by "M" type, but here are some points to address your question.

Pros:

- Well understood, and very old, design that most know how to work with;
- Numerous vendors continue to manufacture various connector topologies with the 'UHF Connector' specifications. Note the PL-259 & SO-239 are but two examples of many compatible part numbers that all mate with each other - the PL-258 is another example;
- Is somewhat mechanically robust;
- The ~4 mm center pin is quite large as connector center pins go and provides peace of mind for high power uses below 30 MHz.

Cons:

- Impedance-bump loss mechanisms become measurable above just 30 MHz and problematic above 50 MHz;
- Expiration of the original mil standard decades ago leaves interface specifications subject to some silly interpretations (example: the not-quite-compatible 'metric' UHF Connector);
- Absolutely no mechanical mechanism to deter ingress of moisture into the mating interface;
- Complete reliance on shell torque for shield path electrical continuity.

The inferior UHF connector continues to appear on ham and CB gear mostly due to market inertia. At this point, the devil you know is better than the devil you don't. Folks are simply accustomed in making good use of the UHF Connector where it makes sense to do so: <50 MHz with weatherization treatments applied by the user.

Another way to think of this is if ham and CB gear were suddenly made with BNC, TNC or N connectors, the cry heard throughout the land would be deafening..., but fun to observe.

### Reference

- https://en.wikipedia.org/wiki/UHF_connector
- http://www.hamradio.me/connectors/uhf-connector-test-results.html

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/142/pros-cons-of-the-pl259-so239-connector-m-type, by Timtech, Walter Underwood K6WRU, JSH. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
