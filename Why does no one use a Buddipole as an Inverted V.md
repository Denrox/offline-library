# Why does no one use a Buddipole as an Inverted V?

*Tags: antenna, antenna-theory, dipole · score 5*

## Question

I have been looking at the Buddipole, and I've seen the most popular configuration is as a standard dipole with the arms parallel to the ground. I've also seen it configured as an upright V, as well as configured in a sloped condition. But I haven't found anyone that uses it as an inverted V.

It looks like there could be some advantages to it. Sloping the arms down at 45 degrees would relieve some of the mechanical strain on the arms as well as lower the center of gravity. The antenna would also be more omnidirectional (assuming you want that). Finally, I'm not an expert on impedance matching, but I think it would also bring the impedance closer to 50 ohms which would eliminate the balun requirement, right?

Am I overlooking some key detail here? Why is this not a more popular configuration?

## Answer (score 3, by Aleksander Alekseev - R2AUK)

The 50 Ohm impedance doesn't eliminate the need of the balun. A balun prevents the feed line to work as a part of the antenna (eliminates common mode current). You can find more info on this topic in the article [Baluns: What They Do And How They Do It [PDF]](http://www.arrl.org/files/file/History/History%20of%20QST%20Volume%201%20-%20Technology/AntComp1-Lewallen%281%29.pdf) by Roy Lewallen, W7EL.

I guess the reason why most people don't use Buddipole as an inverted V is that if you want an inverted V you can erect a full-sized inverted V on a fishing rod. If you are using Buddipole which is a shortened (= less efficient) dipole, you probably want something else. Directivity for instance, i.e. a dipole configuration.

I also suspect that many users of Buddipole don't actually care about directivity or anything else and just experiment with different configurations for fun.

## Answer (score 3, by Edwin van Mierlo)

There are 4 questions in the original post:

1.

Why does no one use a Buddipole as an Inverted V?

2.

I think it would also bring the impedance closer to 50 ohms which would eliminate the balun requirement, right?

3.

Am I overlooking some key detail here?

4.

Why is this not a more popular configuration?

There are good answers given for question 2, but not for the others. Reason is probably that questions 1/3/4 are quite speculative.

1. Why does no one use a Buddipole as an Inverted V?

"no one" probably is an assumption which is speculative. However I must say that I have experience with the Buddipole. I have "bended down" the elements. I cannot recall if the results were any different then the elements horizontal. While never really experimented or measured it, I am not sure about either advandtages or disadvantages of such.

However to say that "no one" uses this, is probably an overstretch

1. Am I overlooking some key detail here?

I believe that in order to answer that you need to experiment, measure, and probably apply complex math's to answer such a question. As the Buddipole itself is a compromise antenna, there are many design factors to take into account, which makes the math on detail even more complex.

Chances are that some detail is indeed overlooked, simplisticly speaking. (no disrespect to OP)

1. Why is this not a more popular configuration?

This would be speculative, but in my opinion; if you need an inverted V, you need to get the feedpoint up higher than traditionally done with the Buddipole. And while you have the feedpoint higher, you may as well run a half-wave (two quarter wave) wires, to have a *normal* inverted V.

I have done it, I cannot recall any difference vs the normal dipole config. Saying that, I was not looking or executing any measurements either, so if there was a difference then I probably would not have noticed it. Other than that; I would guess you need to "just try it" and experience yourself.

## Answer (score 2, by hobbs - KC2G)

A vee-dipole brings the impedance *down* compared to the same dipole in "straight" configuration. If you've got that theoretical half-wave in free-space with its 72-ish ohms of impedance then sure, maybe you want to bring it down towards 50. But a Buddipole almost always has too *little* impedance to start with, so you don't want to reduce it any further.

Mechanically, the peak of a Buddipole is usually not very high up, so you can't tilt the elements down very much before you have to start worrying about them contacting the ground, or at least people's eyes. And even when you mount them straight, those whips flex towards the ground anyway.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/14874/why-does-no-one-use-a-buddipole-as-an-inverted-v, by SandPiper, Aleksander Alekseev - R2AUK, Edwin van Mierlo, hobbs - KC2G. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
