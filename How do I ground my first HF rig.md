# How do I ground my first HF rig?

*Tags: antenna-system, transceiver, vertical-antenna, grounding, safety · score 3*

## Question

I want to preface this question saying that I am very new to HF and just got my general license. I have only operated using 2m/70cm handhelds and am completely unfamiliar with antenna setup.

I recently acquired a Kenwood TS-930S transciever, around 100 feet of RG-58 coax, and a Hy-Gain AV-14AVQ vertical trap dipole.

My first question regards the transceiver. It has a ground terminal on the back, bot its power cord is also grounded. Should I assume that the chassis is grounded through the cord's ground pin? Should I build an additional plug with only a ground pin and attach the chassis terminal to that? Should I construct a bonding bus and attach the chassis terminal to that even though this is my only piece of equipment and there is nothing else to bond to? Should I run a long wire out of the house and install a second ground rod?

The second one is about the antenna. It did not come with a loading coil and I am wondering if it needs one.

The third one regards antenna grounding. The antenna manual says that all you need is a ground rod, but I have heard that using ground radials can be very helpful. If I do decide to use them, what band should they be optimized for? Should I put traps on the radials? Should I devise some sort of switch to switch between sets of radials? Do I even need these radials?

Thank you for reading this, as I am in need of help on these issues.

## Answer (score 4)

Q1. My first question regards the transceiver. It has a ground terminal on the back, but its power cord is also grounded. Should I assume that the chassis is grounded through the cord's ground pin?

A1. Do nothing; the 3-wire AC power cord fulfilled the requirement. Adding anything will corrupt the electrical system, exposing you to equipment damage, malfunction, electrical shock, and fires. It is also guaranteed to generate noise and interference because you use a daisy-chained equipment ground.

Q2. The second one concerns the antenna. It did not come with a loading coil, and I wonder if it needs one.

A2. No, it came with the antenna. FWIW, it is not a dipole antenna; it is an unbalanced vertical antenna. Here is the description from Mississippi Finest Junk: *"The AV-14AVQ 18-foot radiator has a loading coil at its base that allows precision antenna resonating."*

Q3. Q4, and Q5. The antenna manual says all you need is a ground rod, but I have heard that using ground radials can be very helpful. If I decide to use them, what band should they be optimized for? Should I put traps on the radials? Should I devise some switch to switch between sets of radials? Do I even need these radials?

A ground rod is fine and is part of the lightning protection, but it does nothing for RF. The impedance is too high, and the coupling is purely inductive to dirt. You will want radials. How many and how long depends on your wallet. At a minimum, you will need a Radial Plate and enough 16 to 20 AWG wire to make 16 radials. 4 1/4 wave lengths radials for each of the 4 bands. Keep adding 16 radials until your wallet screams "bloody murderer."

Lastly, do not take grounding advice from amateur. Most of it is outdated and dangerous, and based on 1950 house electrical codes, back when home electrical outlets had 2-wires and no ground. Very little of what a ham radio operator tells you will comply with any known electrical codes or best practices. If you pound a ground rod outside the shack and connect your station ground to it, it is guaranteed to generate noise and interference, placing your radio in a dangerous Ground Loop. Lightning does not have to strike your home or property to wipe you out. If lightning hits your neighbor's tree, it will wipe out your radio equipment, and your home wiring going to the radio, burning it up and possibly causing fire. If you are operating the radio, you are going to have a bad hair day the mortician cannot fix.

NEC article 810 covers all CB and Amateur radio wiring requirements. It is based on a Single-Point Ground, which all commercial radio operators use. Mike Holt is the leading authority on NEC electrical codes and education, and I worked for him. Mike and I wrote an illustrated guide on article 810 to help amateurs get through the BS Uncle Elmer laid down in the 50's.

Mike Holts Illustrated Guide to Article 810

## Answer (score 2, by Mike Waters)

There are lots of grounding myths that just keep getting repeated over and over until people believe it.

As a result, they either suffer lightning damage to their equipment or their radiated signal is weaker.

Here is the definitive website about grounding.

https://www.w8ji.com/ground_systems.htm

Tom Rauch is a *genius*. He also has pages about antennas.

*You can believe about anything you read there.*

Should I run a long wire out of the house and install a second ground rod?

Not if you don't want lightning striking your pole outside to make a path through your house wiring to your new radio! The grounding point on the back is meant for bonding other equipment on your ham bench together. W8JI's website will explain why.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/22518/how-do-i-ground-my-first-hf-rig, by Sprock3t, Mike Waters. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
