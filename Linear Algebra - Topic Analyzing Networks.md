# Topic: Analyzing Networks

The diagram below shows some of a car's electrical network. The battery is on the left, drawn as stacked line segments. The wires are drawn as lines, shown straight and with sharp right angles for neatness. Each light is a circle enclosing a loop.

The designer of such a network needs to answer questions like: How much electricity flows when both the hi-beam headlights and the brake lights are on? Below, we will use linear systems to analyze simpler versions of electrical networks.

For the analysis we need two facts about electricity and two facts about electrical networks.

The first fact about electricity is that a battery is like a pump: it provides a force impelling the electricity to flow through the circuits connecting the battery's ends, if there are any such circuits. We say that the battery provides a **potential** to flow. Of course, this network accomplishes its function when, as the electricity flows through a circuit, it goes through a light. For instance, when the driver steps on the brake then the switch makes contact and a circuit is formed on the left side of the diagram, and the electrical current flowing through that circuit will make the brake lights go on, warning drivers behind.

The second electrical fact is that in some kinds of network components the amount of flow is proportional to the force provided by the battery. That is, for each such component there is a number, its **resistance**, such that the potential is equal to the flow times the resistance. The units of measurement are: potential is described in **volts**, the rate of flow is in **amperes**, and resistance to the flow is in **ohms**. These units are defined so that $$\text{volts}=\text{amperes}\cdot\text{ohms}$$.

Components with this property, that the voltage-amperage response curve is a line through the origin, are called **resistors**. (Light bulbs such as the ones shown above are not this kind of component, because their ohmage changes as they heat up.) For example, if a resistor measures $$2$$ ohms then wiring it to a $$12$$ volt battery results in a flow of $$6$$ amperes. Conversely, if we have electrical current of $$2$$ amperes through it then there must be a $$4$$ volt potential difference between its ends. This is the **voltage drop** across the resistor. One way to think of a electrical circuits like the one above is that the battery provides a voltage rise while the other components are voltage drops.

The two facts that we need about networks are Kirchhoff's Laws.

- *Current Law.* For any point in a network, the flow in equals the flow out.
- *Voltage Law.* Around any circuit the total drop equals the total rise.

In the above network there is only one voltage rise, at the battery, but some networks have more than one.

For a start we can consider the network below. It has a battery that provides the potential to flow and three resistors (resistors are drawn as zig-zags). When components are wired one after another, as here, they are said to be in **series**.

By Kirchhoff's Voltage Law, because the voltage rise is $$20$$ volts, the total voltage drop must also be $$20$$ volts. Since the resistance from start to finish is $$10$$ ohms (the resistance of the wires is negligible), we get that the current is $$(20/10)=2$$ amperes. Now, by Kirchhoff's Current Law, there are $$2$$ amperes through each resistor. (And therefore the voltage drops are: $$4$$ volts across the $$2$$ oh m resistor, $$10$$ volts across the $$5$$ ohm resistor, and $$6$$ volts across the $$3$$ ohm resistor.)

The prior network is so simple that we didn't use a linear system, but the next network is more complicated. In this one, the resistors are in **parallel**. This network is more like the car lighting diagram shown earlier.

We begin by labeling the branches, shown below. Let the current through the left branch of the parallel portion be $$i_1$$ and that through the right branch be $$i_2$$, and also let the current through the battery be $$i_0$$. (We are following Kirchoff's Current Law; for instance, all points in the right branch have the same current, which we call $$i_2$$. Note that we don't need to know the actual direction of flow— if current flows in the direction opposite to our arrow then we will simply get a negative number in the solution.)

The Current Law, applied to the point in the upper right where the flow $$i_0$$ meets $$i_1$$ and $$i_2$$, gives that $$i_0=i_1+i_2$$. Applied to the lower right it gives $$i_1+i_2=i_0$$. In the circuit that loops out of the top of the battery, down the left branch of the parallel portion, and back into the bottom of the battery, the voltage rise is $$20$$ while the voltage drop is $$i_1\cdot 12$$, so the Voltage Law gives that $$12i_1=20$$. Similarly, the circuit from the battery to the right branch and back to the battery gives that $$8i_2=20$$. And, in the circuit that simply loops around in the left and right branches of the parallel portion (arbitrarily taken clockwise), there is a voltage rise of $$0$$ and a voltage drop of $$8i_2-12i_1$$ so the Voltage Law gives that $$8i_2-12i_1=0$$.

$$
\begin{array}{rcrcrcr} i_0&- &i_1 &- &i_2 &= &0 \\ -i_0&+ &i_1 &+ &i_2 &= &0 \\ & &12i_1 & & &= &20 \\ & & & &8i_2 &= &20 \\ & &-12i_1 &+ &8i_2 &= &0 \end{array}
$$

The solution is $$i_0=25/6$$, $$i_1=5/3$$, and $$i_2=5/2$$, all in amperes. (Incidentally, this illustrates that redundant equations do indeed arise in practice.)

Kirchhoff's laws can be used to establish the electrical properties of networks of great complexity. The next diagram shows five resistors, wired in a **series-parallel** way.

This network is a **Wheatstone bridge** (see Problem 4). To analyze it, we can place the arrows in this way.

Kirchoff's Current Law, applied to the top node, the left node, the right node, and the bottom node gives these.

