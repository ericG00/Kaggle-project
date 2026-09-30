import requests
import numpy
import pandas
import matplotlib
import seaborn
from pyjstat import pyjstat

base_url = "https://data.ssb.no/api/pxwebapi/v2/tables/07230/data?lang=no&outputFormat=json-stat2&valuecodes[ContentsCode]=*&valuecodes[Tid]=2025&valuecodes[Region]=*&valuecodes[Boligtype]=*&heading=ContentsCode,Tid,Boligtype&stub=Region"

datasett = pyjstat.Dataset.read(base_url)
df = datasett.write("dataframe")
# 48 X 5 - rad: region, kolonner: informajon
print(df.head(10))
