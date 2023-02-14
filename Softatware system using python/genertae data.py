import pandas as pd
import numpy as np
import string
import random


df=pd.read_excel("Book1.xlsx")
df=df.drop('Card ID ',axis=1)
df.columns=["National_ID"]

def id_generator(size=12, chars=string.ascii_uppercase + string.digits):
      return ''.join(random.choice(chars) for _ in range(size))

df["Card_ID"]=df["National_ID"].apply(lambda x : id_generator())

def generate_names():
  first_names=('mohammed','Ahmed ','badr',"Elsadiq","Wagdi","Khaled","nour","somia","hoda","eman","rahma","reem","sara","amera","abdulrhman")
  last_names=('nader','Samir','Abdullah',"Amir","yasser","Zaid","Mohsen","Elsadiq","omar","ali")
  return random.choice(first_names)+" "+random.choice(last_names)

df["names"]="a"
df["names"]=df["names"].apply(lambda x:generate_names())

string="Alexandria Aswan Asyut Beheira Beni_Suef Cairo Dakahlia Damietta Faiyum Gharbia Giza Ismailia Kafr_El_Sheikh Luxor Matruh Minya Monufia New_Valley North_Sinai Port_Said Qalyubia Qena Red_Sea Sharqia Sohag South_Sinai Suez "

names_of_govs=list(string.split())
len(names_of_govs)

def govs(names_of_govs5=names_of_govs):
    index=random.randint(0,26)
    return names_of_govs5[index]
df["governorate"]=df["National_ID"].apply(lambda x : govs())

df["balance"]=1
df["balance"]=df["balance"].apply(lambda x : random.randint(100,2000))
df["paid_on raod"]=df["balance"].apply(lambda x : random.randint(100,5000))
df["voiltaion_should_paid"]=df["balance"].apply(lambda x : random.randint(1000,5000))
df["sum_voiltaion_paid"]=df["balance"].apply(lambda x : random.randint(2000,10000))

df.to_csv("data_hack.csv",index=False)



