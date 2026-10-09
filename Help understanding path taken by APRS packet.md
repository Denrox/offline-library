# Help understanding path taken by APRS packet

*Tags: aprs · score 9*

## Question

I'm looking at some raw APRS packets over APRS-IS. I'd like to determine which stations heard particular packets, but I'm having trouble understanding how TNC-2 paths work. Here are two examples:

```
2016-05-19 05:51:46 PDT: PACCTY>APN390,HEBOWX,KFALLS,OR2*,qAR,STUKEL:
2016-05-19 05:55:32 PDT: PACCTY>APN390,WIDE1-1,OR2-1,qAR,W7GC-4:

```

Can you explain how I can determine the actual path the packet took? Also, how do I differentiate this from the path that the sender, PACCTY requested?

## Accepted answer (score 8, by rclocher3)

According to the way things work for simple AX.25 packets, the part after ">" is the destination address. However, the APRS specification commonly repurposes fields, with the goal being to keep the packet as small as possible. The destination field is like that: most APRS packets are broadcast rather than sent to a specific station, so when an APRS packet isn't meant for a specific station then the destination field is pressed into service to hold something else. If the "destination" starts with AP, then it's a code that indicates what device or software package sent the packet. In this case, a "destination" of the pattern APN3xx means that the packet was sent by a Kantronics KPC-3. (The destination can also be Mic-E encoded, in which case it holds the latitude and part of the longitude of the sending station, plus a few other miscellaneous data flags.)

Similarly, WIDE1-1 doesn't actually mean that the packet was repeated by a station of that name. In this case, WIDE1-1 is an instruction for how to repeat the packet, which was part of the packet when it was first sent. It requests that a "wide" digipeater (one with a wide coverage area, like on a mountaintop) repeat the packet, but only once; if a second "wide" digipeater should hear the rebroadcast packet, then the second digipeater wouldn't repeat it.

Apparently qAR is the "Q-construct" that indicates that the packet was was successfully "Igated" to APRS-IS, the APRS internet packet routing system.

I'm reasonably familiar with APRS, but not an expert. Even so I'll give the second part of your question a go, but I reserve the right to be wrong ;)

PACCTY>APN390,HEBOWX,KFALLS,OR2*,qAR,STUKEL: This packet was sent by PACCTY using a Kantronics KPC-3. It was digipeated by HEBOWX, KFALLS, and OR2, and then copied onto APRS-IS, the internet APRS packet network, by STUKEL. It's unlikely that that exact path was requested by the sender; it's more likely that the original path request was WIDE1-1,WIDE2-1. WIDE1-1 is a request for a small home digipeater to rebroadcast the packet. WIDE2-1 is a request for a high-up digipeaters to rebroadcast. Each station that rebroadcasts the packet puts its call sign into the path.

PACCTY>APN390,WIDE1-1,OR2-1,qAR,W7GC-4: Here we have a packet that was never digipeated before being copied to the internet; we can tell because there is no asterisk. The original packet was heard by Igate W7GC-4 and copied onto APRS-IS there. (The packet probably was digipeated, but when multiple copies of a packet are received on APRS-IS, then one is chosen at random to be kept, and the rest are ignored as being redundant.)

Because this packet was copied to APRS-IS before being digipeated, we have a better look at the original path request. As I suspected, WIDE1-1 is in there first as an invitation for small home digipeaters to repeat the packet. Next comes OR2-1. That could be a station OR2 with an SSID of "-1". But given that the first packet didn't contain OR2-1, it seems like it is more likely to be an alias. Maybe it works like WIDE2-1, but just in Oregon? I'm not sure.

Just for grins, let's look again at the first packet and assume that it was sent with WIDE1-1,WIDE2-1 to see how digipeaters modify the packets going through them.

PACCTY>APN390,WIDE1-1,WIDE2-1: original packet  
PACCTY>APN390,HEBOWX*,WIDE2-1: packet was heard and digipeated by HEBOWX, which responded to the alias WIDE1 and substituted its own call sign  
PACCTY>APN390,HEBOWX,KFALLS*: packet was heard and digipeated by KFALLS, responding to the alias WIDE2  
PACCTY>APN390,HEBOWX,KFALLS,OR2*,qAR,STUKEL: packet was heard and copied to APRS-IS (but not digipeated) by STUKEL

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6213/help-understanding-path-taken-by-aprs-packet, by watkipet, rclocher3. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
