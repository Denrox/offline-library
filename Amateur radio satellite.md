# Amateur radio satellite

An **amateur radio satellite** is an artificial satellite built and used by [amateur radio operators](Amateur%20radio%20operator.md). It forms part of the Amateur-satellite service. These satellites use [amateur radio frequency allocations](Amateur%20radio%20frequency%20allocations.md) to facilitate communication between [amateur radio](Amateur%20radio.md) stations.

Many amateur satellites receive an **OSCAR** designation, which is an acronym for **Orbiting Satellite Carrying Amateur Radio**. The designation is assigned by AMSAT, an organization which promotes the development and launch of amateur radio satellites. Because of the prevalence of this designation, amateur radio satellites are often referred to as OSCARs.

These satellites can be used free of charge by licensed amateur radio operators for voice ([FM](Frequency%20modulation.md), [SSB](Single-sideband%20modulation.md)) and data ([AX.25](AX.25.md), [packet radio](Packet%20radio.md), [APRS](Automatic%20Packet%20Reporting%20System.md)) communications. Currently, over 18 fully operational amateur radio satellites are in orbit. They may be designed to act as [repeaters](Repeater.md), as linear transponders, and as store and forward digital relays.

Amateur radio satellites have helped advance the science of satellite communications. Contributions include the launch of the first satellite voice transponder (OSCAR 3) and the development of highly advanced digital "store-and-forward" messaging transponder techniques.

The Amateur Radio Satellite community is very active in building satellites and in finding launch opportunities. Lists of functioning satellites need updating regularly, as new satellites are launched and older ones fail. Current information is published by AMSAT. AMSAT has not been actively involved in the launch and operation of most amateur satellites in the last two decades beyond allocating an OSCAR number.

### Hardware

The first amateur satellites contained telemetry beacons. Since 1965, most OSCARs carry a linear transponder for two-way communications in real time. Some satellites have a bulletin board for store-and-forward digital communications, or a digipeater for direct [packet radio](Packet%20radio.md) connections.

### Orbits

Amateur satellites have been launched into low Earth orbits and into highly elliptical orbits.

### Operations

#### Satellite communications

Currently, amateur satellites support many different types of operation, including [FM](Frequency%20modulation.md) voice and [SSB](Single-sideband%20modulation.md) voice, as well as digital communications of [AX.25](AX.25.md) [FSK](Frequency-shift%20keying.md) ([Packet radio](Packet%20radio.md)) and [PSK-31](PSK31.md).

##### Mode designators

Uplink and downlink designations use sets of paired letters following the structure **X/Y** where **X** is the uplink band and **Y** is the downlink band. Occasionally, the downlink letter is rendered in lower case (i.e., **X/y**). With a few exceptions, the letters correspond to IEEE's standard for radar frequency letter bands:  
  
- Designator

**HAVULSS2CXKR**

- Band   15 m   10 m   2 m   70 cm   23 cm   13 cm   9 cm   5 cm   3 cm   1.2 cm   6 mm
- Frequency  
(General)   21 MHz   29 MHz   145 MHz   435 MHz   1.2 GHz   2.4 GHz   3.4 GHz   5 GHz   10 GHz   24 GHz   47 GHz

Prior to the launch of OSCAR 40, operating modes were designated using single letters to indicate both uplink and downlink bands. While deprecated, these older mode designations are still widely used in casual conversation.  
  
- Mode A: [2 m](2-meter%20band.md) uplink / [10 m](10-meter%20band.md) downlink
- Mode B: [70 cm](70-centimeter%20band.md) uplink / 2 m downlink
- Mode J: 2 m uplink / 70 cm downlink

##### Doppler shift

Due to the high orbital speed of the amateur satellites, the uplink and downlink frequencies will vary during the course of a satellite pass. This phenomenon is known as the Doppler effect. While the satellite is moving towards the ground station, the downlink frequency will appear to be *higher* than normal. Hence, the receiver frequency at the ground station must be adjusted *higher* to continue receiving the satellite. The satellite in turn, will be receiving the uplink signal at a *higher* frequency than normal so the ground station's transmitted uplink frequency must be *lower* to be received by the satellite. After the satellite passes overhead and begins to move away, this process is reversed. The downlink frequency will appear *lower* and the uplink frequency will need to be adjusted *higher*. The following mathematical formulas relate the Doppler shift to the velocity of the satellite.

