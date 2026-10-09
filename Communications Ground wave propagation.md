# Communications : Ground wave propagation

*Tags: antenna, propagation · score 8*

## Question

I was studying ground wave propagation, my book writes the lines about it without explaining it. I really do not know any explanation for these queries coming in my mind. I've Googled it, and you will get nothing so good for these queries on Ground wave propagation.

1.

When the radio signal travels along the earth's surface, how it induces current in it? (I read somewhere that the electric field part of the wave will make electrons go out of association with the nucleus, all this happening in earth, hence currents)

2.

How will the wave tilt towards the earth after the induction of current in the earth?

3.

The attenuation of the surface increases very rapidly with increase in frequency of the signal. How?

Note: Answer only for the level of Class 12 students required.

I seriously do not know anything about the last two questions. Any help would be praised for the one who will solve all these three questions.

## Answer (score 9, by Marcus Müller)

So, I'll take this very smoothly. The idea is to take you from ray optics gradually to an understanding of radiomagnetic waves as actual waves, and show that it all makes sense.

## 1 idea: Refraction on a material interface (high->low density)

We remember what happens when we have ray of light, leaving a optically denser medium (e.g., water) into a less dense one (e.g. air):

The ray is *refracted* away from the normal of the interface (image taken from wikipedia's refraction article & cropped).

We can actually calculate how $\theta_1$ and $\theta_2$ are related; it's *Snell's law* that you might already know:

$$\frac{\sin(\theta_1)}{\sin(\theta_2)}= \frac{n_2}{n_1}$$

with $n_i$ being the *refractive index* of the medium (air or water).

## 2 idea: Water on a sphere

Now, imagine you're standing on sphere (like, a planet). Your planet is completely covered in very very salty water, and above that, is air.

You're of the water-dwelling kind, and you hold an orange laser pointer nicely horizontally:

So, in this drawing, you stand at point $B$, and hold your laser pointer straight vertically (that is, perpendicularly to the planet radius $\bar{BA}$. At point $C$, the ray hits the saltwater-air interface in the angle $\delta$.

Our job is now to find $\delta$, because we know the refractive indices of air and saltwater, and we can then calculate under which angle the ray will leave the saltwater¹.

We know that on the saltwater-air-interface, the ray will be refracted *away* from the normal, that is, closer to the ocean surface. So, the ray will already have one "bend", that looks like it "hugs" the ocean surface curvature a bit.

## 3 idea: Water in layers.

Now we realize that this ocean is pretty deep, and that the water isn't constantly salty – the deeper waters are way more salty than the waters close to the surface.

Let's even think these different degrees of saltiness come in layers. Then, we can imagine there being a lot of interfaces like the water-air interface from the second idea :)

Since salty water is at the bottom and has a higher refractive index than less salty water, we get such a bend at every interface. The ray is getting bend more and more to "hug" the spheres, until, at the end, it practically "rides" on a circle-like shape that it really can't leave (because it's always refracted back a little bit more).

## 4 idea: From rays to waves

Now, the first big thing to simply swallow is: Laser light and, let's say, mediumwave radio broadcast, are really just the same thing: electromagnetic waves. There's zero difference between them, other than that an orange laser has maybe a wavelength of 600 nm, whereas your medium wave broadcast might have a wavelength of 600 m, that is, one billion of the wavelength.

So, whereas the saltwater layers seem "huge" to a ray of light, which you might have already learned to model as "plane wave front", these layers might be "small" compared to the wavelength of a medium wave transmission.

Now, imagine that instead of a small, cute laser pointer, you used a giant lamp consisting of thousands of laser pointers, mounted atop of each other: A large "tower" that shines kind of a beam (consisting of many laser rays). Now, the lower laser pointers are in deeper, saltier waters, and get bent more within shorter distance than the upper ones.

There's an old analogy that physics teachers often employ: imagine this group of rays being a marching band, nicely arranged to all start marching at the exact same instant. While the upper-water band members move relatively straight and only rarely meet a water-water level interface, the band members close to the ground are often making a bend in their path. The overall front of the marching band seems to "slouch" around the curvature of the earth.

This analogy isn't as bad as it sounds at first: The refractive index $n$ is actually just a measure for how much slower than in vacuum the light is in that medium. So, the "deepwater rays" simply *are* slower than the "not as saltywater rays". That means that the whole wavefront (marching band front) does follow a curve.

## 5 idea: we don't have salty water, but earth will do.

Obviously, you're not a water-dwelling alien controlling a giant marching band consisting of laser beams.

Instead, you have an antenna. But that antenna very much sends out an electromagnetic wavefront. As electromagnetic waves permeate air, trees, hills, dry earth, not-so-dry-earth, small animals, large animals, buildings, tapestries and people, they are, just like the special case of visible light, slowed down in media.

In the case of ground waves, the lower parts of the wave front permeates earth. Earth has a higher conductivity as air – and that means it slows down the electromagnetic wave. How that slowing down happens isn't actually very easy to explain - in the end, earth has physical properties that increase its $n$.

¹ I haven't had the time to properly test my calculations, but if they are correct, that angle is, if we set the earth radius to 1, $\delta=90° - 2\arcsin\left(\pm \sqrt{\frac l{2+2l}}\right)$, but that's actually not that important here. If you want to have some geometry in your presentation, deriving that angle from the ratio of earth radius (set arbitrarily to 1) and water height would definitely be a cool thing.  
For the things I want to explain, it's not important what this angle is, exactly.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9854/communications-ground-wave-propagation, by Selena, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
