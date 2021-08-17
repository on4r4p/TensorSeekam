#!/usr/bin/python3 
import warnings
warnings.filterwarnings('ignore',category=FutureWarning) 
import subprocess
import imagehash
import shutil
import signal
import os
import sys
import time
import datetime
import random
import curses
import cv2
import tensorflow as tf
import numpy as np
import warnings
warnings.filterwarnings('ignore',category=FutureWarning)
from dateutil import parser
from collections import Counter
from PIL import Image
from PIL import ExifTags
from glob import glob, iglob
from pathlib import Path
     
def signal_handler(sig, frame):
    try:
        curses.endwin()
    except:
        pass

    print('Exiting..')
    sys.exit(0)

def TotalCounter():
     global TotalFileNbrSaved

     TotalFileNbrSaved = TotalFileNbrSaved + 1
     return


def QuickLoadTotalFiles():
     global TotalFilesNbrSaved
     global TotalGlobalFiles

     if os.path.exists("./Datas/TempSaves/Total.Files.Nbr.saved"):
              with open("./Datas/TempSaves/Total.Files.Nbr.saved") as f:
                    content = f.readlines()
                    content = [x.strip() for x in content]
                    for line in content :
                         if "TotalGlobalFiles" in line:
                            try:
                              TotalGlobalFiles = int(str(line.split("=")[1]))
                            except Exception as e:
                                print("\nTotalGlobalFiles err :",e)
                                print("Will have to count total files number ..\nPlease wait...")
                                TotalGlobalFiles = len(glob(Seek+"*"))

                         if "TotalFilesNbrSaved" in line:
                            try:
                              TotalFilesNbrSaved = int(str(line.split("=")[1]))
                              #print(TotalFilesNbrSaved)
                            except Exception as e:
                                   TotalFilesNbrSaved = TotalGarage + TotalGarage  + TotalLiving + TotalOther + TotalFailed
     else:
          print("\n./Datas/TempSaves/Total.Files.Nbr.saved not found.\nWill have to count total files number..\nPlease wait...")
          TotalGlobalFiles = len(glob(Seek+"*"))
          TotalFilesNbrSaved = TotalGarage + TotalGarage  + TotalLiving + TotalOther + TotalFailed



def Savethistoo(tosave):

          if not os.path.exists(str(TempSaves)):
               os.makedirs(str(TempSaves))
          print("Saving Files to proceed after Substract in  ",str(TempSaves)+"Files_After_Substract.debug\n") 
          with open(str(TempSaves)+"Files_After_Substract.debug","w") as f:
                    for file in tosave:
                         f.write(str(file)+"\n")

def SubstractList():
     global FilesLeft

     print("Substracting Files Already Saved From Files List Left To Proceed.\nPlease Wait...\n")
     FilesLeft = list((Counter(FilenamesLeft)-Counter(FilenamesSaved)).elements())
#     Savethistoo(FilesLeft)
     return

def LoadFilesSaved():
     global FilenamesSaved
     if os.path.exists(str(TempSaves)+"FilesAlready.saved"):
              print("Loading Files Already Saved From ",str(TempSaves)+"FilesAlready.saved\n")
              with open(str(TempSaves)+"FilesAlready.saved") as f:
                    for line in f:
                         FilenamesSaved.append(os.path.basename(line.rstrip()))
              return QuickLoadTotalFiles()
     else:
          print("%s not found."%(str(TempSaves)+"FilesAlready.saved"))
#          sys.exit()
          return AlreadySaved("TensorPart")

def LoadFilesLeft():
     global FilenamesLeft

     if os.path.exists(str(TempSaves)+"FilesLeft.saved"):
              print("Loading Files Left To Proceed from ",str(TempSaves)+"FilesLeft.saved\n")
              with open(str(TempSaves)+"FilesLeft.saved") as f:
                    for line in f:
                         FilenamesLeft.append(os.path.basename(line.rstrip()))
              return SubstractList()
     else:
          print("%s not found."%(str(TempSaves)+"FilesLeft.saved"))
          sys.exit()
def SaveAlreadySavedFiles():

          if not os.path.exists(str(TempSaves)):
               os.makedirs(str(TempSaves))
          print("Saving Files Already Saved in ",str(TempSaves)+"FilesAlready.saved\n") 
          with open(str(TempSaves)+"FilesAlready.saved","w") as f:
                    for file in SavedAlready:
                         f.write(str(file)+"\n")
          return LoadFilesSaved()

def SaveFilesLeft():

          if not os.path.exists(str(TempSaves)):
               os.makedirs(str(TempSaves))
          if not os.path.exists(str(TempSaves)+"FilesLeft.saved"):
               print("Saving Files Left To Proceed in ",str(TempSaves)+"FilesLeft.saved\n") 
               with open(str(TempSaves)+"FilesLeft.saved","w") as f:
                    for file in Path(UnknownCam).glob('*'):
                         f.write(str(file.name)+"\n")
               return LoadFilesLeft()
          else:
               return LoadFilesLeft()


def Log(part,filename):

          if not os.path.exists(str(TempSaves)):
               os.makedirs(str(TempSaves))

          with open(str(TempSaves)+"Total.Files.Nbr.saved","w") as f:
                    f.write("TotalGlobalFiles="+str(TotalGlobalFiles))
                    f.write("\nTotalFilesNbrSaved="+str(TotalFileNbrSaved))
                    f.write("\nTotalGarden="+str(TotalGarden))
                    f.write("\nTotalLiving="+str(TotalLiving))
                    f.write("\nTotalGarage="+str(TotalGarage))
                    f.write("\nTotalPictures="+str(TotalOther))
                    f.write("\nTotalFailed="+str(TotalFailed))
          if part == "sort":
               with open(str(TempSaves)+"LastPic.part1.saved","w") as f:
                    f.write(str(filename))
                    return
          if part == "tensort":
               with open(str(TempSaves)+"LastPic.part2.saved","w") as f:
                    f.write(str(filename))
                    return


def nothing(x):
    pass

