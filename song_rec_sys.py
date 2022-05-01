import pandas as pd
from random import *
import webbrowser
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


df=pd.read_csv('song_data.csv')

#to sort the dataset
# df["rank"]="0"
# df.to_csv("song_data.csv",index=False)
# sdf=df.sort_values(by=['energy'],ascending=False)
# sdf.to_csv('song_data.csv',index=False)

# sdf['rank']=sdf.groupby('rank').cumcount()+1
# sdf.to_csv('song_data.csv',index=False)

att=pd.read_csv('song_data.csv',usecols=(3,4,6,8,9,10,11,12,13,14))
tar=pd.read_csv('song_data.csv',usecols=['rank'])


#checking there are no empty/null values
#print(df.isnull().sum())

def genre(s):
    df_g=df.loc[df['genre']==s]
    if len(df_g)>5:
        print("\nHere are some songs of ",s," genre: ")
        for i in range(5):
            print(i+1,".",df_g.iloc[i]['name']," by ",df_g.iloc[i]['artists'])
    elif len(df_g)<=5 and len(df_g)>0:
        for i in range(len(df_g)):
            print(i+1,".",df_g.iloc[i]['name'], " by ", df_g.iloc[i]['artists'])
    else:
        print("There is no genre like that :( ")

def similar(s):
    try:
        df_n=df.loc[df['name'] == s]
        assert len(df_n) != 0
    except:
        print("\nThere is no such song :(")
    else:
        pf=PolynomialFeatures()
        a=pf.fit_transform(att)
        lr=LinearRegression()
        b=lr.fit(a, tar)

        pred=b.predict(pf.fit_transform([[df_n.iloc[0]['danceability'], df_n.iloc[0]['energy'], df_n.iloc[0]['loudness'],  df_n.iloc[0]['speechiness'], df_n.iloc[0]['acousticness'],  df_n.iloc[0]['instrumentalness'],  df_n.iloc[0]['liveness'],  df_n.iloc[0]['valence'],  df_n.iloc[0]['tempo'],df_n.iloc[0]['duration_ms']]]))
        n = round(pred[0][0])

        if n>100:
            pred_name=df.loc[df['rank'] == 100]
        else:
            pred_name=df.loc[df['rank'] == n]
        print("\n----------------")
        print("\nHere's a similar song for you: ",
        pred_name.iloc[0]['name'], " by ", pred_name.iloc[0]['artists'])
    
    

def certain(s):
    try:
        df_art=df.loc[df['artists']==s]
        assert len(df_art)!=0
    except:
        print("\nThere is no such artist :(")
    else:
        print("Here are songs by ", s, ": \n")
        for i in range(len(df_art)):
            print(i+1,".", df_art.iloc[i]['name'])

def random():
    rn=randint(0,len(df)-1)
    rsamp=df.iloc[rn]
    print("Here's a song for you: '",rsamp['name'],"' by ",rsamp['artists'])

def redirect(s):
    try:
        df_name=df.loc[df['name']==s]
        assert len(df_name)!=0
    except:
        print("\nThere is no such song :(")
    else:
        url=df_name.iloc[0]['y_link'];
        webbrowser.open(url)

#menu-driven interface
while True: 
    print("----------------------------------------------")
    print("\nSONG RECOMMENDATION SYSTEM\n")
    print("Choose any of the following options:\n\n")
    print("1. Which kind of song do you want to listen today? (Genre)\n")
    print("2. Do you want to listen to a similar song?\n")
    print("3. Do you want songs of a certain artist?\n")
    print("4. Random song\n")
    print("5. Do you want to listen to a song in YouTube?\n")
    print("6. Exit\n\n")
    ch=int(input("Enter choice: "))

    if ch==1:
        print("\n\n------SONG BASED ON GENRE-----\n")
        s=input("Enter genre: ")
        genre(s)
        cont = input("\nDo you want to continue?(yes/no): ")
        if cont == "no":
            break
    elif ch==2:
        print("\n\n---------SIMILAR SONG--------\n")
        s=input("Enter song: ")
        similar(s)
        cont = input("\nDo you want to continue?(yes/no): ")
        if cont == "no":
            break
    elif ch==3:
        print("\n\n--------SONGS OF CERTAIN ARTIST------------\n")
        s=input("Enter artist: ")
        certain(s)
        cont = input("\nDo you want to continue?(yes/no): ")
        if cont == "no":
            break
    elif ch==4:
        print("\n\n-------RANDOM SONG-------\n")
        random()
        cont=input("\nDo you want to continue?(yes/no): ")
        if cont=="no":
            break
    elif ch==5:
        print("\n\n-------REDIRECT TO YOUTUBE-------\n")
        s=input("Enter song you want to listen in YouTube: ")
        redirect(s)
        cont = input("\nDo you want to continue?(yes/no): ")
        if cont == "no":
            break
    elif ch==6:
        print("Exited Program")
        break
    else:
        cont=input("Wrong option :( Try again?(yes/no): ")
        if cont=="no":
            break