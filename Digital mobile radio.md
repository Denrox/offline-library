# Digital mobile radio

**Digital Mobile Radio** (**DMR**) is a digital radio standard for voice and data transmission in non-public radio networks. It was created by the European Telecommunications Standards Institute (ETSI), and is designed to be low-cost and easy to use. DMR, along with [P25 phase II](Project%2025.md) and [NXDN](NXDN.md) are the main competitor technologies in achieving 6.25 kHz equivalent bandwidth using the proprietary AMBE+2 vocoder. DMR and P25 II both use two-slot TDMA in a 12.5 kHz channel, while NXDN uses discrete 6.25 kHz channels using frequency division and [TETRA](TETRA.md) uses a four-slot TDMA in a 25 kHz channel.

DMR was designed with three tiers. DMR tiers I (Unlicensed) and II (Conventional Licensed) were first published in 2005, and DMR III (Trunked version) was published in 2012, with manufacturers producing products within a few years of each publication.

The primary goal of the standard is to specify a digital system with low complexity, low cost and interoperability across brands, so radio communications purchasers are not locked into a proprietary solution.

### Specifications

The DMR interface is defined by the following ETSI standards:

- TS 102 361-1: Air interface protocol
- TS 102 361-2: Voice and General services and facilities
- TS 102 361-3: Data protocol
- TS 102 361-4: Trunking protocol

The DMR standard operates within the existing 12.5 kHz channel spacing used in land mobile frequency bands globally, but achieves two voice channels through two-slot TDMA technology built around a 30 ms structure. The modulation is 4-state [FSK](Frequency-shift%20keying.md), which creates four possible symbols over the air at a rate of 4,800 symbols/s, corresponding to 9,600 bit/s. After overhead, forward error correction, and splitting into two channels, there is 2,450 bit/s left for a single voice channel using DMR, compared to 4,400 bit/s using P25 and 64,000 bit/s with traditional telephone circuits.

The standards are still (as of late 2015) under development with revisions being made regularly as more systems are deployed and improvements are discovered. It is very likely that further refinements will be made to the standard, which will necessitate firmware upgrades to terminals and infrastructure in the future to take advantage of these new improvements, with potential incompatibility issues arising if this is not done.

DMR covers the RF range 30 MHz to 1 GHz.

There are DMR implementations, that operate as low as 66 MHz (within the European Union, in 'Lo-Band VHF' 66–88 MHz.)

### DMR Tiers

#### DMR Tier I

DMR Tier I products are for licence-free use in the European [PMR446 band](PMR446.md). Tier I products are specified for non-infrastructure use only (meaning without the use of repeaters). This part of the standard provides for consumer applications and low-power commercial applications, using a maximum of 0.5 watts RF power.

Note that a licence free allocation is not present at this frequency outside of Europe, which means that PMR446 radios including DMR Tier I radios can only be used legally in other countries once an appropriate radio licence is obtained by the operator.

Some DMR radios sold by Chinese manufacturers (most notably Baofeng) have been mis-labelled as DMR Tier I. A DMR Tier I radio would only use the PMR446 licence–free frequencies, and would have a maximum transmitted power of 0.5 watts as required by law for all PMR446 radios.

Although the DMR standard allows Tier I DMR radios to use continuous transmission mode, all known Tier I radios currently use TDMA, the same as Tier II. This is probably due to the 40% battery savings that come with transmitting only half the time instead of continuously.

#### DMR Tier II

DMR Tier II covers licensed conventional radio systems, mobiles and hand portables operating in PMR frequency bands from 66 to 960 MHz. The ETSI DMR Tier II standard is targeted at those users who need spectral efficiency, advanced voice features and integrated IP data services in licensed bands for high-power communications. A number of manufacturers have DMR Tier II compliant products on the market. ETSI DMR specifies two slot TDMA in 12.5 kHz channels for Tier II and III.

#### DMR Tier III

DMR Tier III covers trunking operation in frequency bands 66–960 MHz. Tier III supports voice and short messaging handling similar to [TETRA](TETRA.md) with built-in 128 character status messaging and short messaging with up to 288 bits of data in a variety of formats. It also supports packet data service in a variety of formats, including support for IPv4 and IPv6. Tier III compliant products were launched in 2012. In April 2013, [Hytera](Hytera.md) participated in the completion of the DMR Tier III interoperability (IOP) test.

### DMR Association

In 2005, a memorandum of understanding (MOU) was formed with potential DMR suppliers including Tait Communications, Fylde Micro, Selex, Motorola, Hytera, Sanchar Communication, [Vertex Standard](Yaesu%20%28brand%29.md), [Kenwood](Kenwood%20Corporation.md) and [Icom](Icom%20Incorporated.md) to establish common standards and interoperability. While the DMR standard does not specify the vocoder, MOU members agreed to use the half rate DVSI Advanced Multi-Band Excitation (AMBE) vocoder to ensure interoperability. In 2009, the MOU members set up the DMR Association to work on interoperability between vendors' equipment and to provide information about the DMR standard. Formal interoperability testing has been taking place since 2010. Results are published on the DMR Association web site. There are approximately 40 members of the DMR Association.

The standard allows DMR manufacturers to implement additional features on top of the standards which has led to practical non-interoperability issues between brands, in contravention to the DMR MOU.

### Amateur radio use

