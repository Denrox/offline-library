# Can an external VFO be injected into a commercial rig?

*Tags: transceiver, oscillator, vfo · score 3*

## Question

Constraints of various kinds preclude any investment in a rig at present; so I find myself pondering the means to get back on the band piece-meal.

Say I were successful in an attempt to throw together a DDS/VFO. Say further a good deal longer down the line I plan to acquire a commercial rig.

Could I use my VFO with a commercial rig? Is there any advantage to a facility as mentioned above?

## Accepted answer (score 3, by HarveyB)

This falls under the heading of "Depends on the Commercial Rig"... Some commercial Ham gear is equipped with a connection for external VFO, so for those it's a "plug and play" solution. For other gear it would depend on your ability to find the correct spot in the signal chain to inject the signal from your VFO. I know of hams who have built a DDS VFO and added it to old crystal controlled commercial VHF radios to get a very nice, rugged, rig. Things to be aware of if you go this route are that the VFO frequency will need to be offset from the receive frequency (by the 1st IF freq.). Also, VHF/UHF rigs may also need the VFO to run at a sub multiple of the "tuned" frequency. (Common practice in crystal controlled rigs is to multiply the crystal frequency with analog multipliers.) Most of the DDS kits around have this ability built into the controller firmware.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1753/can-an-external-vfo-be-injected-into-a-commercial-rig, by VU2NHW, HarveyB. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
