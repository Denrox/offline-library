# Slow-scan television

**Slow-scan television** (**SSTV**) is a picture transmission method, used mainly by [amateur radio operators](Amateur%20radio%20operator.md), to transmit and receive static pictures via radio in monochrome or color.

A literal term for SSTV is narrowband television. Analog broadcast television requires at least 6 MHz wide channels, because it transmits 25 or 30 picture frames per second (see ITU analog broadcast standards), but SSTV usually only takes up to a maximum of 3 kHz of bandwidth. It is a much slower method of still picture transmission, usually taking from about eight seconds to a couple of minutes, depending on the mode used, to transmit one image frame.

Since SSTV systems operate on voice frequencies, amateurs use it on shortwave (also known as [HF](High%20frequency.md) by [amateur radio](Amateur%20radio.md) operators), [VHF](Very%20high%20frequency.md) and [UHF](Ultra%20high%20frequency.md) radio.

### Current systems

A modern system, having gained ground since the early 1990s, uses a personal computer and special software in place of much of the custom equipment. The sound card of a PC, with special processing software, acts as a modem. The computer screen provides the output. A small digital camera or digital photos provide the input.

1

2

3

4

- A spectrogram of the beginning of an SSTV transmission

1

Calibration header

2

VIS code

3

RGB scanlines

4

Sync pulses

#### Modulation

Like the similar radiofax mode, SSTV is an analog signal. SSTV uses [frequency modulation](Frequency%20modulation.md), in which every different value of brightness in the image gets a different audio frequency. In other words, the signal frequency shifts up or down to designate brighter or darker pixels, respectively. Color is achieved by sending the brightness of each color component (usually red, green and blue) separately. This signal can be fed into an [SSB](Single-sideband%20modulation.md) transmitter, which in part modulates the carrier signal.

There are a number of different modes of transmission, but the most common ones are *Martin M1* (popular in Europe) and *Scottie S1* (used mostly in the USA). Using one of these, an image transfer takes 114 (M1) or 110 (S1) seconds. Some black and white modes take only 8 seconds to transfer an image.

#### Header

A calibration header is sent before the image. It consists of a 300-millisecond leader tone at 1,900 Hz, a 10 ms break at 1,200 Hz, another 300-millisecond leader tone at 1,900 Hz, followed by a digital VIS (vertical interval signaling) code, identifying the transmission mode used. The VIS consists of bits of 30 milliseconds in length. The code starts with a start bit at 1,200 Hz, followed by 7 data bits (LSB first; 1,100 Hz for 1, 1,300 Hz for 0). An even parity bit follows, then a stop bit at 1,200 Hz. For example, the bits corresponding the decimal numbers 44 or 32 imply that the mode is Martin M1, whereas the number 60 represents Scottie S1.

#### Scanlines

A transmission consists of horizontal lines, scanned from left to right. The color components are sent separately one line after another. The color encoding and order of transmission can vary between modes. Most modes use an RGB color model; some modes are black-and-white, with only one channel being sent; other modes use a YC color model, which consists of luminance (Y) and chrominance (R–Y and B–Y). The modulating frequency changes between 1,500 and 2,300 Hz, corresponding to the intensity (brightness) of the color component. The modulation is analog, so even though the horizontal resolution is often defined as 256 or 320 pixels, they can be sampled using any rate. The image aspect ratio is conventionally 4:3. Lines usually end in a 1,200 Hz horizontal synchronization pulse of 5 milliseconds (after all color components of the line have been sent); in some modes, the synchronization pulse lies in the middle of the line.

#### Modes

Below is a table of some of the most common SSTV modes and their differences. These modes share many properties, such as synchronization and/or frequencies and grey/color level correspondence. Their main difference is the image quality, which is proportional to the time taken to transfer the image and in the case of the AVT modes, related to synchronous data transmission methods and noise resistance conferred by the use of interlace.

- Family  Developer  Name  Color  Time  Lines
- AVT   Ben Blish-Williams, AA7AS / AEA   8  BW or 1 of R, G, or B  8 s  128×128
- 16w  BW or 1 of R, G, or B  16 s  256×128
- 16h  BW or 1 of R, G, or B  16 s  128×256
- 32  BW or 1 of R, G, or B  32 s  256×256
- 24  RGB  24 s  128×128
- 48w  RGB  48 s  256×128
- 48h  RGB  48 s  128×256
- 104  RGB  96 s  256×256
- Martin   Martin Emmerson - G3OQD   M1  RGB  114 s  240¹
- M2  RGB  58 s  240¹
- Robot   Robot SSTV   8  BW or 1 of R, G or B  8 s  120
- 12  YUV  12 s  128 luma, 32/32 chroma × 120
- 24  YUV  24 s  128 luma, 64/64 chroma × 120
- 32  BW or 1 of R, G or B  32 s  256 × 240
- 36  YUV  36 s  256 luma, 64/64 chroma × 240
- 72  YUV  72 s  256 luma, 128/128 chroma × 240
- Scottie   Eddie Murphy - GM3SBC   S1  RGB  110 s  240¹
- S2  RGB  71 s  240¹
- DX   RGB   269 s   320 x 256

