import random
import os
import sys
os.system("clear")
try:
        readme=open("DATA/list.txt","r")
except IOError:
        print "*** MISSING PROGRAM FILES    ******* "
        print "\n"
        print " Please include files necessary for this game."
        print " If you had copied this from someone else, ( author :shyam :) ) include file named \"list.txt\" and place it inside \"DATA\" folder in pwd"
        print "\n"
        print "*************************************** "
        sys.exit()
clueFlag=0
if len(sys.argv) > 1:
        clueFlag=1

deathCount=5
fileLines=[]
dash=[]
guessWordList=[]


for lines in readme:
        fileLines.append(lines)
randNameIndex=random.randint(0,len(fileLines))

guessWord=fileLines[randNameIndex].strip()

for letters in guessWord:
        dash.append("_")

print "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
print "<<<<<<<<<<<<<<<<                                                     <<<<<<<<<<<<<<<<<<"
print "<<<<<<<<<<<<<<<<                \"THE GAME BEGINS\"                  >>>>>>>>>>>>>>>>>>"
print "<<<<<<<<<<<<<<<<                                                     <<<<<<<<<<<<<<<<<<"
print "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
print "<<<<<<<<<<<<<<<<                                                             <<<<<<<<<<"
print "<<<<<<<<<<<<<<<<         This is a game of \"Hangman\",                        >>>>>>>>>>"
print "<<<<<<<<<<<<<<<<       Mission to guess the given word.                      >>>>>>>>>>"
print "<<<<<<<<<<<<<<<< Each wrong guess moves you one step closer to being hanged. >>>>>>>>>>"
print "<<<<<<<<<<<<<<<                                                              <<<<<<<<<<"
print "<<<<<<<<<<<<<<<  !!!  You have only 5 LIVES to guess, GOOD LUCK !!!          <<<<<<<<<<"
print "<<<<<<<<<<<<<<<                                                              <<<<<<<<<<"
print "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
print "\n"
print "\n"
print "*******    GUESS THE COUNTRY/STATE/CITY NAME *******"
print "\n"
print "         "+' '.join(dash)
print "\n"
for l in guessWord:
        guessWordList.append(l);
if clueFlag:
        print guessWord

while(deathCount > 0 ):
        if dash.count("_") == 0:
                os.system("clear")
                print "\n"
                print "\n"
                print "\n"
                print "\n"
                print "\n"
                print "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
                print "<<<<<<<<<<<<<<<<<<<<<<                                     <<<<<<<<<<<<<<<<<<<<<<<<<<<<"
                print "<<<<<<<<<<<<<<<<<<<<<<          CONGRATULATIONS, WINNER    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
                print "<<<<<<<<<<<<<<<<<<<<<<                                     <<<<<<<<<<<<<<<<<<<<<<<<<<<<"
                print "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
                print "\n"
                print "                  YOU RIGHTLY GUESSED    :   \"  " + guessWord    + "  \""
                print "\n"
                print "\n"
                print "\n"
                print "\n"
                print "                         HAVE A GOOD DAY !, Bye   "
                print "\n"
                break
        letter=raw_input("Enter your choice [ a-z ] : ")
#       print "YOU ENTERED "  + letter
        index=0
        if letter in guessWord:
                iter=-1;
                for ll in guessWordList:
                        iter=int(iter)+1
                        if ll == letter:
                                dash[iter]=letter
                os.system("clear")
                print "\n"
                print "         ******************* GOOD  GUESSS ****** "
                print "                 YOU ARE ALIVE STILL........."
                print "\n"
                print "         "+' '.join(dash)
                print "\n"
                continue
        else:
                deathCount=deathCount-1
                print "\n"
                print "\n"
                print "\n"
                if deathCount != 0:
                        os.system("clear")
                        print "*************************************************************************"
                        print "ONE STEP CLOSER TO DEATH ......... you have " + str(deathCount) + " MORE LIVES , GUESS AGAIN !!!"
                        print "\n"
                        print "         "+' '.join(dash)
                        print "\n"
                        continue
                else:
                        os.system("clear")
                        print "         ************************** "
                        print "                 YOU LOSER !!!!!!   "
                        print "         ***************************"
                        print "         IT WAS SIMPLE TO GUESS :D " + guessWord
                        print "         ========================="
                        print "\n"
                        break

readme.close();
