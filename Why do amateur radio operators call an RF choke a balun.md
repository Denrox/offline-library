# Why do amateur radio operators call an RF choke a balun?

*Tags: antenna-theory, balun, jargon, choke-balun · score 19*

## Question

When using a balanced antenna such as a half wave dipole, with an unbalanced feed line such as coax, an RF choke can be used to block RF current emitted by the transmitter from splitting up at the antenna feed point and traveling along the antenna and also down the outside of the coax. Without the choke, the outer shield of the coax becomes a radiating part of the antenna, which is usually not desirable.

Why do amateur radio operators refer to the RF choke in this instance as a balun?

To me it seems that the RF choke isn't a balun and doesn't convert an unbalanced transmission line to a balanced system at all, but rather just removes one of the effects of connecting an unbalanced transmission line to a balanced antenna, that being the unwanted current traveling on the outside of the shield of the coax, by blocking it.

Isn't a real balun for example a ferrite ring with wires arranged such that common mode current is cancelled out in the same way that a transmission line operates while at the same time allowing differential mode current to pass?

## Accepted answer (score -2, by Andrew)

Everyone knows that balun stands for Balanced to Unbalanced and is an AC electrical device which can be used as an impedance transformer and is also used to convert an unbalanced or single ended AC system to a balanced or differential AC system and vice versa.

A common example of usage of this device is to enable an unbalanced coaxial transmission line to be used to feed a balanced dipole antenna split in the middle with the feed point in the center.

Very quickly, there are a few different types of balun :

1.

Voltage balun which behaves like an isolation transformer and removes the DC ground or common connection between input and output and allows the output to 'float'.

2.

Current balun which allows conversion from balanced to unbalanced but with a ground or common connection between input and output thereby referencing one side of the balanced system to the same ground as the input.

3.

Delay line baluns which used 1/4 wave length sections of coax cable as impedance transformers.

One of the desirable effects of using a voltage balun with coax and a dipole antenna for example is that because the balun is a low impedance device which blocks common mode current, all of the current present on the inside of the coax is transferred through the balun and no current can split up at the end of the coax braid and flow down the outside of the coax.

This prevents an undesirable effect commonly known as "common mode current on the outside of the coax" which basically makes the outside of the coax part of the antenna.

Because an RF choke can prevent current on the outside of coax just like a voltage balun does, confusion has arisen and there is a widespread belief that when used with an antenna an RF choke *is* a balun.

Unfortunately while both devices can produce one same result amongst many variables, this common misconception also confuses anyone trying to understand how antennas and transmission lines work.

An RF choke is in fact not a balun and doesn't convert a balanced to unbalanced system at all, but rather is an inferior band-aide solution to get ridding of common mode current.

An RF choke can't be used on it's own as an impedance transformer, and if you use coax with a balanced dipole antenna and an RF choke in line to stop the common mode current on the outside of the coax problem, you still end up with an unbalanced dipole with one side which has a DC connection to the ground of the input, which is not the same result you get with a voltage balun which provides DC isolation between input and output.

Also it's far easier to get an acceptable common mode rejection using a proper balun to get rid of undesirable common mode current than it is to get the exact impedance required in an RF choke to block the same current, especially since the effectiveness of an RF choke is highly frequency dependent whereas a balun isn't as much.

Saying that an RF choke is a balun because both things block common mode current is the same thing as saying that a hammer is a brick because you can use both to bang in nails so let's all build our houses out of hammers, or sea water is the same as tap water because there are fish in both so it's ok to drink both, etc. !

The result is that there are probably many antenna installations out there with a dipole for the driven element that don't work as well as they could because one side of the antenna has a DC connection to ground causing an unbalance in what is supposed to be a balanced system, and with RF chokes which don't actually block that much common mode current, thereby messing up the radiation pattern and being more susceptible to local interference, where a real balun wouldn't have these problems.

Hope that all makes sense !

**RF CHOKEVOLTAGE BALUN**

## Answer (score 26, by Phil Frost - W8II)

"Balun" is a portmanteau of "balanced" and "unbalanced". Anything made to interconnect a balanced and unbalanced load can be called a balun.

A common-mode choke (like a length of coax wound over a ferrite ring) works as a balun because it inserts a high impedance in the common-mode without affecting the differential-mode. By action similar to a voltage divider, most of the current will then favor the differential-mode.

Note that a common-mode choke is not quite the same thing as an RF choke. An RF choke is more or less just an inductor, albeit one with the intended application of blocking RF current. A common-mode choke is a four-terminal device which looks like an RF choke to common-mode current, but to differential-mode current it looks simply like a transmission line.

Typically the differential-mode impedance will be something like 50 or 75 ohms: it's simply the design feedpoint impedance of the antenna. A decent common-mode choke can provide a common-mode impedance of 4000 ohms. Because the differential-mode impedance is so much lower, the common-mode current will be very low, practically negligible.

A common-mode choke like this accomplishes the objective of converting between a balanced and unbalanced load. It's easy to manufacture, has low loss, high power handling, can be effective over a wide band, is inexpensive, and works even if the "balanced" load isn't quite perfectly balanced.

This is by no means the only way to make a balun, but for HF and lower this particular design has a lot of advantages, making it very popular. It is very much a proper balun, and with an appropriate design and application can be a superb solution.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15747/why-do-amateur-radio-operators-call-an-rf-choke-a-balun, by Andrew, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
