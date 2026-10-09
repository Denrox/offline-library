# How do I put an RJ-45 connector on to repair a Kenwood MC-59 microphone cable?

*Tags: kenwood, audio-interface, repair, microphone · score 5*

## Question

I've got a Kenwood MC-59 microphone, which started fraying around the place where the mic cable goes into the body. I thought I'd cut it off and put a new RJ-45 jack on it.

After cutting the cable, I discovered something completely unexpected. Although it looks as if the RJ-45 plug has 8 insulated connectors:

the cable itself has only 7 (plus a shield):

Has anyone ever repaired one of these cables before, and if so - what goes where? How did you do it?

## Accepted answer (score 8, by user3486184)

Here's how to repair a Kenwood MC-59 microphone cable (ships with the TM-V71a, probably the 710, and a few LMR radios as well).

First, if you didn’t know already, behind the rubber boot at the end of the Kenwood MC-59 mic cable is a regular RJ-45 jack:

**Step 0**. If you want to avoid all this, the cord is part Kenwood E30-7543-18 at PacParts.com. (They also carry Kenwood 881M59-7889-72, which might be the same, and is a lot cheaper.) Avoid the cables that sell for under $10 on eBay - they will work, but will sound awful. The Kenwood cable has a shield that covers the clock line. If your cable doesn't have that, you’ll get a terrible buzzing noise in your audio - as if cicadas have infested your mic.

If you want to repair the existing cable yourself, you’ll need:

- 1/4 inch (6.35mm) heat shrink, about 2-3 inches (50-75mm)
- a network cable to sacrifice
- an EZ-RJ45 jack
- two paper clips
- soldering iron
- diagonal cutters
- RJ-45 crimpers
- utility knife (if your crimper doesn’t have a cutter)

**Step 1**. I'll assume you're repairing the head because the mic cord is wearing where the bottom of the boot meets the wire. That's what happened with mine. First, pull the rubber boot down, then disconnect the RJ-45 jack from the mic head.

**Step 2**. If it's still attached, cut the RJ-45 jack off the cable with diagonal cutters.

**Step 3**. Trim about 1 inch (25 mm) of the remaining jacket. Carefully unweave the braid from the clock line (on mine it was the white wire), separate the copper braid from the cloth braid, and wind the copper braid into a wire. (Although my original RJ-45 jack had two black wires, they were not electrically connected.)

**Step 4**. **Very important**: now is the time to pull the boot down as far as it will go, and put the heat shrink on the wire. I ended up wishing I'd made my heat shrink longer - it fits, but exposes the same weak spot the cable originally had. If I'd added an extra inch (25 mm) or so, I'd have a stronger cable, I think. You can slide the boot partway down the curly part of the cord if you need more room.

**Step 5**. Sacrifice the network cable and take out about 3 inches (75 mm) of one wire. (I used the white/brown, so I wouldn't confuse it with the other wires.) Strip the wire back on one end. Carefully tack-solder that end of it to the base of the copper braid. I tried not to solder the whole braid so I would have some flexibility.

**Step 6**. Feed the individual wires through the EZ-RJ45 jack. Order here is important. On my jack, it was:

- yellow
- grey
- white
- originally black connected to the shield, now white and brown
- blue
- black
- red
- green

Leave the wires long to give you plenty of room to work.

Here's a face-on diagram of the jack:

**Step 7**. Adjust the EZ-RJ45 jack first so it's in position, then put the heat shrink where it needs to be. Slide the EZ-RJ45 jack so it no longer covers the heat shrink. Heat the heat shrink so it conforms to the wire. Slide the EZ-RJ45 jack back down over the heat shrink.

**Step 8**. Crimp the EZ-RJ45. I didn't have the official EZ-RJ45 crimper, so I used my RJ-45 crimper and then trimmed the wires off with a utility knife.

**Step 9**. Check all the wires for continuity with the RJ-45 connector on the other end. I used an ohmmeter with a couple of sewing pins held by mini-grabber test leads as probes.

**Step 10**. You're almost done! (If the boot weren't so tight, you'd be done. But it's tight, and unless you're careful, it will push the heat shrink out of shape as you slide it up.) Deform two paperclips and slide them between the wire and the boot, and use those to wedge the boot around the heatshrink.

Note as you slide the boot up that it has an orientation. Make sure the cut in the molded boot matches the tab in the EZ-RJ45 jack.

Connect the mic head to the EZ-RJ45 jack. Slide the boot up, and the repair is complete. The cable can now be reconnected to the radio.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/14458/how-do-i-put-an-rj-45-connector-on-to-repair-a-kenwood-mc-59-microphone-cable, by user3486184. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
