# Long callsigns in WSJT-X?

*Tags: ft8, wsjt-x, jt65 · score 5*

## Question

During the month of May (2018) a lot of Belgian club stations can use callsigns in the format OT70xxx. (The xxx is always 3 letters, for example our club station uses OT70TRA.)

In WSJT-X it seems impossible to set this call as 'mycall'; the call gets truncated.

Any clues how we could solve this? Except for making QSOs with all text in 'free text'?

## Accepted answer (score 5, by hobbs - KC2G)

For the current "77-bit" versions of FT8 and MSK144 (as supported by wsjt-x version 2.0, released in late 2018, and newer), you can use these callsigns without doing anything special. Any combination of letters, numbers, and slashes, up to 11 characters total, can be used as a callsign.

If your callsign is "nonstandard", meaning that it doesn't follow the rules described below for pre-2.0 versions, there are some differences in behavior:

- Your CQ or CQ-response messages won't include a grid square (there are no bits available for that)
- In other messages during a QSO with you (signal report / RRR / 73 / RR73), either your callsign or the other party's callsign will be replaced by a 12-bit "hash" instead of transmitting the callsign directly.
- When callsigns are hashed, they are displayed in angle brackets like <KC2G> in the wsjt-x GUI.
- Hashing shouldn't make any difference to your life 99% of the time, but occasionally a "hash collision" will occur (two callsigns on the air at the same time share the same hash), leading to confusion about who is calling who.
- The protocol is designed so that each party transmits their own and the other party's complete (non-hashed) callsign at least once during each QSO, which should satisfy amateur radio operating rules.

Using versions of wsjt-x prior to 2.0 (including the version in effect when this question was asked), such callsigns were impossible; the only callsigns that could be used in a complete QSO were "standard" 28-bit callsigns. "Standard" callsigns use a complicated encoding which covers the great majority of amateur callsigns in the world, but excludes some special ones like the one in the question, and cannot support most prefixes and suffixes. The rules for standard callsigns are:

- there must be a digit,
- there cannot be more than three letters after the last digit,
- there cannot be more than two characters (either letters or numbers) *before* the last digit.

In version 2.0, callsigns that conform to these rules will use the standard encoding and not have to worry about hashing.

## Answer (score 2, by mike65535)

According to K1JT himself, the callsign field is rather restricted and must meet the same parameters as the one for JT65.

https://sourceforge.net/p/wsjt/mailman/message/35254350/

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10231/long-callsigns-in-wsjt-x, by ON5MF Jurgen, hobbs - KC2G, mike65535. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
