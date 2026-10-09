# Why must twin-lead conductor spacing be small to avoid radiation?

*Tags: antenna, feed-line, theory · score 9*

## Question

A transmission line does not radiate when the spacing between the two wires is very small when compared to the wavelength, but the transmission line begins to radiate when the spacing between the lines becomes comparable to the wavelength of the signal. Why is this?

## Accepted answer (score 5, by Phil Frost - W8II)

Twin-lead transmission lines don't radiate because the opposite fields from each conductor cancel, but when the spacing is far apart this does not happen.

First, let's consider the magnetic field around an infinite, straight conductor with uniform current throughout. In this image, the conductor is just right of center, and the current is coming straight out of the page.

Now let's add next to it another conductor, with the current going the other way:

Add these fields together, and you get:

For distances far away relative to the conductor spacing, the fields are equal but opposite, so when added together they cancel. Radiation is, by definition, a field that extends to infinity. If there are no fields far away, then it can't be radiating.

However, we made an assumption of *uniform* current. When the spacing between the conductors is small, this is a mostly true assumption. Although the current isn't exactly uniform, we must travel many multiples of the conductor spacing before there's any appreciable change in phase.

However, when the conductor spacing is large, then this is no longer true. Remember, the current is reversing direction periodically, and if we look at the field from just one conductor this means the field is alternating between clockwise and counterclockwise swirl. The changes to this field only propagate at the speed of light, so if we zoom the graph out to be a wavelength wide or more, we'd see those changes propagating away as waves.

In the image above, the wavelength appears to be approximately four units. Now if we add that second conductor, two units away, we get this:

Notice how the fields don't cancel. They don't cancel because on the scale of the conductor spacing (which is not small relative to the wavelength) there can be significant changes in phase. Thus, there are regions of constructive interference where the fields don't cancel. These regions extend out to infinity, and thus, the feedline radiates.

*Images were generated with a Javascript vector field grapher by Kevin Mehall*

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/3508/why-must-twin-lead-conductor-spacing-be-small-to-avoid-radiation, by Danny Paul, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
