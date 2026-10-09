# Antenna traps - problem with frequency change

*Tags: antenna-construction, trap · score 3*

## Question

I built a two-band antenna (20 and 40m) with traps. I made the traps as a parallel LC circuit on the AL7 toroidal core (3 MHz - 40 MHz), I also used a 1KV ceramic capacitor. I've tuned everything up and it works very well.

The problem appears when I increase the power above 50W. The antenna resonance shifts to the right by approx **200kHz**. When I shift the transmit frequency towards the antenna resonance, it shifts again by **200kHz**. When I finish the transmission, the antenna's resonance slowly returns to its place.

I am looking for an answer to what could be causing this.

I checked that nothing heats up during this power. I am concerned that I used the wrong type of capacitor - ceramic, which is not very stable?

**Edit:** I tried with a T94-6 double core and a thicker winding wire. Nothing has changed

## Accepted answer (score 4, by Artur)

I am very pleased that my traps have started working properly! The problem was solved by mica capacitors. It turned out that the ceramic capacitors I used had poor temperature and capacity parameters. Mica capacitors have proven themselves perfectly and the frequency does not shift any more. I made the antenna for the bands that I like best 20/40/80/17 / 30m. Everything works very well! Here's my trap in action:

Thanks to everyone for your help.

## Answer (score 3, by Phil Frost - W8II)

What you describe does indeed sound like a thermal issue. If you have some unstable components, even a small change in temperature which is difficult to detect can be sufficient to cause the issues you describe.

Are you tuning the trap such that its resonance is in the 20 meter band? This would mean when you transmit on 20 meters, current circulating in the trap is at a maximum, and so are losses. If any of your components are not so thermally stable, this could be enough to shift the resonance frequency.

This would also explain why the resonance drifts away, and when you "chase" it, it drifts away more. It's drifting away until the losses are low enough that it reaches thermal equilibrium, but when you subsequently increase the transmitter frequency the losses go up again, further heating the components, causing the resonance to shift yet more. I'd suspect if you keep repeating this, eventually you'll notice something getting warm, and then quite hot. Of course you probably don't want to be transmitting outside the ham band at 50 watts.

Here's a way to test this hypothesis: get a "compressed air" (they don't actually contain air) duster, like this:

Fire up the transmitter, and get the resonance frequency to drift up.

Now turn the can upside down, and spray it on your trap for a fraction of a second. The can contains a rapidly evaporating liquid: normally the "air" these spray is the vapors from this liquid. When upside down, the liquid will evaporate on your trap, cooling it. Take care to avoid spraying your skin unless you enjoy a little frostbite. Safety glasses also not a bad idea.

Does the resonance come back down after you do this? If so, thermal instability is the issue.

What can you do to fix this? A simple solution may be to tune the trap so its resonance is outside the 20 meter band. The idea is to find a place where the impedance is high enough to mostly isolate the upper section of the antenna, but with enough distance between transmit and resonance frequencies that losses are lower. Besides avoiding the thermal stability issue this will also increase your antenna efficiency.

Of course, if you identify which components are causing the problem you could pursue alternatives with a lower temperature coefficient. Ceramic capacitors come in varieties with different dielectrics, and some are very stable and some are very much not.

You can also consider alternative construction methods. A common technique is to use some length of coax instead of discrete capacitors. Searching for "coaxial trap" should turn up some resources.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18442/antenna-traps-problem-with-frequency-change, by Artur, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
