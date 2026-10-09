# How to determine number of turns for a 1:1 balun?

*Tags: dipole, electronics, balun, choke-balun · score 8*

## Question

I would like to make a 1:1 balun with М1000НМ ferrite core (magnetic permeability - 1000) and 1 mm thick copper wire using triple bifilar winding. Unfortunately I didn't manage to find a clear instruction on how to determine the required number of turns. Some sources say to use 3-5 turns, others suggest to use about 20.

I would like to use the balun in 3.5-14.35 Mhz range. The target impedance is 50 ohms. I would like to use the balun as a part of a dipole, to connect a coax cable to it.

I have a lot of copper wire. If I just wind as many turns as possible (it will be about 20 for this core) will it be OK?

UPD: TWIMC I've found a great article that explains a lot about baluns and why my original idea to use a voltage balun with a dipole was not that great http://www.arrl.org/files/file/History/History%20of%20QST%20Volume%201%20-%20Technology/AntComp1-Lewallen(1).pdf

UPD2: Here is a research done by G3TXQ on RFI chokes which you might find very useful http://www.karinya.net/g3txq/chokes/

## Accepted answer (score 7, by Phil Frost - W8II)

The ideal number of turns depends on core material, geometry, and frequency. This is why you find such variance in how many turns should be used.

More turns increases the choking impedance up to a point, but decreases the choke's self-resonant frequency (SRF). Once the SRF goes below the operating frequency, adding more turns increases the distributed capacitance and decreases the overall choking impedance.

You could determine the optimal number of turns empirically. [Measure the common-mode current](How%20to%20detect%20common-mode%20currents%20or%20RF%20in%20the%20shack.md) when transmitting a test signal, then add or remove turns until you find a number of turns that minimizes the common-mode current.

With appropriate test equipment the choking impedance can be measured directly as well. See G3TXQ's method, for example.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12395/how-to-determine-number-of-turns-for-a-1-1-balun, by Aleksander Alekseev - R2AUK, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
