import os
import pandas as pd 
from pydub import AudioSegment
from gtts import gTTS 

def textToSpeech(text,filename):       #It will make a mp3 file from the given text
    mytext = str(text)
    language = "hi"
    myobj = gTTS(text = mytext,lang = language,slow = False)
    myobj.save(filename)


def mergeAudios(audios):             # It will return pydub audio segments
    combined = AudioSegment.empty()
    for audio in audios:
        combined+=AudioSegment.from_mp3(audio)
    return combined

def generateSkeleton():
    #1Generate Kripya Dhyan Dijiye
    audio = AudioSegment.from_mp3('/home/sparsh/Desktop/Railway System/railway.mp3')
    start = 88000
    finish = 90200
    audioProcessed = audio[start:finish]
    audioProcessed.export('/home/sparsh/Desktop/Railway System/file1.mp3',format="mp3")

    #2Generate from City
   

    #3 se Chalkar
    start = 91000
    finish = 92200
    audioProcessed = audio[start:finish]
    audioProcessed.export('/home/sparsh/Desktop/Railway System/file3.mp3',format="mp3")
    
    #4 via city
    

    #5 Ke raste
    start = 94000
    finish = 95000
    audioProcessed = audio[start:finish]
    audioProcessed.export('/home/sparsh/Desktop/Railway System/file5.mp3',format="mp3")

    #6 city ko jane wali
   


    #7city ko jaane wali gadi sankhya
    start = 96000
    finish = 98900
    audioProcessed = audio[start:finish]
    audioProcessed.export('/home/sparsh/Desktop/Railway System/file7.mp3',format="mp3")

    #8 train number and name
    

    #9 kuch hi samay mei platform sankhya
    start = 105500
    finish = 108200
    audioProcessed = audio[start:finish]
    audioProcessed.export('/home/sparsh/Desktop/Railway System/file9.mp3',format="mp3")

    #10 generate platform number
    

    #11 pe aa rahi hai
    start = 109000
    finish = 112250
    audioProcessed = audio[start:finish]
    audioProcessed.export('/home/sparsh/Desktop/Railway System/file11.mp3',format="mp3")




def generateAnnouncement(filename):
    df = pd.read_excel(filename)
   # print(df)
    for index,item in df.iterrows():          #function of pandas
        #Generate from City
        textToSpeech(item['from'],'/home/sparsh/Desktop/Railway System/file2.mp3')

        #Generate via City
        textToSpeech(item['via'],'/home/sparsh/Desktop/Railway System/file4.mp3')

        #Generate to City
        textToSpeech(item['to'],'/home/sparsh/Desktop/Railway System/file6.mp3')

        #generate train number and train name
        textToSpeech(item['train_no']+ " "+ item['train_name'],'/home/sparsh/Desktop/Railway System/file8.mp3')

        #generate platform number
        textToSpeech(item['platform'],'/home/sparsh/Desktop/Railway System/file10.mp3')

        audios = [f"/home/sparsh/Desktop/Railway System/file{i}.mp3" for i in range(1,12)]

        announcement= mergeAudios(audios)
        announcement.export(f'/home/sparsh/Desktop/Railway System/announcement_{index+1}.mp3',format = "mp3")


if __name__ == "__main__":
    print("Generating Skeleton...")
    generateSkeleton()
    print("Now generating Announcement...")
    generateAnnouncement("/home/sparsh/Desktop/Railway System/announce_hindi.xlsx")



