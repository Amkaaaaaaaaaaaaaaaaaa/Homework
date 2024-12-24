#Data_clear
import pandas as pd

main_path = 'Homework2/'
df0 = pd.read_csv(main_path + 'python_course_py4econ/5_Visualization/data/2404.csv')
df1 = pd.read_csv(main_path + 'python_course_py4econ/5_Visualization/data/2405.csv')
df2 = pd.read_csv(main_path + 'python_course_py4econ/5_Visualization/data/2408.csv')
df3 = pd.read_csv(main_path + 'python_course_py4econ/5_Visualization/data/2409.csv')
df4 = pd.read_csv(main_path + 'python_course_py4econ/5_Visualization/data/2410.csv')

#Bosoogoor negtgeh
df = pd.concat([df0, df1, df2, df3, df4])

df

#Baganii ner uurchlult
df = df.rename(columns={
    'date_ind': 'Date_Ind',
    'title' : 'Titile',
    'price_total' : 'Price_Total',
    'date': 'Date',
    'Утасны дугаар': 'Phone',
    'room_num': 'Room_number',
    'ad_text': 'Ad_Text',
    'Байршил:': 'Bairshil',
    'location:': 'Location'})

#Count NA

na_count = df.isna().sum().sum()

#Duplicated

date_duplicated = df['Date'].duplicated().sum()




