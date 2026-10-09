# Around the world propagation?

*Tags: propagation · score 9*

## Question

Is it possible to transmit a signal around the world and receive it? Has anyone done it, and how? If not, how could this be accomplished? Assuming a complete path around the world, what kind of time delay should one expect on their transmission?

## Accepted answer (score 6, by Phil Frost - W8II)

It's possible on HF (and below), and people have done it. It takes some combination of:

- high power transmitter
- sensitive receive antenna
- directional antenna(s)
- quiet RF location
- lucky propagation conditions

In this case, the path is (roughly) any great circle around earth, so the distance is the Earth's circumference. The signal moves at the speed of light, so we can ask Wolfram Alpha for "circumference of the Earth at the speed of light" and get

$$ \frac{24901.47\text{mi}}{c} \approx 134 \text{ milliseconds} $$

Of course there are less spectacular ways to communicate around the world:

- [store-and-forward amateur satellites](Store-and-forward%20capable%20satellites%20in%20operation.md)
- linked VHF / UHF repeaters (example: EchoLink)
- traffic nets

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/775/around-the-world-propagation, by Adam Davis, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
