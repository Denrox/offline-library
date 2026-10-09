# Question about Isolating Transformer NZART exam question

*Tags: transformer, new-zealand · score 3*

## Question

I found this question about isolating transformers in the NZART question bank, but I can't figure out the meaning of the answer. Either the answer is misleading or I'm fundamentally misunderstanding something:

```
#10.10 An isolating transformer is used to:

1. ensure that faulty equipment connected to it will blow a fuse in the
distribution board

2. ensure that no voltage is developed between either output lead and ground

3. ensure that no voltage is developed between the output leads

4. step down the mains voltage to a safe value

```

The answer is given as:

```
2) ensure that no voltage is developed between either output lead and ground

```

Now I understand what an isolating transformer is, but the answer doesn't make sense because if there is no voltage developed between either output and the ground then that necessarily means that the voltage difference between the two output leads is 0 because if there were a different voltage on either output lead then one of them must be a different voltage than ground.

if Vg = V1 and Vg = V2 then V1 must = V2, making the transformer useless.

## Accepted answer (score 1, by webmarc)

Yeah, it's a poorly worded question/answer. There's no **DC** voltage developed between either output lead vs ground.

You're absolutely correct that there's AC potential developed, because... well... duh. One of the main purposes of an isolation transformer is to isolate **DC** potential and the question either doesn't make that clear *or* is trying to get at a different characteristic of the device.

## Answer (score 2, by tomnexus)

I agree it's poorly worded, but with MCQs you have to choose the least incorrect answer. 2 is still the obvious choice, the rest are totally wrong or deliberately opposite to the truth.

What they intended is to say that there is no enforced potential between either output and ground. This is quite different to a normal mains socket, where Hot/Live is at 230 V AC and Neutral is at ~0 V. Also no current, AC or DC, will flow through the transformer, so you will get no leakage to earth from any capacitors in the device under test, for example in the EMC filters.

The question is surely written thinking about the problem of measuring voltages on a valve HF amplifier. With an isolation transformer in place, you are less likely to die if you touch something, and you can safely clip your (earthed) scope ground anywhere. Better than lifting the ground of your scope and hoping its transformer does the job.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/22151/question-about-isolating-transformer-nzart-exam-question, by spl, webmarc, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