- Where:
- $$f_d$$  =  doppler corrected downlink frequency
- $$f_u$$  =  doppler corrected uplink frequency
- $$f$$  =  original frequency
- $$v$$  =  velocity of the satellite relative to ground station in m/s.  
Positive when moving towards, negative when moving away.
- $$c$$  =  the speed of light in a vacuum ($$3\times10^8$$ m/s).

- Change in frequency  Downlink Correction  Uplink Correction

$$
\Delta f=f\times\frac{v}{c}
$$

$$
f_d=f(1+\frac{v}{c})
$$

$$
f_u=f(1-\frac{v}{c})
$$

Due to the complexity of finding the relative velocity of the satellite and the speed with which these corrections must be made, these calculations are normally accomplished using satellite tracking software. Many modern [transceivers](Transceiver.md) include a computer interface that allows for automatic doppler effect correction. Manual frequency-shift correction is possible, but it is difficult to remain precisely near the frequency. [Frequency modulation](Frequency%20modulation.md) is more tolerant of doppler shifts than single-sideband, and therefore FM is much easier to tune manually.

#### FM satellites

A number of low Earth orbit (LEO) OSCAR satellites use [frequency modulation](Frequency%20modulation.md) (FM). These are also commonly referred to as "FM LEOs" or the "FM Birds". Such satellites act as FM [amateur radio repeaters](Amateur%20radio%20repeater.md) that can be communicated through using commonly available amateur radio equipment. Communication can be achieved with handheld transceivers using manual doppler correction. Satellite passes are typically less than 15 minutes long.

### Launches

#### Past launches

The names of the satellites below are sorted in chronological order by launch date, ascending. The status column denotes the current operational status of the satellite. **Green** signifies that the satellite is currently operational, **orange** indicates that the satellite is partially operational or failing.  **Red** indicates that the satellite is non operational and  **black** indicates that the satellite has re-entered the Earth's atmosphere (or never successfully left it). The *country* listing denotes the country that constructed the satellite and not the launching country.

