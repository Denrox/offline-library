# Does geology affect radio signals?

*Tags: propagation, earth · score 5*

## Question

following on from an earlier question about [Iron Ore](Does%20iron%20ore%20in%20the%20ground%20affect%20my%20signal.md) affecting radio waves... are there any other geological properties that can affect radio waves?

Are certain frequencies more susceptible to geology than others?

## Answer (score 9, by Marcus Müller)

## Other Effects

are there any other geological properties that can affect radio waves?

Yes, there are other effects.

Basically, **every** material affects the propagation of radio waves.

### Absorption

That one's kind of obvious: radio wave hits medium (e.g. soil), gets absorbed.

That's the reason you can't look through a piece of coal – light is just a wave at a high frequency, and coal absorbs light very well.

On the radio frequency scale, that happens with all kinds of geological materials, if they don't reflect. Since you seem to be studying something geology-related: this is commonly used for radio earth exploration. Dry sand, for example, doesn't absorb all too well, but denser/moister clay does. Thus, you can build a radar that can look through sand (using the right wavelength/frequency), and "see" the clay, the salt or the aquifer below. Keyword: *ground-penetrating radar*.

### Reflection

Keywords: *Radar, Synthetic Aperture Radar, Remote Sensing*

A very common thing to observe is that metal surfaces reflect radio waves – simply because metals are excellent conductors of electricity. That leads to the fact that there can't be an electrical field *inside* the metal, and together with the physical equations describing waves, that leads to the wave having to bounce off the surface.

Now, on a geological scale, that means that reflection on the ground will work better the better the ground conducts (and it will be "straighter" and less scatter-y the flatter the ground is). Thus, saltwater bodies without waves reflect waves very well.

#### Corner Reflectors

Also, for example, if you have a wave hitting a 90° corner of reflective material (e.g. the side of ship and its deck, a sharp cliff and the sea beneath), you get nearly all of the transmitted energy back in the direction the wave came from. That's the same principle why bike reflectors have these pyramidal structures:

You'll see that being used for radio purposes, e.g. to make vessels more visible to ship radars by maximizing the amount of radio energy getting reflected back at the emitter. Can you spot the corner reflector in this seal relaxation pod buoy?

#### Scattering

On a smaller scale, flat ("flat" in the scale of a wavelength – ie. what's flat for a 200m wavelength isn't necessarily flat for a 3cm wavelength, or for light, which has some 600 nm wavelength) surface produce a "sharp" reflection, whereas rough surfaces scatter the power in all directions, randomly.

That is very commonly used in radar-based earth exploration: A satellite illuminates the earth with radio waves of horizontal polarization, and registers how much is reflected back with the same polarization, and with vertical polarization. If one polarization dominates, you have flat surfaces that you illuminate, if both polarizations are equally common, the things you illuminate randomly rotate the polarization by reflection on rough/randomly oriented smaller surfaces. You can often see SAR imagery with false colors, where one color means "transmitted horizontal, received vertical", another means "transmitted horizontal, got horizontal", another means "transmitted vertical, got vertical", and you mix these together to get an overall image. Here's an example of NASA's SAR imagery of Haiti after the disaster there (that link is good – read it!).

Vegetation with leaves and tree trunks has a high degree of random scattering, leading to much cross-polarization, which is green in the picture. Buildings have a lot of right angles, so they contain a lot of corner reflectors (see above), and thus dominant polarizations, as well as being bright due to the high amount of reflected energy at corner reflectors.

### Diffraction

Then, we have effects like diffraction – the fact that when a wave hits some kind of obstacle with an edge, it extends behind that edge. Here's an example from the wikipedia page on Diffraction. The plane wave enters from left, and then hits the yellow obstacle with a small slit in the middle.

The very same happens at the tops of mountains – at the crest, the waves "break" and diffract behind, reaching valleys that definitely don't have a line of sight to the transmitter.

In low-incident-angle spaceborne synthetic aperture radar earth imaging, that can lead to artifacts in areas that should be in the radio shadow.

### Refraction

This is usually less commonly seen with respect to geological properties, but at the same scale: if you have a material where specific electromagnetical properties change, you can "bend" waves. This is usually observed in the atmosphere, not the earth itself, so it's less of a geological than a meteorological phenomenon.

### Waveguides

You might know that the wave inside coax cables is not actually transported as electrical current in the metal conductors, but as wave in the isolator between – and the same effect can be seen with the earth and well-conducting parts of the atmosphere, especially when these are being ionized by solar radiation. So, that's at least half a geological phenomenon.

## Frequency Dependency

Keywords: *Electromagnetic Theory basics, Wavelength, Dipole*

Are certain frequencies more susceptible to geology than others?

Yes. But it's basically all a question of the relation of the size of the geological feature and the wavelength. Just like a large flat piece of copper is a very good reflector for waves of let's say 2 m wavelength, but needs to be very very polished to work well as reflector for light waves (a mirror), these effects simply scale. "Polishing to a mirror finish" simply means nothing but "making flat at the scale of light wavelengths".

Of course, given that certain things have certain sizes, yes, things are dependent on frequency (since that is proportional to the inverse of wavelength).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7711/does-geology-affect-radio-signals, by Diatu, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
