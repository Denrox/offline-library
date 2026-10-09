# How to Evaluate Antenna Data

*Tags: antenna · score 10*

## Question

I found some data on antennas that had been tested for a specific radio. I'm trying to decipher what this data means and how one would go about gathering it. Are there any good resource for learning how to read and understand this data?

Specifically, please explain the following metrics:

- dBS9
- The relationship between dBm (the power ratio in decibels (dB) of the measured power referenced to one milliwatt (mW)) and antenna length.

For instance, in the following chart, which group of antennas operates optimally: the one in the blue freehand circle, those in the red freehand circle, or neither?

What common methods/software exist for obtaining this kind of data?

## Accepted answer (score 3, by imabug)

Without a lot of information on the person's testing methodology, I'll assume that dBS9/dBm refer to the signal strength received by the radio the antenna being tested is attached to.

There are several different ways to interpret what's in the graph. You could ask "For a given antenna length, which antenna performs best" (look at the cluster around 15 inches for example), in which case it would be the one that gives the highest dBS9/dBm.

You could also look at the graph as one of those cost/performance type graphs. If you define your criteria as "short antenna and high dBS9/dBm", then the best antennas would be towards the upper left portion of the graph while the worst ones would be in the lower right portion.

"Operating optimally" requires you to define what "optimally" means, and this is going to be different for different circumstances. Do you want the highest dBm? Shortest antenna?

For just received signal strength, the ones you circled in red are great performers. Do you want to be carrying around a 35-45" antenna with you though?

Conversely, the one circled in blue is a great antenna if you want something short, but receive performance kind of sucks.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/197/how-to-evaluate-antenna-data, by Dan, imabug. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
