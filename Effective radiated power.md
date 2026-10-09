# Effective radiated power

**Effective radiated power** (**ERP**), synonymous with **equivalent radiated power**, is an IEEE standardized definition of directional radio frequency (RF) power, such as that emitted by a radio transmitter. It is the total power that would have to be radiated by a [half-wave dipole antenna](Dipole%20antenna.md) to give the same radiation intensity (signal strength, or power flux density, expressed as power per area) as the actual source antenna at a distant receiver located in the direction of the antenna's strongest beam (main lobe). ERP measures the combination of the power emitted by the transmitter and the ability of the antenna to direct that power in a given direction. It is equal to the input power to the antenna multiplied by the gain of the antenna. It is used in electronics and telecommunications, particularly in broadcasting to quantify the apparent power of a broadcasting station experienced by listeners in its reception area.

An alternate parameter that measures the same thing is **effective isotropic radiated power** (**EIRP**). Effective isotropic radiated power is the hypothetical power that would have to be radiated by an isotropic antenna to give the same ("equivalent") signal strength as the actual source antenna in the direction of the antenna's strongest beam. The difference between EIRP and ERP is that ERP compares the actual antenna to a half-wave dipole antenna, while EIRP compares it to a theoretical isotropic antenna. Since a half-wave dipole antenna has a gain of about 1.64 (or about 2.15 [dB](Decibel.md)) compared to an isotropic radiator, if ERP and EIRP are expressed as power their relation is $$\ \mathsf{EIRP}_\mathsf{(W)} \approx 1.64 \times \mathsf{ERP}_\mathsf{(W)}\ $$ If they are expressed in decibels $$\ \mathsf{EIRP}_\mathrm{(dBm)} \approx \mathsf{ERP}_\mathrm{(dBm)} + 2.15\ \mathsf{dB}\ $$

### Definitions

Effective radiated power and effective isotropic radiated power both measure the power density a radio transmitter and antenna (or other source of electromagnetic waves) radiate in a specific direction: in the direction of maximum signal strength (the "main lobe") of its radiation pattern. This apparent power is dependent on two factors: the total power output and the radiation pattern of the antenna – how much of that power is radiated in the direction of maximal intensity. The latter factor is quantified by the antenna gain, which is the ratio of the signal strength radiated by an antenna in its direction of maximum radiation to that radiated by some *necessarily named* standard antenna. (Without specifying a standard for comparison there can be no ratio.) For example, a 1,000 watt transmitter feeding an antenna with a gain of 4× compared to a theoretical isotropic antenna, or about 6 dBi, will radiate the same power in the direction of its main lobe, and thus the same EIRP, as a 4,000 watt transmitter feeding the theoretical isotropic antenna radiates in all directions equally. So ERP and EIRP are measures of radiated power that can compare different combinations of transmitters and antennas on an equal basis.

In spite of the names, ERP and EIRP do not measure transmitter power or total power radiated by the antenna; they are just measures of signal strength along the main lobe. They give no information about power radiated in other directions or total power. ERP and EIRP are always greater than the actual total power radiated by the antenna.

The difference between ERP and EIRP is that antenna gain has traditionally been measured in two different units, comparing the antenna to two different standard antennas, both theoretical; an isotropic antenna and a (perfect, lossless) half-wave dipole:

- *Isotropic gain* is the ratio of the power density (signal strength, in power per area) received at a point far from the antenna (i.e. in its far field) in the direction of its maximum radiation (i.e. its main lobe), $$\ S_\mathsf{max}\ $$, to the power density received at the same point from a hypothetical lossless isotropic antenna, which radiates equally in all directions, $$\ S_\mathsf{max,iso}\ $$: $$\ \mathrm{G}_\mathsf{i} = \frac{\ S_\mathsf{max}\ }{\ S_\mathsf{max,iso}\ }\ $$ Gain is often expressed in logarithmic units of [decibels](Decibel.md) (dB). The gain relative to an isotropic antenna and expressed in decibels, dBi, is given by

$$
\ \mathrm{G}_\mathsf{(dB_i)} = 10\ \log_{10}\left( \frac{\ S_\mathsf{max}\ }{\ S_\mathsf{max,iso}\ } \right)\ 
$$

