# Soldering PL-259.. with a torch?

*Tags: coaxial-cable, pl259-so239-connector · score 5*

## Question

I came across this article about torch soldering PL-259 coax connectors. It seemed like a good idea since the body needs a lot of heat to get solder to flow into the holes.

It's a little vague when describing the soldering technique for soldering the braid. It says to heat the area between two holes and after about 10 seconds the solder will flow. The problem is I can't get the solder near the holes before the flame of my little butane torch melts it away. So then I tried pulling the torch away just before bringing the solder in. But the solder won't melt unless the barrel is super hot. And then it only flows for a second. Afterwords I'm left with an overheated barrel.

It seems like a catch 22. In order for the barrel to be hot enough to flow solder it also has to be hot enough to melt coax.

A large iron directly on the hole seems a little more focused. But then the solder won't flow very far past the immediate opening of the hole.

Maybe I'm missing something about the technique.

## Accepted answer (score 8, by Glenn W9IQ)

Our friends in the UK and other parts of the world are now wondering how you could even begin to solder a PL259 connector with a torch (aka flashlight)! But in their vernacular, you of course are referring to a burning torch.

In general, when you heat a metallic object with the hopes of applying solder, the heat will cause oxidation to form on the metallic surfaces. This will frustrate the application of solder. A better technique is to prepare the mating surfaces with a paste type electronics flux prior to heating the surfaces. Make certain to use a flux rated for electronic components to avoid conductivity, contamination or future corrosion.

The general issue of how to heat a PL259 connector body has been a topic for decades. There is a delicate balance between applying sufficient heat so as to allow the solder to flow into the holes and the braid without using so much heat so as to melt the dielectric material or the pin support insulator. It is a skill that takes practice to perfect. Be ready to sacrifice some coax and connectors to the learning process. I have had better success soldering silver plated connectors.

One technique to avoid overheating the connector is to apply heat away from a hole while touching the solder to the hole area. As soon as the solder starts to melt, remove the heat and continue to apply solder. There is generally enough residual heat in the body of the connector to allow the solder to flow.

Some people, including me, have had success with not soldering the braid at all. Instead the braid is folded back over the outer jacket of the coax and then the connector body is forcibly screwed on so as to pinch the braid between the outer jacket and the inner threaded part of the connector. This may not be a good solution if the braid is subjected to moisture or high humidity that would promote oxidation of the mating surfaces.

More recently, crimp type coaxial connectors have overtaken most coaxial cable applications. These have the same or better reliability than solder type connectors. But the key to a successful installation is to have the correct tool, including the right die set, for the job. Here is a picture of such a tool from DX Engineering for the larger size coaxial cables:

There are several vendors of these types of tools. The quality tools are of a ratcheting design with changeable die sets. The connectors that are used with these types of tools look like this:

Once you are equipped with the right tools, you will never want to go back to soldered PL259 connectors again.

## Answer (score 5, by Mike Waters)

I've often used a propane torch to quickly **preheat** PL259s, but seldom for the actual soldering.

Once the connector is preheated, it is a quick and simple matter to flow solder into the holes and the *pre-tinned* braid using a 50 watt soldering iron.

(These days I use a Steinl heat gun instead of the torch flame for preheating, as it gives much better control over the temperature.)

This method minimizes the damage to the plastic dielectric and outer jacket.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12845/soldering-pl-259-with-a-torch, by Paul, Glenn W9IQ, Mike Waters. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
