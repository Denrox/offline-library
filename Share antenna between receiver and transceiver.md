# Share antenna between receiver and transceiver?

*Tags: antenna, receiver, antenna-system · score 12*

## Question

I recently put up a fan dipole for 80/40/20/10. I'm looking for a way to share this antenna with a receive-only SDR and my shack transceiver. Obviously I can just switch this antenna between the two manually, but I was hoping there was a way to have both hooked up at the same time without transmitting into my SDR.

Is there a practical, cost effective way to accomplish this? It would be great to have a waterfall display of the entire band while I'm going at it.

## Accepted answer (score 8, by Pete NU9W)

Back in the olden days, before transceivers took over, the transmitter and receiver were separate units, and the receiver had to be protected from the transmitter. The solution then, as now, is an electronic T/R switch. One approach is an RF sensor that triggers a relay; the MFJ-1708 is one example. A more sophisticated approach uses an active element to isolate the receiver. Used to be a vacuum tube, and if you do a Google search you'll find lots of DIY TR switch projects for vintage radio fans.

## Answer (score 4, by WPrecht)

Without serious isolation, you will smoke the SDR the first time you transmit. Typical (i.e., cheap) coax switches *suck* at isolation. If you are lucky it'll be 30 dB down. That's still enough to smoke the SDR easily unless you are QRP.

The only way that comes to mind is to make a relay that drops out the SDR when you key up your rig. Most rigs have a signal line to key an amp up, you can use this signal to drive the relay. Basically the inverse of the amp keying circuit.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1685/share-antenna-between-receiver-and-transceiver, by s3c, Pete NU9W, WPrecht. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
