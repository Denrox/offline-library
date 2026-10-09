# Scoring quality of Morse Code "fist"?

*Tags: cw · score 10*

## Question

When learning, teaching oneself, or training a class in Morse Code sending using a hand key, how can acceptable quality be scored (other than the letters being correct terms of dot-dash sequence)? There a big difference between the dots being a bit shorter than the dahs at widely varying WPM between characters and words, and nice perfect 3:1 timing at an exact 13 WPM, etc. What objective metric should be used to determine a "passing score"?

(Objective metric requested because many humans are too good at "hearing" the expected message even if there were errors or near errors in the coding. And it's not hard to measure key open/closure timings to millisecond precision for use in any objective scoring algorithm.)

Was there a metric used for acceptability quality in any country back when Morse Code sending was tested as required part of a license exam?

## Answer (score 6, by Phil Frost - W8II)

One quantification would be to measure jitter. Ideal Morse code is synchronized to a clock of dits. Wikipedia describes (emphasis mine):

The duration of a dash is three times the duration of a dot. Each dot or dash is followed by a short silence, equal to the dot duration. The letters of a word are separated by a space equal to three dots (one dash), and the words are separated by a space equal to seven dots. *The dot duration is the basic unit of time measurement in code transmission.*

A computer decoder could then recover a clock from this rhythm. When a transition between on and off is detected, this is compared to the clock. Any error is fed back to the clock synchronization algorithm, and additionally the magnitude of the error is recorded.

One can then take all of these errors and analyze them through any number of statistical means. I'd suggest the standard deviation as a general figure of merit.

If you break the jitter into error during what type of rhythmic unit you can get specific about what aspects of the rhythm are bad. For example, jitter in word spaces is not so bad as jitter in dit timing. You can adjust your scoring metric accordingly.

Since the decoder also tracks the sending speed, you can analyze that statistically to determine to what extent the sender increased or decreased speed, while possibly maintaining a good rhythm.

## Answer (score 2, by Joe Cotton)

This is exactly a matter of the CW measurement of "weight". With this weight measurement, the dahs are shorter or longer. A longer dah means a heavier weight. Weight is adjustable in most electronic keyers or Bugs. Personally, I like a longer dah, a heavier weight to my sending. I use a straight key only. People who are used to a heavier weight will complain about a lighter weight, and visa versa. The dits are usually less variable, and it usually is not as important if the dits are shorter than normal, but it does matter if the dits are so long that they start to be confused with dahs. IMHOOP.

"...There a big difference between the dots being a bit shorter than the dahs at widely varying WPM ..."

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1501/scoring-quality-of-morse-code-fist, by hotpaw2, Phil Frost - W8II, Joe Cotton. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
