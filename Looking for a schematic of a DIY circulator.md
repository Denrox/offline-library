# Looking for a schematic of a DIY circulator

*Tags: filter, duplexer · score 7*

## Question

I would like to build a simple HF, VHF or UHF circulator to get a better understanding of how these devices work. Sadly at the moment I'm unaware of any articles or books that provide corresponding schematics and description. Could you please recommend a good source on the subject or maybe share a schematic?

## Answer (score 9, by Marcus Müller)

Puh! That's a big one you're planning:

Most circulators are *passive, magnetic material circulators*:

These circulators are basically a three-port resonant cavity in a cylindric shape, where the cavity is filled with ferr*i*magnetic material, typically special ferrite disks.

The electromagnetic properties of magnetized ferrite are used to break up the geometric symmetry – now energy flows more in one direction (say, counterclockwise) than in the other (cw).

Thus, the magnetic properties of the circulator material become pretty crucial for it to work at all; it sounds like a bit of a daunting task to build one from scratch, but since you're not afraid to do so:

Pozar's *Microwave Engineering* has a short section on magnetic circulators (section 9.6 in the third edition); it's rather advanced.

corresponding schematics

Not being a component that is representable in electronics, but only in field/wave propagation terms, there's no electric schematic that you could find.

Here's a drawing of how a stripline Y-junction circulator might be built, from a book titled *Ferrites at Microwave Frequencies*.

You'll notice that circulators are inherently frequency-selective due to their cavity nature. So, you'll need the tools to build a well-defined cavity for your frequencies of interest, access to the raw ferrimagnetic discs, the ability to fix, shift them very finely, and potentially to rework them without them losing ferrimagnetism.

When you put all this into a case that holds the elements into place and ensures all the dimensions, you end up with something like source pdf:

## Answer (score 5, by Mike Waters)

A circulator can probably be constructed from coaxial cable. However, you will also need ferrite and magnets.

From https://wa8dbw.ifip.com/Circulator.html :

A circulator is best thought of as a "Magic Box" containing three transmission lines spaced 120 degrees apart. These transmission lines are placed between two disks of ferrite material. On the other side of the ferrite is a non-ferrous ground plane and then a magnet followed by a ferrous pole piece that shields the unit from external magnetic fields.

Usually on circulators designed for the VHF/UHF (50 - 512 MHz) frequencies will have a means of tuning each transmission line so that insertion loss and isolation can be optimized at the desired center frequency range.

From http://www.e-meca.com/rf-microwave-blog/isolator-circulator-basics:

An RF circulator is a three-port ferromagnetic passive device used to control the direction of signal flow in a circuit and is a very effective, low-cost alternative to expensive cavity duplexers in base station and in-building mesh networks. Examples of both applications will be covered later in this article.

To understand how these components control the signal flow, think of a cup of water into which you place a spoon and stir in a clockwise motion. If you sprinkle some pepper into the cup and continue to stir, you will notice that the pepper easily follows the circular motion of the water. You can also see that it would be impossible for the pepper to move in a counterclockwise direction because the water motion is just too strong. The interaction of the magnetic field to the ferrite material inside isolators and circulators creates magnetic fields similar to the water flow in the cup. The rotary field is very strong and will cause any RF/microwave signals in the frequency band of interest at one port to follow the magnetic flow to the adjacent port and not in the opposite direction.

**Description of *circulator***, from Wikipedia article:

A circulator is a passive, non-reciprocal three- or four-port device, in which a microwave or radio-frequency signal entering any port is transmitted to the next port in rotation (only).

Here's a **circulator using transmission lines**. Per Marcus Müller:

... It's really nice, kind of a circular bucket-brigade device made of "signal storage" delay lines. That's an elegant active way to build a circulator.

This **circulator schematic** from VA3IUL uses CLC406 op-amps and covers DC to 100 MHz.

Found at the YO3DAC VA3IUL Homebrew RF Circuit Design Ideas website.

Here's a circulator using **no magnets** based on parametrically-modulated coupled-resonator loops behind a $9 paywall.

I found that by Googling homemade rf circulator -vector. There are information and construction articles and even a video there. (I did not follow many of those links in the Google search results.)

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16075/looking-for-a-schematic-of-a-diy-circulator, by Aleksander Alekseev - R2AUK, Marcus Müller, Mike Waters. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