$$
\begin{array}{rl} i_0 &= i_1+i_2 \\ i_1 &= i_3+i_5 \\ i_2+i_5 &= i_4 \\ i_3+i_4 &= i_0 \end{array}
$$

Kirchhoff's Voltage Law, applied to the inside loop (the $$i_0$$ to $$i_1$$ to $$i_3$$ to $$i_0$$ loop), the outside loop, and the upper loop not involving the battery, gives these.

$$
\begin{array}{rl} 5i_1+10i_3 &= 10 \\ 2i_2+4i_4 &= 10 \\ 5i_1+50i_5-2i_2 &= 0 \end{array}
$$

Those suffice to determine the solution $$i_0=7/3$$, $$i_1=2/3$$, $$i_2=5/3$$, $$i_3=2/3$$, $$i_4=5/3$$, and $$i_5=0$$.

Networks of other kinds, not just electrical ones, can also be analyzed in this way. For instance, networks of streets are given in the exercises.

### Exercises

*Many of the systems for these problems are mostly easily solved on a computer.*

**Problem 1**  —

Calculate the amperages in each part of each network.

1. This is a simple network.

2. Compare this one with the parallel case discussed above.

3. This is a reasonably complicated network.

**Problem 2**  —

In the first network that we analyzed, with the three resistors in series, we just added to get that they acted together like a single resistor of $$10$$ ohms. We can do a similar thing for parallel circuits. In the second circuit analyzed,

the electric current through the battery is $$25/6$$ amperes. Thus, the parallel portion is **equivalent** to a single resistor of $$20/(25/6)=4.8$$ ohms.

1. What is the equivalent resistance if we change the $$12$$ ohm resistor to $$5$$ ohms?
2. What is the equivalent resistance if the two are each $$8$$ ohms?
3. Find the formula for the equivalent resistance if the two resistors in parallel are $$r_1$$ ohms and $$r_2$$ ohms.

**Problem 3**  —

For the car dashboard example that opens this Topic, solve for these amperages (assume that all resistances are $$2$$ ohms).

1. If the driver is stepping on the brakes, so the brake lights are on, and no other circuit is closed.
2. If the hi-beam headlights and the brake lights are on.

**Problem 4**  —

Show that, in this Wheatstone Bridge,

$$r_2/r_1$$ equals $$r_4/r_3$$ if and only if the current flowing through $$r_g$$ is zero. (The way that this device is used in practice is that an unknown resistance at $$r_4$$ is compared to the other three $$r_1$$, $$r_2$$, and $$r_3$$. At $$r_g$$ is placed a meter that shows the current. The three resistances $$r_1$$, $$r_2$$, and $$r_3$$ are varied— typically they each have a calibrated knob— until the current in the middle reads $$0$$, and then the above equation gives the value of $$r_4$$.)

*There are networks other than electrical ones, and we can ask how well Kirchoff's laws apply to them. The remaining questions consider an extension to networks of streets.*

**Problem 5**  —

Consider this traffic circle.

This is the traffic volume, in units of cars per five minutes.

$$
\begin{array}{r|c|c|c} &\textit{North} &\textit{Pier} &\textit{Main} \\ \hline \textit{into} &100 &150 &25 \\ \textit{out of} &75 &150 &50 \end{array}
$$

We can set up equations to model how the traffic flows.

1. Adapt Kirchoff's Current Law to this circumstance. Is it a reasonable modelling assumption?
2. Label the three between-road arcs in the circle with a variable. Using the (adapted) Current Law, for each of the three in-out intersections state an equation describing the traffic flow at that node.
3. Solve that system.
4. Interpret your solution.
5. Restate the Voltage Law for this circumstance. How reasonable is it?

**Problem 6**  —

This is a network of streets.

The hourly flow of cars into this network's entrances, and out of its exits can be observed.

$$
\begin{array}{r|c|c|c|c|c} &\textit{east\ Winooski} &\textit{west\ Winooski} &\textit{Willow} &\textit{Jay} &\textit{Shelburne} \\ \hline \text{into} &80 &50 &65 &-- &40 \\ \text{out of} &30 &5 &70 &55 &75 \end{array}
$$

(Note that to reach Jay a car must enter the network via some other road first, which is why there is no "into Jay" entry in the table. Note also that over a long period of time, the total in must approximately equal the total out, which is why both rows add to $$235$$ cars.) Once inside the network, the traffic may flow in different ways, perhaps filling Willow and leaving Jay mostly empty, or perhaps flowing in some other way. Kirchhoff's Laws give the limits on that freedom.

1. Determine the restrictions on the flow inside this network of streets by setting up a variable for each block, establishing the equations, and solving them. Notice that some streets are one-way only. (*Hint:* this will not yield a unique solution, since traffic can flow through this network in various ways; you should get at least one free variable.)
2. Suppose that some construction is proposed for Winooski Avenue East between Willow and Jay, so traffic on that block will be reduced. What is the least amount of traffic flow that can be allowed on that block without disrupting the hourly flow into and out of the network?

Solutions

---

*Source: Wikibooks, Linear Algebra/Topic: Analyzing Networks (https://en.wikibooks.org/wiki/Linear_Algebra/Topic%3A_Analyzing_Networks), by Wikibooks contributors, CC BY-SA 4.0.*
