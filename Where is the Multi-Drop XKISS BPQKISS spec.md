# Where is the Multi-Drop XKISS / BPQKISS spec?

*Tags: packet, ax.25 · score 5*

## Question

In packet radio, AX.25 is a fairly common layer-2 protocol. Many TNCs implement AX.25 in firmware, so the operator interfaces to the TNC with a serial port, using the TNC's firmware from a shell-like interface.

Many TNCs also allow a "raw mode" where data packets are sent directly over the serial port for the host computer to manage. KISS is a common protocol for this.

XKISS is "extended KISS" and it has about 3 very simple improvements over KISS. Kantronics TNC documentation indicates that it was conceived by John Wiseman, G8BPQ. Kantronics TNCs provide an XKISS mode, in addition to a standard KISS mode.

TAPR has some detailed documents for AX.25 and KISS on their FTP site. Where is some documentation to describe XKISS in detail?

## Accepted answer (score 2, by oh7lzb)

**Karl Medcalf, WK5M**, of **Kantronics**, has published a paper titled **Multi-Drop KISS operation** for **ARRL CNC v10** conference (San Jose, California, 1991). That document was distributed as a PostScript file, at some point a copy was in the source code of the Linux ax25-tools, in the *doc* directory. It seemed a bit hard to find an URL for the file now, so I ran it through ps2pdf and placed a copy on my server:

http://he.fi/pub/oh7lzb/bpq/multi-kiss.pdf

I checked the old G8BPQ DOS software installers, which include the BPQKISS firmware, hoping to find an original spec. KISSROMS.DOC says:

The protocol used for this multidropped option was changed from version 3.59a onwards to be compatible with similar software produced by KANTRONICS for their range of TNCs. The new version is called BPQKISS, and replaces the old JKISSP.

I would expect Karl's document to document XKISS as implemented by Kantronics. This recent post (2010) by **John Wiseman, G8BPQ** seems to say so:

The Kantronics XKISS uses the same enhancements as my BPQKISS.

The Linux kernel AX.25 implementation (mkiss module) is apparently based on that document, so that's one place to look into if you wish to see actual source code.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/474/where-is-the-multi-drop-xkiss-bpqkiss-spec, by Jacob, oh7lzb. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
