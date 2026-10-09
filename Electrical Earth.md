# Electrical Earth

*Tags: antenna-theory, grounding, antenna-system · score 3*

## Question

I have moved to a new flat which is on the 4 floor, luckily the landlord has let me put an OCF dipole outside with coax feeding through an existing hole in the window frame. I'm looking for some earthing opinions as a dedicated grounding rod is out of the question.

I considered bonding the rig to its DC supply chassis-chassis however the PSU lacks an ground lug (it is earthed via the 13A plug) so should I bond the rig to the earth terminal at the outlet? A friend suggested providing an rf earth via the rig to an artificial ground unit and that to the outlet earth or a length of random wire.

## Accepted answer (score 5, by Glenn W9IQ)

Congratulations on getting permission to install an antenna. There are many hams that rent that would love to be in your position.

As Phil correctly asks, why do you need an earth connection? Here are some possible reasons to be thinking about earthing in your situation.

**Common Mode Current**

An OCF antenna is an inherently imbalanced antenna. Such an antenna directly fed with coax will likely cause common mode current to flow on the shield of the coax. The effects from common mode current can include:

- RF shocks or burns from the touching the transceiver, microphone, or power supply when transmitting
- Interference to nearby electronic devices such as headphones, speakers, stereos, smoke alarms, PCs, etc. when transmitting
- Problems bringing the SWR into specification
- Short adjustments to the length of coax cable or simply touching the coax cable causes changes in the SWR
- Interference from local electronics devices such as TVs, PCs, routers, etc. getting into your receiver during receive
- The antenna pattern does not exhibit the expected behavior

If you experience any of these issues, you may be able to reduce the common mode current by installing a high quality, 1:1, *current* balun at the feedpoint of the antenna. There is virtually no downside to such a balun so it is often recommended as a preventative measure.

Make certain that the length of your coax cable is not an odd multiple of a quarter wavelength on any bands on which you wish to operate. Incorporate a +/- 5% safety margin in your length calculations.

For severe cases, placing another 1:1 current balun on the coax just before it enters the shack may prove helpful. These are sometimes called "isolation baluns" or similar to indicate that both sets of connections are SO-239s to facilitate easy coaxial connections.

**Lightning Protection**

Lightning protection mechanisms and its associated earthing (grounding) system are often controlled by local code or regulations. In much of the USA, for example, the NEC specifies minimum lightning protection requirements. Many hams will install a static discharge unit on the coaxial cable which is bonded to a field of specially installed ground rods. These rods must then be properly bonded to the facility's electrical safety ground system.

Due to the very high di/dt characteristics of lightning, an effective protection system utilizes very short, low resistance, low inductance connections in order to shunt as much current as possible to the ground field in order to mitigate potentially large voltage spikes. All internal shack equipment should be connected to the common lightning ground connection through an equipotential connection point. A shack located on a fourth floor makes all of this a very difficult task. In such situations, you must often make due with the best that you can. If you can run a large gauge ground wire down to a ground rod below your window, this might suffice for your lightning ground connection. Connecting to the safety ground of the apartment wiring is a last resort and will probably be minimally beneficial. But do consult your local codes and regulations to make certain you are in compliance.

If you simply cannot install an effective lightning protection system, then try to leave your antenna disconnected from the station when not in use and when lightning is in the vicinity. Ideally the entire coax should be moved outside of the building when not in use so as to keep any lightning or static discharge current as far away as possible from the shack equipment, occupants, and furnishings.

**Safety Ground**

The mains circuits in most modern buildings include a safety ground as part of the wiring and this is brought out as a ground or earth pin on the respective outlets. The purpose of this ground is to provide a safe return of AC current in the event of a wiring failure elsewhere in the system or in the connected device.

From a ham radio perspective, most modern equipment is powered by a 12 volt AC to DC power supply so the mains circuit and its safety ground terminates in one place within this supply. The need to further bond the chassis of all other low voltage equipment to the safety ground is largely a carryover from the days of tubed equipment and may not be warranted. If the equipment chassis are already connected to an equipotential ground point for lightning protection, then further connecting to the mains ground can introduce unintended ground loops. Some of the DC power supplies no longer connect the minus 12 volt pin to the chassis of the supply for this reason (if permitted by local regulations).

Some local regulations may require specific inter-equipment safety ground wiring so always make sure to consult your local regulations or a knowledgeable electrician before finalizing your installation.

**Further Reading**

The ARRL recently published a new book that covers all aspects of station grounding: Grounding and Bonding for the Radio Amateur by Ward Silver. The book does a nice job of summarizing best practices in all aspects of safety, lightning, and RF grounds.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10251/electrical-earth, by user7286370, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
