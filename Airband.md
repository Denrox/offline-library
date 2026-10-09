# Airband

**Airband** or **aircraft band** is the name for a group of frequencies in the [VHF](Very%20high%20frequency.md) [radio spectrum](Radio%20spectrum.md) allocated to radio communication in civil aviation, sometimes also referred to as *VHF*, or phonetically as *"Victor"*. Different sections of the band are used for radionavigational aids and air traffic control.

In most countries a license to operate airband equipment is required and the operator is tested on competency in procedures, language and the use of the phonetic alphabet.

### Spectrum usage

The VHF airband uses the frequencies between 108 and 137 MHz. The lowest 10 MHz of the band, from 108 to 117.95 MHz, is split into 200 narrow-band channels of 50 kHz. These are reserved for navigational aids such as VOR beacons, and precision approach systems such as ILS localizers.

As of 2012, most countries divide the upper 19 MHz into 760 channels for [amplitude modulation](Amplitude%20modulation.md) voice transmissions, on frequencies from 118 to 136.975 MHz, in steps of 25 kHz. In Europe, it is becoming common to further divide those channels into three (8.33 kHz channel spacing), potentially permitting 2,280 channels. Some channels between 123.100 and 135.950 are available in the US to other users such as government agencies, commercial company advisory, search and rescue, military aircraft, glider and ballooning air-to-ground, flight test and national aviation authority use. A typical transmission range of an aircraft flying at cruise altitude (35,000 ft (10,668 m)), is about 200 nmi (230 mi; 370 km) in good weather conditions.

#### Other bands

Aeronautical voice communication is also conducted in other frequency bands, including satellite voice on [Inmarsat](Inmarsat.md), Globalstar or Iridium.

Moreover, in oceanic and remote areas, frequencies in the [high frequency](High%20frequency.md) (HF) band between 2.850 and 22 MHz are used for voice communication, since their propagation properties allow communication over wider areas (see also Shanwick Oceanic Control). In this frequency range also a *High Frequency Data Link* (*HF Data Link*, *HFDL*) is used for Controller-Pilot Data Link Communications.

Military aircraft also use a dedicated UHF-AM band from 225.0 to 399.95 MHz for air-to-air and air-to-ground, including air traffic control communication. This band has a designated emergency and guard channel of 243.0 MHz.

Aeronautical radio navigation aids (navaids) use other frequencies:

- Non-directional beacons (NDB)s operate on low frequency and [medium frequency](Medium%20frequency.md) bands 190–415 kHz and 510–535 kHz.
- VHF omnidirectional range (VOR) and Doppler VOR (DVOR) radio beacons use frequencies in the [very high frequency](Very%20high%20frequency.md) (VHF) band between 108.00 and 117.95 MHz.
- Instrument landing system (ILS) consists of a localizer operating in VHF band between 108.00 and 112 MHz, a glide slope operating in the [UHF](Ultra%20high%20frequency.md) range of 329.3–335.0 MHz and marker beacons at 75 MHz.
- Distance measuring equipment (DME) uses the UHF band between 960 and 1215 MHz. (Within this band, two segments, around 1030 MHz and 1090 MHz, are reserved for Secondary Surveillance Radar and Automatic dependent surveillance-broadcast transmissions. Furthermore, some military systems make use of this band, e.g. Tactical Air Navigation, TACAN. The part 960-1164 MHz of the band is also allocated to the aeronautical mobile (route) service, for use by next generation aeronautical communication systems.)

#### Channel spacing

Channel spacing for voice communication on the airband was originally 200 kHz until 1947, providing 70 channels from 118 to 132 MHz. Some radios of that time provided receive-only coverage below 118 MHz for a total of 90 channels. From 1947 to 1958 the spacing became 100 kHz; from 1954 split once again to 50 kHz and the upper limit extended to 135.95 MHz (360 channels), and then to 25 kHz in 1972 to provide 720 usable channels. On 1 January 1990 the frequencies between 136.000 and 136.975 MHz were added, resulting in 760 channels.

Increasing air traffic congestion has led to further subdivision into narrow-band 8.33 kHz channels in the ICAO European region; since 2007, all aircraft flying above FL195 are required to have communication equipment for this channel spacing.

The introduction of 8.33 kHz channel spacing has resulted in a 6-digit channel numbering scheme, where the 8.33 kHz channel designators differ from the actual frequency; e.g. 8.33 kHz channel 118.010 tunes the frequency 118.0083 MHz (see figure).