def AlreadySaved(mode):
 global SavedAlready
 global TotalGarden
 global TotalLiving
 global TotalGarage
 global TotalOther
 global TotalFailed

 if mode is "TensorPart":
     exclude = ['UnknownCam'] #,'Failed','Other']

     for path in Path(Master).iterdir():

         if path.name not in exclude:
               print("\nLoading all files's names already saved in "+str(path.name))

               if str(path)+"/" == Garage:
                    cntfile = 0
                    for file in Path(path).rglob('*'):
                        cntfile = cntfile + 1
                        SavedAlready.append(file.name)
                        TotalCounter()

                    TotalGarage = cntfile
                    print("\nDone Loading "+str(TotalGarage)+" names from "+str(Garage))
                    print("\nNumber of Filenames Already Saved currently loaded is now :",len(SavedAlready)) 

               elif str(path)+"/" == Living:
                    cntfile = 0
                    for file in Path(path).rglob('*'):
                        cntfile = cntfile + 1
                        SavedAlready.append(file.name)
                        TotalCounter()

                    TotalLiving = cntfile
                    print("\nDone Loading "+str(TotalLiving)+ " names from "+str(Living))
                    print("\nNumber of Filenames Already Saved currently loaded is now :",len(SavedAlready)) 
               elif str(path)+"/" == Garden:
                    cntfile = 0
                    for file in Path(path).rglob('*'):
                        cntfile = cntfile + 1
                        SavedAlready.append(file.name)
                        TotalCounter()

                    TotalGarden = cntfile
                    print("\nDone Loading "+str(TotalGarden)+" names from "+str(Garden))
                    print("\nNumber of Filenames Already Saved currently loaded is now :",len(SavedAlready))

               elif str(path)+"/" == Picture:
                    cntfile = 0
                    for file in Path(path).rglob('*'):
                        cntfile = cntfile + 1
                        TotalCounter()

                    TotalOther = cntfile
                    print("\nDone Loading "+str(TotalOther)+" names from "+str(Picture))
                    print("\nExcluding those files from (alreadysaved) since TensorPart is focusing on IpCamera files")
                    print("\nNumber of Filenames Already Saved currently loaded is now :",len(SavedAlready))

               elif str(path)+"/" == Bogus:
                    cntfile = 0
                    for file in Path(path).rglob('*'):
                        cntfile = cntfile + 1
                        TotalCounter()

                    TotalFailed = cntfile
                    print("\nDone Loading "+str(TotalFailed)+" names from "+str(Bogus))
                    print("\nExcluding those files from (alreadysaved) since TensorPart is focusing on IpCamera files")
                    print("\nNumber of Filenames Already Saved currently loaded is now :",len(SavedAlready))




 if mode is "SeekPart":
     exclude = [] 

     for path in Path(Master).iterdir():
         cntfile = 0
         if path.name not in exclude:
               print("\nLoading all files's names already saved in "+str(path.name))

               for file in Path(path).rglob('*'):
                    cntfile = cntfile + 1
                    TotalCounter()
                    SavedAlready.append(file.name)

               if str(path)+"/" == Garage:
                    TotalGarage = cntfile
                    print("\nDone Loading "+str(TotalGarage)+" names from "+str(Garage))
                    print("\nNumber of Filenames Already Saved currently loaded is now :",len(SavedAlready))
               elif str(path)+"/" == Living:
                    TotalLiving = cntfile
                    print("\nDone Loading "+str(TotalLiving)+ " names from "+str(Living))
                    print("\nNumber of Filenames Already Saved currently loaded is now :",len(SavedAlready))
               elif str(path)+"/" == Garden:
                    TotalGarden = cntfile
                    print("\nDone Loading "+str(TotalGarden)+" names from "+str(Garden))
                    print("\nNumber of Filenames Already Saved currently loaded is now :",len(SavedAlready))
               elif str(path)+"/" == Picture:
                    TotalOther = cntfile
                    print("\nDone Loading "+str(TotalOther)+" names from "+str(Picture))
                    print("\nNumber of Filenames Already Saved currently loaded is now :",len(SavedAlready))
               elif str(path)+"/" == Bogus:
                    TotalFailed = cntfile
                    print("\nDone Loading "+str(TotalFailed)+" names from "+str(Bogus))
                    print("\nNumber of Filenames Already Saved currently loaded is now :",len(SavedAlready))

 QuickLoadTotalFiles()

def FindTimeStamp(Date,masterpath):
          Loop = 0
          DigitMissed = 14 - len(Date)
          tmp= ""
          Year=''.join(Date[0:4])
          Month= ''.join(Date[4:6])
          Day= ''.join(Date[6:8])
          Hour= ''.join(Date[8:10])
          Minute= ''.join(Date[10:12])
          Sec=''.join(Date[12:14])
          format = str(Year+"-"+Month+"-"+Day+" "+Hour+":"+Minute+":"+Sec)
          if int(Year) not in range(2017,2021) :
               if "9" in Year: 
                    padding = Year.index("9")
                    diff = 3 - padding
                    Year = "2019"
                    Date = Date[padding+diff:len(Date)]
                    for i in range(0,len(Year)):
                         if i <= padding+diff:
                              tmp += Year[i]
                    Date = tmp+Date
                    return(FindTimeStamp(Date,masterpath))
               elif "8" in Year: 
                    Year = "2018"
                    diff = 3 - padding
                    Date = Date[padding+diff:len(Date)]
                    for i in range(0,len(Year)):
                         if i <= padding+diff:
                              tmp += Year[i]
                    Date = tmp+Date
                    return(FindTimeStamp(Date,masterpath))
               elif "7" in Year:
                    Year = "2017"  
                    diff = 3 - padding
                    Date = Date[padding+diff:len(Date)]
                    for i in range(0,len(Year)):
                         if i <= padding+diff:
                              tmp += Year[i]
                    Date = tmp+Date
                    return(FindTimeStamp(Date,masterpath))
               else:
                    Year = "2018"
                    Date = Date[4:len(Date)]
                    Date = Year+Date
                    return(FindTimeStamp(Date,masterpath))


          format = str(Year+"-"+Month+"-"+Day+" "+Hour+":"+Minute+":"+Sec) 
          try:
                    dt = parser.parse(format)
                    finalpath = masterpath+str(Year)+"/"+str(Month)+"/"+str(Day)+"/"
                    return finalpath

          except Exception as e:
                    Loop = Loop +1
                    print(e)
                    if "month must be in" in str(e):
                         if int(Month) is 00:
                              Month = "08"
                              Date = Date[0:4] + Month + Date[6:len(Date)]
                              return(FindTimeStamp(Date,masterpath))
                         else:
                              Month = str("%02d" % random.randint(1,12))
                              Date = Date[0:4] + Month + Date[6:len(Date)]
                              return(FindTimeStamp(Date,masterpath))
                    if "day is out of range" in str(e):
                         if Day[0] is "8":
                            Day = "0"+Day[1]
                            Date = Date[0:6] + Day + Date[8:len(Date)]
                            return(FindTimeStamp(Date,masterpath))
                         else:
                              Day = str("%02d" % random.randint(1,29))
                              Date = Date[0:6] + Day + Date[8:len(Date)]
                              return(FindTimeStamp(Date,masterpath))
                    if "hour must be in" in str(e):
                         if Hour[0] is "8":
                              Hour = "0"+Hour[1]
                              Date = Date[0:8] + Hour + Date[10:len(Date)]
                              return(FindTimeStamp(Date,masterpath))
                         else:
                              Hour = str("%02d" % random.randint(0,23))
                              Date = Date[0:8] + Hour + Date[10:len(Date)]
                              return(FindTimeStamp(Date,masterpath))
                    if "minute must be in" in str(e):
                         if Minute[0] is "8":
                              Minute = "0"+Minute[1]
                              Date = Date[0:10] + Minute + Date[12:len(Date)]
                              return(FindTimeStamp(Date,masterpath))
                         else:
                              Minute = str("%02d" % random.randint(0,59))
                              Date = Date[0:8] + Minute + Date[10:len(Date)]
                              return(FindTimeStamp(Date,masterpath))
                    if "second must be in" in str(e):
                         if Sec[0] is "8":
                              Sec = "0"+Sec[1]
                              Date = Date[0:12] + Sec
                              return(FindTimeStamp(Date,masterpath))
                         else:
                              Sec = str("%02d" % random.randint(0,59))
                              Date = Date[0:12] + Sec
                              return(FindTimeStamp(Date,masterpath))


                    if "Unknown string format" in str(e):
                         while len(Date) != 14:
                              Date = Date+"0"
                         return(FindTimeStamp(Date,masterpath))
            

