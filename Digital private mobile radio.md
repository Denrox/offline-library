# Digital private mobile radio

**dPMR** or digital private mobile radio, is a common air interface for digital mobile communications. dPMR is an open, non-proprietary standard that was developed by the European Telecommunications Standards Institute (ETSI) and published under the reference ETSI TS 102 658.

A simplified version of the dPMR protocol intended for licence-free applications was also published by ETSI under the reference TS 102 490.

dPMR is very similar to [NXDN](NXDN.md) protocol implementation by [Kenwood](Kenwood%20Corporation.md) and [Icom](Icom%20Incorporated.md); both now offer dual-standard equipment (July 2013).

### Specifications

- Access method: FDMA
- Transmission rate: 4,800 bit/s
- Modulation: four-level [FSK](Frequency-shift%20keying.md)

What is significant is that dPMR achieves all this in a 6.25 kHz channel.

Because the emission mask is so tight, two 6.25 kHz dPMR signals can be used next to each other within a 12.5 kHz channel without causing interference to each other or adjacent channels. Compliance with EN301 166 at 6.25 kHz for current equipment provides some measure of guarantee that interference issues will be no different with either 12.5 kHz or 25 kHz. Frequency co-coordinators in the USA have even made recommendations to the FCC about setting up new 6.25 kHz systems adjacent to existing systems, outlining parameters to avoid harmful interference.

dPMR equipment complies with the relevant European standard ETSI EN 301 166 as well as the FCC emission mask applicable for operation in the US.

dPMR supports several voice coding algorithms. Class A equipment is based on AMBE+2 vocoder, Class R uses RALCWI (Robust Advanced Low Complexity Waveform Interpolation) vocoder, and Class M equipment uses manufacturer specific algorithm. Equipment from these different classes is not interoperable in digital mode and therefore, must revert to analog FM mode.

### dPMR functionality

#### dPMR446

dPMR446 radios are licence-free products for use in the 446.0–446.2 MHz band within Europe.

These are fully digital versions of [PMR446](PMR446.md) radios.

dPMR446 radios comply with the ETSI TS 102 490 open standard and are limited to 500 mW RF power with fixed antennas per ECC Decision (05)12. They are ideally suited to recreational and professional users who do not need wide area coverage with base stations and repeaters.

dPMR446 equipment is capable of voice, data and voice+data modes of operation.

This means that dPMR446 can provide voice calls, text messaging (SMS), status and embedded data such as GPS position etc.

#### dPMR Mode 1

This is the peer to peer mode of dPMR (without repeaters or infrastructure) but without the limitations of the licence-free counterpart. It can operate all typical licensed PMR frequency bands and without the RF power limits of dPMR446. As well as offering voice and data, dPMR446 Mode 1 also supports combined voice+data so it is possible to embed data into a voice call or automatically append it at the end of a call.

#### dPMR Mode 2

dPMR Mode 2 operations include repeaters and other infrastructure. This brings extra functionality such as analogue or digital network interfaces which can be IP based. Inclusion of repeaters and base stations means that wide area coverage is possible even more so when multiple repeaters are used. Such multiple repeaters can be managed by dynamic channel selection or they can be part of a co-channel wide area network.

#### dPMR Mode 3

dPMR Mode 3 can offer multichannel, multisite trunked radio networks. This ensures optimum use of spectrum and optimum density of radio traffic.

Management of the radio network starts from the authentication of radios that wish to connect. Calls are set up by the infrastructure when both parties have responded to the call request ensuring optimum use of the radio resource. Calls may be diverted to other radios, landline numbers or even IP addresses. The infrastructure managing these beacon channels would be capable of placing a call to another radio whether that radio is using the same site or another site within the network.

### Interoperability

With all forms of technology it is vital that products from any manufacturer will interoperate without conflict. To ensure that this will be the case, ETSI has also developed and published a range of European standards for compliance and interoperability testing.

These standards are the ETSI TS 102 587 series for dPMR446 and the ETSI TS 102 726 series for licensed dPMR Mode1, 2 and 3 products.

### Implementations

- Icom IDAS
- Kenwood NEXEDGE
- Midland D-series

### The dPMR Association

A dPMR Memorandum of Understanding (MoU) group was created in 2007 by a group of companies who wished to support the latest digital PMR radio technology known as dPMR. The group currently includes radio and silicon manufacturers, protocol, software and systems developers. Members have agreed to work for the common aims of interoperability, compliance and success of dPMR. In 2011 the group was renamed the dPMR Association.

---

*Source: Wikipedia, Digital private mobile radio (https://en.wikipedia.org/wiki/Digital_private_mobile_radio), by Wikipedia contributors, CC BY-SA 4.0.*
