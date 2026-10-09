# What is the purpose of limiting radio output power?

*Tags: legal, rf-power, rfi · score 5*

## Question

According to article 25, section I, § 4 (25.7) ITU's Radio Regulations:

The maximum power of amateur stations shall be fixed by the administrations concerned.

In my country this is 500W for CEPT License, 100W for CEPT Novice License, 1500W with additional permission (additional call sign for whoever has CEPT License) and 50W for < 30MHz or 15W for > 30 MHz for automated stations.

Why this exact values? Why not 1 or 2 but 1,5 KW? Is there a underlying reason? Why can't i go 1 MW if i had the money? *And yes, i know that higher power not always means larger range.*

## Accepted answer (score 4, by Hamsterdave)

To add to Phil Frost's answer above, I suspect the 1.5kW number used in the US is a combination of practicality and convenience.

From a practicality standpoint, 1.5kW can be viewed as the point in the power to signal strength curve where your return on investment begins diminishing rapidly, at least in a hobbyist/residential scenario. To achieve a 1 S-unit improvement over a 1.5kW PEP signal, you'd need a whopping **6kW**. At that point you begin to tax the typical infrastructure of a residential dwelling, as a Class AB amplifier would pull a bare minimum of 12kW to develop 6kW PEP (Class AB amps are very inefficient). In the US, the average home in the 1960s had wiring that could handle 15-20 amps, but not a heck of a lot more than that, so operating a large amplifier could pose a safety risk without special installation considerations. The grid was also not all that robust back then, so some guy constantly hammering on the grid with rapid 20kW on/off cycles is going to present technical problems for the utility company, not to mention the neighbors.

The necessary hardware to develop 6kW was also uncommon and very expensive back then, and even today would be cost prohibitive with modern components (enormous surplus Russian broadcast tubes excepted).

100-300 watts has been the "barefoot" standard for HF transmitters since at least the mid 1940s, primarily owing to the availability of affordable PA tubes in that range. If you're running 6kW or more, there will be such a disparity of power between you and the "average" ham (3+ S-units assuming identical antennas and symmetrical propagation) that you will be unable to hear many, perhaps most, of the people who can hear you. This increases the likelihood that you will unintentionally interfere with others. As your output power increases, the inevitable spurs and harmonics of your signal also increase in power, and filtering is not always a simple matter. With the current requirements for spectral purity (-50dB I believe), a 6kW amplifier could have spurs that approach 50mW PEP. On HF in good conditions, this is sufficient for reception hundreds of miles away. Achieving the -60dB or more that would be necessary to keep the HF spectrum fairly clean is not a trivial matter.

Finally I would posit that the precise number, 1,500 watts, was a bit of rounding for the sake of convenience. A 2 S-unit (12dB) increase above the typical 100w transmitter would be 1,**600** watts. To make it a nice round number that is easy to remember, 1,500 was "close enough".

## Answer (score 7, by Phil Frost - W8II)

I'd speculate a large part of the justification is that amateur stations, unlike commercial broadcast stations, are not periodically certified to meet spurious emission regulations. Or any regulations at all. While the station operator is responsible for ensuring the proper operation of his or her station, realistically amateurs will not always have the resources or technical knowledge to do this well, all of the time.

Additionally, the amateur radio allocations are a shared resource. 100W is more than sufficient for worldwide communication with some skill, and with 1000W it's almost too easy. Having amateurs compete for the highest power to be louder than everyone else to get the most DX contacts would ruin the band for anyone with more modest equipment.

Lastly, a 1kW station is already a safety hazard if not properly controlled, and can cause extremely annoying RFI issues for neighbors. Think of what a 1MW station could do. Broadcast stations operating at high power must undergo certification to assure safety, and license applications are reviewed to assure a new transmitter isn't going to cause unacceptable interference. No such regulation exists for amateurs, and regulatory bodies instead rely the good judgement of amateur station operators, and when that fails, reasonable power limits to put an upper bound on the damage that can be done.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7384/what-is-the-purpose-of-limiting-radio-output-power, by Hex, Hamsterdave, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
