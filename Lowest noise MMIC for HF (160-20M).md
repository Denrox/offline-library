# Lowest noise MMIC for HF? (160-20M)

*Tags: hf, lna · score 3*

## Question

I recently learned that these fancy modern ultra-low noise MMIC, while having <1dB noise figure around 1Ghz could be quite bad at low frequencies due to 1/f noise.

What is lowest noise MMIC then for 160-20M bands? I am only aware of MAR-6 and INA-02184/INA-02186 having noise figure of ~2-3dB.

Does it even make sense to try to reduce noise figure of preamp below 3dB in these bands or environment noise is stronger anyway?

## Accepted answer (score 4, by Phil Frost - W8II)

The ambient noise on HF is so high that such a low noise figure will not appreciably improve performance. On 20 meters, the minimum ambient noise temperature you will encounter is about $3 \times 10^6 \:\mathrm K$, which corresponds to a noise figure of about 40 dB. Noise goes up with wavelength, reaching $3 \times 10^{10} \:\mathrm K$ or 80 dB around 1 MHz.

As a rule of thumb, if the noise figure of your receiver is 10 dB below the ambient noise, it adds no significant noise. So for HF, a receiver with a noise figure below 30 dB is already as good as it gets. See [How can I calculate the effects of an LNA, antenna gain, etc. on noise performance?](How%20can%20I%20calculate%20the%20effects%20of%20an%20LNA%2C%20antenna%20gain%2C%20etc.%20on%20noise%20performance.md) for some additional detail.

Also a point of fact: the second "M" in "MMIC" is for "microwave". As such, there are no MMICs for HF. At HF, wavelengths are so long that there's no need to shrink things to MMIC sizes. By modern standards HF hardly even qualifies as RF, and excellent performance can be achieved with discrete components or ICs not even marketed for RF.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18082/lowest-noise-mmic-for-hf-160-20m, by BarsMonster - R2AYN, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
