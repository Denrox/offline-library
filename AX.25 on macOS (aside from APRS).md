# AX.25 on macOS (aside from APRS)

*Tags: software, aprs, packet, macos, ax.25 · score 5*

## Question

I'd like to send raw AX.25 packets from a macOS PC using a KISS TNC (mobilinkd TNC2). I've sent APRS packets with this set up using Xastir, but I'd like to send other information besides just APRS (i.e. put my own information into the AX.25 packet).

There are several AX.25 terminal programs for Linux, but they all seem to rely on the AX.25 features built into the Linux kernel (which macOS doesn't have). How do I send AX.25 packets from a macOS PC?

## Answer (score 5, by Tmanok)

Xastir isn't bad at all but I recently encountered something called YAAC (Yet Another APRS Client). On it's site it states the following:

YAAC can be used as a stand-alone APRS client, an APRS RF-Internet gateway (I-Gate), or as a AX.25 digipeater. It supports 16 different data reporting views as delivered, and can be extended with user-written "plugins" to add more functionality.

I'm sure there's already plugins available and with the AX.25 "digipeater" you should be able to also send packets. Keeping in mind it should automate much of what Scott Earle pointed out earlier: "crafting AX.25 packets" would really be a pain.

If you'd like to download it for OS X, it's available on Source Forge and the original website has source code available if you'd like to manually compile the software.

Note that "MacAPRS" has been discontinued although that too was an AX.25 iGate packet manager. Hope I've helped!

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7733/ax-25-on-macos-aside-from-aprs, by watkipet, Tmanok. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
