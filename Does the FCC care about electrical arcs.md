# Does the FCC care about electrical arcs?

*Tags: united-states, legal, fcc · score 6*

## Question

There are a lot of videos on YouTube from people who have built high voltage sources and are sending electric arcs from one place to another. Although they have no intention to emit radio waves, they are probably creating a lot of noise. I have known DC motors to be bad just because of arcing across the commutator, and it is not too hard for someone's science project to send foot-long bolts flying through the air. Does the FCC have any regulations limiting that practice?

## Accepted answer (score 10, by hobbs - KC2G)

Absolutely! FCC Part 15 defines three broad classes of devices:

*Intentional radadiator.* A device that intentionally generates and emits radio frequency energy by radiation or induction.

*Unintentional radiator.* A device that intentionally generates radio frequency energy for use within the device, or that sends radio frequency signals by conduction to associated equipment via connecting wiring, but which is not intended to emit RF energy by radiation or induction.

*Incidental radiator.* A device that generates radio frequency energy during the course of its operation although the device is not intentionally designed to generate or emit radio frequency energy. Examples of incidental radiators are dc motors, mechanical light switches, etc.

and a few other definitions that we'll want for later are

*Radio frequency (RF) energy.* Electromagnetic energy at any frequency in the radio spectrum between 9 kHz and 3,000,000 MHz.

*Harmful interference.* Any emission, radiation or induction that endangers the functioning of a radio navigation service or of other safety services or seriously degrades, obstructs or repeatedly interrupts a radiocommunications service operating in accordance with this chapter.

Although most of the time when we talk about Part 15 we're thinking about unlicensed intentional radiators, or unintentional radiators, incidental radiators are *also* regulated. 15.1(a) says

This part sets out the regulations under which an intentional, unintentional, or incidental radiator may be operated without an individual license.

If it makes radio waves between 9kHz and 3THz, intentionally or not, it needs to either follow the rules in Part 15, or be licensed according to the rules in some other Part.

So which sections of Part 15 apply to incidental radiators? Well, almost none of them. Most of them are dedicated to specific types of intentional or unintentional radiators. But one section that applies to *all* kinds of radiators is section 15.5, "General conditions of operation", which contains some text that you've probably seen on a label somewhere:

(b) Operation of an intentional, unintentional, or incidental radiator is subject to the conditions that no harmful interference is caused and that interference must be accepted that may be caused by the operation of an authorized radio station, by another intentional or unintentional radiator, by industrial, scientific and medical (ISM) equipment, or by an incidental radiator.

(c) The operator of a radio frequency device shall be required to cease operating the device upon notification by a Commission representative that the device is causing harmful interference. Operation shall not resume until the condition causing the harmful interference has been corrected.

So there are no specific frequency bands, field strength measurements, or other technical standards prescribed (as there are for intentional and unintentional radiators). The conditions for operating an incidental radiator are that you don't cause harmful interference to licensed users (navigation, public safety, broadcast, hams, or anything else), and that upon receiving proper notification that your device is causing interference, you stop using that device until the interference is mitigated.

Also relevant is section 15.23, "Home-built devices" which states

(a) Equipment authorization is not required for devices that are not marketed, are not constructed from a kit, and are built in quantities of five or less for personal use.

(b) It is recognized that the individual builder of home-built equipment may not possess the means to perform the measurements for determining compliance with the regulations. In this case, the builder is expected to employ good engineering practices to meet the specified technical standards to the greatest extent practicable. The provisions of §15.5 apply to this equipment.

which says that if you build it yourself, you're exempt from certification requirements but you're *not exempt from following the rules* about interference.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15694/does-the-fcc-care-about-electrical-arcs, by Display Name, hobbs - KC2G. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
