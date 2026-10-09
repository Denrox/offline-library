# How can one convert from Grid Square to Lat/Long?

*Tags: location, maidenhead-locator · score 4*

## Question

Can someone explain how can get the Lat/Lon of a given Grid square? (the middle of the grid would be the best). I've looked at this (that does the "reverse"...from lat/lo to grid"):

[How can one convert from Lat/Long to Grid Square?](How%20can%20one%20convert%20from%20Lat%20Long%20to%20Grid%20Square.md)

But i need to do the inverse...

Anyone can explain in step by step?

Many thanks!

## Answer (score 3, by Edwin van Mierlo)

if by "Grid" you mean "Maidenhead Locator" then here is a similar [question](Convert%20maidenhead%20grid%20square%20to%20lat%20long%20in%20Excel.md), with some sample Python code as answer.

The result from the code will be

```
Lon = (start_lon) to (end_lon)
Lat = (start_lat) to (end_lat)

```

From that you can easily calculate the "middle" of the square. or you can take the code and adapt, here is the code from the above mentioned question/answer:

```
# -*- coding: utf-8 -*-
#maiden head to lon/lat

__MH__ = 'HK34wh'

def GetLon(ONE, THREE, FIVE):
StrStartLon = ''
StrEndLon = ''

Field = ((ord(ONE.lower()) - 97) * 20)
Square = int(THREE) * 2
SubSquareLow = (ord(FIVE.lower()) - 97) * (2/24)
SubSquareHigh = SubSquareLow + (2/24)

StrStartLon = str(Field + Square + SubSquareLow - 180 )
StrEndLon = str(Field + Square + SubSquareHigh - 180 )

return StrStartLon, StrEndLon

def GetLat(TWO, FOUR, SIX):
StrStartLat = ''
StrEndLat = ''

Field = ((ord(TWO.lower()) - 97) * 10)
Square = int(FOUR)
SubSquareLow = (ord(SIX.lower()) - 97) * (1/24)
SubSquareHigh = SubSquareLow + (1/24)

StrStartLat = str(Field + Square + SubSquareLow - 90)
StrEndLat = str(Field + Square + SubSquareHigh - 90)

return StrStartLat, StrEndLat

def main(strMaidenHead = __MH__):
if len(strMaidenHead) < 6: strMaidenHead = __MH__

ONE = strMaidenHead[0:1]
TWO = strMaidenHead[1:2]
THREE = strMaidenHead[2:3]
FOUR = strMaidenHead[3:4]
FIVE = strMaidenHead[4:5]
SIX = strMaidenHead[5:6]

(strStartLon, strEndLon) = GetLon(ONE, THREE, FIVE)
(strStartLat, strEndLat) = GetLat(TWO, FOUR, SIX)

print ('Start Lon = ' + strStartLon)
print ('End   Lon = ' + strEndLon)
print ()
print ('Start Lat = ' + strStartLat)
print ('End   Lat = ' + strEndLat)

return strStartLon, strEndLon, strStartLat, strEndLat

#BEGIN
if __name__ == '__main__':
main ()
sys.exit ('end of script: '+ os.path.basename(__file__) + os.linesep + 'by: Edwin van Mierlo')
#END

```

(for the purists amongst you, no; this is not very 'pythonic', but it does work)

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6462/how-can-one-convert-from-grid-square-to-lat-long, by Michele MichelinoK Costantino, Edwin van Mierlo. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
