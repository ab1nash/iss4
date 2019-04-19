# import pandas as pd
import numpy as np
import requests 
# import matplotlib.pyplot as plt
# import seaborn as sns
from urllib.request import urlopen
from bs4 import BeautifulSoup
url = "https://www.smbc-comics.com/"
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')
images=soup.find_all("img")
print(images[4]['src'])
url=images[4]['src']
r = requests.get(url)
with open("download.png",'wb') as f: 
  
    # Saving received content as a png file in 
    # binary format 
  
    # write the contents of the response (r.content) 
    # to a new file in binary mode. 
    f.write(r.content)