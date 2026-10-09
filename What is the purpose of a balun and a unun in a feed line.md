# What is the purpose of a balun and a unun in a feed line?

*Tags: antenna-construction, feed-line, balun · score 15*

## Question

I have never understood how a balun or a unun works and under which situation I need to use either of them in an antenna feed line.

## Accepted answer (score 11, by Walter Underwood K6WRU)

A balun matches a balanced load to an unbalanced line, but it can also do other useful things. A current balun can present a high impedance to common-mode signals, which will help reject noise. Common mode signals are the same on both conductors, so are not "balanced" or differential.

An unun is an impedance transformer, usually 4:1 or 9:1, which matches an unbalanced antenna to a feedline. A 9:1 transformer is often used for an end-fed half wave antenna.

This document by Jim Brown (K9YC) is long, but tremendously helpful in understanding baluns, chokes, and reducing RF noise:

"A Ham's Guide to RFI, Ferrites, Baluns, and Audio Interfacing"

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/13/what-is-the-purpose-of-a-balun-and-a-unun-in-a-feed-line, by Dinesh Cyanam, Walter Underwood K6WRU. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
