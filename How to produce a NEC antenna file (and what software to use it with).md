# How to produce a NEC antenna file (and what software to use it with)?

*Tags: antenna, antenna-theory, wire-antenna, antenna-modeling · score 5*

## Question

So I'm really trying to get to grips with antenna radiation patterns, and more importantly things that are to close to the antenna that might interfere.

I've downloaded Qantenna and 4NEC2 to try and model my antenna and see what I can do, however neither of these programs allow you to 'make' an antenna (as far as I can tell) they require you to import an NEC file. Is there a free piece of software that will make a NEC file for a simple quarter wave whip antenna?

## Answer (score 6, by KJ7LNW)

I recommend the xnec2c antenna simulator for Linux. It has a few features that qantenna and 4nec2 do not:

1. Xnec2c supports parallel execution by forking for fast simulation.
2. It uses accelerated math libraries such as OpenBLAS, LAPACK, or Intel MKL if available.
3. It is capable of drawing 3D structures without running it through the NEC2 tooling. For example, 4nec2 can only draw a helix after it runs through the NEC2 output, which is slow (maybe this changed in new releases?). The qantenna tool doesn't draw helixes at all.
4. Xnec2c integrates with xnec2c-optimize to tune antennas for characteristics like high gain and low VSWR.

- xnec2c website: https://www.xnec2c.org/
- xnec2c github: https://github.com/KJ7LNW/xnec2c/
- xnec2c-optimize: https://github.com/KJ7LNW/xnec2c-optimize

(Bias Disclaimer: Xnec2c was originally written by Neoklis, 5B4AZ and I have since taken over as maintainer for the project. While that may sound biased, I have used both 4nec2 and qantenna, and IMHO xnec2c is faster, easier to use, and has a more intuitive UI.)

## Answer (score 5, by ntsakonas)

It is true that 4nec2 is a bit non-intuitive when it comes to creating a new antenna, but it is easy to start from scratch and create anything, without the need to import.

4nec2 provides 4 different methods to edit the antenna model and you can find them on the Settings menu. By default, the 'Nec Editor (new)' is selected but you can change it to 'Geometry edit' which uses a 3d antenna creation tool but it is quite hard to use. Selecting either of the two first options means that you are quite comfortable to use directly NEC2 commands. Under the Edit menu there is the option 'Input (.nec) file' and clicking on this option opens the editor you have previously selected on the Settings menu.

I suggest to leave the 'Nec Editor (new)' selected and try to work the geometry of your antenna using 3d coordinates.For this example make sure you have selected this option.

Here is how to create a model for a vertical whip antenna. note: this is just the procedure not that the model will be the one that will serve 100% your purpose.

the tricky part is that 4nec2 does not have a 'create new' option.So, create an empty text file with any editor (e.g notepad) and save it where you prefer using the .nec extension. eg: vertical_whip.nec you don't have to put anything on this file yet.just an empty file.

now on 4nec2 select 'File->Open 4nec2 in/out file' and open the empty file you just created (e.g the vertical_whip.nec).You will notice that 4nec2 will start a new antenna project.

Now select 'Edit->Input (.nec) file' and you will be presented with a spreadsheet like screen, and the 'Geometry' tab will be selected. This is where you enter the antenna geometry. Let's enter the geometry of the vertical whip and make use of the symbols on 4nec2.

The length of a vertical quarter wave whip (in feet) is given by the formula length = 234/F , where F is the frequency in Mhz.So to make our life easier we will use a few symbols.Go to 'Symbols' tab and enter the following symbols ont he first column 'Symbols and equations', one on each row:

F=144

L=234/F

(in this example I use 144Mhz for frequency but since we use it in a symbol we can move the design at any frequency)

make sure that at the bottom of the tab under section 'Scaling' the 'Feet' radio button is selected (because all the dimensions in the model will be in feet)

Now switch to 'Geometry' tab and click on the first row and first column and from the drop down select 'wire' to add the antenna element. on the second column (Tag) just enter 1 as this is the first wire on the model.on the 'Segs' enter 11 and then enter the following (X,Y,Z) pairs:

X1=0,Y1=0,Z1=0 X2=0,Y2=0,Z2=L Radius=0.001

this will create a vertical wire of length L centered at the axis and at height 0 feet from ground

Move to 'Source/Load' tab and click on the first row on the first column and select 'current source'. The next two parameter define where to place the feedpoint of the antenna. We need it to be on Tag 1 (our first and only wire) on segment 1 (which is the lower end of the antenna). Enter 1 on 'Real' and 0 on 0 on 'Imag' and you are done here.

Move to 'Freq/Ground' and enter F on the frequency box, so that the frequency is taken from our symbols.on the 'Environment' section select 'Real ground' and also select 'Good' on ground type below.

Select 'File->Save' to save the model and you can close the editor.

4nec2 will update the geometry of the antenna and the 'Geometry' window will display your antenna.If it is not visible just press F3, or if the window is visible and the geometry was not updated just select 'View->reset' on the geometry window.

you can now model your antenna by pressing F7 and selecting 'far field pattern'. The Frequency should already be set to 144Mhz.Click on the 'Generate' button and you should see the antenna pattern.

Note that this is not necessarily the best way to model a vertical antenna but it is a good start to create models from scratch.

Make sure you read 4nec2 help files and also the 4 parts article on starting modelling with nec.

http://wireless.ictp.it/school_2005/download/nec2/nec_part1.pdf

(I cannot post more than 2 links so this is the first part and the rest is just changing the file name to nec_part2.pdf,nec_part3.pdf,nec_part4.pdf)

Hope this helps you to get started.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5405/how-to-produce-a-nec-antenna-file-and-what-software-to-use-it-with, by FraserOfSmeg, KJ7LNW, ntsakonas. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
