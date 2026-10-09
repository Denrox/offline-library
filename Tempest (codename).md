# Tempest (codename)

**TEMPEST** is a codename under the U.S. National Security Agency specification and a NATO certification referring to spying on information systems through leaking emanations, including unintentional radio or electrical signals, sounds, and vibrations. TEMPEST covers both methods to spy upon others and how to shield equipment against such spying. The protection efforts are also known as emission security (EMSEC), which is a subset of [communications security](Communications%20security.md) (COMSEC). The reception methods fall under the umbrella of radiofrequency MASINT.

The NSA methods for spying on computer emissions are classified, but some of the protection standards have been released by either the NSA or the Department of Defense. Protecting equipment from spying is done with distance, shielding, filtering, and masking. The TEMPEST standards mandate elements such as equipment distance from walls, amount of shielding in buildings and equipment, and distance separating wires carrying classified vs. unclassified materials, filters on cables, and even distance and shielding between wires or equipment and building pipes. Noise can also protect information by masking the actual data.

While much of TEMPEST is about leaking electromagnetic emanations, it also encompasses sounds and mechanical vibrations. For example, it is possible to log a user's keystrokes using the motion sensor inside smartphones. Compromising emissions are defined as unintentional intelligence-bearing signals which, if intercepted and analyzed (side-channel attack), may disclose the information transmitted, received, handled, or otherwise processed by any information-processing equipment.

### Shielding standards

Many specifics of the TEMPEST standards are classified, but some elements are public. Current United States and NATO Tempest standards define three levels of protection requirements:

