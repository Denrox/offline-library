# Counterpoise for telescopic antenna AL-800 as a portable/base antenna on 70cm?

*Tags: antenna · score 4*

## Question

Recently I bought a telescopic antenna, model AL-800: http://www.pryme.com/index.php?l=product_detail&p=2155

It is 863mm (34 inches) long when fully extended. When retracted, it is 785mm long.

Will adding, for example, 4 ground radials increase the transmitting ability?

I'm thinking about using it as a portable base antenna that could be fit inside a backpack or fixed to a roof.

What do you think? Is there any reason for doing this? If yes, will using 1/4-wavelength radials be fine, like 4 radials that are each 17cm long?

## Answer (score 3, by jcoppens)

The 'inventions' done to make an antenna are generally considered a trade secret by the manufacturers. I found out how my dual band works, when it got crushed after traveling in the cargo hold of an airplane. It's not simple coils... So simulating it in nec is not a simple task.

When used with an HT, all antennas assume that the user has the antenna in his hand, and the body will act as a (bad) 'counterpoise'. Of course, if you want to improve the situation, and make the use more independent of the user's position and 'pose', a groundplane would help. If nothing else, it will reduce the RF current to the hand of the operator.

On the other hand, I'd think twice about adding 3 (or 4) pointy things to the antenna, which will mostly be traveling at or near eye-height. It seems like an invitation for lawsuits.

Note that you groundplane will only work at 70cm. If you want them to work on 2m too, you'll have to add radials for that frequency.

And a final note: if you *only* want 70 cm, think about looking for a J-pole based design, or a vertical dipole, Neither needs a groundplane, and move the high current node up in the antenna.

## Answer (score 3, by G4ZLZ)

Try a practical test as follows. Find a consistantly-readable but weak station (like a medium-distance repeater) and note the signal strength when you hand-hold the antenna on a handie, possibly at arms' length. Then place the handie and antenna on the centre of a car roof and note the difference in signal strength (if any). That will indicate if the antenna would benefit from a ground plane. Some types (like an end-fed half-wave dipole) will not generate strong ground currents (if correctly matched) whereas a quarter-wave monopole does benefit from a ground plane. The antenna gain is suspiciously similar to that of a quarter wave monopole on 70 cm IF the units are dBi. In that case I wonder if the top (retractable) section is the radiator and the "bulge" at the top of the fixed section is a coil acting like a choke. This is pure speculation...

My guess is that radials will not be much help. If you do use them, then try braid instead of wire, or a metal sheet, and pay lots of attention to making an excellent ground connection at the antenna base. If you don't, then resistive losses will kill the potential gains.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2309/counterpoise-for-telescopic-antenna-al-800-as-a-portable-base-antenna-on-70cm, by Marc, jcoppens, G4ZLZ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
