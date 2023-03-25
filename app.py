import streamlit as st  # Con il comando streamlit run app.py crea un server front end




import pandas as pd


st.text('Prova testo')

age = st.slider('How old are you?', 0, 130, 2)

age1 = st.slider('How old are you??', 0, 130, 3)



number = st.number_input('Insert a number',0)

d1={'a':[age,age1,number]}


chart_data = pd.DataFrame(d1)  

st.area_chart(chart_data)






progress_text = "Operation in progress. Please wait."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):

    if percent_complete < 99:
        time.sleep(0.1)
        my_bar.progress(percent_complete + 1, text=progress_text)
    else :
        my_bar.progress(percent_complete + 1, text='Complete')
        
df = pd.read_csv('company_sales_data.csv')

df = df[['month_number', 'facecream', 'facewash', 'toothpaste', 'bathingsoap',
       'shampoo', 'moisturizer']]




chart_data1 = pd.DataFrame(df)   
 
st.line_chart(chart_data1)


