# Mathematica notebook for NEC2 (NEC, Numerical Electromagnics Code)

*Tags: antenna, antenna-modeling · score 3*

## Question

Are there any open source Mathematica notebooks that interface with NEC2? I am primarily interested in plotting the NEC2 results from Mathematica.

## Accepted answer (score 3, by K7PEH)

I use Mathematica with NEC4 which would work essentially the same as with NEC2. I find Mathematica to be a great front end to NEC4 for not only graphing results but also preparing functions for various mathematical operations (i.e. doing Calculus with the resulting solutions).

Originally, I created a notebook of various functions that I wrote to perform the operations I used in plotting results or doing other operations on the solution data. This was integrated with NEC4 to the point that I even prepared the input geometry description of the antenna using Mathematica. Also, I would execute NEC4 from Mathematica passing the names of input data files and the names of my desired output file for subsequent loading into Mathematica structures.

I no longer do that because it was just too much of a hassle to maintain and it provided no real benefits. Now, I prepare the antenna geometry data using an editor and also several Python programs I wrote to create geometry for configurations that consisted of many "wires" in specific geometry patterns. For example, radials for an antenna or patch work such as when I modeled my pickup truck as a ground plane.

I execute NEC4 as an ordinary batch like program producing the output solution file. I also have Python programs that read and scrape the desired data from the formatted print created by NEC4 and then I create individual data files for later import into Mathematica.

I have a variety of execution types where I know the type of data being produced which my Python scraping programs handle. For example, scraping the antenna feed point input data which provides the data I use to compute the SWR at the feed point. I also scrape the gain data for producing 3D plots of the radiation field.

I have a whole list of ideas of things to do, other graphs to produce and doing a better job of modeling transmission lines of various types using the manufacturers data (R, L, and C models).

For my 80-meter dipole that is fed with 450-ohm ladder line I do a full frequency sweep from 3.0 MHz to 54 MHz for every 10 KHz. This is a whole lot of data. For the gain data to do the radiation patterns my resulting data file is 240 MB in size and that is filtering the data to every 100 KHz. However, using this data I do a full 3D interpolation of the gain data to create smoothed functions I use for example for Integration or taking Derivatives. Using some of the Mathematica built in functions, I can use the resulting SWR data from the frequency sweep to find all the resonant spots of the antenna where I define resonance as the bandwidth of an SWR that is under 2:1.

So, in summary, my work consists of the following:

1. Mathematic function source of my own functions.
2. Python programs used to aid in creation of antenna geometry input.
3. Python programs used to scrape the formatted output of NEC4.

Right now, I think I have around 40 of my own Mathematica functions that perform various operations or plot graphs. And, maybe a half-dozen Python programs that generate "repeated" structures for antenna geometry data. And, about 4 formatted output scraper Python programs that pull the interesting data from the so-called "pretty-print" produced by NEC4.

Oh, I have also modified the NEC4 program to generate other data of interest as well and also to track performance since some of my executions take as long as an hour (large frequency sweeps). Although NEC2 is coded in Fortran ala Fortran 77 or something close to that, NEC4 is coded in Fortran 90 plus some features from Fortran 95. NEC4 is licensed from Lawrence Livermore Laboratories. At the time I got my license about 6 years ago it was $300.

**A Simple Example -- 20 meter vertical with perfect ground**

The antenna itself is a ground mounted vertical that is made from 1/2 copper tubing (I actually have this antenna though not set up right now, I made it myself from Home Depot materials). For this model I chose a perfect ground (an option in NEC4/NEC2) but a more realistic ground without radials and then a model with radials can be done as well. I use this antenna with 4 radials so I don't get as good of an SWR as this example shows but it is a working and effective antenna.

I first set up my Mathematica notebook environment as shown below:

The statements above establish my working directory for NEC4 work and then I import my Mathematica function library supporting the NEC4 work. By the way, this is all done with an Apple iMac-24 running OS X El Capitan.

Next, I read in the antenna input solution data. This is the data that specifies the feed point voltage (R/X), feed point current (R/X), and feed point Impedance (R/X), feed point Admittance (R/X), and Power in Watts (R) for each frequency of the specified frequency sweep (given by the data file governing the solution). The integer values 1,1,1,0 in each column are the wire tag number, segment number, and the voltage (R/X) which is reported as integers 1 and 0 for the complex value 1.0+j0.0

Here are the Mathematica statements that read in the antenna input:

As you can see, I use a function that I wrote called readAntennaInput[] which is given the file name of the file with this data that was scraped by one of my Python programs from the NEC4 output data.

The array returned, given the Mathematica label of antinput is 12 rows by 71 columns. Each column is a different frequency for the frequency sweep.

Here is a portion of that data:

You can see the individual frequency columns as row one designates the frequency beginning with 14.0 MHz and incrementing by 0.005 MHz until the maximum frequency of the sweep 14.35 MHz (the entire 20 meter band). The floating point numbers you see in each column are the R and X values of the parameters mentioned above. The two rows that have whole numbers are the R and X of the antenna feed point impedance.

Next I prepare the SWR function. This is an interpolated function that computes the SWR based on a nominal value of 50.0 ohms Real. Thus, SWR of 1:1 would suggest 50 ohms input impedance for the antenna.

The function that I wrote to compute this SWR Function is called prepareSWRFunction as you see above. With this function I can do Calculus such as find minimums, do integration, do differentiation and so on. Most importantly it creates nice smooth plots:

The plot function that I wrote uses the Calculus to find the minimum which is essentially taking the derivative and setting it to zero which all Calculus students have learned to do. The result is reported as the first line that is labeled Minimum SWR Position Vector. The next two lines of output basically extract the individual data of SWR and Frequency of minimum SWR.

Next is the plot itself. The vertical Axes is SWR and the horizontal Axes is frequency. The green line is actually the SWR curve and it is nice and flat over the entire 20 meter spectrum (the perfect ground model helps that result).

The blue horizontal line is the marker for an SWR of 2:1 which I consider my maximum for desired SWR. The yellowish line is the minimum SWR which is 1.38:1.

Unfortunately, on this particular run I did not include the gain data so a 3-dimensional radiation field plot is not available. If anyone is interested I can add that but probably will not get to it until next week.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7114/mathematica-notebook-for-nec2-nec-numerical-electromagnics-code, by ZJL, K7PEH. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
