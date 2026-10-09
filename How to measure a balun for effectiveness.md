# How to measure a balun for effectiveness?

*Tags: balun, measurement · score 6*

## Question

It seems there are almost as many "balun" designs as there are web pages about "baluns". There's lots of accusations pointed in all directions ("design Z isn't a balun OR a choke", "design Y is overkill", "design X could lead to spurious emissions/overheating/loss-of-limbs…") and given how hard such an ostensibly simple thing seems to be to understand, I'd like to be able to test any balun I might make or purchase.

How might I go about measuring a balun or a line choke to see if it will work as intended?

## Answer (score 2, by Edwin van Mierlo)

"How might I go about measuring a balun or a **line choke** to see if it will work as intended?" (emphasis added)

Steve Hunt (G3TXQ, SK) has measured many chokes, coaxial toroid wound, coaxial air wound, as well as some bifilar wound.

The results of his measurements can be found here: http://karinya.net/g3txq/chokes/

At the bottom of the page he explains how he measured the chokes, using a two port VNA.

Also a good explanation on why resistive chokes (R > X) are better then reactive chokes.

I have used his charts with great success winding my own chokes, using the "black" areas (this is where R > X) of the charts I managed to wind chokes specifically for the bands intended. While in the beginning I did use air-wound-coaxial chokes, the chart is clearly demonstrating that this is not ideal, as they are mostly reactive not resistive.

This explanation may not be as scientific as it seems, it would give a good starting point for your own measurements of chokes.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6153/how-to-measure-a-balun-for-effectiveness, by natevw - AF7TB, Edwin van Mierlo. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
