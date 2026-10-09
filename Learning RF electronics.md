# Learning RF electronics

*Tags: receiver, electronics · score 7*

## Question

I've been studying and building test circuit for actually several YEARS now, so far with no success. It sounds ridiculous but it's true.

So I feel like I have a good understanding or RLC circuits, I can calculate phase shifts and impedances etc., I am good with simplifying series/parallel combination circuits, good with transistor and NFET amplifiers, and good in working out input and output impedance (in this case not a good grasp of complex impedance).

The problem is I feel like I need a real Elmer at this stage to help me put it all together, on my own I'm getting nowhere.

The trouble is that the hobby has changed, courses have changed... all the courses I looked at teach legality, legislation, etc. While this may be very important for end users to follow these guidelines and be licensed to do so for me that's not where the 'passion' of the hobby is.I'm just trying to receiver but not transmit so I won't be annoying anyone (although I know some receivers leak RF from their LO).

The problem is that I'm in a remote area so it's unlikely I'll find someone locally to learn from. Is anyone aware of online resources where I can get that sort of learning? I don't need links to the legal and legislative aspect of the hobby, that there's already tons of, I'm asking people who are passionate about electronics, not law.

EDIT undone for clarity

## Accepted answer (score 4, by Glenn W9IQ)

I am always happy to hear of someone that is trying to better their understanding and education. Congratulations and welcome.

I agree that it is nice to have someone to personally talk with but let's start with some basics.

To do proper prototyping and to understand where you are going wrong with RF circuits, you need some basic test equipment. A DVM, a wide bandwidth oscilloscope, an RF generator, a variable power supply, and an RLC meter are the minimum. Then you need a nice assortment of components from which you can draw - resistors, capacitors, transistors, standard IC's, etc. You also need a good library of technical information - manufacturer data sheets, text books, and on-line help are rich sources of information with the catch that many Internet sources can send you down the wrong path. So without trying to sound old school, some good books are essential. Consider publications from the ARRL, such as the Handbook, or from RSGB as good sources of practical, RF information.

If you are serious about RF design, you need to tackle complex math. It really isn't too difficult once you get a few basics down - or as I have told students - it really is not that complex once you master the basics! Excel now has fairly good complex math support so that you can play with basic concepts and formulas to confirm or re-enforce your learning.

In a similar vein, you need to be comfortable with logarithmic math. RF electronics easily achieves a system power gain of 1,000,000 and more. It gets tiring to keep writing all of those zeros, decimal places, and exponents. The dB should be your best RF friend.

If you haven't already done so, assemble a few RF kits to deepen your understanding. A receiver, a transceiver, or even a kit for some test gear that you need are great ways to learn by hands-on observation and experimentation. Start with a few simple kits and work your way up to more complex kits.

An alternative to kits is to build circuits based on the datasheet examples from IC and transistor manufacturers. Many times their sample circuits are nearly complete designs that allow you to learn from the assembly and testing process.

Once you have a few kits under your belt, come up with a usable, practical circuit that you would like to design. Having a purpose for the circuit provides more motivation and clarity than simply 'trying something'. But like the kits, be realistic with your first few ventures. Don't shoot for a DSP receiver but rather something like an RF field strength meter. Then work your way up to the big goal.

Don't hesitate to use this forum to ask questions. There are a lot of bright and experienced people here that are more than willing to help. So do some research and if you come up dry or uncertain, come here for answers (but not opinions).

You may find some local resources in the form of 'maker' events or ham radio clubs in your area. Attend ham radio/electronic 'swapfests' in your area. You can buy parts for your parts draws cheaply and often meet like minded people. Many university professors are more than willing to take a non-student under their wing when they see a truly motivated individual. I got my start in electronics in grade school thanks to a university professor who was willing to correspond with me (yes, the pre-email era) on digital circuit topics. My first question for him was to ask how a JK flip flop worked. Thanks to his generosity, I had designed and built a 50 MHz frequency counter by my freshman year in high school. It was a powerful lesson for me and I have since followed in his path. I was also blessed to have a great ham radio mentor, Walt Fitting - W9OI, who was a constant source of inspiration and motivation.

Finally, if all else fails, seeing that you are in New Zealand, I would be willing to come down for say a month or two to personally tutor you. Or so my wife tells me as she compiles her travel itinerary. Wait... I am getting an update... apparently it will take 3 months to properly tutor you.

## Answer (score 4, by Brian K1LI)

I heartily recommend the three-volume set, "Hands-on Radio Experiments," by Ward Silver, N0AX. These books organize Ward's excellent *QST* columns to develop knowledge in specific areas.

Ward introduces the free *LTSpice* circuit simulator in volume 2. This is a great way to delve into virtually every aspect of electronic design without the expense of building a lab. I have used *LTSpice* to better understand published circuits and to develop my own low-cost, high-power, SSB transmitter.

I have Elmered younger and older students alike with the Snap Circuits SC-300 home electronics learning lab. It's also a good complement to *LTSpice*.

Hands-on Radio Experiments, volumes 1 and 2

Hands-on Radio Experiments, volume 3

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/11850/learning-rf-electronics, by Glenn W9IQ, Brian K1LI. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
