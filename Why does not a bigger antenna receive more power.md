# Why does not a bigger antenna receive more power?

*Tags: antenna, antenna-theory · score 6*

## Question

According to http://www.antenna-theory.com/basics/aperture.php, the power received by an antenna depends on the power density of the incoming wave, the wave length (which I consider to be fixed) and the antenna gain. So if I want to receive more power I need to build an antenna with higher gain, but this means that the antenna would be much more directive. Let us say that I want to stick with a non directive antenna, because I do not know in advance the direction I will be receiving from.

According to the equations in the webpage, there is nothing I can do to improve the received power once I fix wave length and gain. However, this strikes me: I would expect a bigger antenna to intercept more RF power, and thus making more available at its terminals. Why does not this happen? Are there tricks (maybe using non linear components?) to actually collect more incoming RF power in all directions, without making the antenna directional?

## Accepted answer (score 9, by Phil Frost - W8II)

### Argument A: reciprocity

By reciprocity, we can flip this question around and ask it from the perspective of the transmitter. Assuming we've done the obvious like minimize feedline losses, and we're holding the geography, frequency, and so on constant, how can we get a higher fraction of the transmitter's power to appear at the receive antenna's feedpoint?

If the transmitter has some omnidirectional antenna like a vertical monopole, most of the radiated energy is going in the wrong direction to ever reach the receiver, and is thus lost.

Increasing the directivity of the transmitting antenna sends a higher proportion of the transmitter's power towards the receiving station, accomplishing the goal.

It should be intuitively obvious from the law of conservation of energy that a higher gain is the only option here, which if losses are already minimized means a higher directivity.

### Argument B: phase coherence

Consider you have an omnidirectional antenna like a vertical monopole, and the received power at the feedpoint is 1μW.

Wanting to receive more power, you install another identical antenna beside it. This 2nd antenna, having a nearly identical path to the transmitter as the 1st, receives another 1μW.

In total you're receiving 2μW, but to get the full 2μW combined into a single port requires that the phases of the two antennas are adjusted so they add coherently.

Unfortunately, this means the array has acquired more directivity. While some phasing arrangement may work for one transmitter location, there will be other possible geometries which place the transmitter closer to one of the antennas and farther from the other, thus altering the phase at which the signals combine. Thus the antenna array is no longer omnidirectional.

So, while a longer wire, or a larger array of antennas will indeed intercept more power, it's not possible to *coherently* combine those powers without increasing directivity.

### MIMO

An array of antennas does indeed receive more power, the difficulty is it's often unknown what phasing of the antennas will result in the signal combining coherently. One solution is to make the phasing variable, and to dynamically adjust it for maximum signal clarity.

Modern communication systems (Wi-Fi, cell phones) can do this dynamically by separately digitizing the signal from each antenna, then dynamically adjusting the phasing in software. This is effectively an antenna array that's always "pointed" in the optimal direction, thus obtaining a higher link quality without the disadvantages of a directional antenna.

### Collinear arrays

For terrestrial communications in predominately flat terrain, it's safe to assume the other station is near the horizon, that is, not flying overhead, and not underground, although the direction may be unknown. In these cases it's possible to maintain a omnidirectional (meaning uniform along the azimuth) pattern by increasing the directivity in the elevation axis. That is, making a "flatter" doughnut.

Often this is achieved with a collinear array. A quarter-wave monopole above a ground plane has gain of 5.2 dBi, and a dipole 2.2 dBi: when you see omnidirectional antennas with higher gains they are usually collinear arrays with a "flatter" pattern.

## Answer (score 2, by Mike Waters)

One way to accomplish this is by stacking multiple vertical dipoles or horizontal "halo" loop antennas (or a turnstile array with two straight dipoles at 90°) on a vertical mast. Such an array can have nearly 360° coverage and increased gain over a single vertical or loop.

Such an antenna array can be said to be directional, but in a practical way: it has increased gain at lower angles --towards the horizon-- but decreased gain at the unwanted higher angles.

The antennas are connected using a carefully designed "phasing harness" made from either balanced line (for UHF and above) or coax (usually VHF). They are often used by FM broadcast or television stations.

**This is the pattern and gain of the antenna described above:For comparison, here is the gain and pattern of a dipole:**

It appears that the stacked array wins, even if it has those high lobes. It has quite a bit more gain at low angles than the dipole.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/11657/why-does-not-a-bigger-antenna-receive-more-power, by Giovanni Mascellani, Phil Frost - W8II, Mike Waters. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
