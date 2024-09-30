
import random
import pandas as pd
counter=[]


def separate_by_langocod(data):
    cpp_list=[]
    p_list=[]
    for i in range(50):
        dat = [data[0][i], data[1][i], data[2][i]]
        if data[2][i]=='C++':
            cpp_list.append(dat)
        elif data[2][i]=='P':
            p_list.append(dat)

    seperated_data=[cpp_list,p_list]
    return seperated_data
def sortbyrating(data):
    return sorted(data.copy(), key=lambda x: x[1])  # x[1] refers to the rating element
def sortbyscore(data):
    return sorted(data,key=lambda x:x[6][0],reverse=True)
def tiebraker(scoreboard_data):

    for i in range(len(scoreboard_data)-1):
        for j in range(len(scoreboard_data)-i-1):
            if(scoreboard_data[j][6][0]==scoreboard_data[j+1][6][0]):
                if(scoreboard_data[j][5][0]<scoreboard_data[j+1][5][0]):
                    temp=scoreboard_data[j]
                    scoreboard_data[j]=scoreboard_data[j+1]
                    scoreboard_data[j+1]=temp
                elif(scoreboard_data[j][5][0]==scoreboard_data[j+1][5][0]):
                    if(scoreboard_data[j][3][0]>scoreboard_data[j+1][3][0]):
                        temp = scoreboard_data[j]
                        scoreboard_data[j] = scoreboard_data[j+1]
                        scoreboard_data[j+1] = temp
                    else:
                        continue
    return scoreboard_data


def pair():
    Team1=[]
    Team2=[]
    paired=[]
    global data_sortl
    global counter1
    global score

    result=[]
    for i in range(len(data_sortl)):
        if len(data_sortl[i]) == 1:
            Team1.append(data_sortl[i][0][0])
            Team2.append("None")
            result.append("Bye")
            data_sortl[i][0][3][0] += 1
            data_sortl[i][0][4].append("Bye")
        else:
            for j in range(len(data_sortl[i])-1):


                    for q in range(j+1,len(data_sortl[i])):

                        data_sortl[i][j] = list(data_sortl[i][j])
                        data_sortl[i][q] = list(data_sortl[i][q])
                        if data_sortl[i][q][0] not in data_sortl[i][j][4]:
                            if data_sortl[i][q][0] not in paired and data_sortl[i][j][0] not in paired:


                                    Team1.append(data_sortl[i][j][0])
                                    Team2.append(data_sortl[i][q][0])
                                    data_sortl[i][j][4].append(data_sortl[i][q][0])
                                    data_sortl[i][q][4].append(data_sortl[i][j][0])
                                    data_sortl[i][j][5][0]+=data_sortl[i][q][1]
                                    data_sortl[i][q][5][0]+=data_sortl[i][j][1]
                                    time_taken=random.randint(5,10)
                                    data_sortl[i][j][3][0]+=time_taken
                                    data_sortl[i][q][3][0]+=time_taken
                                    paired.append(data_sortl[i][q][0])
                                    paired.append(data_sortl[i][j][0])

                                    diff=data_sortl[i][j][1]-data_sortl[i][q][1]
                                    if diff<=5:
                                        a=random.randint(0,1)
                                        if a==0:
                                            result.append(f"{data_sortl[i][j][0]} Wins")
                                            data_sortl[i][j][1]+=2
                                            data_sortl[i][q][1]-= 2
                                            data_sortl[i][j][6][0]+=1
                                        else:
                                            result.append(f"{data_sortl[i][q][0]} Wins")
                                            data_sortl[i][q][1]+=5
                                            data_sortl[i][j][1]-=5
                                            data_sortl[i][q][6][0]+=1
                                    elif diff<10:
                                        a=random.randint(1,20)
                                        if a<=13:
                                            result.append(f"{data_sortl[i][j][0]} Wins")
                                            data_sortl[i][j][1]+= 2
                                            data_sortl[i][q][1]-= 2
                                            data_sortl[i][j][6][0]+=1
                                        else:
                                            result.append(f"{data_sortl[i][q][0]} Wins")
                                            data_sortl[i][q][1] += 5
                                            data_sortl[i][j][1] -= 5
                                            data_sortl[i][q][6][0]+=1
                                    elif diff>=10:
                                        a=random.randint(1,10)
                                        if a<=9:
                                            result.append(f"{data_sortl[i][j][0]} Wins")
                                            data_sortl[i][j][1]+= 2
                                            data_sortl[i][q][1]-= 2
                                            data_sortl[i][j][6][0]+=1
                                        else:
                                            result.append(f"{data_sortl[i][q][0]} Wins")
                                            data_sortl[i][q][1] += 5
                                            data_sortl[i][j][1] -= 5
                                            data_sortl[i][q][6][0]+=1
                                    break
                            else:
                                continue
                        else:
                                continue

            for m in range(len(data_sortl[i])):
                if data_sortl[i][m][0] in paired:
                    continue
                else:
                    Team1.append(data_sortl[i][m][0])
                    Team2.append("None")
                    result.append("Bye")
                    data_sortl[i][m][6][0]+=1
                    data_sortl[i][m][4].append("Bye")

            paired.clear()

    pairings={
        "Team1":Team1,
        "Team2":Team2,
        "Result":result,


    }

    return pairings


