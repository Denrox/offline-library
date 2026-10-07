# Topic: Line of Best Fit

Scientists are often presented with a system that has no solution and they must find an answer anyway. That is, they must find a value that is as close as possible to being an answer.

For instance, suppose that we have a coin to use in flipping. This coin has some proportion $$m$$ of heads to total flips, determined by how it is physically constructed, and we want to know if $$m$$ is near $$1/2$$. We can get experimental data by flipping it many times. This is the result a penny experiment, including some intermediate numbers.

- *number of flips*   30   60   90
- *number of heads*   16   34   51

Because of randomness, we do not find the exact proportion with this sample — there is no solution to this system.

$$
\begin{array}{rcr} 30m &= &16 \\ 60m &= &34 \\ 90m &= &51 \end{array}
$$

That is, the vector of experimental data is not in the subspace of solutions.

$$
\begin{pmatrix} 16 \\ 34 \\ 51 \end{pmatrix}\not\in \{ m\begin{pmatrix} 30 \\ 60 \\ 90 \end{pmatrix} \,\big|\, m\in\mathbb{R}\}
$$

However, as described above, we want to find the $$m$$ that most nearly works. An orthogonal projection of the data vector into the line subspace gives our best guess.

$$
\frac{ \begin{pmatrix} 16 \\ 34 \\ 51 \end{pmatrix}\cdot\begin{pmatrix} 30 \\ 60 \\ 90 \end{pmatrix} }{ \begin{pmatrix} 30 \\ 60 \\ 90 \end{pmatrix}\cdot\begin{pmatrix} 30 \\ 60 \\ 90 \end{pmatrix} } \cdot\begin{pmatrix} 30 \\ 60 \\ 90 \end{pmatrix} =\frac{7110}{12600}\cdot \begin{pmatrix} 30 \\ 60 \\ 90 \end{pmatrix}
$$

The estimate ($$m=7110/12600\approx 0.56$$) is a bit high but not much, so probably the penny is fair enough.

The line with the slope $$m\approx 0.56$$ is called the **line of best fit** for this data.

Minimizing the distance between the given vector and the vector used as the right-hand side minimizes the total of these vertical lengths, and consequently we say that the line has been obtained through **fitting by least-squares**

(the vertical scale here has been exaggerated ten times to make the lengths visible).

We arranged the equation above so that the line must pass through $$(0,0)$$ because we take it to be (our best guess at) the line whose slope is this coin's true proportion of heads to flips. We can also handle cases where the line need not pass through the origin.

For example, the different denominations of U.S. money have different average times in circulation (the $2 bill is left off as a special case). How long should we expect a $25 bill to last?

- *denomination*   1   5   10   20   50   100
- *average life (years)*   1.5   2   3   5   9   20

The plot (see below) looks roughly linear. It isn't a perfect line, i.e., the linear system with equations $$b+1m=1.5$$, ..., $$b+100m=20$$ has no solution, but we can again use orthogonal projection to find a best approximation. Consider the matrix of coefficients of that linear system and also its vector of constants, the experimentally-determined values.

$$
A= \begin{pmatrix} 1 &1 \\ 1 &5 \\ 1 &10 \\ 1 &20 \\ 1 &50 \\ 1 &100 \end{pmatrix} \qquad \vec{v}=\begin{pmatrix} 1.5 \\ 2 \\ 3 \\ 5 \\ 9 \\ 20 \end{pmatrix}
$$

The ending result in the subsection on Projection into a Subspace says that coefficients $$b$$ and $$m$$ so that the linear combination of the columns of $$A$$ is as close as possible to the vector $$\vec{v}$$ are the entries of $$({{A}^{\rm trans}}A)^{-1}{{A}^{\rm trans}}\cdot\vec{v}$$. Some calculation gives an intercept of $$b=1.05$$ and a slope of $$m= 0.18$$.

Plugging $$x=25$$ into the equation of the line shows that such a bill should last between five and six years.

