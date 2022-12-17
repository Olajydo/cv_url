import streamlit as st
from PIL import Image
########## header

st.write("""
# Yusuf Olajide
###### Resume
""")
image = Image.open('profile.png')
st.image(image, width=250)

st.markdown('## Summary', unsafe_allow_html = True)
st.info("""
- Experience Data Scientist and affable team leader who picks things up quickly. You can do anything if you have grit and a growing attitude.
- Mathematician and a critical thinker demonstrated in various projects and remote internships with leading tech companies which has given me the opportunity to use my skill to provide business solutions.
- Yusuf Olajide is passionate about having a positive impact on the world.Storytelling through data-driven insights with a focus on the aim.

""")

with open("yusuf_updated_cv.pdf", "rb") as f:
    PDFbyte=f.read()
st.download_button(label="Download CV", data=PDFbyte, file_name="yusuf_updated_cv.pdf", mime="application/octet-stream")    



###################
# custom function for text printing

def txt(a,b):
    col1,col2 = st.columns([4,2])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)

def txt2(a,b):
    col1, col2 = st.columns([2,1])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)
    
def txt3(a,b):
    col1, col2 = st.columns([4,4])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)



#########

###################
st.write("""
## Work and Experiences
""")

txt2('**Loreon Investment**, Intern, Data Science', 'February, 2022 – July, 2022')
st.info("""
- I provided innovative analytical insights in line with business objectives and conduct detailed data analysis on data used across the business units to evaluate business processes and improve business performance tracking
- I identify, communicate, and endeavor to resolve data gaps that impact the fulfillment of the business functional requirements, by identifying, evaluating, and documenting potential data sources in support of project requirements within the assigned departments in the business.
- Collected, cleaned and preprocessed over 500 rows of sales tickets data from 21 betting outlet daily which enabled proper documentation and tracking of sales KPIs for business growth.
- Used Microsoft Excel functions & formulas to report sales activities from 21 betting outlet of the business daily, enabling management allocate resources appropriately which enabled effective distribution of company resources and reduced operation
- Utilized Data Quality Assessment Framework to pre-process data. Examined and gathered 


""")


txt2('**BCG, Forage**, Data Science and Advance analytics virtual experience program', 'July, 2022 - September, 2022' )
st.info("""
- I provided business innovative ideas to help resolve the customer churn rate 
- I identify and provided the hypothesis framing for churn customer
- I explored the dataset to identify useful insight to understand customers attitudinal features through visualization
- With machine learning I made model to predict for churn customers
- Communicate the interpretation of the model and help identify the important features which will help to reduce and identify customer that is liable to churn and measures to take 

""")

txt2('**British Airways**, Data Science and Advance analytics virtual experience program', 'October 2022 - November, 2022')
st.info("""
- I performed some web scraping using the Python library (Beautiful Soup), which allowed me to collect customer reviews from British airline pages.
- I also performed some text cleaning on the data that appeared messy to prevent it from interfering with the model's results. Also, I performed topic modeling in order to comprehend and identify the subject that is frequently discussed on British Airways websites.
- Performed Sentiment analysis to identify and categorize reviews in order to know customers attitude towards British airways
- Presented my model interpretation with a Microsoft PowerPoint presentation available to stakeholders to help them identify important customer review-related actions 
- Built a predictive model with Machine learning to understand factors influencing customer buying behaviors
- Interpreting and presenting my models and analysis to key stakeholders which help to provide actionable insights to business actions

""")
st.info(""" Experience with using Api to fetch data from numerous sites:
- With the use of rapidAPI i pulled data from linkedin to get the list of data analyst jobs available
- also use the Zoopla API to fetch the list of available properties for rent and sales in Oxoford, including the running cost of each property
""")
st.write("""## Education and Certifications""")
txt('**Bachelor of Technology**, (Pure and Applied Mathematics), Federal University of Technology, Minna, Niger State,Nigeria.','2015-2022')
txt('**Kaggle** Data science Certifications', ' June, 2022') 
txt('**SkillUP** Data science with Python', 'September, 2022')
txt('**SkillUP** Power BI for Beginners', 'October, 2022')
txt('**SkillUP** Introduction to SQL', 'November 2022')

st.write("""
## Skills and Tool
""") 
txt('**Programming**', "Python" )
txt('**Data processing/wrangling**', '"Sql", "Pandas"')
txt('**Machine Learning**', "Scikit-learn")
txt('**Power BI**', "Visualization")

st.write("""## Social-Media""")
txt3('**LinkedIn**', "https://www.linkedin.com/in/yusuf-olajide-a59aba238/")
txt3('**GitHub**', "https://github.com/Olajydo")
txt3('**Twitter**', '@loerareup')
txt3('**Phone Number**:', '070744551994')
