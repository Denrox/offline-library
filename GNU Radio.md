# GNU Radio

- GNU Radio
- Original author Eric Blossom
- Developers GNU Radio Community  
President: Josh Morman  
Maintainer: Marcus Müller
- Release 2001 (2001)
- Stable release

3.10.12.0  / 20 February 2025

- Written in C++, Python
- Operating system Cross-platform
- Available in English
- Type Radio
- License 2007: GPL-3.0-or-later  
2001: GPL-2.0-or-later
- Website www.gnuradio.org
- Repository

- github.com/gnuradio/gnuradio.git

**GNU Radio** is a free software development toolkit that provides signal processing blocks to implement [software-defined radios](Software-defined%20radio.md) and signal processing systems. It can be used with external radio frequency (RF) hardware to create software-defined radios, or without hardware in a simulation-like environment. It is widely used in hobbyist, academic, and commercial environments to support both wireless communications research and real-world radio systems.

### Overview

The GNU Radio software provides the framework and tools to build and run software radio or just general signal-processing applications. The GNU Radio applications themselves are generally known as "flowgraphs", which are a series of signal processing blocks connected together, thus describing a data flow.

As with all [software-defined radio](Software-defined%20radio.md) systems, reconfigurability is a key feature. Instead of using different radios designed for specific but disparate purposes, a single, general-purpose, radio can be used as the radio front-end, and the signal-processing software (here, GNU Radio), handles the processing specific to the radio application.

These flowgraphs can be written in either C++ or Python. The GNU Radio infrastructure is written entirely in C++, and many of the user tools (such as GNU Radio Companion) are written in Python. Flowgraphs can also be constructed in the GNU Radio Companion GUI.

GNU Radio is a signal processing package and part of the GNU Project. It is distributed under the terms of the GNU General Public License (GPL), and most of the project code is copyrighted by the Free Software Foundation.

### Software

#### GNU Radio Companion

The GNU Radio Companion is a graphical UI used to develop GNU Radio applications. This is the front-end to the GNU Radio libraries for signal processing. GRC was developed by Josh Blum during his studies at Johns Hopkins University (2006–2007), then distributed as free software for the *October 2009 Hackfest*. Starting with the 3.2.0 release, GRC was officially bundled with the GNU Radio software distribution.

GRC is effectively a Python code-generation tool. When a flowgraph is *compiled* in GRC, it generates Python code that creates the desired graphical user interface (GUI) windows and widgets, and creates and connects the blocks in the flowgraph.

GRC currently supports GUI creation using the Qt toolkit.

#### Plotting and Displays

GNU Radio provides many common plotting and data visualization data sinks, including FFT displays, symbol constellation diagrams, and scope displays. These are commonly used both for debugging radio applications and as the user-interface to a final application.

#### Out-of-Tree (OOT) Modules

Many users create "out-of-tree modules" for use with GNU Radio, which allows users to create their own custom blocks. OOTs typically contain one or more custom blocks, and example flowgraphs to exercise those blocks.

---

*Source: Wikipedia, GNU Radio (https://en.wikipedia.org/wiki/GNU_Radio), by Wikipedia contributors, CC BY-SA 4.0.*
