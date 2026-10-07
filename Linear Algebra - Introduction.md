# Introduction

This book helps students to master the material of a standard undergraduate linear algebra course.

The material is standard in that the topics covered are Gaussian reduction, vector spaces, linear maps, determinants, and eigenvalues and eigenvectors. The audience is also standard: sophomores or juniors, usually with a background of at least one semester of calculus and perhaps with as many as three semesters.

The help that it gives to students comes from taking a developmental approach—this book's presentation emphasizes motivation and naturalness, driven home by a wide variety of examples and extensive, careful exercises. The developmental approach is what sets this book apart, so some expansion of the term is appropriate here.

Courses in the beginning of most mathematics programs reward students less for understanding the theory and more for correctly applying formulas and algorithms. Later courses ask for mathematical maturity: the ability to follow different types of arguments, a familiarity with the themes that underlie many mathematical investigations like elementary set and function facts, and a capacity for some independent reading and thinking. Linear algebra is an ideal spot to work on the transition between the two kinds of courses. It comes early in a program so that progress made here pays off later, but also comes late enough that students are often majors and minors. The material is coherent, accessible, and elegant. There are a variety of argument styles—proofs by contradiction, if and only if statements, and proofs by induction, for instance—and examples are plentiful.

So, the aim of this book's exposition is to help students develop from being successful at their present level, in classes where a majority of the members are interested mainly in applications in science or engineering, to being successful at the next level, that of serious students of the subject of mathematics itself.

Helping students make this transition means taking the mathematics seriously, so all of the results in this book are proved. On the other hand, we cannot assume that students have already arrived, and so in contrast with more abstract texts, we give many examples and they are often quite detailed.

In the past, linear algebra texts commonly made this transition abruptly. They began with extensive computations of linear systems, matrix multiplications, and determinants. When the concepts—vector spaces and linear maps—finally appeared, and definitions and proofs started, often the change brought students to a stop. In this book, while we start with a computational topic, linear reduction, from the first we do more than compute. We do linear systems quickly but completely, including the proofs needed to justify what we are computing. Then, with the linear systems work as motivation and at a point where the study of linear combinations seems natural, the second chapter starts with the definition of a real vector space. This occurs by the end of the third week.

Another example of our emphasis on motivation and naturalness is that the third chapter on linear maps does not begin with the definition of homomorphism, but with that of isomorphism. That's because this definition is easily motivated by the observation that some spaces are "just like" others. After that, the next section takes the reasonable step of defining homomorphism by isolating the operation-preservation idea. This approach loses mathematical slickness, but it is a good trade because it comes in return for a large gain in sensibility to students.

One aim of a developmental approach is that students should feel throughout the presentation that they can see how the ideas arise, and perhaps picture themselves doing the same type of work.

The clearest example of the developmental approach taken here—and the feature that most recommends this book—is the exercises. A student progresses most while doing the exercises, so they have been selected with great care. Each problem set ranges from simple checks to reasonably involved proofs. Since an instructor usually assigns about a dozen exercises after each lecture, each section ends with about twice that many, thereby providing a selection. There are even a few problems that are challenging puzzles taken from various journals, competitions, or problems collections. (These are marked with a "**?**" and as part of the fun, the original wording has been retained as much as possible.) In total, the exercises are aimed to both build an ability at, and help students experience the pleasure of, *doing* mathematics.

### Applications and Computers.

The point of view taken here, that linear algebra is about vector spaces and linear maps, is not taken to the complete exclusion of others. Applications and the role of the computer are important and vital aspects of the subject. Consequently, each of this book's chapters closes with a few application or computer-related topics. Some are: network flows, the speed and accuracy of computer linear reductions, Leontief Input/Output analysis, dimensional analysis, Markov chains, voting paradoxes, analytic projective geometry, and difference equations.

These topics are brief enough to be done in a day's class or to be given as independent projects for individuals or small groups. Most simply give the reader a taste of the subject, discuss how linear algebra comes in, point to some further reading, and give a few exercises. In short, these topics invite readers to see for themselves that linear algebra is a tool that a professional must have.

### For people reading this book on their own.

