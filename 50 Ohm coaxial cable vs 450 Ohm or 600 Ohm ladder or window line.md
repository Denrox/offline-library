# 50 Ohm coaxial cable vs 450 Ohm or 600 Ohm ladder or window line?

*Tags: feed-line, coaxial-cable · score 16*

## Question

What are the relative advantages and disadvantages of using 50 Ohm coaxial cable as opposed to 450 Ohm or 600 Ohm ladder or window line?

## Accepted answer (score 3, by on4aa)

### Cheaper & less loss

The main advantage of two-wire transmission lines over coaxial cable is, apart from reduced cost, also much lower loss. This is because the dielectric in two-wire lines is predominantly air. Plastic dielectrics provide more loss. In that respect, open-wire line has the least loss of all two-wire transmission lines, window-line a bit more and twin-lead ribbon line even more so.

### Loss measurements

A classic paper by Wes Stewart, N7WS reports on loss measurements of 450Ω "Wireman" window-line. An impedance-matched, 100ft length of medium-grade type 552 window-line showed 0.24dB loss at 20MHz under dry conditions. In contrast, the *ARRL Antenna Book* reports for an impedance-matched 100ft length of RG-213 coaxial cable at the same frequency a loss of slightly more than 1.0dB.

### Additional mismatch loss

Please, notice twice the use of the word "impedance-matched" in the previous paragraph. This is because a mismatched line will suffer additional power loss. The maximum voltage and current amplitudes on a mismatched line are proportional to the square root of the standing-wave ratio $(\sqrt{SWR})$. This increase in effective current raises the ohmic losses $(I^{2}R)$ accordingly, whereas the increase in effective voltage increases the losses in the dielectric $(\frac{E^{2}}{R})$.

### Typical use case

From a practical point of view, suppose you happen to have a severely mismatched antenna and you chose to perform the impedance matching not at the antenna but in the shack. In such a case, it is in your interest to use a two-wire line of sufficient voltage and current rating over a coaxial cable. Not only will the loss and cost be much lower than with coax, also a voltage breakdown of the dielectric will be less likely to occur.

For insanely high power levels (broadcast), four- and five-wire lines may offer a solution.

## Answer (score 5, by AA6YQ)

The primary advantages of coax with respect to ladder line are

1. most transceivers are equipped with coax connectors, whereas using ladder line requires a balun or balanced tuner
2. coax is not affected by nearby metal objects, unlike ladder line
3. the impedance of coax doesn't change when it rains or snows, unlike ladder line

The primary advantages of ladder line with respect to coax are

1. lower loss at frequencies of 28 MHz and up
2. easier to make connections
3. can drive a balanced antenna (e.g. a dipole) without a balun
4. lower weight

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/111/50-ohm-coaxial-cable-vs-450-ohm-or-600-ohm-ladder-or-window-line, by Timtech, on4aa, AA6YQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
