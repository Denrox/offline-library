# Maximum size of a command on an RLC Club Deluxe 2

*Tags: repeater · score 3*

## Question

With reference to an RLC Club Deluxe 2 repeater controller:

1. What is the maximum size of a command?
2. What is the maximum size of a macro?

The manual does mention "Limits on Macros" but all it says is:

Since one macro can call another, you may wonder if macro 500 could call 501, which could call 502, which could call 503, etc., until you recalled 100 macros or so. The answer is not quite. There are other limits. One is that if the total time it takes the processor to decode and execute the whole chained macro sequence is more than one half second or so, the controller may reset itself. It is unlikely that you will ever reach this limit (it would probably take more than 20 macros are hooked together even come close to this limit). The other limit restricts how deeply the macros can be nested (called from another macro). This is not a limit on how many commands can be called inside of a macro. It is not a limit on how many macros can be executed from one Mac. It is a limit on one macro calling another macro that calls another macro that calls another macro.

## Accepted answer (score 1, by Glenn W9IQ)

Each macro can hold 100 bytes.

There are 200 standard commands, another 300 that are for internal macros and another 500 for user macros.

OP Edit: I was able to find a searchable version of the manual. There I found only one reference to a maximum command length, and it also happens to mention a macro maximum length.

The message length is limited to the maximum command length (about 200 characters) or if used in a macro, by the space left in a macro (less than 100 characters).

For the macro size limit, we refer to a URL in a comment by glenn-w9iq, which takes us to the RLC-Club FAQs page on the RLC wiki. It says:

Q: What are the macro size limits on the RLC-Club?

A: All RLC-Club macros can hold up to 100 bytes. A byte of macro storage roughly corresponds with a digit stored in it, but that relationship isn't exact. The easiest way to find out how much space a macro takes is to program it, then ask the controller how full the macro is with command 054. If you want to figure it out manually, use the equation 1 + (3 * NumCommands) + TotalDataDigits = MacroSizeInBytes. For example:

```
 055 500                 ; erase macro - doesn't use any space
 056 500 036 001 002 003 ; speak "one two three" - one command, 9 data digits
 056 500 038             ; be quiet - one command, no data digits
 056 500 000 12          ; connect ports 1 and 2 - one command, 2 data digits
;
Total space used = 1 + ( 3 * 3 ) + 11 = 21 bytes.

```

So for lack of anything more specific, it appears these are the answers:

1. The maximum size of a command is "about 200 characters".
2. The maximum size of a macro is 100 bytes which is "less than 100 characters".

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9741/maximum-size-of-a-command-on-an-rlc-club-deluxe-2, by Joshua, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
