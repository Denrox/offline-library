# Antenna for receiving 868MHz rocket telemetry: QFH(QHA), Helical, or?

*Tags: antenna, antenna-construction, uhf · score 7*

## Question

I'm building a radio communication system for an amateur rocket project. We've decided to use LoRa 868MHz system. My question is, which antenna for the ground station will be the best choice? We're aiming for both vertical and horizontal gain, as we have to receive telemetry both mid-flight and after landing, to locate the rocket. Also, if QFH, then how to maintain precision while building such a small QFH antenna?

## Answer (score 3, by Glenn W9IQ)

My question is, which antenna for the ground station will be the best choice?

This answer to this question requires that some data be gathered and calculations performed in order to provide a reliable answer. The primary formula is the Friis equation but I will break it into its constituent parts. You have not given enough of the data required to calculate your specific situation, so I will work through some examples.

**Link Budget**

The link budget is a determination of the maximum loss that the signal can endure and still allow for reliable communications. This data can normally be gathered from the manufacturer's data sheets for the receiver and transmitter. These figures are typically expressed in the units of dBm (decibels compared to 1 millwatt). Let's assume for this exercise that the receiver has a sensitivity of -130 dBm and the transmitter puts out 10 dBm. The link budget is therefore:

$$dB_{Link}= dBm_t-dBm_r \tag 1$$

which yields 140 dB in this case. Often the manufacturer's data is a bit optimistic so we will build in a safety factor for this later.

**Free Space Path Loss**

The next factor that comes into play is the free space path loss (FSPL). This phenomenon occurs because the signal is spreading out as it travels so this reduces the irradiance for a given receive antenna aperture (think about how a flashlight/torch shone on an object, appears to be dimmer the further away the object becomes) . FSPL in dB is given as:

$$dB_{FSPL}=20\log\left(\frac{4\pi d}{\lambda}\right) \tag 2$$

where $\lambda$ is the wavelength of the frequency involved (300/Frequency in MHz) and d is the distance in meters. The dB is a unit that compares the ratio of two powers. Because it is calculated using a logarithm, very large or small ratios are expressed as a more "manageable" number.

The 868 MHz signal has a wavelength of ~0.346 meters. The distance is the line of sight distance to the maximum expected altitude of the rocket. Consider that this must also include the downrange drift of the rocket as well as the separation distance of the receive antenna sight from the launch point. To take an extreme number, let's use the ~118 km achievement of the GoFast rocket. This gives us an FSPL of ~133 dB.

This 133 dB is subtracted from the 140 dB link budget calculated earlier leaving 7 dB. Because this number is positive, we have 7 dB of link budget "left over" so the antennas can offer moderate performance and still meet this requirement.

But to use a more practical example for amateur rockets achieving a maximum line of sight height of say 500 meters, the FSPL is ~85 dB. Subtracting this from the 140 dB link budget leaves a very respectable 55 dB budget. This means that there is plenty of link budget left - the antennas can be quite marginal.

**Antenna Gain**

Antenna gain can be loosely thought of as how well an antenna can focus its radiated power. The higher the gain of the antenna, generally the narrower (more focused) the main lobe (beam) of the antenna becomes. The same concept can be applied to an antenna that is receiving signals. The gain of the receive antenna and the gain of the transmit antenna added together is the total antenna gain. Antenna gain is typically specified as dBi (dB gain compared to an isotropic antenna)

The antenna on the rocket will likely have minimal or negative gain due to the constraints of rocket mass and geometry as well as the orientation of the antenna relative to the ground station. For example, a small dipole installed along the length of the rocket body would normally have a gain of ~ 5 dBi. But if the ground station is directly under at the launch point, the gain could be closer to -10 dBi due to the main lobe of the antenna being perpendicular to the body of the rocket and therefore not favorable in the direction of the ground antenna. This often makes a strong case for locating the ground antenna somewhat downrange in order to have a better gain perspective.

For the ground antenna, one must give consideration to the fact that as the gain of the antenna increases, the main lobe typically becomes narrower. This often then necessitates that the ground antenna be steerable to follow the flight path of the rocket. For a low altitude rocket, it may be sufficient to point the ground antenna towards the expected apogee.

The referenced QFH (Quadrifilar Helix) has been optimized to allow non-geosynchronous satellite signals to be received without the need to aim the antenna towards the path of the satellite. The trade-off is that the antenna has relatively low gain due to its main lobe being nearly hemispherical. The gain depends heavily on construction details but typically ranges from 0 to 3 dBi.The QFH antenna also has circular polarization. If used with a linearly polarized antenna, there is a 3 dB gain penalty incurred.

If we use these two antennas together and include the 3 dB penalty for circular to linear cross polarization, the combined worse case gain is -13 dB and the best case gain is 5 dB. It is a best practice to allow at least a 10 dB safety margin in the link budget but even with this we still have ample (positive) dB's left in the link budget so this antenna pair should function well for this sample application. It might, however, be marginal for the GoFast rocket example.

Due to the construction complexity of a QFH antenna, I would consider a simple quarter wave ground plane antenna or a vertical 1/2 wave dipole as the ground antenna for this example. Either one would be kept at least 1 meter off of the ground via a non-conducting support with the top of the antenna tilted to ~60 degrees away from the line of trajectory of the rocket. Due to the large remaining link budget, an error in the tilting of either of these antennas will not be detrimental to communications. The gain of either of these antennas will exceed 4 dBi and the 3 dB polarization penalty is not incurred.

**Recovery Phase**

Finding the rocket once it has returned to ground presents some unique challenges. The foliage and ground will attenuate the transmitter signal and the terrain will scatter the transmitter signal. The receive antenna needs to be directional so that you can scan for the location of the rocket by sweeping the main lobe of the antenna back and forth. The receive antenna must also be easily carried in order to "go into the field" to find the downed rocket. A small Yagi antenna works well for these purposes.

Typically visual or GPS tracking of the landing trajectory gets the observer very close to the actual landing location. This helps in the recovery phase since this effectively increases the link budget. In the event of a parachute failure, the recover phase can be very frustrating.

**Conclusion**

The Friis equation provides an analytical method to determine if line of sight communications are possible. The example worked through in this answer is purely hypothetical so the OP should collect the parameters that apply to the specific application and use the described formulas to calculate the necessary antenna gains for the specific application.

If the link budget cannot be met with reasonable antennas, then the receiver sensitivity, the transmitter power, and even the frequency used are candidates for improving the link budget to make it a reliable communications system.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12373/antenna-for-receiving-868mhz-rocket-telemetry-qfh-qha-helical-or, by leller, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
