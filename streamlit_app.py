from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

"""
# Cross Sectional Child Income Statistics by College Tier and Parent Income Percentile
### Authors: Vincent Wilmet, Marinie Tao, Alia Haiji

Drawing on the data collected by [Opportunity Insights](https://opportunityinsights.org/data/), a research lab at Harvard 
led by the famous economist [Raj Chetty](https://scholar.google.com/citations?hl=en&user=PhDDPiUAAAAJ&view_op=list_works&sortby=pubdate),
we aim to visualize the _full_ landscape of education (in)equalities. 

The data is derived by a mix of Obama's [College Scorecard (2015)](https://collegescorecard.ed.gov/) and de-identified 
public data from 1996-2014 American [income tax returns (W-2 Forms)](https://www.irs.gov/forms-pubs/about-form-w-2). 
The *70+ million* children<->parent pairs were drawn between 1978-1991 if they are claimed as dependents by the parent tax 
filers in the U.S, cross referenced and validated with proof of enrollment via the [1098-T forms](https://www.irs.gov/forms-pubs/about-form-1098-t)
submitted to the United States Internal Revenue Service (IRS) by a student/their university.

## Figure 1: Post Graduation Parent's Earning by Tier
"""

image = Image.open("img/Post-grad-parent-earning-by-tier.png")
st.image(image, caption="Post Graduation Parent's Earning by Tier") #Image name

"""
Here we can see that having a strong education, like an Ivy Plus education, creates a large proportion of high income earners.
Now lets see if the same translates to their children. 

If the parents went to a strong school, what is the income of their children?

## Figure 2: Post Graduation Student Earnings by Tier
"""
option = st.selectbox(
     'View figure by ',
     ('Values', 'Percentile'))

st.write('You selected:', option)

if option == 'Values': image = Image.open("img/Post-grad-earning-by-tier.png")
elif option == 'Percentile': image = Image.open("img/Post-Grad Earnings Percinetile by Tier.png")

st.image(image, caption="Post Graduation Student Earnings by Tier")

"""
## Figure 3:  Relationship between Partents Mean Income and Kids Income
"""
option = st.selectbox(
     'View figure by ',
     (  '(1) Ivy Plus', 
        '(2) Other elite schools (public and private)',
        '(3) Highly selective public',
        '(4) Highly selective private',
        '(5) Selective public',
        '(6) Selective private',
        '(7) Nonselective four-year public',
        '(8) Nonselective four-year private not for profit',
        '(9) Two-year (public and private not for profit)',
        '(10) Four-year for profit',
        '(11) Two-year for profit',
        '(12) Less than two-year schools of any type',
        '(13) Attending college with unsufficient data',
        '(14) Late attender (23-28)',
        '(15) Never attended college (before 2013)'))

st.write('You selected:', option)

if option == '(1) Ivy Plus': image = Image.open("img/") 
elif option == '(2) Other elite schools (public and private)': image = Image.open("img/")
elif option == '(3) Highly selective public': image = Image.open("img/")
elif option == '(4) Highly selective private': image = Image.open("img/")
elif option == '(5) Selective public': image = Image.open("img/")
elif option == '(6) Selective private': image = Image.open("img/")
elif option == '(7) Nonselective four-year public': image = Image.open("img/")
elif option == '(8) Nonselective four-year private not for profit': image = Image.open("img/")
elif option == '(9) Two-year (public and private not for profit)': image = Image.open("img/")
elif option == '(10) Four-year for profit': image = Image.open("img/")
elif option == '(11) Two-year for profit': image = Image.open("img/")
elif option == '(12) Less than two-year schools of any type': image = Image.open("img/")
elif option == '(13) Attending college with unsufficient data': image = Image.open("img/")
elif option == '(14) Late attender (23-28)': image = Image.open("img/")
elif option == '(15) Never attended college (before 2013)': image = Image.open("img/Post-grad-earning-by-tier.png")


st.image(image, caption="Relationship between Partents Mean Income and Kids Income")



"""
## Links:

* Code: [github](https://github.com/vincentwi/streamlit-example)
* Resources: [Opportunity Insights](https://opportunityinsights.org/data/)
* Report: [link to our report]()
* Website: [you're on it right now](share.streamlit.io/vincentwi/streamlit-example)
* Further Reading: 
        + [IMPROVING EQUALITY OF OPPORTUNITY: NEW INSIGHTS FROM BIG DATA](https://onlinelibrary.wiley.com/doi/10.1111/coep.12478) [via CS](https://onlinelibrary-wiley-com.ezproxy.universite-paris-saclay.fr/doi/pdf/10.1111/coep.12478)
        + [Mobility Report Cards: The Role of Colleges in Intergenerational Mobility](https://opportunityinsights.org/wp-content/uploads/2018/03/coll_mrc_slides.pdf)


MIT License
Copyright © Vincent Wilmet 2022
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""