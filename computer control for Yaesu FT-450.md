# computer control for Yaesu FT-450

*Tags: yaesu, remote-control, computer-aided-transceiver, ft-450d · score 5*

## Question

I just acquired a Yaesu FT-450 and am interested in what it can do when connected to my PC.

I see that there is programming software available with which one can load information into the 450's memory from a spreadsheet-like file, which would be much easier than keying the data in via the buttons on the 450 front panel.

But does anybody know if there is a program available which essentially emulates a software-defined radio for the 450- that is, something that maps all the control functionality of the 450 onto the screen of the 450, so it can be operated in real-time through the keyboard and mouse?

## Answer (score 4, by Adam KC0DAD)

I'm not aware of an application that has full control of every feature. However, there are a variety of applications available that work for basic functions. FLRIG will give you many of the most common features. I use the related program, FLDigi, for operating digital modes with my FT-450D. Its rig control is sufficient that I don't generally have to turn back to my radio.

BTW, be careful about using the term software-defined radio. I understand you to mean you want software that lets you control the radio. The term software-defined radio more commonly refers to a radio that performs filtering and shaping functions in software rather than hardware. The FT-450D (and I believe the FT-450) is actually such a radio. The radio control you are asking for is commonly called "rig control" or some-times "rig-cat".

## Answer (score 3, by Farren)

Yaesu makes software like what you're looking for: Go the yaesu.com and find the FT-450D page, click on the Files tab, and look for: PCC-450 Software V1.13 and Reference Manual (07/18/14)

The PCC-450 software runs on Windows and connects to the radio over a serial port. You can drive nearly every feature of the radio. I find it easier to use this software than to go through the radio menus.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9489/computer-control-for-yaesu-ft-450, by niels nielsen, Adam KC0DAD, Farren. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
