#!/usr/bin/env python

import datetime
import math


def osterrechnung(tage):
	return osterdatum + datetime.timedelta(days=tage)

def datumkonvert(datum):
	return datetime.datetime.strptime(datum, "%m/%d/%Y")

jahr = datetime.date.today().year

zeit = datetime.datetime.now().time()
minzeit= datetime.time(7,55)
maxzeit= datetime.time(17)

a = jahr % 19
b = jahr % 4
c = jahr % 7

k = math.floor(jahr / 100)
p = math.floor((8*k + 13)/25)
q = math.floor(k / 4)
M = (15 + k - p - q) % 30
d = (19 * a + M) % 30
N = (4 + k - q) % 7
e = (2 * b + 4 * c + 6 * d + N) % 7
ostersonntag = (22 + d + e)

monat = 3

if(ostersonntag > 31):
	ostersonntag = ostersonntag % 31
	monat = 4

ostern = (f"{monat}/{ostersonntag}/{jahr}")

osterdatum = datumkonvert(ostern)

karfreitag = osterrechnung(-2) 
ostermontag = osterrechnung(1)
auffahrt = osterrechnung(39)
pfingstmontag = osterrechnung(50)

neujahr = datumkonvert(f"01/01/{jahr}")
berchtoldstag = datumkonvert(f"01/02/{jahr}")
nationalfeiertag = datumkonvert(f"08/01/{jahr}")
weihnachten = datumkonvert(f"12/25/{jahr}")
stephanstag = datumkonvert(f"12/26/{jahr}")
#testtag = datumkonvert(f"08/22/{jahr}")

heuteSTR = datetime.date.today().strftime("%m/%d/%Y")
heute = datumkonvert(heuteSTR)

feiertage = [
karfreitag,
ostermontag,
auffahrt,
pfingstmontag,
neujahr,
berchtoldstag,
nationalfeiertag,
weihnachten,
stephanstag,
#testtag
]


if(heute not in feiertage and minzeit <= zeit <= maxzeit):
	exec(open("Mail.py").read())