Eurocontrol's "8.33 kHz Voice Channel Implementation Guidelines" document provides recommendations regarding institutional provisions, flight planning, operational procedures, aircraft retrofit, safety, frequency management and State's management aspects for the deployment of 8.33 kHz channel spacing communications.

Outside of Europe, 8.33 kHz channels are permitted in many countries but not widely used as of 2021.

The emergency communication channel 121.5 MHz is the only channel that retains 100 kHz channel spacing in the US; there are no channel allocations between 121.4 and 121.5 or between 121.5 and 121.6

#### Modulation

Aircraft communications radio operations worldwide use [amplitude modulation](Amplitude%20modulation.md) (AM), predominantly A3E double sideband with full carrier on VHF, and J3E [Single-sideband modulation](Single-sideband%20modulation.md) (SSB) with suppressed carrier on HF. Besides being simple, power-efficient and compatible with legacy equipment, AM and SSB permit stronger stations to override weaker or interfering stations. Additionally, this method does not suffer from the capture effect found in [FM](Frequency%20modulation.md). Even if a pilot is transmitting, a control tower can "talk over" that transmission and other aircraft will hear a somewhat garbled mixture of both transmissions, rather than just one or the other. Even if both transmissions are received with identical signal strength, a heterodyne will be heard where no such indication of blockage would be evident in an FM system.

#### Offset carrier (CLIMAX)

To provide wide-area coverage that exceeds the line-of-sight range of a single ground transmitter, air traffic control often employs multiple ground stations broadcasting the same audio simultaneously on the same channel. To prevent severe audio distortion and heterodyne beats that would occur if the transmitters operated at the exact same frequency, a multi-carrier offset technique—commonly referred to as "CLIMAX"—is utilized as a standard operational procedure.

In a CLIMAX system, the participating transmitters are slightly offset from the assigned center frequency. According to International Civil Aviation Organization (ICAO) Annex 10 standards, offset configurations for 25 kHz spaced channels include a two-carrier system (±5 kHz), a three-carrier system (0 kHz and ±7.3 kHz), a four-carrier system (±2.5 kHz and ±7.5 kHz), and a five-carrier system (0 kHz, ±4 kHz, and ±8 kHz).

While CLIMAX operations are a long-established standard for 25 kHz channel spacing, the modern transition to narrower 8.33 kHz channels makes offset implementation significantly more technically demanding. Adapting multi-carrier operations to fit within this tighter bandwidth—such as utilizing highly stable two-carrier systems with ±2.5 kHz offsets—is the primary focus of ongoing technical discussion and development.

#### Audio properties

The audio quality in the airband is limited by the RF bandwidth used. In the newer channel spacing scheme, the largest bandwidth of an airband channel is limited to 8.33 kHz, so the highest possible audio frequency is 4.166 kHz. In the 25 kHz channel spacing scheme, an upper audio frequency of 12.5 kHz would be theoretically possible. However, most airband voice transmissions never actually reach these limits. Usually, the whole transmission is contained within a 6 kHz to 8 kHz bandwidth, corresponding to an upper audio frequency of 3 kHz to 4 kHz. This frequency, while low compared to the top of the human hearing range, is sufficient to convey speech. Different aircraft, control towers and other users transmit with different bandwidths and audio characteristics.

#### Digital radio

A switch to digital radios has been contemplated, as this would greatly increase capacity by reducing the bandwidth required to transmit speech. Other benefits from digital coding of voice transmissions include decreased susceptibility to electrical interference and jamming. The change-over to digital radio has yet to happen, partly because the mobility of aircraft necessitates complete international cooperation to move to a new system and also the time implementation for subsequent changeover.

### Unauthorised use

It is illegal in most countries to transmit on the airband frequencies without a suitable license, although an individual license may not be required, for instance in the US where aircraft stations are "licensed by rule". Many countries' regulations also restrict communications in the airband. For instance, in Canada, airband communications are limited to those required for "the safety and navigation of an aircraft; the general operation of the aircraft; and the exchange of messages on behalf of the public. In addition, a person may operate radio apparatus only to transmit a non-superfluous signal or a signal containing non-profane or non-obscene radiocommunications."

Listening to airband frequencies without a license is also an offense in some countries. However, in certain countries, such as the UK, it is permissible to listen to as it is covered under navigational and weather related transmissions. Such activity has been the subject of international situations between governments when tourists bring airband equipment into countries which ban the possession and use of such equipment.

---

*Source: Wikipedia, Airband (https://en.wikipedia.org/wiki/Airband), by Wikipedia contributors, CC BY-SA 4.0.*