- *Dipole gain* is the ratio of the power density (signal strength, in power per area) received at a point far from the antenna (i.e. in its far field) in the direction of its maximum radiation (i.e. its main lobe), $$\ S_\mathsf{max}\ $$, to the power density received at the same point from a hypothetical lossless half-wave dipole antenna, $$S_\mathsf{max,dipole}$$:$$\ \mathrm{G}_\mathsf{d} = \frac{\ S_\mathsf{max}\ }{\ S_\mathsf{max,dipole}\ }\ $$ The gain relative to a half-wave dipole antenna and expressed in decibels, dBd, is given by $$\ \mathrm{G}_\mathsf{(dB_d)} = 10\ \log_{10}\left( \frac{\ S_\mathsf{max}\ }{\ S_\mathsf{max,dipole}\ } \right)\ $$

In contrast to an isotropic antenna, the dipole has a "donut-shaped" radiation pattern; its radiated power is maximum in directions perpendicular to the antenna, declining to zero on the antenna axis. Since the radiation of the dipole is concentrated in horizontal directions (assuming the antenna axis is vertical), the gain of a half-wave dipole is greater than that of an isotropic antenna. The isotropic gain of a half-wave dipole is about 1.64, or, in decibels, $$\ 10\ \log_{10}(1.64) \approx 2.15\ \mathsf{dB}\ ,$$ so $$\ G_\mathsf{i} \approx 1.64\ G_\mathsf{d} ~.$$ In decibels $$\ G_\mathsf{(dB_i)} \approx G_\mathsf{(dB_d)} + 2.15\ \mathsf{dB} ~.$$

The two measures EIRP and ERP are based on the two different standard antennas above:

- EIRP is defined as the RMS power input required to a theoretical lossless isotropic antenna to radiate the same maximum power density far from the antenna as the actual transmitter and antenna do in the direction of greatest power (i.e. the main lobe). It is equal to the power input to the transmitter's antenna multiplied by the antenna gain relative to isotropic $$\ \mathrm{EIRP} = G_\mathsf{i}\ P_\mathsf{in} ~.$$ The ERP and EIRP are also often expressed in [decibels](Decibel.md) (dB). The input power in decibels is usually calculated with comparison to a reference level of one watt (W): $$\ P_{\mathsf{in}\ \mathsf{(dB_W)}} = 10\ \log_{10} P_\mathsf{in} ~.$$ Since multiplication of two factors is equivalent to addition of their decibel values $$\ \mathsf{EIRP}_\mathsf{(dB_W)} = G_\mathsf{(dB_i)} + P_{\mathsf{in}\ \mathsf{(dB_W)}}\ $$

- ERP is defined as the RMS power input required to a theoretical lossless half-wave dipole to give the same maximum power density far from the antenna as the actual transmitter. It is equal to the power input to the transmitter's antenna multiplied by the antenna gain relative to a (theoretical, perfect, lossless) half-wave dipole: $$\ \mathsf{ERP} = G_\mathsf{d}\ P_\mathsf{in} ~.$$ In decibels $$\ \mathsf{ERP}_\mathsf{(dB_W)} = G_\mathsf{(dB_d)} + P_{\mathsf{in}\ \mathsf{(dB_W)}} ~.$$

Since the two definitions of gain only differ by a constant factor, so do ERP and EIRP $$\ \mathsf{EIRP}_\mathsf{(W)} \approx 1.64 \times \mathsf{ERP}_\mathsf{(W)} ~.$$ In decibels $$\ \mathsf{EIRP}_\mathsf{(dB_W)} \approx \mathsf{ERP}_\mathsf{(dB_W)} + 2.15\ \mathsf{dB} ~.$$

### Relation to transmitter output power

The transmitter is usually connected to the antenna through a number of different parts such as a filter, transmission line and impedance matching network. Since these components may have significant losses $$\ L\ ,$$ the power applied to the antenna is usually less than the output power of the transmitter $$\ P_\mathsf{TX} ~.$$ The relation of ERP and EIRP to transmitter output power is $$\ \mathsf{EIRP}_\mathsf{(dB_W)} = P_{\mathsf{TX}\ \mathsf{(dB_W)}} - L_\mathsf{(dB)} + G_\mathsf{(dB_i)}\ ,$$ $$\ \mathsf{ERP}_\mathsf{(dB_W)} = P_{\mathsf{TX}\ \mathsf{(dB_W)}} - L_\mathsf{(dB)} + G_\mathsf{(dB_i)} - 2.15\ \mathsf{dB} ~.$$ Losses in the antenna itself are included in the gain.

