# Calculation of transceiver current draw

*Tags: power-supply, efficiency · score 4*

## Question

My radio manual says its current draw is 22A. But in my naivety I would have calculated as follows:

If the radio 'put out' 100W and I have a 13.8V supply then (using the formula power = VxI) 100W/13.8V = 7.2A.

So, it looks that I'm way out (comparing 22A with 7.2A). Is my transceiver terribly inefficient or is this normal?

## Accepted answer (score 6, by hotpaw2)

The rest (of the current) is why your transmitter requires heat sinks (and/or airflow for thermal dissipation). Linear amplifiers are usually not anywhere close to 100% efficient. A high SWR might reduce the efficiency even further.

If it's a transceiver, then the receive circuitry, front panel, and transmit idle bias also takes some wattage to run.

## Answer (score 8, by hobbs - KC2G)

Some of both!

1. It's normal for a linear power amplifier for HF to be something like 50% - 60% efficient. So to make 100W, the radio probably needs 170 - 200 W.
2. There are other power draws in the radio, let's say about 20W if it's a fancy modern rig with lots of electronics and a backlit LCD.
3. Your radio is 13.8V nominal, but it's probably rated for 13.8V +/- 15% (11.73 - 15.87 V) and it probably makes rated power at 12V (people tend to be unhappy otherwise). Combining the previous two points, assuming it pulls 220W at 12V, that could be more than 18A of steady-state draw for key-down 100W out.
4. Add a little bit for transients (maybe inrush current for fans starting up, or relays switching), accessories (if supported, e.g. the Icom tuner port), and a little bit of fudge factor just to be safe, and 22A doesn't sound outlandish as a maximum rating.

All that said, you should expect the *average* to be quite a bit less. You're not transmitting 100% of the time; if you're doing SSB phone or any other non-constant-power mode your average power output will be significantly less than 100W; transients aren't happening all the time by definition, etc. But when choosing power supply, wire, etc. you should still plan for 22A at least.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16098/calculation-of-transceiver-current-draw, by KHWP, hotpaw2, hobbs - KC2G. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
