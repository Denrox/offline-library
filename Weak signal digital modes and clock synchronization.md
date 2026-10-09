# Weak signal digital modes and clock synchronization

*Tags: software-defined-radio, digital-modes, jt65 · score 5*

## Question

Why to some weak signal digital modes (jt9, jt65, etc.) require knowing a clock time? Does knowing this clock time provide any gain in signal detection ability? (lower required S/N?)

What clock synchronization accuracy to what master clock source is required?

## Answer (score 3, by Scott Earle)

Knowing when a signal is likely to be present helps the software to decode signals. If signals are of varying lengths, and sent at any time, then it's much harder to decode weak signals that may or not be present.

An analogy is the 'old' RS-232 serial data protocol, which could run in 'synchronous' (clocked) or 'asynchronous' modes: knowing from the clock signal when a byte is going to start and when it is going to finish, allows more data to be sent down the wire because you don't need to add 'start bits' and 'stop bits' to tell the listener when a byte starts and stops.

Having everyone send their signal from hh:mm:00-hh:mm:47 means that the software KNOWS exactly when data will be present. And if it can't find any signals that start and end within that exact timeframe then it is certain that there is nothing decodable sent in that time slot.

Generally, by synchronising the times during which data can be sent, allows the software designers to make assumptions while decoding that VASTLY improve the throughput of data at extremely low signal levels.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10302/weak-signal-digital-modes-and-clock-synchronization, by hotpaw2, Scott Earle. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
