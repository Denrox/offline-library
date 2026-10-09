# Do I need a separate SWR meter if the transceiver has one built-in?

*Tags: impedance-matching, swr-meter · score 6*

## Question

I'm going to buy Yaesu FT-891 as my first transceiver.

I know that I can measure SWR with it if I use FM mode and minimum power, which is 5W for this transceiver. However, I don't know whether it's always safe. For instance, if I connect a completely untuned wideband antenna, the SWR can be large and all 5W will return to the transceiver.

Do I also need something like an MFJ-259C for preliminary tuning of the antenna or will I be just fine with only the FT-891?

## Accepted answer (score 9, by Phil Frost - W8II)

You'll be fine to start without an additional SWR meter.

An SWR meter doesn't provide any protection. With or without an SWR meter, you'd want to start on a new antenna on low power, then increase power only after measuring the SWR.

Don't worry too much. If transmitting at much less than maximum power you won't damage anything even with the worst possible load. The peak voltage and current at low power is still less than when transmitting full power into a matched load. If you make a mistake, the radio's protection circuitry should reduce power automatically.

An external SWR meter only gets you more precise measurements. Some radios only have an unlabeled bar graph for "SWR" which gives only a qualitative measurement. Some may not indicate SWR directly but instead are just showing the power reduction due to the protection circuitry, and thus may not indicate any issue until the power is increased. A proper SWR meter will probably show both forward and reverse power on a meter calibrated in watts, and often there's a way to adjust the range so the meters provide a useful measurement at high and low powers.

I wouldn't spend money on an antenna analyzer unless you are specifically interested in antenna design.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12262/do-i-need-a-separate-swr-meter-if-the-transceiver-has-one-built-in, by Aleksander Alekseev - R2AUK, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