### Relation to signal strength

If the signal path is in free space ([line-of-sight propagation](Line-of-sight%20propagation.md) with no [multipath](Multipath%20propagation.md)) the signal strength (power flux density in watts per square meter) $$\ S\ $$ of the radio signal on the main lobe axis at any particular distance $$r$$ from the antenna can be calculated from the EIRP or ERP. Since an isotropic antenna radiates equal power flux density over a sphere centered on the antenna, and the area of a sphere with radius $$\ r\ $$ is $$\ A = 4\pi\ r^2\ $$ then $$\ S(r) = \frac{\ \mathsf{EIRP}\ }{\ 4\pi\ r^2\ } ~.$$ Since $$\ \mathrm{EIRP} = \mathrm{ERP} \times 1.64\ ,$$ $$\ S(r) = \frac{\ 0.410 \times \mathsf{ERP}\ }{\ \pi\ r^2\ } ~.$$ After dividing out the factor of $$\ \pi\ ,$$ we get: $$\ S(r) = \frac{\ 0.131 \times \mathsf{ERP}\ }{\ r^2\ } ~.$$

However, if the radio waves travel by [ground wave](Ground%20wave.md) as is typical for medium or longwave broadcasting, [skywave](Skywave.md), or indirect paths play a part in transmission, the waves will suffer additional attenuation which depends on the terrain between the antennas, so these formulas are not valid.

### Dipole vs. isotropic radiators

Because ERP is calculated as antenna gain (in a given direction) as compared with the maximum directivity of a half-wave [dipole antenna](Dipole%20antenna.md), it creates a mathematically virtual effective dipole antenna oriented in the direction of the receiver. In other words, a notional receiver in a given direction from the transmitter would receive the same power if the source were replaced with an ideal dipole oriented with maximum directivity and matched polarization towards the receiver and with an antenna input power equal to the ERP. The receiver would not be able to determine a difference. Maximum directivity of an ideal half-wave dipole is a constant, i.e.,  0 dBd = 2.15 dBi . Therefore, ERP is always 2.15 dB less than EIRP. The ideal dipole antenna could be further replaced by an isotropic radiator (a purely mathematical device which cannot exist in the real world), and the receiver cannot know the difference so long as the input power is increased by 2.15 dB.

The distinction between dBd and dBi is often left unstated and the reader is sometimes forced to infer which was used. For example, a [Yagi–Uda antenna](Yagi%20Uda%20antenna.md) is constructed from several dipoles arranged at precise intervals to create greater energy focusing (directivity) than a simple dipole. Since it is constructed from dipoles, often its antenna gain is expressed in dBd, but listed only as dB. This ambiguity is undesirable with respect to engineering specifications. A Yagi–Uda antenna's maximum directivity is  8.77 dBd = 10.92 dBi . Its gain necessarily must be less than this by the factor η, which must be negative in units of dB. Neither ERP nor EIRP can be calculated without knowledge of the power accepted by the antenna, i.e., it is not correct to use units of dBd or dBi with ERP and EIRP. Let us assume a 100 watt (20 dBW) transmitter with losses of 6 dB prior to the antenna. ERP < 22.77 dBW and EIRP < 24.92 dBW, both less than ideal by  η  in dB. Assuming that the receiver is in the first side-lobe of the transmitting antenna, and each value is further reduced by 7.2 dB, which is the decrease in directivity from the main to side-lobe of a Yagi–Uda. Therefore, anywhere along the side-lobe direction from this transmitter, a blind receiver could not tell the difference if a Yagi–Uda was replaced with either an ideal dipole (oriented towards the receiver) or an isotropic radiator with antenna input power increased by 1.57 dB.

### Polarization

Polarization has not been taken into account so far, but it must be properly clarified. When considering the dipole radiator previously we assumed that it was perfectly aligned with the receiver. Now assume, however, that the receiving antenna is circularly polarized, and there will be a minimum 3 dB polarization loss *regardless* of antenna orientation. If the receiver is also a dipole, it is possible to align it orthogonally to the transmitter such that theoretically zero energy is received. However, this polarization loss is not accounted for in the calculation of ERP or EIRP. Rather, the receiving system designer must account for this loss as appropriate. For example, a cellular telephone tower has a fixed linear polarization, but the mobile handset must function well at any arbitrary orientation. Therefore, a handset design might provide dual polarization receive on the handset so that captured energy is maximized regardless of orientation, or the designer might use a circularly polarized antenna and account for the extra 3 dB of loss with amplification.