This book's emphasis on motivation and development make it a good choice for self-study. But, while a professional instructor can judge what pace and topics suit a class, if you are an independent student then perhaps you would find some advice helpful.

Here are two timetables for a semester. The first focuses on core material.

- *week*  *Monday*  *Wednesday*  *Friday*
- 1  One.I.1  One.I.1, 2  One.I.2, 3
- 2  One.I.3  One.II.1  One.II.2
- 3  One.III.1, 2  One.III.2  Two.I.1
- 4  Two.I.2  Two.II  Two.III.1
- 5  Two.III.1, 2  Two.III.2  Exam
- 6  Two.III.2, 3  Two.III.3  Three.I.1
- 7  Three.I.2  Three.II.1  Three.II.2
- 8  Three.II.2  Three.II.2  Three.III.1
- 9  Three.III.1  Three.III.2  Three.IV.1, 2
- 10  Three.IV.2, 3, 4  Three.IV.4  Exam
- 11  Three.IV.4, Three.V.1  Three.V.1, 2  Four.I.1, 2
- 12  Four.I.3  Four.II  Four.II
- 13  Four.III.1  Five.I  Five.II.1
- 14  Five.II.2  Five.II.3  Review

The second timetable is more ambitious (it supposes that you know One.II, the elements of vectors, usually covered in third semester calculus).

- *week*  *Monday*  *Wednesday*  *Friday*
- 1  One.I.1  One.I.2  One.I.3
- 2  One.I.3  One.III.1, 2  One.III.2
- 3  Two.I.1  Two.I.2  Two.II
- 4  Two.III.1  Two.III.2  Two.III.3
- 5  Two.III.4  Three.I.1  Exam
- 6  Three.I.2  Three.II.1  Three.II.2
- 7  Three.III.1  Three.III.2  Three.IV.1, 2
- 8  Three.IV.2  Three.IV.3  Three.IV.4
- 9  Three.V.1  Three.V.2  Three.VI.1
- 10  Three.VI.2  Four.I.1  Exam
- 11  Four.I.2  Four.I.3  Four.I.4
- 12  Four.II  Four.II, Four.III.1  Four.III.2, 3
- 13  Five.II.1, 2  Five.II.3  Five.III.1
- 14  Five.III.2  Five.IV.1, 2  Five.IV.2

See the table of contents for the titles of these subsections.

To help you make time trade-offs, in the table of contents I have marked subsections as optional if some instructors will pass over them in favor of spending more time elsewhere. You might also try picking one or two topics that appeal to you from the end of each chapter. You'll get more from these if you have access to computer software that can do the big calculations.

The most important advice is: do many exercises. The recommended exercises are labeled throughout. (The answers are available.) You should be aware, however, that few inexperienced people can write correct proofs. Try to find a knowledgeable person to work with you on this.

Finally, if I may, a caution for all students, independent or not: I cannot overemphasize how much the statement that I sometimes hear, "I understand the material, but it's only that I have trouble with the problems" reveals a lack of understanding of what we are up to. Being able to do things with the ideas is their point. The quotes below express this sentiment admirably. They state what I believe is the key to both the beauty and the power of mathematics and the sciences in general, and of linear algebra in particular (I took the liberty of formatting them as poems).

*I know of no better tactic*  
* than the illustration of exciting principles*  
*by well-chosen particulars.*  
*--Stephen Jay Gould*

*If you really wish to learn*  
* then you must mount the machine*  
* and become acquainted with its tricks*  
*by actual trial.*  
*--Wilbur Wright*

Jim Hefferon  
Mathematics, Saint Michael's College  
Colchester, Vermont USA 05439  
http://joshua.smcvt.edu  
2006-May-20

*Author's Note.* Inventing a good exercise, one that enlightens as well as tests, is a creative act, and hard work.

The inventor deserves recognition. But for some reason texts have traditionally not given attributions for questions. I have changed that here where I was sure of the source. I would greatly appreciate hearing from anyone who can help me to correctly attribute others of the questions.

---

*Source: Wikibooks, Linear Algebra/Introduction (https://en.wikibooks.org/wiki/Linear_Algebra/Introduction), by Wikibooks contributors, CC BY-SA 4.0.*
