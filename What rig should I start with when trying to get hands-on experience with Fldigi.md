# What rig should I start with when trying to get hands-on experience with Fldigi?

*Tags: digital-modes, software, equipment, fldigi · score 3*

## Question

I would like to get hands-on experience with Fldigi. What setup is recommendable?

## Accepted answer (score 4, by Phil Frost - W8II)

Nearly any SSB HF rig will do.

You need some way to get audio out of the receiver and into your computer, and out of your computer and into the transmitter. Most modern transceivers provide some kind of connection for this. In a pinch, you can use the headphone and microphone connections.

It's also convenient (through not necessary) if Fldigi can key the radio for you. With some fiddling, you can usually rig up something that uses one of the control lines on a serial port to control a relay or optioisolator to key the radio. Methods vary based on the radio, so just search the internets for a rig you are considering.

Even better is to get a rig which supports control over a serial connection. Fldigi uses hamlib, so anything supported by hamlib will work. Usually there's a serial port on the back of the radio, and if you don't have a serial port on your computer a USB cable can be had for $20 or so.

Get the list of supported radios by running rigctl -l. Your version might be different, but I get:

```
Rig #  Mfg                    Model                   Version         Status
 1  Hamlib                 Dummy                   0.5             Beta
 2  Hamlib                 NET rigctl              0.3             Beta
 101  Yaesu                  FT-847                  0.5             Beta
 103  Yaesu                  FT-1000D                0.0.6           Alpha
 104  Yaesu                  MARK-V FT-1000MP        0.0.5           Alpha
 105  Yaesu                  FT-747GX                0.4.1           Beta
 106  Yaesu                  FT-757GX                0.4.1           Beta
 107  Yaesu                  FT-757GXII              0.4             Stable
 109  Yaesu                  FT-767GX                1.0             Stable
 110  Yaesu                  FT-736R                 0.3             Stable
 111  Yaesu                  FT-840                  0.1             Untested
 113  Yaesu                  FT-900                  0.1             Untested
 114  Yaesu                  FT-920                  2010-08-23      Stable
 115  Yaesu                  FT-890                  0.1             Stable
 116  Yaesu                  FT-990                  0.2.1           Alpha
 117  Yaesu                  FRG-100                 0.4             Beta
 118  Yaesu                  FRG-9600                0.2             Untested
 119  Yaesu                  FRG-8800                0.2             Untested
 120  Yaesu                  FT-817                  0.5.1           Beta
 121  Yaesu                  FT-100                  0.4.1           Beta
 122  Yaesu                  FT-857                  0.4             Beta
 123  Yaesu                  FT-897                  0.3.3           Beta
 124  Yaesu                  FT-1000MP               0.1.1           Beta
 125  Yaesu                  MARK-V Field FT-1000MP  0.0.5           Alpha
 126  Yaesu                  VR-5000                 0.2             Alpha
 127  Yaesu                  FT-450                  0.22.1          Beta
 128  Yaesu                  FT-950                  0.22.2          Stable
 129  Yaesu                  FT-2000                 0.22.1          Stable
 130  Yaesu                  FTDX-9000               0.22.1          Untested
 131  Yaesu                  FT-980                  0.1             Alpha
 132  Yaesu                  FT-DX5000               0.22            Alpha
 133  Vertex Standard        VX-1700                 1.1             Alpha
 201  Kenwood                TS-50S                  0.8             Untested
 202  Kenwood                TS-440                  0.8.0.6.1       Alpha
 203  Kenwood                TS-450S                 0.8.1           Beta
 204  Kenwood                TS-570D                 0.8.2           Stable
 205  Kenwood                TS-690S                 0.8.1           Beta
 206  Kenwood                TS-711                  0.8.0.6.1       Untested
 207  Kenwood                TS-790                  0.8.2           Alpha
 208  Kenwood                TS-811                  0.8.0.6.1       Untested
 209  Kenwood                TS-850                  0.8.1           Beta
 210  Kenwood                TS-870S                 0.8.0           Beta
 211  Kenwood                TS-940S                 0.8.0.6.1       Alpha
 213  Kenwood                TS-950SDX               0.8             Beta
 214  Kenwood                TS-2000                 0.8.4           Beta
 215  Kenwood                R-5000                  0.6.1           Alpha
 216  Kenwood                TS-570S                 0.8.1           Stable
 217  Kenwood                TH-D7A                  0.5             Alpha
 219  Kenwood                TH-F6A                  0.5             Beta
 220  Kenwood                TH-F7E                  0.5.1           Beta
 221  Elecraft               K2                      20120615        Beta
 222  Kenwood                TS-930                  0.8             Untested
 223  Kenwood                TH-G71                  0.5             Beta
 224  Kenwood                TS-680S                 0.8.1           Beta
 225  Kenwood                TS-140S                 0.8.1           Beta
 226  Kenwood                TM-D700                 0.5             Beta
 227  Kenwood                TM-V7                   0.5             Beta
 228  Kenwood                TS-480                  0.8.5           Untested
 229  Elecraft               K3/KX3                  20120615        Beta
 230  Kenwood                TRC-80                  0.8             Alpha
 231  Kenwood                TS-590S                 0.8.1           Beta
 232  SigFox                 Transfox                20111223        Alpha
 233  Kenwood                TH-D72A                 0.5.1           Alpha
 234  Kenwood                TM-D710                 0.5             Untested
 302  Icom                   IC-1275                 0.7             Beta
 303  Icom                   IC-271                  0.7             Untested
 304  Icom                   IC-275                  0.7.1           Beta
 306  Icom                   IC-471                  0.7             Untested
 307  Icom                   IC-475                  0.7.1           Beta
 309  Icom                   IC-706                  0.7.1           Untested
 310  Icom                   IC-706MkII              0.7.1           Untested
 311  Icom                   IC-706MkIIG             0.7.2           Stable
 312  Icom                   IC-707                  0.7             Untested
 313  Icom                   IC-718                  0.7.1           Beta
 314  Icom                   IC-725                  0.7.1           Stable
 315  Icom                   IC-726                  0.7             Stable
 316  Icom                   IC-728                  0.7             Untested
 319  Icom                   IC-735                  0.7.1           Beta
 320  Icom                   IC-736                  0.7             Untested
 321  Icom                   IC-737                  0.7             Untested
 322  Icom                   IC-738                  0.7             Untested
 323  Icom                   IC-746                  0.7.1           Beta
 324  Icom                   IC-751                  0.7.1           Beta
 326  Icom                   IC-756                  0.7.1           Alpha
 327  Icom                   IC-756PRO               0.7             Untested
 328  Icom                   IC-761                  0.7.1           Stable
 329  Icom                   IC-765                  0.7             Stable
 330  Icom                   IC-775                  0.7.1           Untested
 331  Icom                   IC-781                  0.7.1           Untested
 332  Icom                   IC-820H                 0.7             Alpha
 334  Icom                   IC-821H                 0.7             Alpha
 335  Icom                   IC-970                  0.7             Untested
 336  Icom                   IC-R10                  0.7             Untested
 337  Icom                   IC-R71                  0.7             Untested
 338  Icom                   IC-R72                  0.7             Untested
 339  Icom                   IC-R75                  0.7             Beta
 340  Icom                   IC-R7000                0.7.0           Alpha
 341  Icom                   IC-R7100                0.7.0           Untested
 342  Icom                   ICR-8500                0.7.1           Beta
 343  Icom                   IC-R9000                0.7.1           Alpha
 344  Icom                   IC-910                  0.7.1           Beta
 345  Icom                   IC-78                   0.7             Untested
 346  Icom                   IC-746PRO               0.7             Stable
 347  Icom                   IC-756PROII             0.7             Alpha
 351  Ten-Tec                Omni VI Plus            0.2             Beta
 352  Optoelectronics        OptoScan535             0.3             Beta
 353  Optoelectronics        OptoScan456             0.3             Beta
 354  Icom                   IC ID-1                 0.7             Untested
 355  Icom                   IC-703                  0.7             Untested
 356  Icom                   IC-7800                 0.7.2           Untested
 357  Icom                   IC-756PROIII            0.7.1           Beta
 358  Icom                   IC-R20                  0.7             Untested
 360  Icom                   IC-7000                 0.7.2           Beta
 361  Icom                   IC-7200                 0.7             Beta
 362  Icom                   IC-7700                 0.7.1           Stable
 363  Icom                   IC-7600                 0.7             Beta
 364  Ten-Tec                Delta II                0.1             Untested
 365  Icom                   IC-92D                  0.7             Untested
 366  Icom                   IC-R9500                0.7.1           Untested
 367  Icom                   IC-7410                 0.7             Untested
 368  Icom                   IC-9100                 0.7             Untested
 369  Icom                   IC-RX7                  0.7             Untested
 401  Icom                   IC-PCR1000              0.8             Beta
 402  Icom                   IC-PCR100               0.8             Beta
 403  Icom                   IC-PCR1500              0.8             Beta
 404  Icom                   IC-PCR2500              0.8             Beta
 501  AOR                    AR8200                  0.6.1           Alpha
 502  AOR                    AR8000                  0.6.1           Beta
 503  AOR                    AR7030                  0.4.1           Beta
 504  AOR                    AR5000                  0.6.1           Beta
 505  AOR                    AR3030                  0.4             Untested
 506  AOR                    AR3000A                 0.5             Beta
 508  AOR                    AR2700                  0.6             Untested
 513  AOR                    AR8600                  0.6.1           Beta
 514  AOR                    AR5000A                 0.6             Alpha
 515  AOR                    AR7030 Plus             0.1             Beta
 516  AOR                    SR2200                  0.1             Beta
 605  JRC                    NRD-525                 0.1             Alpha
 606  JRC                    NRD-535D                0.6             Stable
 607  JRC                    NRD-545 DSP             0.6             Beta
 801  Uniden                 BC780xlt                0.3             Untested
 802  Uniden                 BC245xlt                0.3             Untested
 803  Uniden                 BC895xlt                0.3             Untested
 804  Radio Shack            PRO-2052                0.3             Untested
 806  Uniden                 BC250D                  0.3             Untested
 810  Uniden                 BCD-396T                0.3             Alpha
 811  Uniden                 BCD-996T                0.3             Alpha
 812  Uniden                 BC898T                  0.3             Untested
 902  Drake                  R-8A                    0.5.1           Beta
 903  Drake                  R-8B                    0.5             Untested
 1004  Lowe                   HF-235                  0.3             Alpha
 1103  Racal                  RA6790/GM               0.1             Untested
 1105  Racal                  RA3702                  0.1             Alpha
 1204  Watkins-Johnson        WJ-8888                 0.2             Untested
 1402  Skanti                 TRP8000                 0.2             Untested
 1404  Skanti                 TRP 8255 S R            0.1             Untested
 1501  Winradio               WR-1000                 0.6             Untested
 1502  Winradio               WR-1500                 0.6             Untested
 1503  Winradio               WR-1550                 0.6             Untested
 1504  Winradio               WR-3100                 0.6             Untested
 1505  Winradio               WR-3150                 0.6             Untested
 1506  Winradio               WR-3500                 0.6             Untested
 1507  Winradio               WR-3700                 0.6             Untested
 1601  Ten-Tec                TT-550                  0.2             Beta
 1602  Ten-Tec                TT-538 Jupiter          0.6             Beta
 1603  Ten-Tec                RX-320                  0.6             Stable
 1604  Ten-Tec                RX-340                  0.3             Untested
 1605  Ten-Tec                RX-350                  0.1             Untested
 1607  Ten-Tec                TT-516 Argonaut V       0.2             Stable
 1608  Ten-Tec                TT-565 Orion            0.5             Beta
 1609  Ten-Tec                TT-585 Paragon          0.3             Beta
 1611  Ten-Tec                TT-588 Omni VII         0.3             Alpha
 1612  Ten-Tec                RX-331                  0.1             Beta
 1613  Ten-Tec                TT-599 Eagle            0.4             Untested
 1701  Alinco                 DX-77                   0.7             Beta
 1801  Kachina                505DSP                  0.3             Alpha
 1901  Hamlib                 RPC rig                 0.3             Beta
 2201  TAPR                   DSP-10                  0.2             Alpha
 2301  Flex-radio             SDR-1000                0.2             Untested
 2303  DTTS Microwave Society DttSP IPC               0.2             Alpha
 2304  DTTS Microwave Society DttSP UDP               0.2             Alpha
 2401  RFT                    EKD-500                 0.4             Alpha
 2501  Elektor                Elektor 3/04            0.4             Stable
 2502  SAT-Schneider          DRT1                    0.2             Beta
 2503  Coding Technologies    Digital World Traveller 0.1             Untested
 2506  AmQRP                  DDS-60                  0.1             Alpha
 2507  Elektor                Elektor SDR-USB         0.3.1           Stable
 2508  mRS                    miniVNA                 0.1             Alpha
 2509  SoftRock               Si570 AVR-USB           0.2             Beta
 2511  KTH-SDR kit            Si570 PIC-USB           0.2             Beta
 2512  FiFi                   FiFi-SDR                0.5             Beta
 2513  AMSAT-UK               FUNcube Dongle          0.2             Beta
 2514  N2ADR                  HiQSDR                  0.2             Untested
 2601  Video4Linux            SW/FM radio             0.2.1           Beta
 2602  Video4Linux2           SW/FM radio             0.2.1           Alpha
 2701  Rohde&Schwarz          ESMC                    0.1             Alpha
 2702  Rohde&Schwarz          EB200                   0.1             Untested
 2801  Philips/Simoco         PRM8060                 0.1             Alpha
 2901  ADAT www.adat.ch       ADT-200A                1.36            Beta

```

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/3815/what-rig-should-i-start-with-when-trying-to-get-hands-on-experience-with-fldig, by rvaneijk, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
