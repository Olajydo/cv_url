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
Lover of basketball; critical thinker. passionate about using data science, creativity, and problem-solving to make a difference in the real world.
I have the ability to use my data skill and zealous actions to provide solutions that foster growth in the business fields in which I have had the privilege to work. However, my abilities are not limited to those fields; I am also a quick learner, personable leader with a growth mindset, a great team player, and a good listener. I am competent and can quickly get along with others, present insights, and communicate with a corporate body or individual using my data science skill.

""")

with open("Olajide.pdf", "rb") as f:
    PDFbyte=f.read()
st.download_button(label="Download CV", data=PDFbyte, file_name="Olajide.pdf", mime="application/octet-stream")    



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
- Using the MT5 API, I pulled the live data for various time intervals to analyze and share insights on how to apply a strategy for better trading success.
- Proper documentation and tracking of sales KPIs for business growth were made possible by data that had been collected, cleansed, and preprocessed.
- utilized Python programming to create Bollinger Bands, support & resistance, and SMA for tactical trading.
- With this approach created from these several indications, automation was set up to be used frequently for better and more precise Trading.

""")


txt2('**BCG, Forage**, Data Science and Advance analytics virtual experience program', 'July, 2022 - September, 2022' )
st.info("""
- I identified and offered the hypothesis framing for turnover customer in my firm unique ideas to help reduce the customer churn rate.
- By analyzing the data, insightful information was that was used to explain to the corporate body through visualization how customers' attitudinal characteristics.
- With the aid of machine learning, I created a model to anticipate customer churn, which helped give the optimal business plan for client retention by giving usable insight. 

""")

txt2('**British Airways**, Data Science and Advance analytics virtual experience program', 'October 2022 - November, 2022')
st.info("""
-  I used web scraping to get customer reviews from British Airways site using the Beautiful Soup Python package.
-  In order to prevent it from affecting the model's findings, I also cleaned up the text in the data that appeared disorganized. Additionally, I used topic modeling to understand and recognize the issue that was commonly addressed on British Airways websites.
-  Conducted sentiment analysis to find and analyze reviews in order to understand how people feel about British Airways
-  I provided a Microsoft PowerPoint presentation to stakeholders that included my model interpretation to assist them in recognizing crucial customer review-related activities.
-  developing a predictive model to comprehend the aspects impacting client purchasing decisions, which was used to provide business intelligence solutions to resolve company problems and provide a positive customer experience.

""")
st.info(""" Projects with API :
- With the use of rapidAPI i pulled data from linkedin to get the list of data analyst jobs available
- also use the Zoopla API to fetch the list of available properties for rent and sales in Oxoford, including the running cost of each property
""")
st.write("""## Education and Certifications""")
txt('**B.Tech**, (Pure and Applied Mathematics), Federal University of Technology, Minna, Niger State,Nigeria.','2015-2022')
txt('**Kaggle** Data science Certifications', ' June, 2022') 
txt('**SkillUP** Data science with Python', 'September, 2022')
txt('**SkillUP** Power BI for Beginners', 'October, 2022')
txt('**SkillUP** Introduction to SQL', 'November 2022')

st.write("""
## Skills and Tool
""") 
txt('**Programming**', "Python" )
txt('**Data processing/wrangling**', '"Sql", "Pandas", NoSql')
txt('**Machine Learning**', "Scikit-learn")
txt('**Power BI**', "Visualization")

st.write("""## Social-Media""")
txt3('**LinkedIn**', "https://www.linkedin.com/in/yusuf-olajide-a59aba238/")
txt3('**GitHub**', "https://github.com/Olajydo")
txt3('**Twitter**', '@loerareup')
txt3('**Phone Number**:', '07045511994')
