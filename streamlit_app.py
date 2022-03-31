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
f1option = st.selectbox(
     'View figure by ',
     ("It's Values", "It's Percentiles"))

st.write('You selected:', f1option)

if f1option == "It's Values": image = Image.open("img/Post-grad-parent-earning-by-tier.png")
elif f1option == "It's Percentiles": image = Image.open("img/Post-Grad Earnings Percinetile by Tier.png")

st.image(image, caption="Post Graduation Parent's Earning by Tier") #Image name

"""
Here we can see that having a strong education, like an Ivy Plus education, creates a large proportion of high income earners.
Now lets see if the same translates to their children. 

If the kids go to a strong school, what is their income?

## Figure 2: Post Graduation Student Earnings by Tier
"""
f2option = st.selectbox(
     'View figure by ',
     ('Values', 'Percentile'))

st.write("You selected:", f2option)

if f2option == "Values": image = Image.open("img/Post-grad-earning-by-tier.png")
elif f2option == "Percentile": image = Image.open("img/Post-Grad Earnings Percinetile by Tier.png")

st.image(image, caption="Post Graduation Student Earnings by Tier")

"""
As shown in the graphic above, we are not surprised. The largest proportion of kids who make 150k+ come from Ivy League schools.
Much like how the largest proportion of parents earning $500k+ came from Ivy Plus schools as well. 

But why is this? To understand this question, we must look at the student composition of each of these universities.
How many of them are the children of wealthy parents? Are the rich getting richer? Do students from lower income brackets
have access with equal proportion to those with higher earning parents?. 

## Figure 3: Student Composition by Parent's Income Percentile
"""
    
image = Image.open("img/Student Comp by Parent Income.png")
st.image(image, caption="Student Composition by Parent's Income Percentile") #Image name

"""
Seeing that nearly 60% of the students in an Ivy Plus come from a background where their parents are in the top 10 percentile
for income earning brackets, we get a better picture of how Ivy Plus schools operate. Similarly, we also understand how the 
less/non selective schools and education frameworks operate. 

Thanks to the fact the selective schools have roughly 20% or more of their students come from affluent backgrounds, they
can charge higher tuition costs, which in turn allow for hiring elite educators, research facilities, student dormatories,
amongst many other quality of learning improvements.

But is there a correlation between the Parents income and that of their kids? Knowing that a very small minority of 
low income family students compose the student body populatione in the selective schools, will parents from low income
backgrounds have a low likelihood of getting their kids admitted into these selective schools? And if this is so,
will it have an impact on the income their kids make? We can make this conclusion from the learnings of Figure (1) and 
Figure (2) which tell us that students graduating from selective schools will likely have higher income. Let's look
at the relationship between the Parents income and thier kids, and understanding that implicitly in this is the fact
that lower income families are less often entering selective universties. 

## Figure 4:  Relationship between Partents Mean Income and Kids Income
"""
f4option = st.selectbox(
     'View figure by ',
     (  '(0) All',
        '(1) Ivy Plus', 
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

st.write('You selected:', f4option)

if f4option == '(0) All': image = Image.open("img/Kids_Parents_income correlation_per_school/Relationship between Parents Mean Income and Kids Median Income.png")
elif f4option == '(1) Ivy Plus': image = Image.open("img/Kids_Parents_income correlation_per_school/(1) Ivy Plus.png") 
elif f4option == '(2) Other elite schools (public and private)': image = Image.open("img/Kids_Parents_income correlation_per_school/(2) Other elite schools (private and public).png")
elif f4option == '(3) Highly selective public': image = Image.open("img/Kids_Parents_income correlation_per_school/(3)Highly selective public.png")
elif f4option == '(4) Highly selective private': image = Image.open("img/Kids_Parents_income correlation_per_school/(4) Highly selected private.png")
elif f4option == '(5) Selective public': image = Image.open("img/Kids_Parents_income correlation_per_school/(5) Selective public.png")
elif f4option == '(6) Selective private': image = Image.open("img/Kids_Parents_income correlation_per_school/(6) Selective private.png")
elif f4option == '(7) Nonselective four-year public': image = Image.open("img/Kids_Parents_income correlation_per_school/(7) Nonselective four-year public.png")
elif f4option == '(8) Nonselective four-year private not for profit': image = Image.open("img/Kids_Parents_income correlation_per_school/(8)Nonselective four-year private not-for-profit.png")
elif f4option == '(9) Two-year (public and private not for profit)': image = Image.open("img/Kids_Parents_income correlation_per_school/(9) Two-year (public and private not-for-profit).png")
elif f4option == '(10) Four-year for profit': image = Image.open("img/Kids_Parents_income correlation_per_school/(10)Four-year for-profit.png")
elif f4option == '(11) Two-year for profit': image = Image.open("img/Kids_Parents_income correlation_per_school/(11)Two-year for-profit par mean and k median .png")
elif f4option == '(12) Less than two-year schools of any type': image = Image.open("img/Kids_Parents_income correlation_per_school/(12) Less than two-year schools of any type.png")
elif f4option == '(13) Attending college with unsufficient data': image = Image.open("img/Kids_Parents_income correlation_per_school/(13)Attending college with unsufficient data.png")
elif f4option == '(14) Late attender (23-28)': image = Image.open("img/Kids_Parents_income correlation_per_school/(14) Late attender (23-28).png")
elif f4option == '(15) Never attended college (before 2013)': image = Image.open("img/Kids_Parents_income correlation_per_school/(15) Never attender college (before 2013).png")


st.image(image, caption="Relationship between Partents Mean Income and Kids Income")

"""
Almost always a non zero correlation. 

But lets dig a bit further into the numbers. 

## Figure 5: Colleges with Unsufficient Data   
"""
image = Image.open("img/(1) College with unsufficient data.png")
st.image(image, caption="Colleges with Unsufficient Data Percentile")
"""
There seems to be a weak positive relationship between the parents and kids’ income mean. This is strongly influenced by 
the presence of outliers. Indeed, a possible explanation would be that the kids whose parents went to Ivy League schools,
tend to earn a significantly higher salary than the kids whose parents are in the same earning's percentile.

## Figure 6: Income Correlation between Kids and Parents income illustrating Kids in the Top 10 Percentile    
"""
image = Image.open("img/(2) Income correlation between kids and parents income illustrating kids top 10 percentile.png")
st.image(image, caption="Income Correlation between Kids and Parents income illustrating Kids in the Top 10 Percentile")

"""
Here we highlight the presence of outliers among kids with high income whose parents earn the least. We further reduced 
the impact of outliers by using the median measure instead of the mean.


## Figure 7: Kids Average income by Parent's School Tier 
"""
image = Image.open("img/(3) Kids average income per parent tier schools.png")
st.image(image, caption="Kids Average income by Parent's School Tier")

"""
There is an apparent link between kids’ financial situation and parents' education. This is well captured by the gap 
between the two highest earnings group whose parent went to elite schools and Ivy leagues school and two least earnings 
group whose parents never attended college or were late attenders. 


## Conclusion
Today we learned a lot about income gaps and the path to education inequality which in turn further increases the income
inequality. This negative feedback loop is a serious problem and threat to the democratic values of America's educational
institutions and a potential cause for large population disapproval and distrust.

We strongly suggest a revision to the academic admissions system. Our website is for university admission officers, 
deans and policy makers in the education domain to understand the impact of cross generational wealth on access to 
higher education. We show clearly that wealth is a factor and hope that more equitable action gets taken to allow for 
the disadvantaged to have equal opportunities and higher mobility between economic strata. 

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