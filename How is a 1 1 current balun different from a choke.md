# How is a 1:1 current balun different from a choke?

*Tags: dipole, coaxial-cable, impedance, balun · score 10*

## Question

I have a 10m dipole and am going to feed it with 50 ohm unbalanced feed line (coax). My understanding is the feed point of this style antenna is about 50-75 ohms, and since it is a balanced antenna I'm thinking I need some type of balun. I'm wondering:

- Is a 1:1 current balun the same as a choke?
- Are they the exact same devices internally, or are they different internally and just perform the same function?
- If they are different, do they both keep common mode current off the feed line?
- If they are the same, why are there two different names?

## Accepted answer (score 7, by K7PEH)

Baluns are designed to be transformers (like 1:1 4:1, 6:1, etc.) or choke baluns, and both.

For an antenna, the purpose of a choke balun is to create a high-impedance to common mode currents that would flow on the outside of coaxial cable shielding. These common mode currents can cause all kinds of problems such as RF in the shack, matching problems, and others. So, minimizing common mode currents is a good thing.

Common mode currents arise when you are coupling a balanced antenna to an unbalanced line (usually). For example, connecting coax cable to a dipole antenna. You can use either a 1:1 balun or a choke balun at the feed point of the antenna or where the balanced part of the system meets the unbalanced part. The choke balun usually does the same thing as a regular 1:1 current balun but adds the high impedance path to the common mode currents too.

Also, the names Choke Balun and regular current balun are somewhat interchangeable as both are used to do the same thing in ham radio antenna matching: matching coax to balanced antenna and minimizing common mode currents.

Currently, on my 80-meter dipole, I run 450 ohm ladder line to a 4:1 Current Balun and the remaining 20 feet or so is coax into the shack. In this application, I experimented with both a 4:1 and a 1:1 balun to find the best match and overall SWR on my bands of choice I use with this antenna: 80, 40, 30.

With the same antenna, I have used my own custom made choke balun made from coax turns through 6 toroids -- about 7 turns of coax through all 6 toroids. This worked very effectively except for one thing. This balun was heavy and often would be a factor in my antenna coming down in a wind storm so I replaced it.

So, in answer to your question specifics: (1) they do not always perform the same function but sometimes they do; (2) A regular current balun internally is very much like a transformer where as a choke balun usually focuses on multiple turns through toroids to provide high-impedance to common mode currents; (3) the names are different and some people distinguish between one thing and another by the names and others do not. It is usually not a big deal from my experience unless you are buying something but then you look at the data sheet to understand the balun better.

The image below is of one of my custom made choke baluns. This is an older one that used only five toroids.

The following image shows one of my current baluns, a 1:1 5 KW balun.

## Answer (score 7, by Phil Frost - W8II)

A choke is an inductor which is used to block high frequencies while allowing DC to pass. All chokes are inductors (though sometimes more than one inductor), but not all inductors are chokes: to be called a choke the application must be to block high frequencies. Counterexample: an inductor in a matching network is not a choke, but the same inductor, used to filter RF from a DC power supply, could be called a choke.

A balun is any device designed to connect a balanced source to an unbalanced load or vice-versa. Since most baluns are passive devices they are also reciprocal, meaning they work equally well in either direction. There are many ways to build a balun. Many HF balun designs use a choke, but [chokes are less commonly used in baluns at higher frequencies](Where%20are%20the%20baluns%20for%20VHF%20and%20higher%20How%20can%20one%20be%20made.md).

This is a common-mode choke:

Common-mode current sees a high impedance, and is thus "choked". (Of course there's nothing drawn in this schematic which would introduce such a current, but the real world is not so simple.)

If you put a common-mode choke in a box with a coax connector at one end and screw terminals or some other balanced connector at the other end, you've made one kind of balun. It's 1:1 (because it performs no impedance transformation) and a current balun (because with high choking impedance, common-mode current approaches zero). And while theoretically there may be other possible designs for a 1:1 current balun, in practice "1:1 current balun" means "a common-mode choke with balanced and unbalanced connectors on it".

## Answer (score 5, by Kevin Reid AG6YO)

The name *choke* refers to the electrical component, whereas the name *1:1 current balun* refers to the job it is doing in this case.


There's more than one way to construct a balun. If you hear that something is a balun, that doesn't mean it is or contains a choke. It might, or it might not.


There are purposes for a choke that are not baluns. For a common example, it might be used to suppress interference (RFI/EMI), perhaps even at frequencies very different from those of the intentional signal carried by the cable the choke is on. In this application, both sides would be balanced or both unbalanced.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5563/how-is-a-1-1-current-balun-different-from-a-choke, by Java42, K7PEH, Phil Frost - W8II, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
