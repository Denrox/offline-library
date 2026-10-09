# Can I float an SLA 12v battery at 13.8V forever?

*Tags: power-supply, dc-power, battery-charging · score 5*

## Question

I am considering a battery-backup power source for a radio. Typically, power would be supplied through a standard 13.8V power supply, so the battery would be available if mains power goes out:

```
AC -> 13.8V linear supply --+--> Radio
|
SLA 12V Battery

```

I have read that a sealed lead acid battery will self-regulate its charge-current if you provide it with about 13.8V (at 25C).

What I have not found, however, is whether it is safe to leave it at 13.8V, or if you need to disconnect it after having charged the battery, in which case a more complicated charging circuit would be necessary.

- Can I float an SLA 12v battery at 13.8V forever?
- If so, would it reduce the life of the battery?

## Accepted answer (score 3, by Clark Thomborson)

Short answer: yes, it is safe to float a consumer-grade SLA for long periods of time at 13.8V *if* you don't live in a hot climate. They're designed to *slowly* vent the hydrogen that's produced (*very* slowly) as they self-discharge -- so their casings won't bulge, nor will the vented hydrogen present a significant fire risk, so long as you limit the charging current. See https://content.nfpa.org/-/media/Project/Storefront/Catalog/Files/Research/Research-Foundation/Reports/RFLeadAcidBattery.pdf?rev=035c861de5bc4334be6b17e962d505aa -- where this class of batteries is described (formally, and more correctly) as a VRLA -- "valve-regulated lead acid".

Limiting the charging current will require some additional circuitry -- and you'll find some ideas in the other answers to your question.

You also asked whether this charging regime will cause any degradation in the life-expectancy of your battery. The answer is yes it will. How much? That'll depend on the battery's temperature and on a host of other factors... but I'd *guess* your battery will last for years unless you're thrashing it in some other way than by never fully charging it. The issue at hand is sometimes called "soft sulfation" in the non-technical literature. It'll build up, very slowly, over time -- but is *mostly* dissipated whenever you fully charge the battery. See https://www.sciencedirect.com/science/article/pii/S0378775303010681:

"Lead sulfate accumulation on the negatives: This is the natural consequence of hydrogen evolution from the negative plates that eventually vents out of the batteries. This loss of hydrogen results in a charge imbalance between the positive and negative electrodes. Since the batteries are sealed and an equalization overcharge is not easy to do, this effect will result in a gradual loss of capacity and eventual failure."

## Answer (score 5, by tomnexus)

In addition to the solid answer about the float voltage, you have to consider what happens if the AC power returns when the battery is partially discharged. You can float an SLA battery at 13.8 or 14.0 V but you can't charge it with a 13.8 V high current fixed supply. When the battery is nearly empty and the power is turned on, it will simply blow the main battery fuse or trip the PSU..

For lower power applications, the usual solution is something like this, with the CC/CV charger set to an appropriate rate for your battery:

But this isn't really appropriate for > 10 A loads.

Above this it depends on the relative size of your battery and your radio.

- If the battery is (say) 200 Ah so it can comfortably absorb 40 A, and the radio needs 25 A, then set the charger current limit to 40 A and forget about it.
- If the radio needs 25 A on transmit and the battery is 50 Ah, set the charger to 15 A and let the battery add the other 10 A. It shortens its life to do this, but not by very much, unless you're in a contest 24/7

There are other more complex solutions involving two full-current switchmode converters, found in off-grid solar systems, RV and camper second-battery systems, and boat inverters that accept solar, generators, shore power.

## Answer (score 5, by Ryuji AB1WX)

Lead acid batteries are robust but their use life depends on the level of care built in the system. Float charging at 13.8V (2.30V/cell) is on the high side, which may be okay if your battery is always in the cold environment but that voltage is too high (reduces the lifespan) if the battery can be above "room temperature" say above 25C. You want to drop the voltage further, or disconnect the charging circuit after 24 or 48 hours of float charging at that voltage.

https://batteryuniversity.com/article/bu-403-charging-lead-acid

Look at their Figure 3 and its caption above the figure.

You could use a MOSFET or Schottky diode to switch the supplies.

I had (actually still have) a piece of non-radio equipment powered by lead acid (absorbed glass mat), and I had it on a charger that cuts off until the terminal voltage goes below a threshold so that the battery is automatically topped up after use. That charging logic is gentler than float charging while serving the same function. Those cells significantly declined after a year of use and became virtually useless by year 2. Eventually, I custom-fitted LiFePO4 cells to replace, with the charger adjusted for the chemistry (again, CC/CV charge and cutoff until the voltage goes below a threshold). This worked much better for my situation; I haven't replaced the cells since then. Thus, I found LiFePO4 batteries suitable for long-term backup solutions because of their low self-discharge rate and fairly reliable chemistry. LiFePO4's "weakness" is that it is difficult to determine the state of charge by looking at the terminal voltage since it is fairly constant.

One big advantage of using lithium batteries (LiCoO2, LiFePO4 or another chemistry) for backup power is that lithium cells work well in under-charged states without shortening the battery life (in fact, the battery's life is considerably longer if the cell is not fully charged). Of course, the battery voltage must be above the lowest discharge voltage. Lead acid batteries must maintain a certain voltage near full charge state to maximize the life; both use life and storage life.

I have a deep cycle lead acid battery that I used to use as a backup supply for portable operation. I charge that battery every 6 months, even when I don't use it (and fully charge right after each use), and it is still in decent condition after nearly 10 years. If I treated that battery like the non-radio equipment above (AGM battery used in the factory kit), it would've deteriorated much faster.

#### Addendum / responding to tomnexus's answer

The following circuit would eliminate the voltage drop due to the series diode (his D2) when operating on the battery. Choose R to limit the charging current. The maximum float charge voltage is dropped to 13.5V by the same Schottky diode. The gate bias resistor is noncritical and can be anything reasonable.

The battery must be initially charged to a reasonable state (13+V terminal voltage) before connecting to avoid the MOSFET's body diode conducting.

The same thing can be done with LiFePO4 (4S pack with a BMS), even more effectively.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/23253/can-i-float-an-sla-12v-battery-at-13-8v-forever, by KJ7LNW, Clark Thomborson, tomnexus, Ryuji AB1WX. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
