from pytube import YouTube
import time
import os

mappa = "Downloads"
isExist = os.path.exists(mappa)
if not isExist:
   os.makedirs(mappa)

open("linkek.txt", 'a+')


dontes=""
print("Ha videókat akarsz letölteni, nyomj 'V'-t, ha zenéket 'Z'-t, majd 'ENTER'-t")
dontes=input(dontes)
if(dontes==''):
    exit()

path="Downloads"
dir = os.listdir(path)
if len(dir) == 0:
    rendben=True
else:
    rendben=False
    

if(not rendben):
    print("Helyezd át a korábbi letöltéseket előbb máshova!")
else:
    print("linkek betöltése...")
    for x in open("linkek.txt","r"):
        #link=input(x)
        yt=YouTube(x)
        print("letöltés:",yt.title,"| hossz:",yt.length,"mp")
        if(dontes=='v' or dontes=='V'):

            best = yt.streams.get_highest_resolution()
            best.download("Downloads")
            print("\t -> sikeresen letöltve")
            time.sleep(2)

        if (dontes=='z' or dontes=='Z'):

            video = yt.streams.filter(only_audio=True).first()
            out_file = video.download("Downloads")
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            print("\t -> sikeresen letöltve")
            time.sleep(2)
    print("a kiválasztott videók / zenék le lettek töltve!")
time.sleep(5)