def PostProd(pic):
  OptimalPass1 = 6500
  OptimalPass2= 4000
  OptimalPass3= 3500
  ColgateMaxWhite = 12000

  Hmin = 0
  Smin = 0
  Vmin = 0
  Hmax = 179
  Smax = 255
  Vmax = 255  

  while True:
    timestamp = pic[8:39,823:1280]
    
    hsv = cv2.cvtColor(timestamp, cv2.COLOR_BGR2HSV)
    lower = np.array([Hmin, Smin, Vmin])
    upper = np.array([Hmax, Smax, Vmax])
    mask = cv2.inRange(hsv, lower, upper)
        
    thresh = cv2.bitwise_not(mask)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2,2))
    close = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    blur = cv2.erode(close,kernel,iterations = 1)
    WhitePixel= np.sum(blur == 255)
    BlackPixel= np.sum(blur == 0)
    if WhitePixel < OptimalPass1 and BlackPixel > OptimalPass1:
          Vmin = Vmin + 1
    else:
          break

  Vmin = 0
  firstpass= blur
  Lastpass = False
  while True:
            lower = np.array([Hmin, Smin, Vmin])
            upper = np.array([Hmax, Smax, Vmax])

            mask = cv2.inRange(hsv, lower, upper)
            bit_or = cv2.bitwise_or(mask,firstpass)
            bit_or = cv2.dilate(bit_or,kernel,iterations = 1)
            merge = cv2.addWeighted(blur,0.5,bit_or,0.5,0)
            final = cv2.bitwise_or(merge,mask)
            final = cv2.morphologyEx(final, cv2.MORPH_OPEN, kernel)

            WhitePixel= np.sum(bit_or == 255)
            BlackPixel= np.sum(bit_or == 0)
            if BlackPixel < OptimalPass2 and WhitePixel >= ColgateMaxWhite and Lastpass is False:
               Vmax = Vmax - 1
            else:
                 Lastpass = True

            WhitePixel= np.sum(bit_or == 255)
            BlackPixel= np.sum(bit_or == 0)

            if Lastpass is True and WhitePixel >= ColgateMaxWhite:
               #cv2.waitKey()
               Hmin = Hmin + 1
#               print("Hmin =",Hmin)

            elif Lastpass is True :

                 break
#            cv2.waitKey(10)

  if Lastpass is True:
            allblack = final[:]
            h,b = allblack.shape[:2]    
            for i in range(h):
               for j in range(b):
                    if allblack[i][j] == 128 or allblack[i][j] == 0:
                         allblack[i][j] = 0
                    else:
                         allblack[i][j] = 255

  kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2,2))
  return Hacknslash(allblack)

def Hacknslash(result):
    global LastMask

    left =0
    top =0
    right =24
    bottom = 48

    Date = []
    YOUSHALLPASS = True
    Nbrs = 0
    while Nbrs <= 14:
                Template0 = []
                Template1 = []
                Template2 = []
                Template3 = []
                Template4 = []

                Template5 = []
                Template6 = []
                Template7 = []
                Template8 = []
                Template9 = []
                scrolling = result[top:bottom,left:right]
                if YOUSHALLPASS == True:
                     pixelcnt = 0
                     scrollH = imagehash.average_hash(Image.fromarray(scrolling))
                     Seperator = scrollH - SepH
                     Point = scrollH - PH
                     if Seperator <= 12:
                              Unlock = True
                              YOUSHALLPASS = False
                              pixelcnt = 0
                     elif Point <= 12:
                              Unlock = True
                              YOUSHALLPASS = False
                              pixelcnt = 0
                     else:
                              Unlock = False

                     for hash in zero:
                         Fight = scrollH - hash
                         Template0.append(Fight)
                     for hash in one:
                         Fight = scrollH - hash
                         Template1.append(Fight)
                     for hash in two:
                         Fight = scrollH - hash
                         Template2.append(Fight)
                     for hash in three:
                         Fight = scrollH - hash
                         Template3.append(Fight)
                     for hash in four:
                         Fight = scrollH - hash
                         Template4.append(Fight)
                     for hash in five:
                         Fight = scrollH - hash
                         Template5.append(Fight)
                     for hash in six:
                         Fight = scrollH - hash
                         Template6.append(Fight)
                     for hash in seven:
                         Fight = scrollH - hash
                         Template7.append(Fight)
                     for hash in eight:
                         Fight = scrollH - hash
                         Template8.append(Fight)
                     for hash in nine:
                         Fight = scrollH - hash
                         Template9.append(Fight)

                     Score0 = min(Template0)
                     Score1 = min(Template1)
                     Score2 = min(Template2)
                     Score3 = min(Template3)
                     Score4 = min(Template4)
                     Score5 = min(Template5)
                     Score6 = min(Template6)
                     Score7 = min(Template7)
                     Score8 = min(Template8)
                     Score9 = min(Template9)
                      
                     ScoreList = {str("0"):Score0,str("1"):Score1,str("2"):Score2,str("3"):Score3,str("4"):Score4,str("5"):Score5,str("6"):Score6,str("7"):Score7,str("8"):Score8,str("9"):Score9}
                     BestGuess = min(ScoreList, key=ScoreList.get)
                     Thresh = min(ScoreList.items(), key = lambda item: item[1])[1]

                     if Thresh <= 10:
                              Nbrs= Nbrs + 1
                              Date.append(str(BestGuess))
                              Unlock = True
                              YOUSHALLPASS = False
                else:
                    Unlock= True

                if Unlock is True:
                    checkspace = result[top:bottom,right:right+1]
                    checkhash = imagehash.average_hash(Image.fromarray(checkspace))
                    Fight = checkhash - SpaceH
                    if Fight <= 12:
                         YOUSHALLPASS = False
                    else:
                         pixelcnt = pixelcnt + 1
                         if pixelcnt >= 12:
                              YOUSHALLPASS = True
                         else:
                              pass

                if right < 1280:
                     left = left + 1
                     right = right + 1
                else:
                    return (Date,True)
    LastMask = None
    return (Date,True)

