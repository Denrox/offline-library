# How to change the display order of qt gui sink in gnuradio?

*Tags: gnuradio · score 3*

## Question

I create simple flow graph in gnuradio as below:

The expected output order is:

- 1.qt gui sink
- 2.frequency sink
- 3.time sink

But time sink appear first,then gui sink:

How to change the display order of qt gui sink in gnuradio?

## Accepted answer (score 2, by Phil Frost - W8II)

All QT GUI elements support a GUI hint which dictates how they are laid out in a grid.

All of the QT GUI widgets and plots have a parameter called GUI Hint. This is used to arrange GUIs in the window, as well as assign them to tabs in a QT GUI Tab Widget.

The format is:

(row, column, row span, column span)

For example,

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/19880/how-to-change-the-display-order-of-qt-gui-sink-in-gnuradio, by kittygirl, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
