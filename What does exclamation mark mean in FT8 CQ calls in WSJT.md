# What does exclamation mark mean in FT8 CQ calls in WSJT?

*Tags: software, ft8 · score 9*

## Question

For example, in this screenshot:

WSJT shows !Italy, !Serbia, !U.S.A. What does it mean?

## Accepted answer (score 7, by Pablo Fernandez)

That is something that is activated by "Show DXCC entity and worked before status" (selectable on the "Settings" > "General tab"). From the manual:

When this option is checked WSJT-X appends some additional information to all CQ messages displayed in the Band Activity window. The name of the DXCC entity is shown, abbreviated if necessary. Your “worked before” status for this callsign (according to log file wsjtx_log.adi) is flagged with a single character and a change of background color, as follows:

! Default color bright purple: New DXCC entity

~ Light pink: You have already worked this DXCC entity but not this station

Green: You have previously worked the calling station

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10179/what-does-exclamation-mark-mean-in-ft8-cq-calls-in-wsjt, by Pablo Fernandez. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
