#Data_clear
import pandas as pd
import re

main_path = 'Homework2/'
df0 = pd.read_csv(main_path + 'python_course_py4econ/5_Visualization/data/2404.csv')
df1 = pd.read_csv(main_path + 'python_course_py4econ/5_Visualization/data/2405.csv')
df2 = pd.read_csv(main_path + 'python_course_py4econ/5_Visualization/data/2408.csv')
df3 = pd.read_csv(main_path + 'python_course_py4econ/5_Visualization/data/2409.csv')
df4 = pd.read_csv(main_path + 'python_course_py4econ/5_Visualization/data/2410.csv')

#Bosoogoor negtgeh
df = pd.concat([df0, df1, df2, df3, df4])

df.columns


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

df.isna().sum()
df.isna().sum().sum()

#Duplicated
df.duplicated().sum()

df[df.duplicated()]

df.duplicated(subset=['Date', 'time', 'ad_id'])
duplicated_rows = df[df.duplicated(subset=['Date', 'time', 'ad_id'], keep=False)]
duplicated_rows['ad_id'].value_counts()
duplicated_rows[duplicated_rows['ad_id'] == 8526587]

none_duplicate = duplicated_rows.drop_duplicates(subset=['Date', 'time', 'ad_id'], keep='first')

none_duplicate[none_duplicate['ad_id'] == 8526587]

#Une bolon talbain utgiig toon utga ruu shiljvvleh

df[['Price_Total', 'size']].dtypes

df['new_size'] = df['size'].apply(lambda x: re.findall(r'\d+[\.\d]*', x)[0]).astype(float)
df[['new_size', 'size']]

df[['Price_Total']]

def extract_numeric(value):
    numeric_part = re.findall(r'\d+[\.\d]*', value)
    return float(numeric_part[0]) if numeric_part else None
df['new_Price_Total'] = df['Price_Total'].apply(extract_numeric)
df['new_Price_Total']

df[['new_Price_Total', 'new_size']].dtypes
df[['new_Price_Total', 'Price_Total']]

df[['price_m2']]