def sort_contours(contours):
    boundingBoxes = [cv2.boundingRect(c) for c in contours]
    (contours, boundingBoxes) = zip(*sorted(zip(contours, boundingBoxes)
       , key=lambda b: b[1][0], reverse=False))
    return contours

   



def SortExif(filename,masterpath):

     Bingo = False
     cmd = "identify -verbose "+filename
     jpgexif=subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
     jpgexif=jpgexif.decode("utf-8",errors='ignore')

     if masterpath is Picture:
          for line in jpgexif.split("\n"):
               if "exif:DateTime:" in line:
                    gettime = line.replace("exif:DateTime:","").replace("-","").replace(" ","")
                    Year = gettime[0:4]
                    Month = gettime[5:7]
                    Bingo = False
                    finalpath = masterpath+str(Year)+"/"+str(Month)+"/"
                    return finalpath
          if Bingo is False:
               for line in jpgexif.split("\n"):
                    if "date:create:" in line:
                         gettime = line.replace("date:create: ","").replace("-","").replace(" ","")
                         gettime = gettime[0:12]
                         Year = gettime[0:4]
                         Month = gettime[4:6]
                         Bingo = True
                         finalpath = masterpath+str(Year)+"/"+str(Month)+"/"
                         return finalpath
          if Bingo is False:
               finalpath = masterpath+"NoExifDate/"
               return finalpath
     else:
          for line in jpgexif.split("\n"):
               if "exif:DateTime:" in line:
                    gettime = line.replace("exif:DateTime:","").replace("-","").replace(" ","")
                    gettime = gettime[0:12]
                    Year = gettime[0:4]
                    Month = gettime[5:7]
                    Day = gettime[8:10]
                    Bingo = True
                    finalpath = masterpath+str(Year)+"/"+str(Month)+"/"+str(Day)+"/"
                    return finalpath
          if Bingo is False:
               for line in jpgexif.split("\n"):
                    if "date:create:" in line:
                         gettime = line.replace("date:create: ","").replace("-","").replace(" ","")
                         gettime = gettime[0:12]
                         print(gettime)
                         Year = gettime[0:4]
                         Month = gettime[4:6]
                         Day = gettime[6:8]
                         Bingo = True
                         finalpath = masterpath+str(Year)+"/"+str(Month)+"/"+str(Day)+"/"
                         return finalpath
          if Bingo is False:
               finalpath = masterpath+"NoExifDate/"
               return finalpath




def Move(filename,id,bonusdbg):

     global TotalCams
     global TotalGarden
     global TotalLiving
     global TotalGarage
     global TotalOther
     global TotalFailed

     TotalCounter()

     if TensorPart is False:
        TotalJoined = str(TotalFileNbrSaved)+" / "+ str(TotalGlobalFiles)
        TotalGlobalFilesAdjusted = TotalGlobalFiles
     else:
        TotalGlobalFilesAdjusted = TotalGlobalFiles-TotalOther-TotalFailed
        TotalJoined = str(TotalFileNbrSaved-TotalOther-TotalFailed)+" / "+ str(TotalGlobalFilesAdjusted)

     stdscr = curses.initscr()
     stdscr.timeout(1)
     stdscr.scrollok(1)
     stdscr.clrtoeol()
     stdscr.refresh()
     curses.noecho()
     curses.cbreak()

#     print("\n\n=======Moving Pictures to their respective folders=======\n\n")


     if id == UnknownCam:
          stdscr.clrtoeol()
          stdscr.addstr(0, 0,"Moving file:{0}".format(filename))
          stdscr.clrtoeol()
          stdscr.addstr(1, 0,"Camera Generated file detected.".format())
          stdscr.clrtoeol()
          stdscr.addstr(2, 0,"BonusDbg:{0}".format(bonusdbg))
          stdscr.clrtoeol()
          if not os.path.exists(str(UnknownCam)):
               os.makedirs(str(UnknownCam))
          shutil.copy(filename,UnknownCam)
          stdscr.addstr(3, 0,"Moved to folder:{0}".format(UnknownCam))
          stdscr.clrtoeol()
          stdscr.addstr(4, 0,"Total Files Numbers Saved: {0}".format(TotalJoined))
          stdscr.clrtoeol()
          stdscr.addstr(5, 0,"Total progress: [{1:100}] {0}%".format(round(TotalFileNbrSaved/TotalGlobalFilesAdjusted*100), "#" * round(TotalFileNbrSaved/TotalGlobalFilesAdjusted*100)))
          stdscr.refresh()
          ignore = stdscr.getch()

          TotalCams= TotalCams + 1 
     if id == Garden:
          stdscr.clrtoeol()
          stdscr.addstr(0, 0,"Moving file:{0}".format(filename))
          stdscr.clrtoeol()
          stdscr.addstr(1, 0,"Motion Garden Generated file detected.".format())
          stdscr.clrtoeol()
          stdscr.addstr(2, 0,"BonusDbg:{0}".format(bonusdbg))
          stdscr.clrtoeol()
          finalpath = SortExif(filename,Garden)          
          if not os.path.exists(str(finalpath)):
               os.makedirs(str(finalpath))
          shutil.copy(filename,str(finalpath))
          stdscr.addstr(3, 0,"Moved to folder:{0}".format(finalpath))
          stdscr.clrtoeol()
          stdscr.addstr(4, 0,"Total Files Numbers Saved:{0}".format(TotalJoined))
          stdscr.clrtoeol()
          stdscr.addstr(5, 0,"Total progress: [{1:100}] {0}%".format(round(TotalFileNbrSaved/TotalGlobalFilesAdjusted*100), "#" * round(TotalFileNbrSaved/TotalGlobalFilesAdjusted*100)))
          stdscr.refresh()
          ignore = stdscr.getch()

          TotalGarden = TotalGarden + 1
     if id == Living:
          stdscr.clrtoeol()
          stdscr.addstr(0, 0,"Moving file:{0}".format(filename))
          stdscr.clrtoeol()
          stdscr.addstr(1, 0,"Motion Living Generated file detected.".format())
          stdscr.clrtoeol()
          stdscr.addstr(2, 0,"BonusDbg:{0}".format(bonusdbg))
          stdscr.clrtoeol()
          finalpath = SortExif(filename,Living)          
          if not os.path.exists(str(finalpath)):
               os.makedirs(str(finalpath))
          shutil.copy(filename,str(finalpath))
          stdscr.addstr(3, 0,"Moved to folder:{0}".format(finalpath))
          stdscr.clrtoeol()
          stdscr.addstr(4, 0,"Total Files Numbers Saved:{0}".format(TotalJoined))
          stdscr.clrtoeol()
          stdscr.addstr(5, 0,"Total progress: [{1:100}] {0}%".format(round(TotalFileNbrSaved/TotalGlobalFilesAdjusted*100), "#" * round(TotalFileNbrSaved/TotalGlobalFilesAdjusted*100)))
          stdscr.refresh()
          ignore = stdscr.getch()
          TotalLiving = TotalLiving +1
     if id == Garage:
          stdscr.clrtoeol()
          stdscr.addstr(0, 0,"Moving file:{0}".format(filename))
          stdscr.clrtoeol()
          stdscr.addstr(1, 0,"Ipcam Generated file detected.".format())
          stdscr.clrtoeol()
          stdscr.addstr(2, 0,"BonusDbg:{0}".format(bonusdbg))
          stdscr.clrtoeol()
          loaded = cv2.imread(filename)
          result,Go = PostProd(loaded)
          while Go is False:
            result,Go = PostProd(loaded)

          finalpath=FindTimeStamp(result,Garage)

          if not os.path.exists(str(finalpath)):
               os.makedirs(str(finalpath))

          shutil.copy(filename,str(finalpath))
