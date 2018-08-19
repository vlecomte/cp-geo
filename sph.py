#!/usr/bin/env python3
import sys
from math import *
(r,lat,lon) = [float(s) for s in sys.argv[1:]]
lon *= pi/180
lat *= pi/180
print("({:.3f},{:.3f},{:.3f})".format(r*cos(lat)*cos(lon), r*cos(lat)*sin(lon), r*sin(lat)))