team_names=[]
init_rat=[]
langocod=[]
xcel=pd.read_csv("Data.csv")
team_names=xcel["Team Name"].tolist()
init_rat=xcel["Initial Rting"].tolist()
langocod=xcel["Language of Code"].tolist()


init_data_tab={
    "Team Name":team_names,
    "Initial Ratings":init_rat,
    "Language of Code":langocod
}
init_data_tab1=pd.DataFrame(init_data_tab)
init_data_tab1=init_data_tab1.sort_values(by='Initial Ratings',ascending=False)
data_sortl=[]
scoreboard_data=[]

init_data=[team_names,init_rat,langocod]

df=pd.DataFrame(data=init_data_tab1)
new_index = pd.RangeIndex(1, len(df) + 1)
df = df.set_axis(new_index, axis=0)
print(f"The initial standings are: \n{df}\n")
data_sortl=separate_by_langocod(init_data)

for i in range(len(data_sortl)):
    data_sortl[i]=sortbyrating(data_sortl[i])
    data_sortl[i].reverse()
for i in range(len(data_sortl)):
    for j in range(len(data_sortl[i])):
        data_sortl[i][j]=list(data_sortl[i][j])
        data_sortl[i][j].append([0])
        data_sortl[i][j].append([])
        data_sortl[i][j].append([0])
        data_sortl[i][j].append([0])


for i in range(10):

    pairing=pair()
    for j in range(len(data_sortl)):
        data_sortl[j] = sortbyscore(data_sortl[j])
        data_sortl[j].reverse()
        df1=pd.DataFrame(data=pairing)
    new_index1 = pd.RangeIndex(1, len(df1) + 1)
    df1 =df1.set_axis(new_index1, axis=0)
    print(f"The pairings and results of round {i+1} are \n{df1}")
    for p in range(len(data_sortl)):
        for m in range(len(data_sortl[p])):
            scoreboard_data.append(data_sortl[p][m])
    scoreboard_data = sortbyscore(scoreboard_data)
    scoreboard_data=tiebraker(scoreboard_data)
    print(f"\nThe scoreboard after round {i+1} is: ")
    df2 = pd.DataFrame(scoreboard_data, columns=['Team name', 'Rating','Language of Code','Time Taken','Opponents','RoO','Score'])
    new_index2 = pd.RangeIndex(1, len(df2) + 1)
    df2 = df2.set_axis(new_index2, axis=0)
    print(df2)
    scoreboard_data.clear()
print("\nThe final standings are: ")
print(df2)








