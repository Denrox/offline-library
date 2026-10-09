# Effect of different metals for antenna elements

*Tags: antenna, antenna-construction, physics · score 36*

## Question

Other than rust, corrosion, and other reactions with air that would make the use of a metal unfavorable, how do different metals affect the performance?

Let's give Yagi an example:

Let's say I use 4 different metals for the directors , reflector, and driven element.

One antenna made out of copper, one made out of aluminum, and one made out of a higher resistance conductor, let's say graphite (I know it would snap, I'm just talking theoretical), and iron

Other then the metal variations, the antennas are identical.

So, do different metals with different conductivity and permiability affect the performance of an antenna including gain, efficiency, impedance, elevation, or any other characteristic other then mechanical strength, and chemical reliability in open air.

## Answer (score 47, by Phil Frost - W8II)

Considering just electrical properties, the most significant parameter for your selection of antenna conductor is resistance. You want to keep the resistance to a minimum, because when current flows through a resistance, the electrical power is converted to heat, according to Joule heating:

$$ P = I^2 R $$

Any energy you use to make heat is energy you aren't using to make electromagnetic waves.

So first, you should consider the resistivity ($\rho$) of various metals. A lower resistivity means you will need less of a metal to reduce the resistance to an acceptable target. Here's a selection, ordered from lowest to highest resistivity in nano-ohm-meters (nΩm), of some metals you might consider using in an antenna:

- Silver: 15.9
- Copper: 16.8
- Gold: 24.4
- Aluminium: 26.2
- Zinc: 59.0
- Nickel: 69.9
- Iron: 100
- Tin: 109

I'm not going to list stainless steel because there are so many kinds, but generally stainless steels are not great conductors, being over 100 on this scale.

A high *resistivity* isn't bad in itself, because you can compensate by making the conductor thicker, and end up with the same *resistance*. Thus, you might think copper is the best choice (ruling out silver due to high cost), but when you start making mechanical and cost considerations, you may find aluminium is better. This is because for a sample of copper and another of aluminium of equal resistance, the aluminium sample will be bigger, but stiffer, lighter, and cheaper.

There's another effect to consider here: with increasing frequency, currents like to flow on the surfaces of conductors. This is called the skin effect. The current flowing only on the skin of a conductor effectively reduces the cross-sectional area, and thus the conductance.

Since most of the RF current is only on the surface, it often makes sense to build antennas from tubing for antennas requiring rigid elements (a 440 MHz Yagi), or copper-clad steel for wire antennas requiring tensile strength (a 40 meter dipole). This saves weight and cost for a negligible increase in loss.

Magnetic permeability is a factor in skin depth. With increasing permeability, the skin depth decreases, increasing loss. Of the metals listed above, only iron and nickel have significantly higher permeability. Iron by a factor of about 5000, and nickel by 100 to 600. You could compensate for the reduced skin depth by increasing the surface area of the conductor, but when you consider cost and mechanics, it usually makes more sense to simply avoid iron and nickel and alloys containing them.

## Answer (score 4, by sm5bsz)

If you are interested in space communications (EME and satellites) even small losses are important since losses have room temperature. The sky as well as a good preamp should be well below 100K while losses are about 3 times warmer which makes them 3 times more destructive. When one designs a yagi one can trade between gain/pattern and element losses. The way elements are mounted on a boom tube does matter. Through hole with Starlock washers can cause severe losses to the extent one can feel the heat on the boom tube by hand after running 1 kW power for 5 minutes (a day with no wind that would cool the antenna.) For details look here: http://sm5bsz.com/antennas/sa/losses413.htm

## Answer (score 4, by Adam Davis)

There are two aspect you'll need to take into account. The first can be more easily dismissed as insignificant, and that is the velocity factor of the metal. For common conducting metals the difference between two metals is very small and is generally swamped by other things that affect velocity factor, such as insulation.

The second, and more important aspect is the resistance of the metal. The higher the resistance, the greater the losses to heat. Stainless steel isn't a great conductor, and a simple 50W continuous transmission will heat it too hot to touch without much trouble - a lot of that power is going into heating the metal, and not transmitting the signal. Copper and aluminum are good conductors, but if you could use silver you'd have an even more efficient antenna - it could operate at higher power with thinner wire than the other conductors.

Beyond that, there's little electrically to take into account in choosing a metal for an antenna design - just mechanical, environmental, connection, and cost factors which often weigh more heavily in the decision than the above factors.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1388/effect-of-different-metals-for-antenna-elements, by Skyler 440, Phil Frost - W8II, sm5bsz, Adam Davis. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
