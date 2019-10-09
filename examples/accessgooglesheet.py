'''
Sample program to demo how you can access online google sheet from python
'''

import pandas as pd
import urllib.request

linktocsv = "https://docs.google.com/spreadsheets/d/17nk_AgWIDuh1NHId5P81b3UGO6T7kvo19_Q0ga8Sg6s/edit?usp=sharing"
source = StringIO.StringIO(urllib.request.get(linktocsv).content))
data = pd.read_csv(source)