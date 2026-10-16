# Fldigi

- Fldigi

Fldigi main window snapshot

- Developers Dave Freese (W1HKJ), et al.
- Release 2007
- Stable release

4.2.05 / 23 April 2024 (2024-04-23)

- Written in FLTK, C, C++
- Operating system Windows, macOS, Linux, Android, FreeBSD
- Platform IA-32, x64, IA-64, armel, armhf, mips, mipsel, PowerPC, s390, s390x, SPARC, Raspberry Pi
- Size About 6.5 MB
- Available in 10 languages

List of languages

English, Catalan, Dutch, French, German, Greek, Italian, Polish, Spanish, Russian

- Type [Amateur radio](Amateur%20radio.md) and DSP
- License GPL version 3.0
- Website www.w1hkj.org
- Repository sourceforge.net/p/fldigi/fldigi/ci/master/tree/

**Fldigi** (short for **F**ast **l**ight **digi**tal) is a free and open-source program which allows an ordinary computer's sound card to be used as a simple two-way data modem. The software is mostly used by [amateur radio operators](Amateur%20radio%20operator.md) who connect the microphone and headphone connections of an [amateur radio](Amateur%20radio.md) [SSB](Single-sideband%20modulation.md) or [FM](Frequency%20modulation.md) [transceiver](Transceiver.md) to the computer's headphone and microphone connections, respectively.

This interconnection creates a "sound card defined radio" whose available bandwidth is limited by the sound card's sample rate and the external radio's bandwidth.

Such communications are normally done on the [shortwave](Shortwave%20radio.md) amateur radio bands in modes such as [PSK31](PSK31.md), MFSK, [RTTY](Radioteletype.md), Olivia, and [CW (Morse code)](Morse%20code.md). Increasingly, the software is also being used for data on [VHF](Very%20high%20frequency.md) and [UHF](Ultra%20high%20frequency.md) frequencies using faster modes such as 8-PSK.

Using this software, it is possible for [amateur radio operators](Amateur%20radio%20operator.md) to communicate worldwide while using only a few watts of RF power.

Fldigi software is also used for [amateur radio emergency communications](Amateur%20radio%20emergency%20communications.md) when other communication systems fail due to natural disaster or power outage. Transfer of files, emails, and FEMA ICS forms are possible using inexpensive radio hardware.

### Supported digital modes