We close by considering the times for the men's mile race (Oakley & Baker 1977). These are the world records that were in force on January first of the given years. We want to project when a 3:40 mile will be run.

- *year*   1870   1880   1890   1900   1910   1920   1930
- *seconds*   268.8   264.5   258.4   255.6   255.6   252.6   250.4
- *year*   1940   1950   1960   1970   1980   1990   2000
- *seconds*   246.4   241.4   234.5   231.1   229.0   226.3   223.1

We can see below that the data is surprisingly linear. With this input

$$
A= \begin{pmatrix} 1 & 1860 \\ 1 & 1870 \\ \vdots &\vdots \\ 1 &1990 \\ 1 &2000 \end{pmatrix} \qquad \vec{v} = \begin{pmatrix} 280.0 \\ 268.8 \\ \vdots \\ 226.3 \\ 223.1 \end{pmatrix}
$$

the Python program at this Topic's end gives

$$\text{slope}= -0.35$$ and $$\text{intercept}= 925.53$$ (rounded to two places; the original data is good to only about a quarter of a second since much of it was hand-timed).

When will a $$220$$ second mile be run? Solving the equation of the line of best fit gives an estimate of the year $$2008$$.

This example is amusing, but serves as a caution — obviously the linearity of the data will break down someday (as indeed it does prior to 1860).

### Exercises

*The calculations here are best done on a computer. In addition, some of the problems require more data, available in your library, on the net, in the answers to the exercises, or in the section following the exercises.*

**Problem 1**  —

Use least-squares to judge if the coin in this experiment is fair.

- *flips*   8   16   24   32   40
- *heads*   4   9   13   17   20

**Problem 2**  —

For the men's mile record, rather than give each of the many records and its exact date, we've "smoothed" the data somewhat by taking a periodic sample. Do the longer calculation and compare the conclusions.

**Problem 3**  —

Find the line of best fit for the men's $$1500$$ meter run. How does the slope compare with that for the men's mile? (The distances are close; a mile is about $$1609$$ meters.)

**Problem 4**  — Find the line of best fit for the records for women's mile.

**Problem 5**  —

Do the lines of best fit for the men's and women's miles cross?

**Problem 6**  —

When the space shuttle Challenger exploded in 1986, one of the criticisms made of NASA's decision to launch was in the way the analysis of number of O-ring failures versus temperature was made (of course, O-ring failure caused the explosion). Four O-ring failures will cause the rocket to explode. NASA had data from 24 previous flights.

- *temp °F*   53   75   57   58   63   70   70   66   67   67   67
- *failures*   3   2   1   1   1   1   1   0   0   0   0
- *temp °F*   68   69   70   70   72   73   75   76   76   78   79   80   81
- *failures*   0   0   0   0   0   0   0   0   0   0   0   0   0

The temperature that day was forecast to be $$31^\circ\text{F}$$.

1. NASA based the decision to launch partially on a chart showing only the flights that had at least one O-ring failure. Find the line that best fits these seven flights. On the basis of this data, predict the number of O-ring failures when the temperature is $$31$$, and when the number of failures will exceed four.
2. Find the line that best fits all 24 flights. On the basis of this extra data, predict the number of O-ring failures when the temperature is $$31$$, and when the number of failures will exceed four.

Which do you think is the more accurate method of predicting? (An excellent discussion appears in (Dalal, Folkes & Hoadley 1989).)

**Problem 7**  —

This table lists the average distance from the sun to each of the first seven planets, using earth's average as a unit.

- Mercury   Venus   Earth   Mars   Jupiter   Saturn   Uranus
- 0.39   0.72   1.00   1.52   5.20   9.54   19.2

1. Plot the number of the planet (Mercury is $$1$$, etc.) versus the distance. Note that it does not look like a line, and so finding the line of best fit is not fruitful.
2. It does, however look like an exponential curve. Therefore, plot the number of the planet versus the logarithm of the distance. Does this look like a line?
3. The asteroid belt between Mars and Jupiter is thought to be what is left of a planet that broke apart. Renumber so that Jupiter is $$6$$, Saturn is $$7$$, and Uranus is $$8$$, and plot against the log again. Does this look better?
4. Use least squares on that data to predict the location of Neptune.
5. Repeat to predict where Pluto is.
6. Is the formula accurate for Neptune and Pluto?