### FM example

For example, an [FM](Frequency%20modulation.md) radio station which advertises that it has 100,000 watts of power actually has 100,000 watts ERP, and *not* an actual 100,000-watt transmitter. The transmitter power output (TPO) of such a station typically may be 10,000–20,000 watts, with a gain factor of 5–10× (5–10×, or 7–10 [dB](Decibel.md)). In most antenna designs, gain is realized primarily by concentrating power toward the horizontal plane and suppressing it at upward and downward angles, through the use of phased arrays of antenna elements. The distribution of power versus elevation angle is known as the *vertical pattern*. When an antenna is also directional horizontally, gain and ERP will vary with azimuth (compass direction). Rather than the average power over all directions, it is the apparent power in the direction of the peak of the antenna's main lobe that is quoted as a station's ERP (this statement is just another way of stating the definition of ERP). This is particularly applicable to the huge ERPs reported for shortwave broadcasting stations, which use very narrow beam widths to get their signals across continents and oceans.

#### United States regulatory usage

ERP for FM radio in the United States is always relative to a theoretical [reference half-wave dipole](Dipole%20antenna.md) antenna. (That is, when calculating ERP, the most direct approach is to work with antenna gain in dBd). To deal with antenna polarization, the Federal Communications Commission (FCC) lists ERP in both the horizontal and vertical measurements for FM and TV. Horizontal is the standard for both, but if the vertical ERP is larger it will be used instead.

The maximum ERP for US FM broadcasting is usually 100,000 watts (FM Zone II) or 50,000 watts (in the generally more densely populated Zones I and I-A), though exact restrictions vary depending on the class of license and the antenna height above average terrain (HAAT). Some stations have been grandfathered in or, very infrequently, been given a waiver, and can exceed normal restrictions.

### Microwave band issues

For most microwave systems, a completely non-directional isotropic antenna (one which radiates equally and perfectly well in every direction – a physical impossibility) is used as a reference antenna, and then one speaks of EIRP (effective *isotropic* radiated power) rather than ERP. This includes satellite transponders, radar, and other systems which use microwave dishes and reflectors rather than dipole-style antennas.

### Lower-frequency issues

In the case of medium wave (AM) stations in the United States, power limits are set to the actual transmitter power output, and ERP is not used in normal calculations. Omnidirectional antennas used by a number of stations radiate the signal equally in all horizontal directions. Directional arrays are used to protect co- or adjacent channel stations, usually at night, but some run directionally continuously. While antenna efficiency and ground conductivity are taken into account when designing such an array, the FCC database shows the station's transmitter power output, not ERP.

### Related terms

According to the Institution of Electrical Engineers (UK), ERP is often used as a general reference term for radiated power, but strictly speaking should only be used when the antenna is a half-wave dipole, and is used when referring to FM transmission.

#### EMRP

**Effective monopole radiated power** (**EMRP**) may be used in Europe, particularly in relation to medium wave broadcasting antennas. This is the same as ERP, except that a short vertical antenna (i.e. a short [monopole](Monopole%20antenna.md)) is used as the reference antenna instead of a half-wave dipole.

#### CMF

**Cymomotive force** (**CMF**) is an alternative term used for expressing radiation intensity in volts, particularly at the lower frequencies. It is used in Australian legislation regulating AM broadcasting services, which describes it as: "for a transmitter, [it] means the product, expressed in volts, of:  
(a) the electric field strength at a given point in space, due to the operation of the transmitter; and  
(b) the distance of that point from the transmitter's antenna".

It relates to AM broadcasting only, and expresses the field strength in "microvolts per metre at a distance of 1 kilometre from the transmitting antenna".

### HAAT

The height above average terrain for VHF and higher frequencies is extremely important because the signal coverage (broadcast range) produced by a given ERP dramatically increases with antenna height. Because of this, it is possible for a station of only a few hundred watts ERP to cover more area than a station of a few thousand watts ERP, if its signal travels above obstructions on the ground.

---

*Source: Wikipedia, Effective radiated power (https://en.wikipedia.org/wiki/Effective_radiated_power), by Wikipedia contributors, CC BY-SA 4.0.*
