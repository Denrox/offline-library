# DMR / DSTAR / P25 Software Encode / Decode

*Tags: digital-modes, d-star, digital-voice · score 8*

## Question

The large VHF / UHF digital voice communication modes all require the same AMBE vocoder chip from dvsinc. This surface mount chip can be aquired standalone for a relatively high price or all of the required encode / decode electronics can be preinstalled in the form of various boards such as the DV Mega.

Every single product which transmits and receives most mainstream digital voice modes requires one of these chips from the specific manufacturer.

This introduces limitations, however. In the case of attempting to run a virtual private server providing an analog to digital DMR bridge using the DMRGateway software , I couldn't procede any farther until I plugged a USB fob with the vocoder chip which is completely impossible on a virtual server. Even if I had a physical computer with USB, price is a large limiting factor in this as well.

So basically, at this point, after several hours of research and attempting software packages, there is no way I have found to decode / encode digital voice through the means of software only.

Due to the fact that amateur radio requires unencrypted and usually led by an open-source community, I am wondering if anybody has even heard if this has been done before, if someone is working on it, or if there are any alternative open-source digital voice modes for VHF and above not requiring a separate vocoder chip?

Small Update: Alinco looks like they use an open source GMSK modem using the ITU V.32 protocol. I couldn't really find any other information on this, however.

## Answer (score 7, by Jon Kåre Hellan LA4RT)

Here is a link to a presentation by Bruce Perens K6BP two years ago: http://algoram.com/dcc2014/AMBE_Exposed.pdf. Start at "Can Hams Use Software AMBE?" I am not aware of any significant changes since then. There exists a software solution (mbelib), but it is patent encumbered. So much so that the authors are anonymous.

You are probably aware of the open voice codec "Codec2" by David Rowe: http://www.rowetel.com/?page_id=452. But it doesn't appear to fit your use case.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6683/dmr-dstar-p25-software-encode-decode, by Skyler 440, Jon Kåre Hellan LA4RT. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
