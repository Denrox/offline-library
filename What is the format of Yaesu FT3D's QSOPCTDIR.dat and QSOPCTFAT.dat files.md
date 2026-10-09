# What is the format of Yaesu FT3D's QSOPCTDIR.dat and QSOPCTFAT.dat files?

*Tags: digital-modes, yaesu, software-development · score 3*

## Question

The Yaesu FT3D can send photos, but only if taken with the optional external mic that has a camera. I want to be able to send photos that come from elsewhere, by putting them on the SD card.

But it seems that in addition to putting the jpeg (320x240, max size 40kB, says the video below) on the SD card, you also have to put these into two index files, named QSOPCTDIR.dat and QSOPCTFAT.dat.

It is supposedly possible to do this if you run Windows, with a free of cost program. See this video. I see comments on that video of people failing to use this method even on Windows with the FT3D, though.

It's probably the same format as for audio recordings, which I have examples of:

```
$ od -txC /mnt/tmp/QSOLOG/QSOWAVDIR.dat
0000000 00 00 00 00 20 20 20 20 20 20 20 20 20 20 20 20
0000020 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20
0000040 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 03
0000060 06 19 19 00 00 00 00 00 00 00 00 00 00 00 00 00
0000100 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20
0000120 00 00 00 00 32 30 30 33 30 36 31 39 31 39 33 39
0000140 2e 77 61 76 ff ff ff ff ff ff ff ff ff ff ff ff
0000160 ff ff ff ff ff ff ff ff 00 00 00 00 00 00 00 00
0000200 00 00 00 00 20 20 20 20 20 20 20 20 20 20 20 20
0000220 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20
0000240 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 03
0000260 17 20 33 00 00 00 00 00 00 00 00 00 00 00 00 00
0000300 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20 20
0000320 00 00 00 00 32 30 30 33 31 37 32 30 33 33 30 31
0000340 2e 77 61 76 ff ff ff ff ff ff ff ff ff ff ff ff
0000360 ff ff ff ff ff ff ff ff 00 00 00 00 00 00 00 00
0000400
$ od -txC /mnt/tmp/QSOLOG/QSOWAVFAT.dat
0000000 40 00 00 00 40 00 00 80
0000010

```

Clearly the QSOxxxDIR.dat file contains the file name, but what could the rest be? And that's even assuming the QSOPCTDIR.* files look like QSOWAVDIR.* files. Since I have no photos (nor the optional external Yaesu camera), I have no example files. Both files are 0 bytes.

What could this file format be? Given specs I could easily make a tool to create them.

## Answer (score 2, by Gabriel)

```
$ od -txC QSOPCTDIR.dat
0000000    60  00  00  08  20  20  20  20  20  41  4c  4c  20  20  20  20
0000020    20  20  20  20  20  20  20  20  20  45  41  47  4a  44  52  32
0000040    41  55  49  20  20  20  20  20  20  20  20  20  20  20  20  08
0000060    30  20  30  00  20  08  30  20  30  00  20  08  30  19  43  00
0000100    32  30  32  30  2f  30  38  2f  33  30  20  31  39  3a  34  33
0000120    00  00  2f  35  48  45  41  36  34  63  30  30  30  30  30  31
0000140    2e  6a  70  67  ff  ff  ff  ff  ff  ff  ff  ff  ff  ff  ff  ff
0000160    ff  ff  ff  ff  ff  ff  ff  ff  00  00  00  00  00  00  00  00
0000200

$ od -txC QSOPCTFAT.dat
0000000    40  00  00  00
0000004

```

I've also found this spreadsheet that might help

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16534/what-is-the-format-of-yaesu-ft3d-s-qsopctdir-dat-and-qsopctfat-dat-files, by Thomas, Gabriel. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
