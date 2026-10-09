# Calculating effective SSN (sunspot number)?

*Tags: hf, propagation, sunspots · score 4*

## Question

I am doing research on how SSN-like parameters affect HF radio signals. As I can see, effective SSN is a parameter that is derived from SSN or using other parameters. Does anyone know how to calculate effective SSN?

For example, this file has some parameters: ftp://ftp.swpc.noaa.gov/pub/latest/DSD.txt

ref http://spawx.nwra.com/spawx/ssne.html

## Answer (score 3, by AA6YQ)

SSN is an abbreviation for "Smoothed Sunspot Number".

How the sunspot number should be smoothed depends entirely on what you are doing. Every useful ionospheric model specifies the manner in which recent solar activity is to be conveyed. If wish to run HF propagation predictions using the VOACAP forecasting engine, for example, then you would generate a smoothed sunspot number in the manner it prescribes:

http://www.voacap.com/choosingssn.html

Additional information you may find helpful is here:

https://www.ngdc.noaa.gov/stp/space-weather/solar-data/solar-indices/sunspot-numbers/documentation/readme_sunspot-numbers.pdf

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/4975/calculating-effective-ssn-sunspot-number, by lsc, AA6YQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