- Mode name   Speeds supported   Custom modes
- [Morse code](Morse%20code.md) CW   5–50 words-per-minute   Yes
- PSK   [31](PSK31.md), 63, 63F, 125, 250, 500, 1000   No
- FSQ   2, 3, 4.5, 6   No
- IFKP   0.5, 1.0, 2.0   No
- Contestia   4/125, 4/250, 8/250, 4/500, 8/500, 16/500, 8/1000, 16/1000, 32/1000, 64/1000   Yes
- DominoEX   Micro, 4, 5, 8, 11, 16, 22, 44, 88   No
- Hellschreiber   Feld Hell, Slow Hell, Feld Hell X5, Feld Hell X9, FSK Hell, FSK Hell-105, Hell 80   No
- MFSK   4, 8, 11, 16, 22, 31, 32, 64, 64L, 128, 128L   No
- MT63   500S, 1000S, 2000S, 500L, 1000L, 2000L   No
- Navtex   Navtex   No
- Olivia   4/250, 8/250, 4/500, 8/500, 16/500, 8/1000, 16/1000, 32/1000, 64/2000   Yes
- QPSK   31, 63, 125, 250, 500   No
- 8PSK   125, 250, 500, 1000, 125FL, 250FL, 125F, 250F, 500F, 1000F, 1200F   No
- PSKR   125R, 250R, 500R, 1000R   No
- RTTY   45.45/170, 50/170, 75/170, 75/850   Yes
- SYNOP   SYNOP   No
- THOR   Micro, 4, 5, 8, 11, 16, 22, 25x4, 50x1, 50x2 100   No
- SITORB   SitorB   No
- Throb / ThrobX   1, 2, 4 **/** X1, X2, X4   No
- WEFAX   IOC-576, IOC288   No
- OFDM   500F, 750F, 3500   No

### Portability

#### Operating systems

Fldigi is based on the lightweight portable graphics library FLTK and the C/C++ language. Because of this, the software can run on many different operating systems such as:

- Microsoft Windows (2000 or newer)
- macOS
- Linux,
- FreeBSD,
- OpenBSD,
- NetBSD,
- Solaris.

Additionally, Fldigi is designed to compile and run on any POSIX compliant operating system that uses an X11 compatible window system / graphical user interface.

#### Architectures

The Fldigi software is written in highly portable C/C++ and can be used on many CPU architectures, including:

- amd64
- i386
- armhf/armel
- ia64
- mips
- mipsel
- powerpc
- s390
- s390x
- sparc
- Raspberry Pi.

#### Sound systems

Multiple sound systems are supported by Fldigi, allowing the program to abstract the sound card hardware across differing hardware and operating systems.

- Open Sound System (OSS)
- PortAudio
- PulseAudio
- Read / write to WAV files (file I/O)

### Features

- NBEMS: The narrowband emergency messaging system
- Support for transmitting and receiving in all languages by using UTF-8 character encoding (some modes)
- Connection to external programs via TCP/IP port 7322
- Ability to be used as a KISS modem via TCP/IP port 7342
- Dual-tone multi-frequency (DTMF) encoding and decoding
- Automatic switching of mode and frequency by use of Reed Solomon Identifier signal identification
- Inbuilt macro language and processor for programmable automated control
- Sound card oscillator frequency/skew correction
- Measure sound card oscillator's skew to atomic clock: WWV or WWVH
- Measure RF receiver frequency skew to atomic clock: WWV or WWVH
- Transmit a WWV-like time signal as a calibration reference
- Control of external transmit / receive radio hardware by using GPIO pins. (For embedded hardware)
- Simultaneous decoding of multiple [Morse code](Morse%20code.md) ([CW](Continuous%20wave.md)) signals
- Decoding of Morse code (CW) by self-organizing map artificial neural network (trained artificial intelligence)

### The Fldigi Suite

The "Fldigi Suite" consists of the Fldigi modem and all extension programs released by the same development group. Most of these extensions add more capabilities to Fldigi such as verified file transfer and message passing. Interconnection between these programs and the Fldigi modem is made over TCP/IP port 7322.

Some of the Suite are however standalone programs used for utility or testing purposes only, with no connection to the Fldigi main modem.

#### Flamp

Flamp implements the Amateur Multicast Protocol by Dave Freese, W1HKJ and is a tool for connectionless transferring of files to multiple users simultaneously without requiring any existing infrastructure. The program breaks a given file into multiple smaller pieces, checksums each piece, then transmits each piece one or more times. When all parts are correctly received the sent file is re-assembled and can be saved by receiving stations. This program is useful for multicasting files over lossy connections such as those found on [High frequency](High%20frequency.md) (HF) or during [emergency communications](Amateur%20radio%20emergency%20communications.md).

#### Flarq

Flarq implements the ARQ specification developed by Paul Schmidt, K9PS to transfer emails, text files, images, and binary files over radio. This protocol is unicast and connection-based. The software seamlessly integrates with existing email clients such as Microsoft Outlook, Mozilla Thunderbird, and Sylpheed.

#### Flmsg

Flmsg allows users to send, receive, edit, and create pre-formatted forms. Such a system speeds the flow of information during emergency communications. The software has a number of forms built-in including FEMA ICS forms, MARS reports & messages, Hospital ICS forms, Red Cross messages, IARU and NTS messages.

#### Flwrap

Flwrap is a tool for the sending of files using a simplified drag and drop interface. Data compression is available also, which reduces data transfer times.

#### FLNet

FLNet assists net control operators in keeping track of multiple stations during digital [amateur radio nets](Amateur%20radio%20net.md).

#### FLLog

FLLog is a logging software which keeps track of conversations between amateur radio operators in a database format known as ADIF.

#### FLWkey

FLWkey is a simple interface to control an external piece of hardware called a Winkeyer. This is a [Morse code](Morse%20code.md) keyer which is adjustable via computer commands over USB.

#### Flcluster

This is a telnet client to remote DX cluster servers, which is a real-time reporting of stations heard transmitting, and their frequencies. It does not connect to Fldigi.

#### Flaa

Flaa is a control program for use with the RigExpert AA-xxxx series of antenna analyzers, and does not connect to Fldigi.

#### Flrig

FLRig is a component of the FLDigi suite of applications that enables computer aided control of various radios using a serial or USB connection.

Using FLRig in combination with FLDigi, events such as frequency, power level, receiver gain and audio gain may be adjusted from the computer automatically or by user intervention.

### Test tools

The Fldigi development group also releases a number of open-source programs which assist in the testing, development, and comparison of different modes within Fldigi, such as LinSim, CompText, and CompTTY.

### RSID

To identify the mode being transmitted a signal called an RSID, or Reed-Solomon Identifier, can be transmitted before the data. Using this identifier the receiving software can automatically switch to the proper mode for decoding. The assigning of these identifiers to new modes is coordinated to ensure inter-operation between programs. Currently 7 sound card-digital-modem programs support this standard:

- PocketDigi
- FDMDV
- DM780
- Multipsk
- Fldigi
- AndFlmsg
- TIVAR

RSID operates by sending a short burst of a specific modulation before the data signal, which can be used to automatically identify over 272 digital modes. This burst consists of a 10.766 baud 16-tone MFSK modulation where 15 tones/symbols are sent. The burst occupies 172 Hz of bandwidth and lasts for 1.4 seconds.

### Software architecture

For simple keyboard-to-keyboard communication Fldigi can be operated using just the main window. For more complex uses or file transfer external programs can be attached to the internal TCP/UDP ports 7322 (ARQ), 7342 (KISS), and 7362 (XML-RPC).

The image below helps to illustrate the interconnections and signal-flow within the Fldigi architecture.

### Community-provided extensions

Fldigi allows external programs to attach and send / receive data by connecting to port 7322/ARQ or 7342/KISS. When used this way, Fldigi and the computer's sound card are acting as a "softmodem" allowing text or data sent on one computer to be transferred using the wireless radio link in-between. Programs which have a history of use with Fldigi as the underlying modem include:

- D-Rats - easy to use chatrooms, email, and file transfer over-radio.
- PSKmail - send and receive on-internet e-mail over a remote radio connection.
- Fldigiattach - attach Fldigi as modem for Linux [AX.25](AX.25.md) and TCP/IP connections.
- UIChat - Java-based amateur radio chat program.
- LinkUP - Program for unattended operation and person to person chat.
- Linux - Fldigi can be used in Linux as a KISS (TNC) modem for [AX.25](AX.25.md) and TCP/IP connections.

### Awards and recognitions

- At the 2014 Dayton Hamvention the project lead, Dave Freese (W1HKJ), was recognized with the Technical Excellence Award "for his development and distribution of the Fast Light Digital Modem Application (fldigi) family of programs for use in amateur and emergency communications."
- Fldigi was selected as SourceForge's June 2017 Staff 'Project of the Month'
- Fldigi was one of SourceForge's 'Projects of the Week' for Oct 17, 2016
- Fldigi was selected as SourceForge's December 2017 Community Choice 'Project of the Month'

### Decodeable broadcasts

The broadcasts listed below are transmitted on a regular schedule and can be decoded using Fldigi.

- SITOR text forecasts and storm warnings
- WEFAX visual weather fax
- SYNOP surface synoptic observations
- NAVTEX warnings, forecasts, and safety information broadcasts
- VOA Radiogram Broadcasts
- W1AW Broadcasts

---

*Source: Wikipedia, Fldigi (https://en.wikipedia.org/wiki/Fldigi), by Wikipedia contributors, CC BY-SA 4.0.*