¹ Martin and Scottie modes actually send 256 scanlines, but the first 16 are usually grayscale.

The mode family called AVT (for *Amiga Video Transceiver*) was originally designed by Ben Blish-Williams (N4EJI, then AA7AS) for a custom modem attached to an Amiga computer, which was eventually marketed by AEA corporation.

The Scottie and Martin modes were originally implemented as ROM enhancements for the Robot Research Corporation SSTV unit. The exact line timings for the Martin M1 mode are given in this reference.

The Robot SSTV modes were designed by Robot Research Corporation for their own SSTV units.

All four sets of SSTV modes are now available in various PC-resident SSTV systems and no longer depend upon the original hardware.

##### AVT

AVT is an abbreviation of "Amiga Video Transceiver", software and hardware modem originally developed by "Black Belt Systems" (USA) around 1990 for the Amiga home computer popular all over the world before the IBM PC family gained sufficient audio quality with the help of special sound cards. These AVT modes differ radically from the other modes mentioned above, in that they are synchronous, that is, they have no per-line horizontal synchronization pulse but instead use the standard VIS vertical signal to identify the mode, followed by a frame-leading digital pulse train which pre-aligns the frame timing by counting first one way and then the other, allowing the pulse train to be locked in time at any single point out of 32 where it can be resolved or demodulated successfully, after which they send the actual image data, in a fully synchronous and typically interlaced mode.

Interlace, no dependence upon sync, and interline reconstruction gives the AVT modes a better noise resistance than any of the other SSTV modes. Full frame images can be reconstructed with reduced resolution even if as much as 1/2 of the received signal was lost in a solid block of interference or fade because of the interlace feature. For instance, first the odd lines are sent, then the even lines. If a block of odd lines are lost, the even lines remain, and a reasonable reconstruction of the odd lines can be created by a simple vertical interpolation, resulting in a full frame of lines where the even lines are unaffected, the good odd lines are present, and the bad odd lines have been replaced with an interpolation. This is a significant visual improvement over losing a non-recoverable contiguous block of lines in a non-interlaced transmission mode. Interlace is an optional mode variation, however without it, much of the noise resistance is sacrificed, although the synchronous character of the transmission ensures that intermittent signal loss does not cause loss of the entire image. The AVT modes are mainly used in Japan and the United States. There is a full set of them in terms of black and white, color, and scan line counts of 128 and 256. Color bars and grayscale bars may be optionally overlaid top and/or bottom, but the full frame is available for image data unless the operator chooses otherwise. For receiving systems where timing was not aligned with the incoming image's timing, the AVT system provided for post-receive re-timing and alignment.

##### Other modes

- Family  Developer  Name  Time [sec]  Resolution  Color  VIS  VIS+P
- PD   Paul Turner, G4IJE  
Don Rotier, K0HEO-[SK](Amateur%20radio%20operator.md)   PD50   50.000000   320 x 256   G, R-Y, B-Y
- PD90  89.989120  320 x 256  99  99
- PD120  126.103040  640 x 496  95  95
- PD160  160.883200  512 x 400  98  226
- PD180  187.051520  640 x 496  96  96
- PD240  248.000000  640 x 496  97  225
- PD290   289.000000   800 x 616

#### Frequencies

Using a receiver capable of demodulating [single-sideband modulation](Single-sideband%20modulation.md), SSTV transmissions can be heard on the following frequencies:

- Band  Frequency  Sideband
- [80 meters](80-meter%20band.md)  3.845 MHz (3.73 in Europe)  LSB
- 43 meters  6.925 MHz (pirate radio)  USB
- [40 meters](40-meter%20band.md)  7.171 MHz (7.165 in Europe)  LSB
- [40 meters](40-meter%20band.md)  7.181 MHz (New suggested frequency to include General Class licensees)  LSB
- [40 meters](40-meter%20band.md)  7.214 MHz Australian digital SSTV frequency (Easypal and DIGTRX)  LSB
- [20 meters](20-meter%20band.md)  14.23 MHz Frequency 1 analog  USB
- [20 meters](20-meter%20band.md)  14.227 and 14.233 MHz Frequency 2 analog to alleviate crowding on 14.23  USB
- 15 meters  21.34 MHz  USB
- 11 meters  27.700 international SSTV calling +/- 30khz  USB
- [10 meters](10-meter%20band.md)  28.68 MHz  USB

### Media

- External videos
- Video showing images and the sound generated when sending them as SSTV audio. on YouTube

Encoded image in B/W 8 system.

An SSTV image received by an amateur station transmitted from the ISS using the PD-120 mode.

The resulting picture following decoding of the sample SSTV transmission.

A Spectral Analysis of the sample SSTV transmission

---

*Source: Wikipedia, Slow-scan television (https://en.wikipedia.org/wiki/Slow-scan_television), by Wikipedia contributors, CC BY-SA 4.0.*
