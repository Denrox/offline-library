# What additional information do I get from an RF ammeter, as compared to a regular SWR/wattmeter?

*Tags: rf-power, antenna-system, impedance-matching, swr-meter, history · score 5*

## Question

I've grown up using SWR/power meters. They're "simple" devices: They show forward and reverse power, and show the standing wave ratio. They, however, do not show antenna efficiency. New hams are traditionally instructed to tune their antennas so as to minimize the SWR.

On the other hand, I've been reading about the RF amperemeters. Older radio sets used to have them, and there are people who recommend tuning for maximum antenna current, instead of minimum SWR. Manuals for some of them have statements such as "Tuning for maximum feedline current for any given antenna always gives maximum radiated power.", without going into details why.

So with what extra information does the amperemeter provide me, compared to a regular SWR meter?

## Answer (score 2, by Phil Frost - W8II)

In a way, an SWR measures voltage and current simultaneously, and that's how it's able to separate forward and reverse power. W2AEW has an excellent video on how directional couplers work. One way to convert an SWR meter into an ammeter is to disconnect one of the transformers.

Older equipment included an RF ammeter because that older equipment used vacuum tubes. Tube PAs have a characteristically high output impedance, and thus require a matching network to drive typical loads. Thus in practice tube equipment has what amounts to an antenna tuner built in. The ammeter is a useful tool for tuning the matching network, but the tuning procedure usually involves measuring currents within the PA, not just feedline current.

I would say an ammeter is of little to zero practical use if you already have an SWR meter. If you have tube equipment, there's likely already a ammeter built into it. And if you have solid-state equipment, it has a fixed matching network which is designed for a 50 ohm load. Deviating from 50 ohms will result in one or more of:

- activation of protection circuitry, reducing power output or shutting down the transmitter
- an increase in nonlinear distortion
- overheating and eventual destruction of the transmitter

Measuring feedline current is a tricky business, since it depends on where the meter is placed. You probably know that a VSWR greater than 1:1 means there will be high and low voltage nodes on the feedline. Those high voltage nodes are also low current nodes, and vise-versa.

On the other hand, an SWR meter indicates the same thing regardless of where it's placed. It can do this because it measures voltage as well as current.

It is true that if feedline length, meter position, and frequency are held constant, then more feedline current means more radiated power. However the SWR meter also measures forward power, and more forward power also means more power to the antenna. If you want to tune for maximum power without regard to anything else, the SWR meter allows that.

But given the issues with improperly loading the transmitter above, I would not recommend it. Hams decades ago may have gotten away with it due to the generally more robust equipment and relaxed spurious emission regulation of era, but the times have changed, standards are higher, and there's newer equipment available.

modulo transmission line losses. As the line loss increases, more of the reflected power is absorbed by the line, and the indicated SWR approaches 1:1. For typical feedlines with low loss and moderate SWR the effect is negligible.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12694/what-additional-information-do-i-get-from-an-rf-ammeter-as-compared-to-a-regul, by AndrejaKo, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
