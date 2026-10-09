# 2 meter and 70cm OSCAR expected signal attenuation by topocentric elevation angle, chart?

*Tags: satellites, path-loss · score 3*

## Question

On average, is there a chart, or formula, which shows an expected signal attenuation due to the elevation angle to the satellite's position? I understand that range (distance) is also going to affect the signal path, so in order to simplify the problem, consider this in the context of a LEO circular orbit OSCAR, or, the ISS, where the height above the earth is very near unchanging, and the only thing changing the signal strength is the elevation angle. (Assume also the optimal antenna orientation and polarization). Yes, of course, a low elevation angle typically means the bird is further away, but what I am looking for is the effect of the signal needing to travel through much more atmosphere as the elevation angle is further from the zenith, and closer to the horizon.

When such a chart or formula is then combined with losses due to distance, the hope is a result that is fairly reliable for predicting signal path strength. I imagine height above the earth's surface is also very important. since, for example, a signal from Mars is not going to be changing much in strength due to a change in distance on the same day, compared to the atmospheric attenuation at the zenith compared to at 5 degrees above the horizon. This is why I specified the context of a LEO OSCAR in a circular orbit, or the ISS (ARISS). In such cases, all else being equal and optimal, the signal strength will be more greatly attenuated if it has to travel through more atmosphere because of a low elevation angle. So the question is, *by how much, based on the elevation angle (and band)?*, and, *is there a chart or formula for predicting this attentuation, based on elevation angle (and band)?*.

## Accepted answer (score 5, by hobbs - KC2G)

It's close enough to zero at 2m and 70cm that I wouldn't bother computing it. Judging by ITU-R P.676 the attenuation due to the atmosphere is less than 0.01 dB/km for all frequencies below 1 GHz, and the contribution of water vapor is negligible below 3 GHz. Figure 6 shows that the attenuation at the zenith is 0.03 dB at 1 GHz, and equation 28 says that for elevations between 5 and 90 degrees, it's valid to get the path attenuation by just dividing the zenith attenuation by the sine of the elevation angle. That gives a loss of about 0.35 dB at 5°. So the difference in atmospheric loss between the satellite being straight up and almost on the horizon is about 0.3dB, but the difference in free-space loss due to distance is more than 10dB.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16151/2-meter-and-70cm-oscar-expected-signal-attenuation-by-topocentric-elevation-an, by always_learning, hobbs - KC2G. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
