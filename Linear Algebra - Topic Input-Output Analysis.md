# Topic: Input-Output Analysis

An economy is an immensely complicated network of interdependences. Changes in one part can ripple out to affect other parts. Economists have struggled to be able to describe, and to make predictions about, such a complicated object. Mathematical models using systems of linear equations have emerged as a key tool. One is Input-Output Analysis, pioneered by W. Leontief, who won the 1973 Nobel Prize in Economics.

Consider an economy with many parts, two of which are the steel industry and the auto industry. As they work to meet the demand for their product from other parts of the economy, that is, from users external to the steel and auto sectors, these two interact tightly. For instance, should the external demand for autos go up, that would lead to an increase in the auto industry's usage of steel. Or, should the external demand for steel fall, then it would lead to a fall in steel's purchase of autos. The type of Input-Output model we will consider takes in the external demands and then predicts how the two interact to meet those demands.

We start with a listing of production and consumption statistics. (These numbers, giving dollar values in millions, are excerpted from (Leontief 1965), describing the 1958 U.S. economy. Today's statistics would be quite different, both because of inflation and because of technical changes in the industries.)

- *used by*  
*steel*    *used by*  
*auto*    *used by*  
*others*    *total*
- *value of*  
*steel*    5 395    2 664      25 448
- *value of*  
*auto*    48    9 030      30 346

For instance, the dollar value of steel used by the auto industry in this year is $$2,664$$ million. Note that industries may consume some of their own output.

We can fill in the blanks for the external demand. This year's value of the steel used by others this year is $$17,389$$ and this year's value of the auto used by others is $$21,268$$. With that, we have a complete description of the external demands and of how auto and steel interact, this year, to meet them.

Now, imagine that the external demand for steel has recently been going up by $$200$$ per year and so we estimate that next year it will be $$17,589$$. Imagine also that for similar reasons we estimate that next year's external demand for autos will be down $$25$$ to $$21,243$$. We wish to predict next year's total outputs.

That prediction isn't as simple as adding $$200$$ to this year's steel total and subtracting $$25$$ from this year's auto total. For one thing, a rise in steel will cause that industry to have an increased demand for autos, which will mitigate, to some extent, the loss in external demand for autos. On the other hand, the drop in external demand for autos will cause the auto industry to use less steel, and so lessen somewhat the upswing in steel's business. In short, these two industries form a system, and we need to predict the totals at which the system as a whole will settle.

For that prediction, let $$s$$ be next years total production of steel and let $$a$$ be next year's total output of autos. We form these equations.  

$$
\begin{array}{rl} \text{next year}\textrm{'}\text{s production of steel} &=\text{next year}\textrm{'}\text{s use of steel by steel} \\ &\quad+\text{next year}\textrm{'}\text{s use of steel by auto} \\ &\quad+\text{next year}\textrm{'}\text{s use of steel by others} \\ \text{next year}\textrm{'}\text{s production of autos} &=\text{next year}\textrm{'}\text{s use of autos by steel} \\ &\quad+\text{next year}\textrm{'}\text{s use of autos by auto} \\ &\quad+\text{next year}\textrm{'}\text{s use of autos by others} \end{array}
$$

On the left side of those equations go the unknowns $$s$$ and $$a$$. At the ends of the right sides go our external demand estimates for next year $$17,589$$ and $$21,243$$. For the remaining four terms, we look to the table of this year's information about how the industries interact.

For instance, for next year's use of steel by steel, we note that this year the steel industry used $$5395$$ units of steel input to produce $$25,448$$ units of steel output. So next year, when the steel industry will produce $$s$$ units out, we expect that doing so will take $$s\cdot (5395)/(25\,448)$$ units of steel input— this is simply the assumption that input is proportional to output. (We are assuming that the ratio of input to output remains constant over time; in practice, models may try to take account of trends of change in the ratios.)

Next year's use of steel by the auto industry is similar. This year, the auto industry uses $$2664$$ units of steel input to produce $$30346$$ units of auto output. So next year, when the auto industry's total output is $$a$$, we expect it to consume $$a\cdot (2664)/(30346)$$ units of steel.

Filling in the other equation in the same way, we get this system of linear equation.  

$$
\begin{array}{rcrcrcr} {\displaystyle\frac{5\,395}{25\,448}}\cdot s &+ &{\displaystyle\frac{2\,664}{30\,346}}\cdot a &+ &17\,589 &= &s \\[1em] {\displaystyle\frac{48}{25\,448}}\cdot s &+ &{\displaystyle\frac{9\,030}{30\,346}}\cdot a &+ &21\,243 &= &a \end{array}
$$

Gauss' method on this system.  

$$
\begin{array}{rcrcr} (20\,053/25\,448)s &- &(2\,664/30\,346)a &= &17\,589 \\ -(48/25\,448)s &+ &(21\,316/30\,346)a &= &21\,243 \end{array}
$$

gives $$s=25\,698$$ and $$a=30\,311$$.

Looking back, recall that above we described why the prediction of next year's totals isn't as simple as adding $$200$$ to last year's steel total and subtracting $$25$$ from last year's auto total. In fact, comparing these totals for next year to the ones given at the start for the current year shows that, despite the drop in external demand, the total production of the auto industry is predicted to rise. The increase in internal demand for autos caused by steel's sharp rise in business more than makes up for the loss in external demand for autos.

One of the advantages of having a mathematical model is that we can ask "What if ...?" questions. For instance, we can ask "What if the estimates for next year's external demands are somewhat off?" To try to understand how much the model's predictions change in reaction to changes in our estimates, we can try revising our estimate of next year's external steel demand from $$17,589$$ down to $$17,489$$, while keeping the assumption of next year's external demand for autos fixed at $$21,243$$. The resulting system  

$$
\begin{array}{rcrcr} (20\,053/25\,448)s &- &(2\,664/30\,346)a &= &17\,489 \\ -(48/25\,448)s &+ &(21\,316/30\,346)a &= &21\,243 \end{array}
$$

when solved gives $$s=25\,571$$ and $$a=30\,311$$. This kind of exploration of the model is **sensitivity analysis**. We are seeing how sensitive the predictions of our model are to the accuracy of the assumptions.

Obviously, we can consider larger models that detail the interactions among more sectors of an economy. These models are typically solved on a computer, using the techniques of matrix algebra that we will develop in Chapter Three. Some examples are given in the exercises. Obviously also, a single model does not suit every case; expert judgment is needed to see if the assumptions underlying the model are reasonable for a particular case. With those caveats, however, this model has proven in practice to be a useful and accurate tool for economic analysis. For further reading, try (Leontief 1951) and (Leontief 1965).  
### Exercises

*Hint: these systems are easiest to solve on a computer.*

**Problem 1**  —

With the steel-auto system given above, estimate next year's total productions in these cases.

1. Next year's external demands are: up $$200$$ from this year for steel, and unchanged for autos.
2. Next year's external demands are: up $$100$$ for steel, and up $$200$$ for autos.
3. Next year's external demands are: up $$200$$ for steel, and up $$200$$ for autos.

**Problem 2**  —

In the steel-auto system, the ratio for the use of steel by the auto industry is $$2\,664/30\,346$$, about $$0.0878$$. Imagine that a new process for making autos reduces this ratio to $$.0500$$.

1. How will the predictions for next year's total productions change compared to the first example discussed above (i.e., taking next year's external demands to be $$17,589$$ for steel and $$21,243$$ for autos)?
2. Predict next year's totals if, in addition, the external demand for autos rises to be $$21,500$$ because the new cars are cheaper.