###
          stdscr.addstr(3, 0,"Moved to folder:{0}".format(finalpath))
          stdscr.clrtoeol()
          stdscr.addstr(4, 0,"Total Files Numbers Saved:{0}".format(TotalJoined))
          stdscr.clrtoeol()
          stdscr.addstr(5, 0,"Total progress: [{1:100}] {0}%".format(round(TotalFileNbrSaved/TotalGlobalFilesAdjusted*100), "#" * round(TotalFileNbrSaved/TotalGlobalFilesAdjusted*100)))
          stdscr.clrtoeol()
          stdscr.refresh()
          ignore = stdscr.getch()
          TotalGarage = TotalGarage +1
     if id == Picture:
          stdscr.clrtoeol()
          stdscr.addstr(0, 0,"Moving file:{0}".format(filename))
          stdscr.clrtoeol()
          stdscr.addstr(1, 0,"Other Generated file detected.".format())
          stdscr.clrtoeol()
          stdscr.addstr(2, 0,"BonusDbg:{0}".format(bonusdbg))
          stdscr.clrtoeol()
          finalpath = SortExif(filename,Picture)          
          if not os.path.exists(str(finalpath)):
               os.makedirs(str(finalpath))
          shutil.copy(filename,str(finalpath))
          stdscr.addstr(3, 0,"Moved to folder:{0}".format(finalpath))
          stdscr.clrtoeol()
          stdscr.addstr(4, 0,"Total Files Numbers Saved:{0}".format(TotalJoined))
          stdscr.clrtoeol()
          stdscr.addstr(5, 0,"Total progress: [{1:100}] {0}%".format(round(TotalFileNbrSaved/TotalGlobalFilesAdjusted*100), "#" * round(TotalFileNbrSaved/TotalGlobalFilesAdjusted*100)))
          stdscr.refresh()
          ignore = stdscr.getch()
          TotalOther = TotalOther +1
     if id == Bogus:
          stdscr.clrtoeol()
          stdscr.addstr(0, 0,"Moving file:{0}".format(filename))
          stdscr.clrtoeol()
          stdscr.addstr(1, 0,"Failed to identify this file.".format())
          stdscr.clrtoeol()
          stdscr.addstr(2, 0,"BonusDbg:{0}".format(bonusdbg))
          finalpath = SortExif(filename,Bogus)          
          if not os.path.exists(str(finalpath)):
               os.makedirs(str(finalpath))
          shutil.copy(filename,str(finalpath))
          stdscr.clrtoeol()
          stdscr.addstr(3, 0,"Moved to folder:{0}".format(finalpath))
          stdscr.clrtoeol()
          stdscr.addstr(4, 0,"Total Files Numbers Saved:{0}".format(TotalJoined))
          stdscr.clrtoeol()
          stdscr.addstr(5, 0,"Total progress: [{1:100}] {0}%".format(round(TotalFileNbrSaved/TotalGlobalFilesAdjusted*100), "#" * round(TotalFileNbrSaved/TotalGlobalFilesAdjusted*100)))
          stdscr.refresh()
          ignore = stdscr.getch()
          TotalFailed = TotalFailed + 1
     print()
     return



