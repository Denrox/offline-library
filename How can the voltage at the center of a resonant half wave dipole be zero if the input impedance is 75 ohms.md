# How can the voltage at the center of a resonant half wave dipole be zero if the input impedance is 75 ohms?

*Tags: antenna-theory, impedance, dipole, math · score 8*

## Question

If the input impedance of a resonant half wave dipole at the feed point is 75 + j0 ohms, then if an AC sine wave voltage V is applied to the feed point, how can the voltage at the center be zero ? Ohms law always applies correct ? So for the rms value then voltage is Vrms = Irms x Z right ? so Z = Vrms / Irms = Vrms / 75 +j 0 = 0.

The picture from Wikipedia below clearly shows that the voltage is always zero at the center. My understanding is that this picture shows the standing waves on a dipole. The standing waves are the result of the applied AC voltage across the feed point and vary in amplitude over time but have a fixed voltage profile in space along the length of the dipole. I thought that anywhere along the length of the dipole ohms law always applies.

Is the 'voltage' in the picture the voltage potential with respect to the center of the dipole ? and the one which results from that applied to the feed point ? The applied voltage potential difference results in a current which is the movement of electrons in the dipole in one direction during the positive half cycles of the ac waveform and in the opposite direction during the negative half right ?

What am i missing.

Is the voltage not really zero but rather I / Z = I / 75 + j 0 which is not zero ?

And then, if the voltage is not really zero, how come it's ok to connect the center of the driven element in a yagi to the boom because the voltage at the center is zero ?

Someone please help before my brain implodes !!!! :)

## Accepted answer (score 5, by Andrew)

After all this time no one has actually provided a complete answer to this question so after some investigation i have answered it myself.

Thank you to those people who did give answers however.

The animation in my question is related to the graph shown below. This graph which appears in numerous text books is confusing and misleading, as is the animation in my question.

The graph appears to show a snapshot in an instant of time of the voltage and current of the standing wave on a 1/2 wave dipole when the current is at a maximum, along with the resultant impedance Z.

The graphs confuses the reader in the following three ways.

1.

Any normal person who looks at this graph would assume that the impedance Z at each point on the antenna is the voltage of the standing wave divided by the current of the standing wave at each point according to ohm's law. Then the astute reader asks : how can Z at the center be 73 Ω when the voltage at the center is 0 ? ... Z = E/I so Z = 0/I = 73 Ω ?

2.

The impedance Z is shown as a single number so you get the impression that this impedance Z is a real number which doesn't have any reactance and so no relationship in phase with anything.

3.

The graph shows that the dipole is all one piece and not split in the middle.

To clarify, voltage here means the single ended AC RF voltage potential in volts present on the antenna elements at any point with respect to earth or zero volts, and current means AC RF current flowing through the antenna elements in amps. Voltage and current could be specified in peak, peak to peak, average or RMS, so long as the same units are used in the one context.

In truth the graph is showing the correct distribution of the voltage and current of the standing wave on a 1/2 wave dipole, however the impedance Z it depicts is actually the real part of the feed point impedance which would be present across two feed points terminals positioned along the various points along the length of the dipole elements.

The feed point impedance isn't the voltage of the standing wave divided by the current of the standing wave, but rather is a complex quantity equivalent to the differential voltage of the applied source across the two feed points divided by the resultant current of the standing wave at the feed points, the real part being equal to the radiation resistance of the antenna. For a series current fed center feed point the real part of the impedance is as everyone knows about 73 ohms and for a resonant dipole the current of the standing wave is in phase with the voltage of the applied source at the feed points.

The voltage of the standing wave divided by the current of the standing wave at any point along the antenna is actually called the Wave Impedance, and is a complex quantity which changes along the length of the antenna according to ohm's law. The wave impedance present at each point along the antenna isn't the same thing as the feed point impedance present across two feed point terminals.

The graph confuses feed point impedance with wave impedance and gives the reader the impression that the wave impedance is the feed point impedance by plotting standing wave voltage and current along the dipole with the real part of the feed point impedance. The impedance of free space you read about everywhere is actually the wave impedance of free space.

The animation in my question was taken from the Wikipedia article for a Half Wave Dipole. The text in the article does a very bad job at explaining what the animation is. The voltage and current in the animation are that of the standing wave on the antenna, which is circulating reactive stored energy present due to the fact that the antenna is a resonant system. The voltage and current of the standing wave are close to 90° out of phase with each other. The departure of phase difference away from 90 ° is the in-phase component of the standing wave which is responsible for radiation, the out of phase energy of the standing wave remains in the antenna. The animation erroneously shows that the voltage of the standing wave exists in the gap between the two feed points and so the voltage of the standing wave at the feed points is not always zero during each cycle of applied RF. This is not the case for a resonant antenna where the voltage of the standing wave which is about 90° out of phase with the applied RF at the feed points is always zero at the feed points.

I contacted the author of the animation in Wikipedia and managed to convince him to update the image, although the text in the article still doesn't explain the relationship between feed point impedance, and phase of the source and standing wave of a dipole antenna.

A plumbers delight yagi with the driven element connected to the boom at the center only works when the electrical length of the driven element is exactly 1/2 λ where the center of the driven element is in fact a zero volts all the time, and when its used with a gamma match or similar. In this configuration where the dipole is all one piece, the feed point impedance Z is seen between the center of the dipole and the end of the gamma match, as compared to between the two inner ends of the elements of a dipole split in the middle.

## Answer (score 7, by Cecil - W5DXP)

Look closer at the diagram. At the two wires coming from the source, the voltage is NOT always zero. The only way for the voltage at the center **point** to be zero is for the two source wires to occupy the same **point** which is impossible. Think about the voltage as an electric field which is indeed zero at the **point** halfway between the two wires.

## Answer (score 4, by Glenn W9IQ)

The simple answer is that the graphic is not accurate. There is an RMS voltage present at the center feed point of the dipole that follows Ohm's law relative to the feed point impedance.

Most likely, the graphic is attempting to make the point that a center fed half wave dipole is fed at the current maxima. As such, the feed point voltage is therefore at its minima - but not zero.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12112/how-can-the-voltage-at-the-center-of-a-resonant-half-wave-dipole-be-zero-if-th, by Andrew, Cecil - W5DXP, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