This method was used to help discover Neptune (although the second item is misleading about the history; actually, the discovery of Neptune in position $$9$$ prompted people to look for the "missing planet" in position $$5$$). See (Gardner 1970)

**Problem 8**  —

William Bennett has proposed an Index of Leading Cultural Indicators for the US (Bennett 1993). Among the statistics cited are the average daily hours spent watching TV, and the average combined SAT scores.

- 1960   1965   1970   1975   1980   1985   1990   1992
- *TV*   5:06   5:29   5:56   6:07   6:36   7:07   6:55   7:04
- *SAT*   975   969   948   910   890   906   900   899

Suppose that a cause and effect relationship is proposed between the time spent watching TV and the decline in SAT scores (in this article, Mr. Bennett does not argue that there is a direct connection).

1. Find the line of best fit relating the independent variable of average daily TV hours to the dependent variable of SAT scores.
2. Find the most recent estimate of the average daily TV hours (Bennett's cites Neilsen Media Research as the source of these estimates). Estimate the associated SAT score. How close is your estimate to the actual average? (Warning: a change has been made recently in the SAT, so you should investigate whether some adjustment needs to be made to the reported average to make a valid comparison.)

Solutions

**Computer Code**

```
#!/usr/bin/python
# least_squares.py   calculate the line of best fit for a data set
# data file format: each line is two numbers, x and y
n = 0
sum_x = 0
sum_y = 0
sum_x_squared = 0
sum_xy = 0

fn = raw_input("Name of the data file? ")
datafile = open(fn,"r")
while 1:
ln = datafile.readline()
if ln:
data = ln.split()
x = float(data[0])
y = float(data[1])
n += 1
sum_x += x
sum_y += y
sum_x_squared += x*x
sum_xy += x*y
else:
break
datafile.close()

slope = (n*sum_xy - sum_x*sum_y) / (n*sum_x_squared - sum_x**2)
intercept = (sum_y - slope*sum_x)/n
print "line of best fit: slope= %f  intercept= %f" % (slope, intercept)

```

### Additional Data

*Data on the progression of the world's records (taken from the **Runner's World** web site) is below.*

*Progression of Men's Mile Record*