- **NATO SDIP-27 Level A** (formerly AMSG 720B) and **USA NSTISSAM Level I**  
*"Compromising Emanations Laboratory Test Standard"*  
This is the strictest standard for devices that will be operated in *NATO Zone 0* environments, where it is assumed that an attacker has almost immediate access (e.g. neighbouring room, 1 metre; 3' distance).

- **NATO SDIP-27 Level B** (formerly AMSG 788A) and **USA NSTISSAM Level II**  
*"Laboratory Test Standard for Protected Facility Equipment"*  
This is a slightly relaxed standard for devices that are operated in *NATO Zone 1* environments, where it is assumed that an attacker cannot get closer than about 20 metres (66 ft) (or where building materials ensure an attenuation equivalent to the free-space attenuation of this distance).

- **NATO SDIP-27 Level C** (formerly AMSG 784) and **USA NSTISSAM Level III**  
*"Laboratory Test Standard for Tactical Mobile Equipment/Systems"*  
An even more relaxed standard for devices operated in *NATO Zone 2* environments, where attackers have to deal with the equivalent of 100 metres (330 ft) of free-space attenuation (or equivalent attenuation through building materials).

Additional standards include:

- **NATO SDIP-29** (formerly AMSG 719G)  
*"Installation of Electrical Equipment for the Processing of Classified Information"*  
This standard defines installation requirements, for example in respect to grounding and cable distances.

- **AMSG 799B**  
*"NATO Zoning Procedures"*  
Defines an attenuation measurement procedure, according to which individual rooms within a security perimeter can be classified into Zone 0, Zone 1, Zone 2, or Zone 3, which then determines what shielding test standard is required for equipment that processes secret data in these rooms.

The NSA and Department of Defense have declassified some TEMPEST elements after Freedom of Information Act requests, but the documents black out many key values and descriptions. The declassified version of the TEMPEST test standard is heavily redacted, with emanation limits and test procedures blacked out. A redacted version of the introductory Tempest handbook NACSIM 5000 was publicly released in December 2000. Additionally, the current NATO standard SDIP-27 (before 2006 known as AMSG 720B, AMSG 788A, and AMSG 784) is still classified.

Despite this, some declassified documents give information on the shielding required by TEMPEST standards. For example, Military Handbook 1195 includes the chart at the right, showing electromagnetic shielding requirements at different frequencies. A declassified NSA specification for shielded enclosures offers similar shielding values, requiring, "a minimum of 100 dB insertion loss from 1 kHz to 10 GHz." Since much of the current requirements are still classified, there are no publicly available correlations between this 100 dB shielding requirement and the newer zone-based shielding standards.

In addition, many separation distance requirements and other elements are provided by the declassified NSA red-black installation guidance, NSTISSAM TEMPEST/2-95.

### Certification

The information-security agencies of several NATO countries publish lists of accredited testing labs and of equipment that has passed these tests:

- In Canada: Canadian Industrial TEMPEST Program
- In Germany: BSI German Zoned Products List
- In the UK: UK CESG Directory of Infosec Assured Products, Section 12
- In the U.S.: NSA TEMPEST Certification Program

The United States Army also has a TEMPEST testing facility, as part of the U.S. Army Electronic Proving Ground, at Fort Huachuca, Arizona. Similar lists and facilities exist in other NATO countries.

TEMPEST certification must apply to entire systems, not just to individual components, since connecting a single unshielded component (such as a cable or device) to an otherwise secure system could dramatically alter the system RF characteristics.

### RED/BLACK separation

TEMPEST standards require "RED/BLACK separation", i.e., maintaining distance or installing shielding between circuits and equipment used to handle plaintext classified or sensitive information that is not encrypted (RED) and secured circuits and equipment (BLACK), the latter including those carrying encrypted signals. Manufacture of TEMPEST-approved equipment must be done under careful quality control to ensure that additional units are built exactly the same as the units that were tested. Changing even a single wire can invalidate the tests.

### Correlated emanations

One aspect of TEMPEST testing that distinguishes it from limits on spurious emissions (*e.g.*, FCC Part 15) is a requirement of absolute minimal correlation between radiated energy or detectable emissions and any plaintext data that are being processed.

### Public research

In 1985, Wim van Eck published the first unclassified technical analysis of the security risks of emanations from computer monitors. This paper caused some consternation in the security community, which had previously believed that such monitoring was a highly sophisticated attack available only to governments; Van Eck successfully eavesdropped on a real system, at a range of hundreds of metres, using just $15 worth of equipment plus a television set.

As a consequence of this research, such emanations are sometimes called "Van Eck radiation", and the eavesdropping technique Van Eck phreaking, although government researchers were already aware of the danger, as Bell Labs noted this vulnerability to secure teleprinter communications during World War II and was able to produce 75% of the plaintext being processed in a secure facility from a distance of 80 feet (24 metres). Additionally, the NSA published *Tempest Fundamentals, NSA-82-89, NACSIM 5000, National Security Agency* (Classified) on February 1, 1982. In addition, the Van Eck technique was successfully demonstrated to non-TEMPEST personnel in Korea during the Korean War in the 1950s.

Markus Kuhn has discovered several low-cost techniques for reducing the chances that emanations from computer displays can be monitored remotely. With CRT displays and analog video cables, filtering out high-frequency components from fonts before rendering them on a computer screen will attenuate the energy at which text characters are broadcast. With modern flat panel displays, the high-speed digital serial interface (DVI) cables from the graphics controller are a main source of compromising emanations. Adding random noise to the least significant bits of pixel values may render the emanations from flat-panel displays unintelligible to eavesdroppers but is not a secure method. Since DVI uses a certain bit code scheme that tries to transport a balanced signal of 0 bits and 1 bits, there may not be much difference between two pixel colors that differ very much in their color or intensity. The emanations can differ drastically even if only the last bit of a pixel's color is changed. The signal received by the eavesdropper also depends on the frequency where the emanations are detected. The signal can be received on many frequencies at once and each frequency's signal differs in contrast and brightness related to a certain color on the screen. Usually, the technique of smothering the RED signal with noise is not effective unless the power of the noise is sufficient to drive the eavesdropper's receiver into saturation thus overwhelming the receiver input.

LED indicators on computer equipment can be a source of compromising optical emanations. One such technique involves the monitoring of the lights on a dial-up modem. Almost all modems flash an LED to show activity, and it is common for the flashes to be directly taken from the data line. As such, a fast optical system can easily see the changes in the flickers from the data being transmitted down the wire.

Recent research has shown it is possible to detect the radiation corresponding to a keypress event from not only Wireless (radio) keyboards, but also from traditional wired keyboards [the PS/2 keyboard, for example, contains a microprocessor which will radiate some amount of radio frequency energy when responding to keypresses], and even from laptop keyboards. From the 1970s onward, Soviet bugging of US Embassy IBM Selectric typewriters allowed the keypress-derived mechanical motion of bails, with attached magnets, to be detected by implanted magnetometers, and converted via hidden electronics to a digital radio frequency signal. Each eight character transmission provided Soviet access to sensitive documents, as they were being typed, at US facilities in Moscow and Leningrad.

In 2014, researchers introduced "AirHopper", a bifurcated attack pattern showing the feasibility of data exfiltration from an isolated computer to a nearby mobile phone, using FM frequency signals.

In 2015, "BitWhisper", a "covert signaling channel between air-gapped computers using thermal manipulations" was introduced. BitWhisper supports bidirectional communication and requires no additional dedicated peripheral hardware. Later in 2015, researchers introduced GSMem, a method for exfiltrating data from air-gapped computers over cellular frequencies. The transmission – generated by a standard internal bus – renders the computer into a small cellular transmitter antenna. In February 2018, research was published describing how low-frequency magnetic fields can be used to escape sensitive data from Faraday-caged, air-gapped computers with malware code-named 'ODINI' that can control the low-frequency magnetic fields emitted from infected computers by regulating the load of CPU cores.

In 2018, a class of side-channel attack was introduced at ACM and Black Hat by the Eurecom researchers who named it "screaming channels". This kind of attack targets mixed-signal chips — containing an analog and digital circuit on the same silicon die — with a radio transmitter. The results of this architecture, often found in connected objects, is that the digital part of the chip will leak some metadata on its computations into the analog part, which leads to metadata's leak being encoded in the noise of the radio transmission. Thanks to signal-processing techniques, researchers were able to extract cryptographic keys used during the communication and decrypt the content. This attack class is supposed, by the authors, to be known already for many years by governmental intelligence agencies.

---

*Source: Wikipedia, Tempest (codename) (https://en.wikipedia.org/wiki/Tempest_%28codename%29), by Wikipedia contributors, CC BY-SA 4.0.*