DMR is used on [amateur radio](Amateur%20radio.md) VHF and UHF bands, with the early adoption network development led by DMR-MARC around 2010. The FCC officially approved the use of DMR by amateurs in the US in 2014. In amateur spaces, Coordinated DMR Identification Numbers are assigned and managed by RadioID Inc. Their coordinated database can be uploaded to DMR radios in order to display the name, call sign, and location of other operators. Internet-linked systems allow users to communicate with other users around the world via connected repeaters, or DMR "hotspots" often based on the Raspberry Pi single-board computer. There are currently more than 5,500 repeaters and 16,000 "hotspots" linked to the BrandMeister system worldwide. The low cost and increasing availability of internet-linked systems has led to a rise in DMR use on the amateur radio bands. Some Raspberry Pi-based DMR hotspots, often those running the Pi-Star or WPSD software, allow users to connect to multiple internet-linked DMR networks at the same time. DMR hotspots are often based on the open source Multimode Digital Voice Modem, or MMDVM, hardware with firmware developed by Jonathan Naylor.

Examples of organised amateur radio activities conducted using internet-linked DMR networks include the **World Wide Check-In**, a weekly international net operating on Talk Group 91 of the BrandMeister network.  
### Encryption

Encryption was not defined in the initial releases of the DMR standard, so each DMR radio manufacturer added its own encryption protocol. These early encryption protocols are therefore incompatible with each other. For example, Hytera's Basic Encrypt encryption is completely incompatible with Motorola's Basic Encrypt encryption.

The DMRA now manages an interoperable voice and data encryption scheme for DMR. 40 Bit ARC4, 64 bit DES, 128 and 256 bit AES options are defined. These encryption schemes are interoperable between manufacturers and support voice call late entry, multiple keys, and with no discernible degradation of voice quality.

Some DMR encryption algorithms have been released, such as PC4, released in 2015 with source code available. PC4 is a block cipher specifically designed for DMR radio communication systems, using 253 rounds and a key size from 8 bits to 2112 bits. The block size is 49 bits, which is equal to the size of an AMBE+ DMR voice frame.

A firmware that implements PC4 encryption is available for the Tytera MD-380 and MD-390 radios.

In Motorola Basic Encryption, AMBE frames are encrypted by simple XOR using one of 255 possible static keys.

The Basic mode from other manufacturers offers 10-, 32-, or 64-character keys to produce a 882-bit fixed string of random characters that is combined via XOR with AMBE frames. The entire superframe, rather than each individual AMBE frame, is XORed with this longer static key. A superframe contains 18 AMBE frames, i.e. 882 bits, and it is these 882 bits that will be encrypted with this 882-bit fixed string.

PC4 encryption mode encrypts an entire 49-bit frame in ECB mode. A single bit that differs makes the entire encrypted block completely different.

For the Enhanced (ARC4) or Advanced (AES) mode, each complete superframe is also encrypted with a 32-bit IV (initialization vector). As a result, the encryption is no longer fixed for the same key, but changes with each superframe, improving security.

The DMR standard does not leave any room to store this IV, so the IV (with the addition of an error-correcting code, for a total of 72 bits) replaces 4 low-order bits in each 49-bit AMBE frame. These 4 bits are therefore lost, degrading the voice quality, which is not the case with fixed ciphers in Basic mode. The 72-bit encoded IV is thus spread across all 18 AMBE frames in the superframe.

### Weaknesses in ARC4 DMRA

Motorola has created its standard so that the 40-bit ARC4 (Alleged RC4) can withstand casual attackers. It is supposed to offer 40-bit security, where an attacker must test the 2 possible keys to find the right one. This level of encryption offers no real protection and there is software that allows decoding the key.

RC4 encryption is a stream cipher that must use an IV (initialization vector) each time it performs encryption. The size of this IV should be large enough so that there is no repetition of this IV during the entire use of the same key.

RC4 weak IV encryption has already been compromised in the WEP Wi-Fi encryption system because the IV size was too short (24 bits).

Motorola has opted to use a slightly longer IV size (32-bit) but not that much longer than the WEP's 24-bit IV. Motorola calls this IV the MI (Message Indicator).

Motorola reported that the DMR standard did not define a method for transporting encryption parameters. Its solution embeds a 32-bit initialization vector, together with error-protection data, by replacing selected least-significant bits in the DMR vocoder frames. These bits were selected to minimize degradation of the received voice audio.

According to the author of the DSD-FME software, a DMR specialist, this claim is false because there is the possibility of creating custom DMR frames. Such a frame could therefore have contained a large IV (128 bits for example).

Some users discovered that Anytone radios (such as the Anytone 878) using ARC4, had the IV constant (0x12345678) at the beginning of each transmission. This flaw was fixed in AnyTone D878UVII firmware update V3.03 (2023-12-18).: *5. Modify the firmware to make the AES encryption have a variable Vector(IV) instead of fixed "12345678"*.

The Motorola ARC4 DMRA should by design provide at least 4 billion different IVs, so there should be 4 billion superframes with a different IV (2-bits possible IVs).

But one user discovered that Motorola uses a non-primitive LFSR for the ARC4 to generate the IVs. Instead of 4 billion different IVs, there are only 294,903 different IVs. So instead of a 32-bit IV, you get an 18-bit IV, which is much shorter than the 24-bit WEP Wi-Fi IV.

According to cryptologist Eric Filiol, it is likely that all exported products with a key length of more than 56 bits have a backdoor, as this is a legal requirement due to the Wassenaar Arrangement.

---

*Source: Wikipedia, Digital mobile radio (https://en.wikipedia.org/wiki/Digital_mobile_radio), by Wikipedia contributors, CC BY-SA 4.0.*