def Question(mode):


  if mode == "Train":

    print("\n---- Warning!! ---- \nNo trained files have been found .\n I need them to tell the difference between Ipcamera files \nthat can't be done just be looking at the exifs tags. \nSo in order to do it i must trained Templates pictures and give them a label (the folder's name containing those pics.)\nPut one or more folders containing pictures that you want to identify here: ./Datas/Templates/")


    SkipPartOne = input("If your Templates folders are ready now just say it...\n(yes to train/NO! to skip Tensorflow part) : ").lower().strip()
    print()
    while not(SkipPartOne == "y" or SkipPartOne == "yes" or SkipPartOne == "no!"):
              SkipPartOne = input("If you want to train your Templates folders now just say it...\n(yes to train/no to skip Tensorflow part) : ").lower().strip()
    print()

    if "no!" in SkipPartOne:

            return False
    elif "y" in SkipPartOne:
            return True




  if mode == "Session1":


        SkipPartOne = input("\n---- Warning!! ---- \nFound a previous Session interrupted before the Tensorflow part...\n(y to resume/n to starting over again) : ").lower().strip()
        print()
        while not(SkipPartOne == "y" or SkipPartOne == "yes" or SkipPartOne == "no!"):
              SkipPartOne = input("Found a previous Session interrupted before the Tensorflow part...\n(y to resume/NO! to starting over again) : ").lower().strip()
        print()

        if "no!" in SkipPartOne:

            return False
        elif "y" in SkipPartOne:
            AlreadySaved("SeekPart")
            return True

  if mode == "Session2":


        SkipPartOne = input("\n---- Warning!! ---- \nFound a previous Session interrupted during the Tensorflow part...\n(y to resume/NO! to starting over again) : ").lower().strip()
        print()
        while not(SkipPartOne == "y" or SkipPartOne == "yes" or SkipPartOne == "no!"):
              SkipPartOne = input("Found a previous Session interrupted during the Tensorflow part...\n(y to resume/NO! to starting over again) : ").lower().strip()
        print()

        if "no!" in SkipPartOne:

            return False
        elif "y" in SkipPartOne:
            AlreadySaved("TensorPart")
            return True

  if mode == "delete":



            Deletefolder = input("The programe has finished all its tasks.\nDo you want to deleted this session?\nAnswering yes will delete ./Datas/UnknownCam/ (it is a temporary folder) it will also delete all the checkpoints.files .\n(YES!/n): ").lower().strip()
            print()
            while not(Deletefolder == "yes!" or Deletefolder == "n" or Deletefolder == "no"):
                  Deletefolder = input("The programe has finished all its tasks.\nDo you want to deleted this session?\nAnswering yes will delete ./Datas/UnknownCam/ (it is a temporary folder) it will also delete all the checkpoints.files .\n(YES!/n): ").lower().strip()
                  print()
            if "n" in Deletefolder:
                print("\nOk keeping everything.")
                print("\nExiting now...\n")
                sys.exit(0)
            elif "yes!" in Deletefolder:

                print("\nFine\nDeleting previous checkpoints and ./Datas/UnknownCam/ folder.\n")
                try:
                    shutil.rmtree(UnknownCam)
                except:
                    pass
                try:
                    os.remove("./Datas/TempSaves/LastPic.part1.saved")
                except:
                    pass
                try:
                    os.remove("./Datas/TempSaves/LastPic.part2.saved")
                except:
                    pass
                print("\nExiting now...\n")
                sys.exit(0)