- *time*   *name*   *date*
- 4:52.0   Cadet Marshall (GBR)   02Sep52
- 4:45.0   Thomas Finch (GBR)   03Nov58
- 4:40.0   Gerald Surman (GBR)   24Nov59
- 4:33.0   George Farran (IRL)   23May62
- 4:29 3/5   Walter Chinnery (GBR)   10Mar68
- 4:28 4/5   William Gibbs (GBR)   03Apr68
- 4:28 3/5   Charles Gunton (GBR)   31Mar73
- 4:26.0   Walter Slade (GBR)   30May74
- 4:24 1/2   Walter Slade (GBR)   19Jun75
- 4:23 1/5   Walter George (GBR)   16Aug80
- 4:19 2/5   Walter George (GBR)   03Jun82
- 4:18 2/5   Walter George (GBR)   21Jun84
- 4:17 4/5   Thomas Conneff (USA)   26Aug93
- 4:17.0   Fred Bacon (GBR)   06Jul95
- 4:15 3/5   Thomas Conneff (USA)   28Aug95
- 4:15 2/5   John Paul Jones (USA)   27May11
- 4:14.4   John Paul Jones (USA)   31May13
- 4:12.6   Norman Taber (USA)   16Jul15
- 4:10.4   Paavo Nurmi (FIN)   23Aug23
- 4:09 1/5   Jules Ladoumegue (FRA)   04Oct31
- 4:07.6   Jack Lovelock (NZL)   15Jul33
- 4:06.8   Glenn Cunningham (USA)   16Jun34
- 4:06.4   Sydney Wooderson (GBR)   28Aug37
- 4:06.2   Gunder Hagg (SWE)   01Jul42
- 4:04.6   Gunder Hagg (SWE)   04Sep42
- 4:02.6   Arne Andersson (SWE)   01Jul43
- 4:01.6   Arne Andersson (SWE)   18Jul44
- 4:01.4   Gunder Hagg (SWE)   17Jul45
- 3:59.4   Roger Bannister (GBR)   06May54
- 3:58.0   John Landy (AUS)   21Jun54
- 3:57.2   Derek Ibbotson (GBR)   19Jul57
- 3:54.5   Herb Elliott (AUS)   06Aug58
- 3:54.4   Peter Snell (NZL)   27Jan62
- 3:54.1   Peter Snell (NZL)   17Nov64
- 3:53.6   Michel Jazy (FRA)   09Jun65
- 3:51.3   Jim Ryun (USA)   17Jul66
- 3:51.1   Jim Ryun (USA)   23Jun67
- 3:51.0   Filbert Bayi (TAN)   17May75
- 3:49.4   John Walker (NZL)   12Aug75
- 3:49.0   Sebastian Coe (GBR)   17Jul79
- 3:48.8   Steve Ovett (GBR)   01Jul80
- 3:48.53   Sebastian Coe (GBR)   19Aug81
- 3:48.40   Steve Ovett (GBR)   26Aug81
- 3:47.33   Sebastian Coe (GBR)   28Aug81
- 3:46.32   Steve Cram (GBR)   27Jul85
- 3:44.39   Noureddine Morceli (ALG)   05Sep93
- 3:43.13   Hicham el Guerrouj (MOR)   07Jul99  

*Progression of Men's 1500 Meter Record*

- *time*   *name*   *date*
- 4:09.0   John Bray (USA)   30May00
- 4:06.2   Charles Bennett (GBR)   15Jul00
- 4:05.4   James Lightbody (USA)   03Sep04
- 3:59.8   Harold Wilson (GBR)   30May08
- 3:59.2   Abel Kiviat (USA)   26May12
- 3:56.8   Abel Kiviat (USA)   02Jun12
- 3:55.8   Abel Kiviat (USA)   08Jun12
- 3:55.0   Norman Taber (USA)   16Jul15
- 3:54.7   John Zander (SWE)   05Aug17
- 3:53.0   Paavo Nurmi (FIN)   23Aug23
- 3:52.6   Paavo Nurmi (FIN)   19Jun24
- 3:51.0   Otto Peltzer (GER)   11Sep26
- 3:49.2   Jules Ladoumegue (FRA)   05Oct30
- 3:49.0   Luigi Beccali (ITA)   17Sep33
- 3:48.8   William Bonthron (USA)   30Jun34
- 3:47.8   Jack Lovelock (NZL)   06Aug36
- 3:47.6   Gunder Hagg (SWE)   10Aug41
- 3:45.8   Gunder Hagg (SWE)   17Jul42
- 3:45.0   Arne Andersson (SWE)   17Aug43
- 3:43.0   Gunder Hagg (SWE)   07Jul44
- 3:42.8   Wes Santee (USA)   04Jun54
- 3:41.8   John Landy (AUS)   21Jun54
- 3:40.8   Sandor Iharos (HUN)   28Jul55
- 3:40.6   Istvan Rozsavolgyi (HUN)   03Aug56
- 3:40.2   Olavi Salsola (FIN)   11Jul57
- 3:38.1   Stanislav Jungwirth (CZE)   12Jul57
- 3:36.0   Herb Elliott (AUS)   28Aug58
- 3:35.6   Herb Elliott (AUS)   06Sep60
- 3:33.1   Jim Ryun (USA)   08Jul67
- 3:32.2   Filbert Bayi (TAN)   02Feb74
- 3:32.1   Sebastian Coe (GBR)   15Aug79
- 3:31.36   Steve Ovett (GBR)   27Aug80
- 3:31.24   Sydney Maree (usa)   28Aug83
- 3:30.77   Steve Ovett (GBR)   04Sep83
- 3:29.67   Steve Cram (GBR)   16Jul85
- 3:29.46   Said Aouita (MOR)   23Aug85
- 3:28.86   Noureddine Morceli (ALG)   06Sep92
- 3:27.37   Noureddine Morceli (ALG)   12Jul95
- 3:26.00   Hicham el Guerrouj (MOR)   14Jul98  

