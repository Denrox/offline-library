# How to choose a coaxial cable

*Tags: coaxial-cable · score 5*

## Question

How do you know which coaxial cable to choose for your application?

For instance; I require a cable that has a 50ohm impedance, an operating frequency of 2.4GHz, length of 100mm, and needs to be semi rigid to support the elements of the antenna I am going to make. Requires a RP-SMA connector.

The antenna is going to be used on a video transmitter if that is of importance

What would be a suitable cable and why?

Previously I have used RG316 then gained rigidity with wire strapped to the outer.

## Accepted answer (score 5, by Phil Frost - W8II)

Your primary concerns are likely to contain:


Characteristic impedance ($Z_0$). This is usually dictated by the other components in your system and is usually $50\Omega$ for amateur radio applications. $75\Omega$ components are also not difficult to find due to their widespread application in TV.


Loss. At a given frequency, a given cable will have some loss figure, usually given in units of decibels per unit length. Losses increase with frequency, so a cable that might work fine at 960 kHz wouldn't be much more than a heater at microwave frequencies. Because loss is proportionate to length, at shorter lengths a lossier cable may be more acceptable.


Power handling. Several things limit this. One is loss as above: losses become heat, and excessive heat will damage the cable. The cable must also be able to withstand the voltages associated with the power without suffering dielectric breakdown.


Physical characteristics. Do you need a cable rated for direct burial? UV exposure? If you need a tight bend radius, you probably need a smaller diameter cable. Flexible or rigid? Will the cable need to withstand repeated bending from handling, or is it in a permanent installation? Will people potentially step on the cable? Compatibility with connectors can be a concern: clearly you will not be attaching an SMA connector directly to a 2-inch hardline. Fortunately, coax cables tend towards standard dimensions and thus compatibility with connectors is usually not difficult. For example, there are many cables that have the same physical dimensions as, and accept the same connectors as RG-58.


Cost. The materials and manufacturing techniques used to achieve any of these desirable properties cost something. A good engineer is one that selects the cheapest solution which performs acceptably.


Availability. Can you buy it at the electronics store at the corner, or must it be ordered? Is it in stock? Is it sold by the foot or by the spool?

With these concerns in mind, decide which are most important for your application, then browse distributor and manufacturer catalogs until you find something acceptable. The catalog will specify a few key parameters such as loss at a couple frequencies, basic construction, cost, and size. Pick a few candidates and then read the datasheets, which specify all the parameters in much more detail. Frequently they will also contain helpful information such as compatible connectors, applications to which the cable is especially well suited, etc. Then make your choice.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1810/how-to-choose-a-coaxial-cable, by Ben, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