**Problem 3**  —

This table gives the numbers for the auto-steel system from a different year, 1947 (see Leontief 1951). The units here are billions of 1947 dollars.

- *used by*  
*steel*   *used by*  
*auto*   *used by*  
*others*   *total*
- *value of*  
*steel*   6.90   1.28     18.69
- *value of*  
*auto*   0   4.40     14.27

1. Solve for total output if next year's external demands are: steel's demand up 10% and auto's demand up 15%.
2. How do the ratios compare to those given above in the discussion for the 1958 economy?
3. Solve the 1947 equations with the 1958 external demands (note the difference in units; a 1947 dollar buys about what $1.30 in 1958 dollars buys). How far off are the predictions for total output?

**Problem 4**  —

Predict next year's total productions of each of the three sectors of the hypothetical economy shown below

- *used by*  
*farm*   *used by*  
*rail*   *used by*  
*shipping*   *used by*  
*others*   *total*
- *value of*  
*farm*   25   50   100     500
- *value of*  
*rail*   25   50   50     300
- *value of*  
*shipping*   15   10   0     500

if next year's external demands are as stated.

1. $$625$$ for farm, $$200$$ for rail, $$475$$ for shipping
2. $$650$$ for farm, $$150$$ for rail, $$450$$ for shipping

**Problem 5**  —

This table gives the interrelationships among three segments of an economy (see Clark & Coupe 1967).

- *used by*  
*food*   *used by*  
*wholesale*   *used by*  
*retail*   *used by*  
*others*   *total*
- *value of*  
*food*   0   2 318   4 679     11 869
- *value of*  
*wholesale*   393   1 089   22 459     122 242
- *value of*  
*retail*   3   53   75     116 041

We will do an Input-Output analysis on this system.

1. Fill in the numbers for this year's external demands.
2. Set up the linear system, leaving next year's external demands blank.
3. Solve the system where next year's external demands are calculated by taking this year's external demands and inflating them 10%. Do all three sectors increase their total business by 10%? Do they all even increase at the same rate?
4. Solve the system where next year's external demands are calculated by taking this year's external demands and reducing them 7%. (The study from which these numbers are taken concluded that because of the closing of a local military facility, overall personal income in the area would fall 7%, so this might be a first guess at what would actually happen.)

Solutions

### References

- Leontief, Wassily W. (1951), "Input-Output Economics", *Scientific American*, **185** (4): 15 {{citation}}: Unknown parameter |month= ignored (help).
- Leontief, Wassily W. (1965), "The Structure of the U.S. Economy", *Scientific American*, **212** (4): 25 {{citation}}: Unknown parameter |month= ignored (help).
- Clark, David H.; Coupe, John D. (1967), "The Bangor Area Economy Its Present and Future", *Reprot to the City of Bangor, ME* {{citation}}: Cite has empty unknown parameter: |1= (help); Unknown parameter |month= ignored (help).

---

*Source: Wikibooks, Linear Algebra/Topic: Input-Output Analysis (https://en.wikibooks.org/wiki/Linear_Algebra/Topic%3A_Input-Output_Analysis), by Wikibooks contributors, CC BY-SA 4.0.*