- Launches (past and current)
- Name   Status   Launched   Country
- OSCAR (OSCAR 1)   Decayed   1961-12-12    United States
- OSCAR II (OSCAR 2)   Decayed   1962-06-02    United States
- OSCAR III (OSCAR 3, EGRS-3)   Non-Operational   1965-03-09    United States
- OSCAR IV (OSCAR 4)   Decayed   1965-12-21    United States
- Australis-OSCAR 5 (OSCAR 5, AO-5, AO-A)   Non-Operational   1970-01-23    Australia
- AMSAT-OSCAR 6 (OSCAR 6, AO-6, AO-C, P2A)   Non-Operational   1972-10-15    United States
- AMSAT-OSCAR 7 (OSCAR 7, AO-7, AO-B, P2B)   Semi-Operational   1974-11-15    United States
- AMSAT-OSCAR 8 (OSCAR 8, AO-8, AO-D, P2D)   Non-Operational   1978-03-05    United States
- Radio Sputnik 1 (RadioSkaf-1, RS-1)   Non-Operational   1978-10-26    Soviet Union
- Radio Sputnik 2 (RadioSkaf-2, RS-2)   Non-Operational   1978-10-26    Soviet Union
- UoSat-OSCAR 9 (UOSAT 1, UO-9)   Decayed   1981-10-06    United Kingdom
- Radio Sputniks RS3 through RS8   Non-Operational   1981-12-17    Soviet Union
- AMSAT-OSCAR 10 (Phase 3B, AO-10, P3B)   Non-Operational   1983-06-16    United States  
West Germany
- UoSat-OSCAR 11 (UoSat-2, UO-11, UoSAT-B)   Semi-Operational   1984-03-01    United Kingdom
- Fuji-OSCAR 12 (JAS 1, FO-12)   Non-Operational   1986-08-12    Japan
- Radio Sputnik 10/11 (RadioSkaf-10/11, RS-10/11, COSMOS 1861)   Non-Operational   1987-06-23    Soviet Union
- AMSAT-OSCAR 13 (Phase 3C, AO-13, P3C)   Decayed   1988-06-15    West Germany
- UOSAT-OSCAR 14 (UoSAT-3, UO-14 UoSAT-D)   Non-Operational   1990-01-22    United Kingdom
- UOSAT-OSCAR 15 (UoSAT-4, UO-15, UoSAT-E)   Non-Operational   1990-01-22    United Kingdom
- AMSAT-OSCAR 16 (Pacsat, AO-16, Microsat-1)   Semi-Operational   1990-01-22    United States
- Dove-OSCAR 17 (Dove, DO-17, Microsat-2)   Non-Operational   1990-01-22    Brazil
- Weber-OSCAR 18 (WeberSAT, WO-18, Microsat-3)   Non-Operational   1990-01-22    United States
- LUSAT-OSCAR 19 (LUSAT, LO-19, Microsat-4)   Non-Operational   1990-01-22    Argentina
- Fuji-OSCAR 20 (JAS 1B, FO-20, Fuji-1B)   Non-Operational   1990-02-07    Japan
- AMSAT-OSCAR 21 (RS-14, AO-21, Informator-1)   Non-Operational   1991-01-29    Soviet Union
- Radio Sputnik 12/13 (RadioSkaf-12/13, RS-12/13, COSMOS 2123)   Non-Operational   1991-02-05    Soviet Union
- UoSat-OSCAR 22 (UOSAT 5, UO-22 UoSAT-F)   Non-Operational   1991-07-17    United Kingdom
- KitSAT-OSCAR 23 (KITSAT 1, KO-23, Uribyol-1)   Non-Operational   1992-08-10    South Korea
- Arsene-OSCAR 24 (Arsene, AO-24)   Non-Operational   1993-05-12    France
- KitSAT-OSCAR 25 (KITSAT B, KO-25, Kitsat-2, Uribyol-2)   Non-Operational   1993-09-26    South Korea
- Italy-OSCAR 26 (ITAMSAT, IO-26)   Non-Operational   1993-09-26    Italy
- AMRAD-OSCAR 27 (EYESAT-1, AO-27)   Non-Operational   1993-09-26    United States
- POSAT-OSCAR 28 (POSAT, PO-28, Posat-1)   Non-Operational   1993-09-26    Portugal
- Radio Sputnik 15 (RadioSkaf-15, RS-15, Radio-ROSTO)   Semi-Operational   1994-12-26    Russia
- Fuji-OSCAR 29 (JAS 2, FO-29, Fuji-2)   Semi-Operational   1996-08-17    Japan
- Mexico-OSCAR 30 (UNAMSAT-2, MO-30, Unamsat-B, Kosmos-2334)   Non-Operational   1996-09-05    Mexico  
Russia
- Sputnik 40   Decayed   1997-11-03    France/ Russia
- Thai-Microsatellite-OSCAR 31 (TMSAT-1, TO-31)   Non-Operational   1998-07-10    Thailand
- Gurwin-OSCAR 32 Archived 2012-02-29 at the Wayback Machine (GO-32, Gurwin-1b, Techsat-1b)   Non-Operational   1998-07-10    Israel
- SEDSat-OSCAR 33 (SEDSat, SO-33, SEDsat-1)   Semi-Operational   1998-10-24    United States
- Pansat-OSCAR 34 (PAN SAT, PO-34)   Non-Operational   1998-10-29    United States
- Sputnik 41   Decayed   1997-11-03    France/ Russia
- Sunsat-OSCAR 35 (SUNSAT, SO-35)   Non-Operational   1999-02-23    South Africa
- UoSat-OSCAR 36 (UOSAT 12, UO-36)   Non-Operational   1999-04-21    United Kingdom
- ASU-OSCAR 37 (AO-37, ASUsat-1, ASUSAT)   Non-Operational   2000-01-27    United States
- OPAL-OSCAR 38 (OO-38, StenSat, OPAL)   Non-Operational   2000-01-27    United States
- Weber-OSCAR 39 (WO-39, JAWSAT)   Non-Operational   2000-01-27    United States
- Saudi-OSCAR 41 (SO-41, Saudisat 1A)   Non-Operational   2000-09-26    Saudi Arabia
- Saudi-OSCAR 42 (SO-42, Saudisat 1B)   Non-Operational   2000-09-26    Saudi Arabia
- Malaysian-OSCAR 46 (MO-46, TIUNGSAT-1)   Non-Operational   2000-09-26    Malaysia
- AMSAT-OSCAR 40 (AO-40, Phase 3D, P3D)   Non-Operational   2000-11-16    United States
- Starshine-OSCAR 43 (SO-43, Starshine 3)   Decayed   2001-09-30    United States
- Navy-OSCAR 44 (NO-44, PCSat)   Semi-Operational   2001-09-30    United States
- Navy-OSCAR 45 (NO-45, Sapphire)   Non-Operational   2001-09-30    United States
- BreizhSAT-OSCAR 47 (BO-47, IDEFIX CU1)   Non-Operational   2002-05-04    France
- BreizhSAT-OSCAR 48 (BO-48, IDEFIX CU2)   Non-Operational   2002-05-04    France
- AATiS-OSCAR 49 (AO-49, Safir-M, RUBIN 2)   Non-Operational   2002-12-20    Germany
- Saudi-OSCAR 50 (SO-50, Saudisat-1C)   Operational   2002-12-20    Saudi Arabia
- CubeSat-OSCAR 55 Archived 2012-02-29 at the Wayback Machine (Cute-1)   Operational   2003-06-30    Japan
- CubeSat-OSCAR 57 (CubeSat-XI-IV)   Operational   2003-06-30    Japan
- CanX-1   Non-Operational   2003-06-30    Canada
- DTUSat   Decayed   2003-06-30    Denmark
- AAU Cubesat   Non-Operational   2003-06-30    Denmark
- RS-22 Archived 2012-02-29 at the Wayback Machine (Mozhayets 4)   Operational   2003-09-27    Russia
- AMSAT-OSCAR 51 (Echo, AO-51)   Non-Operational   2004-06-28    United States
- VUSat-OSCAR 52 (HAMSAT, VO-52, VUSat)   Non-Operational    2005-05-05    India  
Netherlands
- PCSat2 (PCSAT2)   Decayed   2005-08-03    United States
- AMSAT-OSCAR 54 (AO-54, SuitSat, Radioskaf)   Decayed   2005-09-08   International
- eXpress-OSCAR 53 (XO-53, SSETI Express)   Non-Operational   2005-10-27   European Space Agency
- CubeSat-OSCAR 58 (CO-58, Cubesat XI-V)   Non-Operational   2005-10-27    Japan
- UWE-1   Non-Operational   2005-10-27    Germany
- NCube-2   Deployment failure   2005-10-27    Norway
- CubeSat-OSCAR 56 (CO-56, Cute-1.7)   Non-Operational   2006-02-21    Japan
- K7RR-Sat   Launch Failure   2006-07-26    United States
- CP2   Launch Failure   2006-07-26    United States
- HAUSAT 1   Launch Failure   2006-07-26    South Korea
- ICE Cube 1   Launch Failure   2006-07-26    United States
- ICE Cube 2   Launch Failure   2006-07-26    United States
- ION   Launch Failure   2006-07-26    United States
- KUTESat   Launch Failure   2006-07-26    United States
- MEROPE   Launch Failure   2006-07-26    United States
- nCUBE 1   Launch Failure   2006-07-26    Norway
- RINCON   Launch Failure   2006-07-26    United States
- SACRED   Launch Failure   2006-07-26    United States
- SEEDS   Launch Failure   2006-07-26    Japan
- Voyager (Mea Huaka'i)   Launch Failure   2006-07-26    United States
- PicPot   Launch Failure   2006-07-26    Italy
- HITSat-OSCAR 59 (HITSat, HO-59)   Decayed   2006-09-22    Japan
- GeneSat-1 Archived 2011-07-16 at the Wayback Machine   Decayed   2006-12-16    United States
- Navy-OSCAR 60 (RAFT, NO-60)   Decayed   2006-12-21    United States
- Navy-OSCAR 61 (ANDE, NO-61)   Decayed   2006-12-21    United States
- Navy-OSCAR 62 (FCAL, NO-62)   Decayed   2006-12-21    United States
- FalconSAT-3   Decayed   2007-03-09    United States
- Libertad-1   Non-Operational   2007-04-17    Colombia
- CAPE-1   Non-Operational   2007-04-17    United States
- CP3   Non-Operational   2007-04-17    United States
- CP4   Non-Operational   2007-04-17    United States
- Pehuensat-OSCAR 63 (PEHUENSAT-1, PO-63)   Decayed   2007-10-01    Argentina
- Delfi-OSCAR 64 (Delfi-C3, DO-64)   Decayed   2008-04-28    Netherlands
- Cubesat-OSCAR 65 (Cute-1.7+APD II, CO-65)   Operational?   2008-04-28    Japan
- Cubesat-OSCAR 66 (SEED II, CO-66)   Operational   2008-04-28    Japan
- COMPASS-1   Semi-Operational   2008-04-28    Germany
- RS-30 Archived 2012-02-29 at the Wayback Machine (Yubileiny, RS-30)   Operational   2008-05-23    Russia
- PRISM Archived 2012-10-25 at the Wayback Machine (HITOMI)   Decayed   2009-01-23    Japan
- KKS-1 Archived 2012-02-29 at the Wayback Machine (KISEKI)   Operational   2009-01-23    Japan
- STARS (KUKAI)   Unknown   2009-01-23    Japan
- Aggiesat2   Decayed   2009-07-30    United States
- PARADIGM (BEVO-1)   Decayed   2009-07-30    United States
- Sumbandila-OSCAR 67 (SumbandilaSat, SO-67)   Decayed   2009-09-17    South Africa
- SwissCube   Operational   2009-09-23    Switzerland
- ITUpSAT1   Operational   2009-09-23    Turkey
- UWE-2   Non Operational   2009-09-23    Germany
- BEESAT   Operational   2009-09-23    Germany
- Hope Oscar 68 Archived 2013-05-28 at the Wayback Machine (XW-1, HO-68)   Beacon-Operational   2009-12-15    China
- AubieSat-1 Archived 2012-04-18 at the Wayback Machine (AO-71)   Non-Operational   2011-10-28    United States
- Masat-1 (MO-72)   Decayed   2012-02-13    Hungary
- ESTCube-1   Non-Operational   2013-05-07    Estonia
- CAPE 2 (LO-75)   Decayed   2013-11-20    United States
- FUNcube-1 (AO-73) [[1]](http://funcube.org.uk/)   Operational   2013-11-21    United Kingdom  
Netherlands
- CubeBug-2 (LUSAT-OSCAR 74)   Operational   2013-11-21    Argentina
- $50SAT   Non-Operational   2013-11-21    United States
- DELFI-N3XT   Non-Operational?   2013-11-21    Netherlands
- ARTSAT INVADER (CO-77)   Decayed   2014-02-27    Japan
- Lituanica SAT-1 (LO-78)   Decayed   2014-02-27    Lithuania
- FunCube-2 (UKube-1)   Non-Operational   2014-07-08    United Kingdom
- QB50P1 (EO-79, FUNcube-3)   Non-Operational   2014-07-19    Belgium
- QB50P2   Semi-Operational   2014-07-19    Belgium
- ARTSAT2-DESPATCH   Non-Operational   2014-12-03    Japan
- Shin’en-2 (FO-82)   Non-Operational   2014-12-03    Japan
- BRICSat-P (OSCAR 83)   Decayed   2015-05-20    United States
- ParkinsonSAT (OSCAR 84, NO-84, PSAT)   Decayed   2015-05-20    United States
- LilacSat-2 (CAS-3H)   Operational   2015-09-19    China
- XW-2 (CAS-3)   Non-Operational   2015-09-19    China
- Lapan-A2 (IO-86)   Operational   2015-09-28    Indonesia
- Fox-1A (OSCAR 85, AO-85)   Non-Operational   2015-10-08    United States
- HORYU-IV   Non-Operational   2016-02-17    Japan
- CHUBUSAT-3   Non-Operational   2016-02-17    Japan
- ÑuSat-1 (LUSEX OSCAR 87, LO-87)   Decayed   2016-05-30    Argentina
- Nayif-1 (EO-88)   Decayed   2017-02-15    United Arab Emirates
- ITF 2   Decayed   2016-12-09    Japan
- LilacSat-1 (QB50, LO-90)   Decayed   2017-04-18    China
- ZHUHAI-1 01/02 (CAS 4A/B)   Non-Operational   2017-06-15    China
- Fox-1B (OSCAR 91, AO-91, RadFxSat)   Semi-Operational   2017-11-18    United States
- Fox-1D (OSCAR 92, AO-92)   Decayed   2018-01-12    United States
- K2SAT   Non-Operational   2018-03-12    South Korea
- DSLWP-A (OSCAR 93, LO-93)   Non-Operational   2018-05-20    China
- DSLWP-B (OSCAR 94, LO-94)   Operational   2018-05-20    China
- Diwata-2 (Philippines-OSCAR 101, PO-101)   Operational   2018-10-29    Philippines
- Es'hail 2 (Qatar-OSCAR 100, QO-100, P4A)   Operational   2018-11-15    Qatar
- Fox-1Cliff (OSCAR 95, AO-95)   Semi-Operational   2018-12-03    United States
- ExseedSat-1 (VUsat-OSCAR 96, VO-96)   Operational   2018-12-03    India
- JY1Sat (Jordan-OSCAR 97, JO-97)   Operational   2018-12-03    Jordan
- D-Star ONE Sparrow   Operational   2018-12-27    Germany
- D-Star ONE iSat   Operational   2018-12-27    Germany
- OrigamiSat (Fuji-OSCAR 98, FO-98)   Decayed   2019-01-18    Japan
- NEXUS (Fuji-OSCAR 99, FO-99)   Decayed   2019-01-18    Japan
- AISAT-1 (ExseedSat-2)   Decayed   2019-04-01    India
- AztechSat 1   Non-Operational   2019-05-12    Mexico
- CAS-7B (BIT Progress-OSCAR 102, BO-102)   Decayed   2019-07-25    China
- BricSat-2 (Navy-OSCAR 103, NO-103)   Decayed   2019-06-25    United States
- PSAT-2 (Navy-OSCAR 104, NO-104)   Decayed   2019-06-25    United States
- HuskySat-1 (HO-107)   Decayed   2019-11-02    United States
- SMOG-P (Magyar-OSCAR 105, MO-105)   Decayed   2019-12-06    Hungary
- ATL-1 (Magyar-OSCAR 106, MO-106)   Decayed   2019-12-06    Hungary
- Taurus-1 (Jinniuzuo-1)   Decayed   2019-12-09    China
- Tianqin-1 (CAS-6, TO-108)   Operational   2019-12-20    China
- DOSAAF-85 (RS-44)   Operational   2019-12-26    Russia
- BY70-2   Decayed   2020-07-03    China
- International Space Station (ISS)   Operational   2020-09-02    United States
- RadFxSat-2 (AmSat Fox-1, AO-109)   Decayed   2024-01-17    United States
- UVSQ-Sat   Rarely   2021-01-24    France
- SDSAT (Satish Dhawan Sat)   Decayed   2021-02-28    India
- SMOG-1 (Magyar-OSCAR 110, MO-110)   Decayed   2021-03-22    Hungary
- DIY-1 (DIY-OSCAR 111, DO-111)   Decayed   2021-03-22    Argentina
- GRBAlpha   Operational   2021-03-22    Slovakia
- MIR-Sat 1 (MIRSAT-OSCAR 112, MO-112)   Decayed   2021-06-03    Mauritius
- LEDSAT   Decayed   2021-08-17    Italy
- CAMSAT XW-3 (HO-OSCAR 113, HO-113, CAS-9)   Operational   2021-12-26    China
- BDSAT-2   Operational   2022-01-03    Czech Republic
- EASAT-2 (Spain-OSCAR 114, SO-114)   Operational   2022-01-13    Spain
- HADES (Spain-OSCAR 115, SO-115)   Operational   2022-01-13    Spain
- SanoSat-1 (Nepal-OSCAR 116, NO-116)   Decayed   2022-01-13    Nepal
- Tevel 1-8   Decayed   2022-01-13    Israel
- Planetum-1   Operational   2022-05-25    Czech Republic
- ForeSail 1   Failure   2022-05-25    Finland
- GreenCube (Italy-OSCAR 117, IO-117)   Non-Operational   2022-07-13    Italy
- Fengtai Shaonian 2 (CAS-5A, Fengtai-OSCAR 118, FO-118)   Operational   2022-12-09    China
- XiWang-4 (Hope-OSCAR 119, HO-119, XW-4, CAS-10)   Operational   2022-11-12    China
- EOS–07 (APRSDP-BTN)   Operational   2023-02-10    Bhutan
- INSPIRE-Sat 7   Decayed   2023-04-15    France
- RoseyCubesat-1   Operational   2023-04-15    Switzerland  Monaco
- IRIS-C   Operational   2023-04-15    Taiwan
- MAYA-6   Decayed   2023-07-19    Philippines
- Veronika   Operational   2023-11-11    Slovakia
- HADES-D (SO-121)   Operational   2023-11-11    Spain
- SONATE-2   Operational   2024-03-04    Germany
- Kashiwa (柏)   Decayed   2024-03-23    Japan
- MESAT 1 (MO-122)   Operational   2024-07-04    United States
- KUBE/QUBE   Operational   2024-08-16    Germany
- SAKURA   Future   2024-08-29    Japan

#### In development

- **KiwiSAT** - A microsatellite built by AMSAT-ZL. Flight-ready, but no launch provider found yet.

### Facts

#### Multinational effort

Currently, 30 countries have constructed a launched OSCAR satellite. These countries, in chronological order by date of launch, include:

1. United States
2. Australia
3. Spain
4. United Kingdom
5. Japan
6. Brazil
7. Argentina
8. Pakistan
9. Russia
10. France
11. Portugal
12. South Korea
13. Italy
14. Mexico
15. Israel
16. Thailand
17. South Africa
18. Malaysia
19. Saudi Arabia
20. Germany
21. India
22. Colombia
23. Netherlands
24. Indonesia
25. United Arab Emirates
26. China
27. Qatar
28. Jordan
29. Philippines
30. Hungary

#### Related names

SuitSat, an obsolete Russian space suit with a transmitter aboard, was officially known as "AMSAT-OSCAR 54". Coincidentally, "Oscar" was the name given to an obsolete space suit by its young owner in the 1958 novel *Have Space Suit—Will Travel,* by Robert A. Heinlein. This book was first published a year after the launch of Sputnik 1, the world's first artificial satellite.

### International regulation

**Amateur-satellite service** (also: *amateur-satellite radiocommunication service*) is – according to *Article 1.57* of the International Telecommunication Union's (ITU) Radio Regulations (RR) – defined as «*A radiocommunication service using space stations on earth satellites for the same purposes as those of the amateur service*.»

#### Classification

This *radiocommunication service* is classified in accordance with *ITU Radio Regulations* (article 1) as follows:  
Radiocommunication service (article 1.19)

- Amateur service (article 1.56)

 - **Amateur-satellite service** (article 1.57)

#### Frequency allocation

The allocation of radio frequencies is provided according to *Article 5* of the ITU Radio Regulations (edition 2012).

In order to improve harmonisation in spectrum utilisation, the majority of service-allocations stipulated in this document were incorporated in national Tables of Frequency Allocations and Utilisations which is within the responsibility of the appropriate national administration. The allocation might be primary, secondary, exclusive, and shared.

- primary allocation: is indicated by writing in capital letters (see example below)
- secondary allocation: is indicated by small letters (see example below)
- exclusive or shared utilization: is within the responsibility of national administrations

**Example of frequency allocation**  —

- **Allocation to services**
- Region 1    Region 2    Region 3
- 135.7–137.8 kHz  
  
FIXED  
MARITIME MOBILE  
Amateur

 135.7–137.8  
  
FIXED  
MARITIME MOBILE  
Amateur

 135.7–137.8  
  
FIXED  
MARITIME MOBILE  
RADIO NAVIGATION  
Amateur

- 7 000–7 100 AMATEUR  
  
  
  
  
**AMATEUR-SATELLITE**

- 14 000–14 250 AMATEUR  
  
  
  
  
  
**AMATEUR-SATELLITE**

- 18 068–18 168 AMATEUR  
  
  
  
  
  
**AMATEUR-SATELLITE**

- 21 000–21 450 AMATEUR  
  
  
  
  
  
**AMATEUR-SATELLITE**

- 24 890–24 990 AMATEUR  
  
  
  
  
  
**AMATEUR-SATELLITE**

- 28–29.7 MHz AMATEUR  
  
  
  
  
  
**AMATEUR-SATELLITE**

- 144–146 AMATEUR  
  
  
  
  
  
**AMATEUR-SATELLITE**

- 5 830–5 850  
  
FIXED-SATELLITE  
(space-to-Earth)  
RADIOLOCATION  
Amateur  
**Amateur-satellite**

— **(space-to-Earth)**

 5 830–5 850  
  
RADIOLOCATION  
Amateur  
**Amateur-satellite**

— **(space-to-Earth)**

- 10.5–10.6 GHz AMATEUR  
  
  
  
  
  
**AMATEUR-SATELLITE**

- 24–24.05 AMATEUR  
  
  
  
  
  
**AMATEUR-SATELLITE**

- 47–47.2 AMATEUR  
  
  
  
  
  
**AMATEUR-SATELLITE**

- 76–77.5 RADIO ASTRONOMY  
  
  
  
  
  
RADIOLOCATIONY  
Amateur  
**Amateur-satellite**  
Space research (space-to-Earth)

- 77.5–78 AMATEUR  
  
  
  
  
  
**AMATEUR-SATELLITE**  
Radio astronomy  
Space research (space-to-Earth)

- 78–79 RADIOLOCATION  
  
  
  
  
  
Amateur  
**Amateur-satellite**  
Radio astronomy  
Space research (space-to-Earth)

- 79–81 RADIOLOCATION  
  
  
  
  
  
RADIO ASTRONOMY  
Amateur  
**Amateur-satellite**  
Space research (space-to-Earth)

- 134–136 AMATEUR  
  
  
  
  
  
**AMATEUR-SATELLITE**  
Radio astronomy

- 136–141 RADIO ASTRONOMY  
  
  
  
  
  
RADIOLOCATION  
Amateur  
**Amateur-satellite**

- 241–248 RADIO ASTRONOMY  
  
  
  
  
  
RADIOLOCATION  
Amateur  
**Amateur-satellite**

- 248–250 AMATEUR  
  
  
  
  
  
**AMATEUR-SATELLITE**  
Radio astronomy

#### Additional allocations

In addition to the formal allocations in the main table such as above, there is also a key ITU-R footnote RR 5.282 that provides for additional allocations:-  
  
  
**5.282** In the bands 435-438 MHz, 1 260-1 270 MHz, 2 400-2 450 MHz, 3 400-3 410 MHz (in Regions 2 and 3 only)  
and 5 650-5 670 MHz, the amateur-satellite service may operate subject to not causing harmful interference to other  
services operating in accordance with the Table (see No. 5.43). Administrations authorizing such use shall ensure that  
any harmful interference caused by emissions from a station in the amateur-satellite service is immediately eliminated  
in accordance with the provisions of No. 25.11. The use of the bands 1 260-1 270 MHz and 5 650-5 670 MHz by the  
amateur-satellite service is limited to the Earth-to-space direction.

Of these, the 435-438 MHz band is particularly popular for amateur/educational small satellites such as Cubesats.

---

*Source: Wikipedia, Amateur radio satellite (https://en.wikipedia.org/wiki/Amateur_radio_satellite), by Wikipedia contributors, CC BY-SA 4.0.*
