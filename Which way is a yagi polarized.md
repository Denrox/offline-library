# Which way is a yagi polarized?

*Tags: yagi, polarization · score 5*

## Question

I am installing a yagi antenna that will receive signals from multiple omni antennas that are vertically polarized. Which way should the elements of the yagi point to match? Up and down, or horizontal?

I must not be asking the question correctly to Google because i can't find an answer anywhere.

Thanks to anyone able to help.

## Accepted answer (score 6, by Graham G8URP)

For a Yagi antenna the electrical polarisation matches the mechanical orientation of the elements. So to receive your vertically polarised signals the elements of your antenna will need to be vertical (i.e. up and down).

It does indeed seem tricky to find a clear illustration of this via Google. Wikipedia does have a clear illustration of how the electric field interacts with a half-wave dipole. It shows how the electric field is aligned with the dipole elements. This picture shows horizontal polarisation.

Source: Wikipedia

A Yagi-Uda antenna uses a half-wave dipole as the driven element. The directors and reflector are in line with the driven element.

The polarisation of a radio wave is always specified as the polarisation of the electric field component of the wave. A radio wave also has a magnetic field component which is at 90° to the electric field (omitted in the picture above). So a vertically polarised radio wave will also have a horizontal magnetic field.

Source: Wikipedia

In the picture above $ \vec {\mathrm{E}} $ represents the (vertical) electric field, $ \vec {\mathrm{B}} $ represents the (horizontal) magnetic field and **z** or $ \vec {\mathrm{V}} $ represent the direction of propagation of the radio wave (travelling towards the right of the picture). The arrows over the variables indicate they are vector quantities - that is, they have both a magnitude, shown for $ \vec {\mathrm{E}} $ and $ \vec {\mathrm{B}} $ by the length of an arrow, and a direction, shown by the direction of the arrow.

(Note that this diagram is a graph of the electric and magnetic field strengths and directions at points along the direction of propagation (the z axis) shown in the picture. If this was visible light we would call this a ray. It is not a picture of what a radio wave would look like if the fields were visible.)

## Answer (score 3, by Louis Seaman)

For what band? If you are looking to DX on HF, then horizontal is the way to go, because as AG5CI said, polarization doesn't make much difference after the first atmospheric refraction. I regularly speak to horizontally polarized stations on my vertical.

However, line-of-sight almost requires you to be polarized the same as the other stations; but here's a case where you need to know your audience...I know guys who do 2M SSB only with a horizontally polarized yagi because it limits interference with most of the other activity on the band, and it can be argued that it might be a bit better for over the horizon ground-wave.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20332/which-way-is-a-yagi-polarized, by T3chie - Bitoku Labs, Graham G8URP, Louis Seaman. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
