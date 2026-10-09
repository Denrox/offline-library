# Why is the total radiated power of array calculated by sum of square of excitation coefficients different from the result by integral of power pattern

*Tags: antenna, math, phased-array · score 3*

## Question

Consider an array with same isotropic antennas, $P_{ele}^n$ is the input power of the n***th*** antenna. As I consider antenna radiation efficiency = 1, the $P_{ele}^n$ is also the radiated power of the n***th*** antenna. If the antenna is matched, this normalized power input is proportional to the square of the input signals, or (in a normalized form) $$P_{ele}^n=|w_n|^2\tag{1}$$ where the $w_n$ is the complex weight of the n***th*** antenna. Then, the radiated power for the whole array is given by the sum of the excitation coefficients at each antenna, $$P_{rad}=\sum_{n}P_{ele}^n=\sum_{n}|w_n|^2\tag{2}$$

Meanwhile, as mentioned in [[1]](https://d1wqtxts1xzle7.cloudfront.net/50621615/Antenna_Theory_Analysis_and_Design_-Third_Edition___Constantine_A._Balanis-with-cover-page-v2.pdf?Expires=1632405475&Signature=SR8dzsbHfFlDrGq58K02G6eDA1nbfPsbdKjE-ertXmz2RLPqMr7VwFXLcAkcUqL%7EVEKsJtWQPZice9DhfAEvisyRNr9GZEqecCyimd055hSHqahzl7XaCd2A0hgZJGHUSNq77GjcGDD%7EtlKTudiC79oTGzI6WmuVZHGB33K5jjSylGzmLHOpqNWBXrTvd2TXNt0ZTSpebZhUu3RN733O84im6g4qjw%7EAvGrAKjcmergoLudLSoKLfrACmjQbJsCu8wI7iFUIJi0Vkq06baulPueO3VhXTdXeKuuEYCShN97IsxbpQ%7EXeZphtH0AIXjWRML-Ds-x%7EpMzEWB5ujDEArA__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA), [[2]](https://ww2.mathworks.cn/help/phased/ug/element-and-array-radiation-patterns-and-responses.html), the total radiated power can be calculated by the integral of the radiated intensity and the square of beampattern is proportional to the radiated intensity. Therefore, the beampattern can be used to calculated the total radiated power, $$P_{rad}=\int |B(\theta,\phi)|^2d\Omega=\int_{0}^{2\pi}\int_{0}^{\pi}|\mathbf{w}^H\mathbf{a}(\theta,\phi)|^2\sin\theta d\theta d\phi\tag{3}\label{eq3}$$ where $B(\theta,\phi)$ is the beampattern, $\mathbf{w}\in \mathbb{C}$ is the weight, $\mathbf{a}(\theta,\phi)$ is the array manifold, $\theta$, $\phi$ are azimuth and elvation angles, and $d\Omega=\sin\theta d\theta d\phi$ is the infinitesimal solid angle.

However, the simulation results im MATLAB of this two calculations are not equal. For a half-wavelength spaced 64-antenna URA (uniform rectangular array), with uniform beamformers applied ($|w_n|=1$), the total radiated can be calculated as $$P_{rad}= \sum_{n}|w_n|^2=64 W\tag{4}$$ However, the result based on \eqref{eq3} is much larger than 64$W$. Then, I thought that the excitation coefficients in calculating beampattern $B(\theta,\phi)$ should be $\mathbf{w^{\prime}}=\frac{1}{2\sqrt{\pi}}(w_1,...,w_{64})$, as each isotropic antenna radiates equally in angular space. Therefore, each isotrropic antenna has $\frac{1}{4\pi}$ power intensity, and $\frac{1}{2\sqrt{\pi}}$ field intensity, which indicates $\mathbf{w^{\prime}}=\frac{1}{2\sqrt{\pi}}(w_1,...,w_{64})$. But the result is still not equal to the 64$W$.

I don't know why these two results are not the same. Is there a scaling factor that I miss? Or I just calclulated wrong? If the scaling factor exists, then why the second calculation does not guarantee energy conservation?

**Reference**

[1]Balanis, Constantine A. Antenna theory: analysis and design. John wiley & sons, 2015.

[2]Element and Array Radiation and Response Patterns

https://ww2.mathworks.cn/help/phased/ug/element-and-array-radiation-patterns-and-responses.html?requestedDomain=cn

## Answer (score 3, by Tesla23)

It's all to do with mutuals, and you can't wish them away - even for 'ideal' antennas.

Consider a simple case, two elements a reasonable distance apart. Give them excitation amplitudes +1 and -1. From your assumptions, the radiated power is 2, irrespective of their locations. The power is no longer radiated isotropically, there is some array pattern, but you assume it integrates to 2 (this is unlikely to be exactly true, but I won't argue at this point).

Now consider the case when you move them closer together, $\lambda/2$, $\lambda/4$, $\lambda/8$ ... As they get closer, their far fields start to cancel more and more over more and more solid angle, and so the radiated power, as measured in the far field reduces - but from your assumption the radiated power is still 2. When they are very close, you still think you are radiating 2, but the far fields are very small. Something is very wrong with your model.

So this clearly demonstrates that with two elements with amplitudes +1 and -1, you have $|a_n|=1$, but the radiated power is not constant at 2, but depends on the spacing between the elements.

Now let's consider a more realistic situation, where the antennas have terminals, and the radiation amplitude of each element is proportional to the current flowing into the terminal (e.g. a dipole), but the power radiated by an element is not simply proportional to the square of the current (independent of other elements), but equal to the product of the voltage and current. When I have two elements, then:

$v_1 = z_{11} i_1 + z_{12} i_2$

$v_2 = z_{21} i_1 + z_{22} i_2$

What you will find is that when the elements get very close that $z_{12} \rightarrow z_{11}$ (look at the mutual impedances of dipoles for example). So then what you find is that if $i_1 = 1$ and $i_2 = -1$ then

$v_1 = z_{11} - z_{12} \rightarrow 0$ as the spacing tends to 0

When the fields tend to cancel in the far field, this is reflected in the input impedance that no power can enter the array.

So for the initial comment where the two elements were 'reasonably spaced', unless $z_{12}=0$, then the presence of the second driven element will affect the radiated power from the first and so the radiated power is unlikely to be 2. The same effects occur for N elements, just the maths is messier, so mutuals means that you can't assume that what you think is unity element excitation will achieve unity radiated power.

So to bring it back to your question, you are assuming that by maintaining the element excitation amplitudes at unity $|a_n|=1$, that the power radiated by each element is also 1. This is not true for two elements as my example above shows, and it appears in the power equations as a mutual interaction. It is not true in general unless you assume mutual interactions are zero, which is not physically possible. If you are dealing in impedances, mutual interactions cause currents in one element alter the voltage across others, if you are dealing in scattering parameters, mutuals cause some of the power you feed to one element to come out the feedpoint of another.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/19982/why-is-the-total-radiated-power-of-array-calculated-by-sum-of-square-of-excita, by tyrela, Tesla23. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