#@timecall
def Whicham(directory):
    global LastPic2
    

    print("\nLoading Pretrained files...\n")
    
    label_lines = [line.rstrip() for line in tf.gfile.GFile("Datas/TempSaves/trained_labels.txt")]

    with tf.gfile.FastGFile("Datas/TempSaves/trained_graph.pb", 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')
    with tf.Session() as sess:
       softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
       

       if LastPic2:
            print("Starting from last session ...\n")
            time.sleep(1)

       for pict in directory:
               try:
                    pict = str(UnknownCam+pict)
                    image_data = tf.gfile.FastGFile(pict, 'rb').read()
                    predictions = sess.run(softmax_tensor, \
                          {'DecodeJpeg/contents:0': image_data})
                    top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
                    for node_id in top_k:
                          human_string = label_lines[node_id]
                          if "living" in human_string:
                               Move(pict,Living,"Living 100%")
                               Log("tensort",pict)
                               break
                          else:
                               Move(pict,Garden,"Garden 100%")
                               Log("tensort",pict)
                               break

               except Exception as e:
                         print("Error(Whicham):",e)
                         pass

def Seekam(jpg):


     FoundMotion = False
     FoundGarage = False
     cmd = "identify -verbose "+jpg
     try:
          jpgexif=subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
          jpgexif=jpgexif.decode("utf-8",errors='ignore')
     except Exception as e:
          curses.endwin()
          print('\nError seekam:',e)
          return

     for exif in MotionExif:
          if str(exif) in str(jpgexif) and not str(exif) in str(BadExif):
               FoundMotion = True
          else:
               if str(exif) == "Quality: 42":
                      if "Quality: 50" in str(jpgexif):
                         FoundMotion = True
               else:
                    FoundMotion = False
                    break
     if FoundMotion == False:

          for exif in GarageExif:
               if str(exif) in str(jpgexif) and not str(exif) in str(BadExif):
                    FoundGarage = True
               else:
                    FoundGarage =  False
                    break

     if FoundGarage == True:
          Move(jpg,Garage,"IpcamFile")
          return
     if FoundGarage == False and FoundMotion == False:
          Move(jpg,Picture,"OtherFile")
          return
     if FoundMotion == True:          
          Move(jpg,UnknownCam,"CameraFile")
          return




def SaveTemplates():
        global Trained
        
        if os.path.exists("./Datas/TempSaves/trained_labels.txt") and os.path.exists("./Datas/TempSaves/trained_graph.pb"):
             print("Pretrained files found..\n")
             Trained = True
        else:

            training = Question("Train")
            if training is True:

                print("Let's beging training..This could take some time..\npython3 train.py \
                      --bottleneck_dir=./Datas/TempSaves/bottlenecks \
                      --how_many_training_steps=2000 \
                      --model_dir=./inception \
                      --summaries_dir=./Datas/TempSaves/training_summaries/basic \
                      --output_graph=./Datas/TempSaves/trained_graph.pb \
                      --output_labels=./Datas/TempSaves/trained_labels.txt \
                      --image_dir=./Datas/Templates")


                os.system("python3 train.py \
      --bottleneck_dir=./Datas/TempSaves/bottlenecks \
      --how_many_training_steps=2000 \
      --model_dir=./inception \
      --summaries_dir=./Datas/TempSaves/training_summaries/basic \
      --output_graph=./Datas/TempSaves/trained_graph.pb \
      --output_labels=./Datas/TempSaves/trained_labels.txt \
      --image_dir=./Datas/Templates")
                Trained = True
            else:
                Trained = False


def LastSession():
        global LastPic
        global LastPic2
        global SKIP1
        global TensorPart


        if not os.path.exists(Master):
                
                try:
                    os.remove("./Datas/TempSaves/LastPic.part1.saved")
                except:
                    pass
                try:
                    os.remove("./Datas/TempSaves/LastPic.part2.saved")
                except:
                    pass
                return






        if os.path.exists("./Datas/TempSaves/LastPic.part1.saved"):
              with open("./Datas/TempSaves/LastPic.part1.saved") as f:
                    content = f.readlines()
                    try:
                        content = str(content[0])
                    
                           
                        if not "ALLDONE" in content:
                              print("Last picture processed during Part 1:",content)
                              answer=Question("Session1")
                              if answer is True:

                                  LastPic = content
                        else:
                               SKIP1 = True
                    except Exception as e:
                        print("lastpic1 err :",e)
                        pass                    

        if os.path.exists("./Datas/TempSaves/LastPic.part2.saved"):
              with open("./Datas/TempSaves/LastPic.part2.saved") as f:
                    content = f.readlines()
                    try:
                        content = str(content[0])
                        if not "ALLDONE" in content:
                              print("Last picture processed during Part 2:",content)
                              answer=Question("Session2")
                              if answer is True:
                                  LastPic2 = content
                                  TensorPart = True
                        else:
                               Question("delete")
                    except Exception as e:
                        print("lastpic2 err :",e)
                        pass 



#################
###### Main #####
#################

def main():
    global SavedAlready
    global LastPic
    global TotalGlobalFiles
    global TotalFileNbrSaved
    global ToMoveFile
    global ToMoveId
    global ToMoveBonus
    global TotalGarage
    global TotalOther
    global TotalCams
    global TotalGarden
    global TotalLiving
    global TotalFailed


    SaveTemplates()
    LastSession()
    
    if SKIP1 is False:
   
            print("\nSeekam files in:",Seek)
            if LastPic:
                print("Proceeding from last session Part1 ...\n")
                time.sleep(1)

            for camfile in SeekList:
                if not LastPic:
                   try:
                      Seekam(camfile)
                      Log("sort",camfile)
                   except Exception as e:
                      curses.endwin()
                      print(e)
                      Move(camfile,Bogus,"Failed 100% ")               
                      TotalFailed = TotalFailed + 1
                if LastPic:
                    if not camfile.name in SavedAlready:
                       try:
                         Seekam(camfile)
                         Log("sort",camfile)
                       except Exception as e:
                          curses.endwin()
                          Move(camfile,Bogus,"Failed 100%")
                          print(e)                      
                          TotalFailed = TotalFailed + 1
            try:
               curses.endwin()
            except Exception as e:
               print(e)

            Log("sort","ALLDONE")
            LastPic = None

            print("\nEnd of Sorting Part 1 ... \n\n")
            print("The story so far :\n")
            print("Found " +str(TotalGarage) +" Identified as from Garage Security Cam.")
            print("Found " +str(TotalOther) +" Identified Random Pictures .")
            print("Found " +str(TotalCams) +" Identified as Security Camera but NOT Sorted yet .")
            print("Found " +str(TotalFailed) +" Failed to be identified.")

            if TotalCams == 0:
                print("\nHaven't found any other Security Cam files to Sort.\n")
                print("\nExiting...")
                sys.exit(0)
            
            if Trained is True:

                print("\n\nNow Attempting to sort Security Cam Files....\n\n")
                TotalCams = 0
                TotalGarden = 0
                TotalLiving = 0
                TotalFailed = 0
##
                if os.path.exists(str(UnknownCam)):

                         SavedAlready = []
                         SaveFilesLeft()
                         Whicham(FilesLeft)
                else:
                    print("\n Cannot find : ",str(UnknownCam))
                    sys.exit()
                try:
                     curses.endwin()
                except:
                         pass

                Log("tensort","ALLDONE")

                print("\n\nAll Done ! \n\n")


                print("The story so far :\n")
                print("Found " +str(TotalLiving) +" Identified as from Living Security Cam.")
                print("Found " +str(TotalGarden) +" Identified as from Garden Security Cam.")
                print("Found " +str(TotalGarage) +" Identified as from Garage Security Cam.")
                print("Found " +str(TotalOther) +" Identified as Pictures.")
                print("Found " +str(TotalFailed) +" Failed to be identified.")

                Question("delete")
                sys.exit(0)

            elif Trained is False:

                 print("No trained files have been found .\n I need them to tell the difference between Ipcamera files \nthat can't be done just be looking at the exifs tags. \nSo in order to do it i must trained Templates pictures and give them a label (the folder's name containing those pics.)\nCant sort Security Cam Files already found\nThose files are saved here :",str(UnknownCam))
                 print("Put one or more folders containing pictures that you want to identify here: ./Datas/Templates/ \nThen launch :\npython3 train.py \
                      --bottleneck_dir=./Datas/TempSaves/bottlenecks \
                      --how_many_training_steps=2000 \
                      --model_dir=./inception \
                      --summaries_dir=./Datas/TempSaves/training_summaries/basic \
                      --output_graph=./Datas/TempSaves/trained_graph.pb \
                      --output_labels=./Datas/TempSaves/trained_labels.txt \
                      --image_dir=./Datas/Templates")
                 print("\nExiting...")
                 sys.exit(0)


####If Skip Part 1 is true ###
    else:

#            NotSavedCnt = 0
#            SavedCnt = 0
           
            Log("sort","ALLDONE")

            print("\nSkipping Part 1 ... \n\n")
            print("\n\nNow Attempting to sort Security Cam Files....\n\n")

            if Trained is True:
                if os.path.exists(str(UnknownCam)):
                         #if not LastPic and not LastPic2:
                         #    SavedAlready = []
                         #    TotalCams = 0
                         #    TotalGarden = 0
                         #    TotalLiving = 0
                         #    TotalFailed = 0

                         SaveAlreadySavedFiles()
                         SaveFilesLeft()
                         ReadyOrNot=input("\nReady to proceed...\nPress Enter to begin.")
                         Whicham(FilesLeft)
                else:
                    print("\n Cannot find : ",str(UnknownCam))
                    sys.exit()
                try:
                     curses.endwin()
                except:
                         pass



                print("\n\nAll Done ! \n\n")

                print("The story so far :\n")
                print("Found " +str(TotalLiving) +" Identified as from Living Security Cam.")
                print("Found " +str(TotalGarden) +" Identified as from Garden Security Cam.")
                print("Found " +str(TotalFailed) +" Failed to be identified.")

                if TotalLiving+TotalGarden+TotalFailed > 0:
                    if TotalFileNbrSaved == TotalGlobalFiles:
                        Log("tensort","ALLDONE")
                        Question("delete")
                    else:
                        print("\n Error Total file saved not equal to initial Total files")
                        print("Total files saved :",TotalFileNbrSaved)
                        print("Total Global Files:",TotalGlobalFiles)
                        print("Anyway im done ..\nLater !")

                sys.exit(0)

            elif Trained is False:
                 print("No trained files have been found .\n I need them to tell the difference between Ipcamera files \nthat can't be done just be looking at the exifs tags. \nSo in order to do it i must trained Templates pictures and give them a label (the folder's name containing those pics.)\nCant sort Security Cam Files already found\nThose files are saved here :",str(UnknownCam))
                 print("Put one or more folders containing pictures that you want to identify here: ./Datas/Templates/ \nThen launch :\npython3 train.py \
                      --bottleneck_dir=./Datas/TempSaves/bottlenecks \
                      --how_many_training_steps=2000 \
                      --model_dir=./inception \
                      --summaries_dir=./Datas/TempSaves/training_summaries/basic \
                      --output_graph=./Datas/TempSaves/trained_graph.pb \
                      --output_labels=./Datas/TempSaves/trained_labels.txt \
                      --image_dir=./Datas/Templates")
                 print("\nExiting...")
                 sys.exit(0)


#####
#####

###
###
if __name__ == '__main__':

#    sys.setrecursionlimit(2323)
    sys.setrecursionlimit(999)
    signal.signal(signal.SIGINT, signal_handler)



    print("""
  _______                        _____           _                   
 |__   __|                      / ____|         | |                  
    | | ___ _ __  ___  ___  _ _| (___   ___  ___| | ____ _ _ __ ___  
    | |/ _ \ '_ \/ __|/ _ \| '__\___ \ / _ \/ _ \ |/ / _` | '_ ` _ \ 
    | |  __/ | | \__ \ (_) | |  ____) |  __/  __/   < (_| | | | | | |
    |_|\___|_| |_|___/\___/|_| |_____/ \___|\___|_|\_\__,_|_| |_| |_|
                                                                     
     \nLoading Please Wait ... """)
    

    SavedAlready = []
    FilesLeft = []
    FilenamesSaved = []
    FilenamesLeft = []

    Seek = input("Directory path full of jpg:")

    if not Seek.endswith("/"):
         Seek = Seek+"/"
    SeekList = iglob(Seek+"*")

    SeekList = Path(Seek).glob('*')

    Master = input("Output Directory:")
    Bogus = str(Master)+"/Failed/"
    UnknownCam = str(Master)+"/UnknownCam/"
    Garage = str(Master)+"/SavedGaragecam/"
    Living = str(Master)+"/SavedLivingcam/"
    Garden = str(Master)+"/SavedGardencam/"
    Picture = str(Master)+"/Other/"


    Templates= "./Datas/Templates/"
    TempSaves="./Datas/TempSaves/"

    


    MotionExif=["Geometry: 640x480+0+0","Pixels: 307200","Compression: JPEG","Quality: 42","Units: Undefined","Orientation: Undefined","exif:ExifOffset: 50","Profile-exif: 146 bytes","jpeg:colorspace: 2"]
    GarageExif=["Geometry: 1280x720+0+0","Pixels: 921600","Compression: JPEG","Quality: 80","Orientation: Undefined","Units: Undefined","jpeg:colorspace: 2"]
    BadExif=["Resolution:","Print size:","exif:ColorSpace:","exif:DateTimeDigitized:","exif:ExposureBiasValue:","exif:ExposureMode:","exif:ExposureTime:","exif:FocalLength:","exif:ImageDescription:","exif:Make:","exif:Model:","exif:Orientation:","exif:Software:","exif:thumbnail:","Profile-app"]



    TmpListGrdn = glob("./Datas/Templates/Garden/*")
    TmpListLiv = glob("./Datas/Templates/Living/*")
    TmpListLivNew = glob("./Datas/Templates/Livingnew/*")

    TmpLivgNbr = len(glob("./Datas/Templates/Living/*"))
    TmpLivgNewNbr = len(glob("./Datas/Templates/Livingnew/*"))
    TmpGrdnNbr = len(glob("./Datas/Templates/Garden/*"))

####
#    TotalGlobalFiles = len(glob(Seek+"*")) ## TO MANY FUCKING FILES
####
    
    TotalGlobalFiles = 0
    TotalFileNbrSaved = 0
####
#    QueueList = []

    TemplatesLoaded = False
    UserLoaded = False
    Trained = False

    TensorPart = False
    SKIP1 = False
    LastPic = None
    LastPic2 = None  


    TotalCams = 0
    TotalGarden = 0
    TotalLiving = 0
    TotalGarage = 0
    TotalOther = 0
    TotalFailed = 0

    ###Main##
    zero = []
    one = []
    two = []
    three = []
    four = []
    five = []
    six = []
    seven = []
    eight = []
    nine = []
    ##loading template hashs
    SpaceH = imagehash.average_hash(Image.open("./Datas/TempSaves/space.png"))
    SepH = imagehash.average_hash(Image.open("./Datas/TempSaves/seperator.jpeg"))
    PH = imagehash.average_hash(Image.open("./Datas/TempSaves/point.jpeg"))

    LastMask = None

    Digitsdir0 =glob("./Datas/DigitsTemplates/0/*")
    Digitsdir1 =glob("./Datas/DigitsTemplates/1/*")
    Digitsdir2 =glob("./Datas/DigitsTemplates/2/*")
    Digitsdir3 =glob("./Datas/DigitsTemplates/3/*")
    Digitsdir4 =glob("./Datas/DigitsTemplates/4/*")
    Digitsdir5 =glob("./Datas/DigitsTemplates/5/*")
    Digitsdir6 =glob("./Datas/DigitsTemplates/6/*")
    Digitsdir7 =glob("./Datas/DigitsTemplates/7/*")
    Digitsdir8 =glob("./Datas/DigitsTemplates/8/*")
    Digitsdir9 =glob("./Datas/DigitsTemplates/9/*")

    for digit in Digitsdir0:
         num = cv2.imread(digit,0)
         zero.append(imagehash.average_hash(Image.fromarray(num)))

    for digit in Digitsdir1:
         num = cv2.imread(digit,0)
         one.append(imagehash.average_hash(Image.fromarray(num)))
    for digit in Digitsdir2:
         num = cv2.imread(digit,0)
         two.append(imagehash.average_hash(Image.fromarray(num)))
    for digit in Digitsdir3:
         num = cv2.imread(digit,0)
         three.append(imagehash.average_hash(Image.fromarray(num)))
    for digit in Digitsdir4:
         num = cv2.imread(digit,0)
         four.append(imagehash.average_hash(Image.fromarray(num)))
    for digit in Digitsdir5:
         num = cv2.imread(digit,0)
         five.append(imagehash.average_hash(Image.fromarray(num)))
    for digit in Digitsdir6:
         num = cv2.imread(digit,0)
         six.append(imagehash.average_hash(Image.fromarray(num)))
    for digit in Digitsdir7:
         num = cv2.imread(digit,0)
         seven.append(imagehash.average_hash(Image.fromarray(num)))
    for digit in Digitsdir8:
         num = cv2.imread(digit,0)
         eight.append(imagehash.average_hash(Image.fromarray(num)))
    for digit in Digitsdir9:
         num = cv2.imread(digit,0)
         nine.append(imagehash.average_hash(Image.fromarray(num)))


    main()

####



