*Progression of Women's Mile Record*

- *time*   *name*   *date*
- 6:13.2   Elizabeth Atkinson (GBR)   24Jun21
- 5:27.5   Ruth Christmas (GBR)   20Aug32
- 5:24.0   Gladys Lunn (GBR)   01Jun36
- 5:23.0   Gladys Lunn (GBR)   18Jul36
- 5:20.8   Gladys Lunn (GBR)   08May37
- 5:17.0   Gladys Lunn (GBR)   07Aug37
- 5:15.3   Evelyne Forster (GBR)   22Jul39
- 5:11.0   Anne Oliver (GBR)   14Jun52
- 5:09.8   Enid Harding (GBR)   04Jul53
- 5:08.0   Anne Oliver (GBR)   12Sep53
- 5:02.6   Diane Leather (GBR)   30Sep53
- 5:00.3   Edith Treybal (ROM)   01Nov53
- 5:00.2   Diane Leather (GBR)   26May54
- 4:59.6   Diane Leather (GBR)   29May54
- 4:50.8   Diane Leather (GBR)   24May55
- 4:45.0   Diane Leather (GBR)   21Sep55
- 4:41.4   Marise Chamberlain (NZL)   08Dec62
- 4:39.2   Anne Smith (GBR)   13May67
- 4:37.0   Anne Smith (GBR)   03Jun67
- 4:36.8   Maria Gommers (HOL)   14Jun69
- 4:35.3   Ellen Tittel (FRG)   20Aug71
- 4:34.9   Glenda Reiser (CAN)   07Jul73
- 4:29.5   Paola Pigni-Cacchi (ITA)   08Aug73
- 4:23.8   Natalia Marasescu (ROM)   21May77
- 4:22.1   Natalia Marasescu (ROM)   27Jan79
- 4:21.7   Mary Decker (USA)   26Jan80
- 4:20.89   Lyudmila Veselkova (SOV)   12Sep81
- 4:18.08   Mary Decker-Tabb (USA)   09Jul82
- 4:17.44   Maricica Puica (ROM)   16Sep82
- 4:15.8   Natalya Artyomova (SOV)   05Aug84
- 4:16.71   Mary Decker-Slaney (USA)   21Aug85
- 4:15.61   Paula Ivan (ROM)   10Jul89
- 4:12.56   Svetlana Masterkova (RUS)   14Aug96

### References

- Bennett, William (March 15, 1993), "Quantifying America's Decline", *Wall Street Journal*{{citation}}: CS1 maint: date and year (link)
- Dalal, Siddhartha; Folkes, Edward; Hoadley, Bruce (Fall 1989), "Lessons Learned from Challenger: A Statistical Perspective", *Stats: the Magazine for Students of Statistics*, pp. 14–18{{citation}}: CS1 maint: date and year (link)
- Gardner, Martin (April 1970), "Mathematical Games, Some mathematical curiosities embedded in the solar system", *Scientific American*, pp. 108–112{{citation}}: CS1 maint: date and year (link)
- Oakley, Cletus; Baker, Justine (April 1977), "Least Squares and the 3:40 Mile", *Mathematics Teacher*{{citation}}: CS1 maint: date and year (link)

---

*Source: Wikibooks, Linear Algebra/Topic: Line of Best Fit (https://en.wikibooks.org/wiki/Linear_Algebra/Topic%3A_Line_of_Best_Fit), by Wikibooks contributors, CC BY-SA 4.0.*
