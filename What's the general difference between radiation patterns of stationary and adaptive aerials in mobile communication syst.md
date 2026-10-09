# What's the general difference between radiation patterns of stationary and adaptive aerials in mobile communication systems?

*Tags: antenna, mobile, radiation-pattern · score 3*

## Question

I am trying to find general difference between radiation patterns of adaptive and stationary antennas (common difference, calculation difference and any other). I am interesting in any example and better any science publication on this theme. Appreciated any help.

You could confused by word "stationary", for this question two things can be applicable "smart antennas" as stationary antennas or even any other antennas (stationary too), and under term "adaptive" I mean "smart antennas" in mobile systems (for example in military systems on wheels).

## Accepted answer (score 2, by Phil Frost - W8II)

Non-adaptive antennas in mobile systems are usually omnidirectional, meaning they radiate equally in all directions. They can also have directional antennas, if there is some means for getting them to point in the right direction. Usually that means the vehicle on which the antenna is mounted has to stop.

Adaptive arrays are directional antennas that automatically point themselves in the right direction. This could be determined by the least mean square (LMS) algorithm, for example. This algorithm works by finding the coefficients for each array element which minimize the error in some known aspect of the signal, like a sub-carrier, synchronization, or error-correction information.

Since the algorithm is dynamic and statistical, we can't say exactly what the radiation pattern will look like, but generally lobes will be placed in the direction of the desired signal, and nulls in the direction of noise sources. It will maintain this orientation even as the stations move, since the LMS algorithm constantly adjusts the coefficients to compensate.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5048/what-s-the-general-difference-between-radiation-patterns-of-stationary-and-ada, by user3417815, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
