#Borna Houmani
#Black to White Video Game
#11/03/14
#Lets the user play BLACK TO WHITE word game (also has animation


import random,time,os


#ANIMATION STARTS
#Sets up list of letters to be used for randomizing animation start
randomchar='''qwertyuiopasdfghjklzxcvbnm'''


#Outputs random letters with box growing around them as they appear
perline=0
print('\n'*4+'\t┌'+'─'*81+'┐\n\t│',end='')
for i in range(79*13):
    print(random.choice(randomchar),flush=open,end='')
    time.sleep(.00099)
    perline+=1
    if perline>80:
        print('│\n\t│',end='')
        perline=0
for i in "Borna Houmani Presentsxbjf":
    print(i,flush=open,end='')
    perline=0
    time.sleep(.00099)
print('│\n\t│',end='')
for i in range(80*9):
    print(random.choice(randomchar),flush=open,end='')
    time.sleep(.00099)
    perline+=1
    if perline>80:
        print('│\n\t│',end='')
        perline=0
for i in ('kjfudmadk│\n\t└'+'─'*81+'┘'):
    print(i,end='',flush=open)
    time.sleep(.00099)
time.sleep(1.5)


#Random letters are removed to reveal the hidden words 'Borna Houmani Presents'
os.system("CLS")
print('\n'*4+'\t┌'+'─'*81+'┐'+('\n\t│'+' '*81+'│')+('\n\t│'+' '*81+'│')*11+('\n\t│'+' '*55+"Borna Houmani Presents    "+'│')+('\n\t│'+' '*81+'│')*9+'\n\t└'+'─'*81+'┘',flush=open)
time.sleep(2)
os.system("CLS")
#Still within the box, the previous message is removed and now it says 'A New Borleans Production' in a different place
print('\n'*4+'\t┌'+'─'*81+'┐'+('\n\t│'+' '*81+'│')+('\n\t│'+' '*81+'│')*4+('\n\t│'+' '*5+"A New Borleans Production"+' '*51+'│')+('\n\t│'+' '*81+'│')+('\n\t│'+' '*81+'│')*15+'\n\t└'+'─'*81+'┘',flush=open)
time.sleep(2)
os.system("CLS")
#At the bottom of the box, previous message is removed and now it says 'Black to White'
print('\n'*4+'\t┌'+'─'*81+'┐'+('\n\t│'+' '*81+'│')+('\n\t│'+' '*81+'│')*20+('\n\t│'+' '*33+"Black to White"+' '*34+'│')+'\n\t└'+'─'*81+'┘',flush=open)
time.sleep(1.5)


#Box moves up until the text is at the top of the screen. Bottom of box turns into loading bar shaped like a battery
for newline in range(13):
    print('\n',flush=open)
    time.sleep(.1)
os.system("CLS")
print('\n\t '+' '*33+"Black to White\n"+('\t┌'+'─'*81+'┐')+('\n\t│'+' '*81+'╠')+'\n\t└'+'─'*81+'┘',flush=open)


#Sets up lists with the individual lines of 'Black' in ascii art to use later
fullBlack=['''\t              888888b.   888             d8888  .d8888b.  888    d8P              ''','''\t              888  "88b  888            d88888 d88P  Y88b 888   d8P               ''','''\t              888  .88P  888           d88P888 888    888 888  d8P                ''','''\t              8888888K.  888          d88P 888 888        888d88K                 ''','''\t              888  "Y88b 888         d88P  888 888        8888888b                ''','''\t              888    888 888        d88P   888 888    888 888  Y88b               ''','''\t              888   d88P 888       d8888888888 Y88b  d88P 888   Y88b              ''','''\t              8888888P"  88888888 d88P     888  "Y8888P"  888    Y88b             ''']
otherBlack=['''\t              888888b.   888             d8888  .d8888b.  888    d8P             ''','''''','''\t              888  .88P  888           d88P888 888    888 888  d8P               ''','''''','''\t              888  "Y88b 888         d88P  888 888        8888888b               ''','''''','''\t              888   d88P 888       d8888888888 Y88b  d88P 888   Y88b             ''','''''']
print()

#Prints every other line in the 'Black' ascii art and progresses loading bar
for i in range(1,10):
    os.system("CLS")
    print('\n\t '+' '*33+"Black to White\n"+('\t┌'+'─'*81+'┐')+('\n\t│'+'//'*i+' '*(80-(i*2))+' '+'╠')+'\n\t└'+'─'*81+'┘\n',flush=open)
    print('\n'.join(otherBlack[:i-1]),flush=open)
    time.sleep(.2)
#Goes back and fills in the missing lines and progresses loading bar
for j in range(1,10):
    os.system("CLS")
    print('\n\t '+' '*33+"Black to White\n"+('\t┌'+'─'*81+'┐')+('\n\t│'+'/'*18+'//'*j+' '*(63-(j*2))+'╠')+'\n\t└'+'─'*81+'┘\n',flush=open)
    print('\n'.join(fullBlack[0:j]),flush=open)
    print('\n'.join(otherBlack[j:]),flush=open)
    time.sleep(.1)
os.system("CLS")
print('\n\t '+' '*33+"Black to White\n"+('\t┌'+'─'*81+'┐')+('\n\t│'+'/'*36+' '*45+'╠')+'\n\t└'+'─'*81+'┘\n',flush=open)
print('\n'.join(fullBlack))


#Prints the word 'BLACK' in ascii art and changes the letters one at a time to the word 'WHITE'. progresses loading bar through it
time.sleep(1)
os.system("CLS")
print('\n\t '+' '*33+"Black to White\n"+('\t┌'+'─'*81+'┐')+('\n\t│'+'/'*40+' '*41+'╠')+'\n\t└'+'─'*81+'┘',flush=open)
print('''\n\t\t       .d8888b.  888             d8888  .d8888b.  888    d8P\n\t\t      d88P  Y88b 888            d88888 d88P  Y88b 888   d8P\n\t\t      Y88b.      888           d88P888 888    888 888  d8P    \n\t\t       "Y888b.   888          d88P 888 888        888d88K     \n\t\t          "Y88b. 888         d88P  888 888        8888888b    \n\t\t            "888 888        d88P   888 888    888 888  Y88b   \n\t\t      Y88b  d88P 888       d8888888888 Y88b  d88P 888   Y88b  \n\t\t       "Y8888P"  88888888 d88P     888  "Y8888P"  888    Y88b''')
time.sleep(.4)
os.system("CLS")
print('\n\t '+' '*33+"Black to White\n"+('\t┌'+'─'*81+'┐')+('\n\t│'+'/'*45+' '*36+'╠')+'\n\t└'+'─'*81+'┘',flush=open)
print('''\n\t\t       .d8888b. 88888888888     d8888  .d8888b.  888    d8P  \n\t\t      d88P  Y88b    888        d88888 d88P  Y88b 888   d8P   \n\t\t      Y88b.         888       d88P888 888    888 888  d8P    \n\t\t       "Y888b.      888      d88P 888 888        888d88K     \n\t\t          "Y88b.    888     d88P  888 888        8888888b    \n\t\t            "888    888    d88P   888 888    888 888  Y88b   \n\t\t      Y88b  d88P    888   d8888888888 Y88b  d88P 888   Y88b  \n\t\t       "Y8888P"     888  d88P     888  "Y8888P"  888    Y88b ''')
time.sleep(.4)
os.system("CLS")
print('\n\t '+' '*33+"Black to White\n"+('\t┌'+'─'*81+'┐')+('\n\t│'+'/'*51+' '*30+'╠')+'\n\t└'+'─'*81+'┘',flush=open)
print('''\n\t\t       .d8888b. 88888888888     d8888 888      888    d8P  \n\t\t      d88P  Y88b    888        d88888 888      888   d8P   \n\t\t      Y88b.         888       d88P888 888      888  d8P    \n\t\t       "Y888b.      888      d88P 888 888      888d88K     \n\t\t          "Y88b.    888     d88P  888 888      8888888b    \n\t\t            "888    888    d88P   888 888      888  Y88b   \n\t\t      Y88b  d88P    888   d8888888888 888      888   Y88b  \n\t\t       "Y8888P"     888  d88P     888 88888888 888    Y88b''')
time.sleep(.4)
os.system("CLS")
print('\n\t '+' '*33+"Black to White\n"+('\t┌'+'─'*81+'┐')+('\n\t│'+'/'*57+' '*24+'╠')+'\n\t└'+'─'*81+'┘',flush=open)
print('''\n\t\t       .d8888b. 88888888888     d8888 888      8888888888 \n\t\t      d88P  Y88b    888        d88888 888      888        \n\t\t      Y88b.         888       d88P888 888      888        \n\t\t       "Y888b.      888      d88P 888 888      8888888    \n\t\t          "Y88b.    888     d88P  888 888      888        \n\t\t            "888    888    d88P   888 888      888        \n\t\t      Y88b  d88P    888   d8888888888 888      888        \n\t\t       "Y8888P"     888  d88P     888 88888888 8888888888''')
time.sleep(.4)
os.system("CLS")
print('\n\t '+' '*33+"Black to White\n"+('\t┌'+'─'*81+'┐')+('\n\t│'+'/'*63+' '*18+'╠')+'\n\t└'+'─'*81+'┘',flush=open)
print('''\n\t\t       .d8888b.  888    888        d8888 888      8888888888 \n\t\t      d88P  Y88b 888    888       d88888 888      888        \n\t\t      Y88b.      888    888      d88P888 888      888        \n\t\t       "Y888b.   8888888888     d88P 888 888      8888888    \n\t\t          "Y88b. 888    888    d88P  888 888      888        \n\t\t            "888 888    888   d88P   888 888      888        \n\t\t      Y88b  d88P 888    888  d8888888888 888      888        \n\t\t       "Y8888P"  888    888 d88P     888 88888888 8888888888 ''')
time.sleep(.4)
os.system("CLS")
print('\n\t '+' '*33+"Black to White\n"+('\t┌'+'─'*81+'┐')+('\n\t│'+'/'*69+' '*12+'╠')+'\n\t└'+'─'*81+'┘',flush=open)
print('''\n\t\t      88       88 888    888        d8888 888      8888888888 \n\t\t      88   o   88 888    888       d88888 888      888        \n\t\t      88  d8b  88 888    888      d88P888 888      888        \n\t\t      88 d888b 88 8888888888     d88P 888 888      8888888    \n\t\t      88d88888b88 888    888    d88P  888 888      888        \n\t\t      8888P Y8888 888    888   d88P   888 888      888        \n\t\t      888P   Y888 888    888  d8888888888 888      888        \n\t\t      88P     Y88 888    888 d88P     888 88888888 8888888888''')
time.sleep(.4)
os.system("CLS")
print('\n\t '+' '*33+"Black to White\n"+('\t┌'+'─'*81+'┐')+('\n\t│'+'/'*75+' '*6+'╠')+'\n\t└'+'─'*81+'┘',flush=open)
print('''\n\t\t      88       88 888    888 8888888 888      8888888888 \n\t\t      88   o   88 888    888   888   888      888        \n\t\t      88  d8b  88 888    888   888   888      888        \n\t\t      88 d888b 88 8888888888   888   888      8888888    \n\t\t      88d88888b88 888    888   888   888      888        \n\t\t      8888P Y8888 888    888   888   888      888        \n\t\t      888P   Y888 888    888   888   888      888        \n\t\t      88P     Y88 888    888 8888888 88888888 8888888888 ''')
time.sleep(1)
os.system("CLS")
print('\n\t '+' '*33+"Black to White\n"+('\t┌'+'─'*81+'┐')+('\n\t│'+'/'*81+'╠')+'\n\t└'+'─'*81+'┘',flush=open)
print('''\n\t\t      88       88 888    888 8888888 88888888888 8888888888 \n\t\t      88   o   88 888    888   888       888     888        \n\t\t      88  d8b  88 888    888   888       888     888        \n\t\t      88 d888b 88 8888888888   888       888     8888888    \n\t\t      88d88888b88 888    888   888       888     888        \n\t\t      8888P Y8888 888    888   888       888     888        \n\t\t      888P   Y888 888    888   888       888     888        \n\t\t      88P     Y88 888    888 8888888     888     8888888888 ''')
#Tells the user to input something to begin. After that, clears the screen and begins
input('\n\n%38sPRESS ENTER TO BEGIN! '%(' '))
os.system("CLS")


#ACTUAL GAME STARTS
#Gives list 'loadingBar' values to be used for random timing later on
loadingBar=[.1,.2,.3,.4,.5,.6,.7,.8,]


#Sets up the dictionary with words in all caps
dictRead=open("dictionary.txt","r")
dictionary=dictRead.readlines()
for dictionaryIndex in range(len(dictionary)):
    dictionary[dictionaryIndex]=(dictionary[dictionaryIndex].rstrip("\n")).upper()


#Sets up the word combonations for different difficulties
difficultyFour=['MILK PAIL','WELL DONE','MICE RATS','CAMP SITE']
difficultyFive=['INK PEN','OIL GAS','FISH BIRD','FIRE HEAT','HAND FOOT','WHEAT BREAD']
difficultySix=['FOUR FIVE','DEAD LIVE','TEARS SMILE','GREEN BROWN','SLEEP DREAM','SNACK MEALS','NORTH SOUTH']
difficultySeven=['ELM OAK','ONE TWO','BREAD TOAST','FLESH BLOOD']
difficultyEight=['FLUTE CELLO','LINEN SHEET','BLACK WHITE','FRESH STALE','SHARP BLUNT']


#Sets up various lists and conditions to use in the leaderboard
leaderboardPoints=[]
leaderboardMode=[]
leaderboardName=[]
leaderboardWords=[]
leaderboardCheat=[]
cheat=False


#Sets up while loops to be used when restarting or ending the game
endGame=False
keepPlaying=True
while endGame==False:
    while keepPlaying==True:


        #Prints title, intro, options for player
        print('''\t\t\t╔═════════╗\n\t\t\t Main Menu\n\t\t\t╚═════════╝\n\nWelcome to "Black to White"!\nThe goal is to turn the word "Black" to the word "White" one letter at a time. Simple as that!\nThe following are your menu options:\n\n\t1. Quick Game\n\t2. Multiplayer\n\t3. Leaderboard\n\t4. Add To Dictionary\n\t--------------------\n\t5. Exit The Game''')
        #Asks the player to pick from any of the options
        menuSelection=input("\nInput the corresponding numbers for any of these options to play or to get a description. ")
        #Bulletproofs selection
        while menuSelection not in ['1','2','3','4','5']:
            menuSelection=input("\nSorry, we didn't recognize that input. Try again. ")
        #Clears the screen
        os.system("CLS")


        #If they chose the first option (Quick Game):
        if menuSelection=='1':
            #Prints title
            print("\t\t\t╔══════════╗\n\t\t\t Quick Game\n\t\t\t╚══════════╝\n")
            #Gives users a description of the option and asks them if they would like to continue
            quickGamecontinue=input('''Don't have any friends? This is the game mode for you!\nPlay the basic, single player version of "Black to White" by changing one letter at a time!\n\nDo you wish to continue? [Y/N]. ''').upper()           
            #Bulletproofs continuation inputs
            while quickGamecontinue=='' or quickGamecontinue[0] not in ['Y','N']:
                quickGamecontinue=input("\nSorry, that isn't a valid input. Try again by typing Yes or No. ").upper()
            #Clears the screen
            os.system("CLS")


            #If they don't want to continue:
            if quickGamecontinue[0]=='N':
                #Runs through loading bar animation
                for i in range(1,9):
                    print('''\t\t\t╔══════════╗\n\t\t\t Quick Game\n\t\t\t╚══════════╝\n\nDon't have any friends? This is the game mode for you!\nPlay the basic, single player version of "Black to White" by changing one letter at a time!\nDo you wish to continue? [Y/N]. \n\n\t\tSending you back to the menu.\n''')
                    print("\t\t     ┌────────────────┐\n\t\t     │"+"/"*(i*2)+" "*((8-i)*2)+'╠'+"\n\t\t     └────────────────┘",flush=open)
                    time.sleep(random.choice(loadingBar))
                    os.system("CLS")             
                #Breaks back to main menu
                break


            #If they want to continue:
            else:
                #Prints title, introduction, and gives difficulty options
                print('''\t\t\t╔══════════╗\n\t\t\t Quick Game\n\t\t\t╚══════════╝\n\nDon't have any friends? This is the game mode for you!\nPlay the basic, single player version of "Black to White" by changing one letter at a time!\n\nHere are the difficulties that you can pick from:\n\n\t1. Four Turn Difficulty\n\t2. Five Turn Difficulty\n\t3. Six Turn Difficulty\n\t4. Seven Turn Difficulty\n\t5. Eight Turn Difficulty''')
                #Aks the user for the difficulty
                singlePlayerdifficulty=input("\nEnter the number corresponding to the difficulty that you would like to play in. ")
                #Bulletproofs difficulty selection
                while singlePlayerdifficulty=='' or singlePlayerdifficulty[0] not in ['1','2','3','4','5'] or int(singlePlayerdifficulty)>5:
                    singlePlayerdifficulty=input("\nSorry, we didn't recognize that input. Please try again. ")
                #Clears the screen
                os.system("CLS")
                #Prints title, introduction, and gives scoring system options
                print('''\t\t\t╔══════════╗\n\t\t\t Quick Game\n\t\t\t╚══════════╝\n\nDon't have any friends? This is the game mode for you!\nPlay the basic, single player version of "Black to White" by changing one letter at a time!\n\nHere are the scoring systems that you can pick from:\n\n\t1. Baby Mode           - No Penalties For Errors\n\t2. Intermediate Mode   - Points Deducted Per Error \n\t3. Hardcore Mode       - Game Over On Error\n''')
                #Asks user for the scoring system of their choice
                scoringSystem=input("Please enter the number corresponding to the scoring system that you would like to play with. ")
                #Bulletproofs scoring system selection
                while scoringSystem=='' or scoringSystem[0] not in ['1','2','3'] or int(scoringSystem)>3:
                    scoringSystem=input("\nSorry, we didn't recognize that input. Please try again. ")


                #Sets up the lists that the user will be using based on the difficulty. Then sets the total amount of points that they start with
                if singlePlayerdifficulty[0]=='1':
                    useDifficulty=difficultyFour
                    totalpoints=8
                elif singlePlayerdifficulty[0]=='2':
                    useDifficulty=difficultyFive
                    totalpoints=10
                elif singlePlayerdifficulty[0]=='3':
                    useDifficulty=difficultySix
                    totalpoints=12
                elif singlePlayerdifficulty[0]=='4':
                    useDifficulty=difficultySeven
                    totalpoints=14
                else:
                    useDifficulty=difficultyEight
                    totalpoints=16


                #Sets up the scoring system that the user chose      
                if scoringSystem[0]=='1':
                    mode='BABY'
                elif scoringSystem[0]=='2':
                    mode='INTERMEDIATE'
                else:
                    mode='HARDCORE'


                #Sets up the variables turns and errors      
                turns=0
                errors=0
                #Picks a random pair of words from the lists representing the difficulty that they chose
                gameStart,gameEnd=(random.choice(useDifficulty)).split(' ')
                #Clears the screen
                os.system("CLS")


                #Animates a loading bar
                for i in range(1,9):
                    print("\t\t\t╔══════════╗\n\t\t\t Quick Game\n\t\t\t╚══════════╝\n\n\n\t\t     Loading your game...\n")
                    print("\t\t     ┌────────────────┐\n\t\t     │"+"/"*(i*2)+" "*((8-i)*2)+'╠'+"\n\t\t     └────────────────┘",flush=open)
                    time.sleep(random.choice(loadingBar))
                    os.system("CLS")


                #Sets up lists for later use    
                listStart=[]
                listEnd=[]
                #Places every character of the starting word into a list as it's own object
                for i in gameStart:
                    listStart.append(i)
                #Places every character of the ending word into a list as it's own object
                for i in gameEnd:
                    listEnd.append(i)
                #Joins the lists with 5 spaces in between each element *important for printing the spaces in between on the actual game
                spacedStart='     '.join(listStart)
                spacedEnd='     '.join(listEnd)
                #Sets up numberStart list
                numberStart=[]
                #Loop that puts 1 number per character of the start word into a list
                for i in range(len(gameStart)):
                    numberStart.append(str(i+1))
                #Joins numbers with 5 spaces between each element *important for lining up the numbers with the letters of the word
                spacedNumberstart='     '.join(numberStart)
                #Sets up boolean to check if an inputed word is real or not
                diction=True


                #Loop while the original word is not the ending word (aka they haven't beaten the game yet)
                while spacedStart!=spacedEnd:

                    
                    #Sets up stringStart variable that is the created word without spaces in between to use for regularly outputting the new words being created
                    stringStart=''
                    for a in listStart:
                        stringStart+=a

                        
                    #Clears the screen
                    os.system("CLS")
                    #Prints title, introduction, game board (letters and numbers with spaces separating them)
                    print('''\t\t\t╔══════════╗\n\t\t\t Quick Game\n\t\t\t╚══════════╝\n\nYour words are:''',gameStart,"and",gameEnd+"\n\nSolve the puzzle by turning the word",gameStart,"to the word",gameEnd,'''one letter at a time!\n\n\n'''+'\t'+'-     '*len(gameStart)+'\n\t'+spacedStart+'\n\t'+'-     '*len(gameStart)+'\n\t'+'^     '*len(gameStart)+'\n\t'+spacedNumberstart+'\n')                   
                    #Asks the user for the number corresponding to the letter they want to change. Uses stringStart to print the current word
                    replace=input("\nEnter the number corresponding to the letter in %s would you like to change. "%stringStart).upper()
                    #Bulletproofs replace
                    while replace=='' or (replace[0] not in spacedNumberstart) or (replace[0] in ['',' ']) or (replace[0].find(' ')!=-1) or len(replace)>1:
                        replace=input("\nSorry, we didn't recognize that input. Try again. ")


                    #Clears the screen
                    os.system("CLS")
                    #Prints title and introduction and:
                    #If they chose to replace a character after the first one
                    if int(replace)>1:
                        #Formats a box around the character they chose and reprints the replace input and their choice
                        print('''\t\t\t╔══════════╗\n\t\t\t Quick Game\n\t\t\t╚══════════╝\n\nYour words are:''',gameStart,"and",gameEnd+"\n\nSolve the puzzle by turning the word",gameStart,"to the word",gameEnd,'''one letter at a time!\n\n\n'''+'\t'+'-     '*(int(replace)-2)+'-    '+'┌ ┐    '+'-     '*(len(gameStart)-int(replace))+'\n\t'+spacedStart+'\n\t'+'-     '*(int(replace)-2)+'-    '+'└ ┘    '+'-     '*(len(gameStart)-int(replace))+'\n\t'+'^     '*len(gameStart)+'\n\t'+spacedNumberstart+"\n\n\nEnter the number corresponding to the letter in %s would you like to change. %s "%(stringStart,replace))
                    #If they chose to replace the first character and reprints the replace input and their choice
                    else:
                        #Formats a box around specifically the first one *this is required because having the box there messes with the spacing
                        print('''\t\t\t╔══════════╗\n\t\t\t Quick Game\n\t\t\t╚══════════╝\n\nYour words are:''',gameStart,"and",gameEnd+"\n\nSolve the puzzle by turning the word",gameStart,"to the word",gameEnd,'''one letter at a time!\n\n\n'''+'       '+'┌ ┐    '+'-     '*(len(gameStart)-int(replace))+'\n\t'+spacedStart+'\n       '+'└ ┘    '+'-     '*(len(gameStart)-int(replace))+'\n\t'+'^     '*len(gameStart)+'\n\t'+spacedNumberstart+"\n\n\nEnter the number corresponding to the letter in %s would you like to change. %s "%(stringStart,replace))
                    

                    #Asks the user what letter they would like to replace their character option with
                    replaceWith=input("\nWhat letter of the alphabet would you like to replace it with? ").upper()
                    #Bulletproofs replaceWith
                    while len(replaceWith)!=1:
                        replaceWith=input("\nSorry, that input was too long. Try again with a single character answer. ").upper()


                    #Replaces the index that they chose (subtracting 1 because it starts at 0) with what they wanted to replace it with    
                    listStart[int(replace)-1]=str(replaceWith)
                    #If the joined list containing the new word isn't in the dictionary:
                    if ''.join(listStart) not in dictionary:
                        #Based on the mode that they are playing on, gives them the appropriate message, adds to error, subtracts 1 point where required
                        if mode=='HARDCORE':
                            input("\n%s is not in the dictionary!\nBecause you are playing on HARDCORE mode, this is GAME OVER. "%(''.join(listStart)))
                            os.system("CLS")
                            diction=False
                            break
                        elif mode=='INTERMEDIATE':
                            input("\n%s is not in the dictionary!\nBecause you are playing on INTERMEDIATE mode, we have deducted one point from your total.\nBut you can still try again! "%(''.join(listStart)))
                            errors+=1
                            totalpoints-=1
                            os.system("CLS")
                        else:
                            input("\n%s is not in the dictionary!\nBecause you are playing on BABY mode, no points have been deducted.\nYou can still try again! "%(''.join(listStart)))
                            errors+=1
                            os.system("CLS")
                        #Resets the word to the most recent correct word that they entered
                        listStart=[]
                        for i in spacedStart:
                            if i!=' ':
                                listStart.append(i)
                    #If the new word is in the dictionary:
                    else:
                        #Sets the printable word on the game screen with the spaces in the middle
                        spacedStart='     '.join(listStart)
                        #Subtract a point from the total
                        totalpoints-=1
                        #Adds to the turn number
                        turns+=1
                        #Clears the screen
                        os.system("CLS")


                #If, right after the loop (meaning that they beat the game), they didn't mess up in hardcore mode
                if diction==True:


                    #Prints title and congratulations message. Displays the amount of turns they took, amount of errors they made, and their final score
                    print('''\t\t\t╔══════════╗\n\t\t\t Quick Game\n\t\t\t╚══════════╝\n\nYour words are:''',gameStart,"and",gameEnd+"\n\nSolve the puzzle by turning the word",gameStart,"to the word",gameEnd,'''one letter at a time!\n\n\n'''+'\t'+'-     '*len(gameStart)+'\n\t'+spacedStart+'\n\t'+'-     '*len(gameStart)+'\n\t'+'^     '*len(gameStart)+'\n\t'+spacedNumberstart+'\n'+"\n\nCongratulations! You solved the puzzle by turning the word",gameStart,"to",gameEnd+" on",mode,"mode!\nBecause it took you",turns,"turns and you made",errors,"error(s), your final score is:",totalpoints,"points!")
                    #Asks the user if they want to add their score to the leaderboard
                    leaderboardQuestion=input("\nWould you like to add your score to the leaderboard? [Y/N]  ").upper()
                    #Bulletproofs leaderboardQuestion
                    while leaderboardQuestion=='' or leaderboardQuestion[0] not in ['Y','N']:
                        leaderboardQuestion=input("\nSorry that isn't a valid input. Try again typing Yes or No. ").upper()
                    #If they chose to add their score to the leaderboard
                    if leaderboardQuestion[0]=='Y':
                        #Sets up the leaderboard lists: Cheat, Points, Mode, Words Given, and Name to use when setting up the leaderboard in the menu
                        if cheat==True:
                            leaderboardCheat.append('Yes')
                        else:
                            leaderboardCheat.append('No')
                        leaderboardPoints.append(totalpoints)
                        leaderboardMode.append(mode)
                        onlyWords=gameStart+' to '+gameEnd
                        leaderboardWords.append(onlyWords)
                        name=input("\nPlease enter your name for the leaderboard. [Under 13 characters]. ")
                        while name=='' or len(name)>12:
                            name=input("\nSorry, names must be between 1-12 letters long. Enter another name, please. ")
                        leaderboardName.append(name)
                        print("You have been added to the leaderboard. To look at the leaderboard, select it on the main menu. ")


                #Asks the user if they would like to go back to the menu
                menuAgain=input("\nWould you like to go back to the menu (Y) or exit the game (N)? [Y/N]. ").upper()
                #Bulletproofs choice
                while menuAgain=='' or menuAgain[0] not in ['Y','N']:
                    menuAgain=input("\nSorry, that isn't a valid input. Try again typing Yes or No. ").upper()
                #If they want to go back to the menu:
                if menuAgain=='Y':
                    os.system("CLS")
                    #Runs through loading bar animation
                    for i in range(1,9):
                        print('''\t\t\t╔══════════╗\n\t\t\t Quick Game\n\t\t\t╚══════════╝\n\n\t\tSending you back to the menu.\n''')
                        print("\t\t     ┌────────────────┐\n\t\t     │"+"/"*(i*2)+" "*((8-i)*2)+'╠'+"\n\t\t     └────────────────┘",flush=open)
                        time.sleep(random.choice(loadingBar))
                        os.system("CLS")             
                    #Breaks back to main menu
                    break
                #If they don't want to go back to the menu:
                else:
                    #Sets variables into a configuration in which none of the loop conditions will be met
                    keepPlaying=False
                    endGame=True
                    diction=False
                    #Breaks from all loops because of the above
                    break           

        #If they chose the second option (multiplayer)
        elif menuSelection=='2':

            #Prints title and introduction
            print('\t\t\t╔═══════════╗\n\t\t\t Multiplayer\n\t\t\t╚═══════════╝\n')
            #Asks user if they would like to continue
            multiplayerContinue=input('''Oh! So you have some friends, eh?\nPlay the classic version of "Black to White" and compare your scores with friends!\n\nDo you wish to continue? [Y/N]. ''').upper()           
            #Bulletproofs continuation inputs
            while multiplayerContinue=='' or multiplayerContinue[0] not in ['Y','N']:
                multiplayerContinue=input("\nSorry, that isn't a valid input. Try again by typing Yes or No. ").upper()
            #Clears the screen
            os.system("CLS")

            
            if multiplayerContinue[0]=='N':
                #Runs through loading bar animation
                for i in range(1,9):
                    print(''''\t\t\t╔═══════════╗\n\t\t\t Multiplayer\n\t\t\t╚═══════════╝\n\nOh! So you have some friends, eh?\nPlay the classic version of "Black to White" and compare your scores with friends!\n\nDo you wish to continue? [Y/N]. \n\n\t\tSending you back to the menu.\n''')
                    print("\t\t     ┌────────────────┐\n\t\t     │"+"/"*(i*2)+" "*((8-i)*2)+'╠'+"\n\t\t     └────────────────┘",flush=open)
                    time.sleep(random.choice(loadingBar))
                    os.system("CLS")             
                #Breaks back to main menu
                break

            
            else:
                #Prints title, introduction, and gives difficulty options
                print(''''\t\t\t╔═══════════╗\n\t\t\t Multiplayer\n\t\t\t╚═══════════╝\n\nOh! So you have some friends, eh?\nPlay the classic version of "Black to White" and compare your scores with friends!\n\nHere are the difficulties that you can pick from:\n\n\t1. Four Turn Difficulty\n\t2. Five Turn Difficulty\n\t3. Six Turn Difficulty\n\t4. Seven Turn Difficulty\n\t5. Eight Turn Difficulty''')
                #Asks the user for the difficulty
                multiplayerDifficulty=input("\nEnter the number corresponding to the difficulty that your group would like to play in. ")
                #Bulletproofs difficulty selection
                while multiplayerDifficulty=='' or multiplayerDifficulty[0] not in ['1','2','3','4','5'] or int(multiplayerDifficulty)>5:
                    multiplayerDifficulty=input("\nSorry, we didn't recognize that input. Please try again. ")
                #Clears the screen
                os.system("CLS")

                
                #Sets up the lists that the user will be using based on the difficulty. Then sets the total amount of points that they start with
                if multiplayerDifficulty[0]=='1':
                    useDifficulty=difficultyFour
                elif multiplayerDifficulty[0]=='2':
                    useDifficulty=difficultyFive
                elif multiplayerDifficulty[0]=='3':
                    useDifficulty=difficultySix
                elif multiplayerDifficulty[0]=='4':
                    useDifficulty=difficultySeven
                else:
                    useDifficulty=difficultyEight


                #Sets up the scoring system that the user chose      
                mode='MULTIPLAYER'



                os.system("CLS")
                print(''''\t\t\t╔═══════════╗\n\t\t\t Multiplayer\n\t\t\t╚═══════════╝\n\nOh! So you have some friends, eh?\nPlay the classic version of "Black to White" and compare your scores with friends!''')
                playerNumber=input("\nHow many people are playing the game, today? [2-9]. ")
                while playerNumber=='' or playerNumber[0] not in ['2','3','4','5','6','7','8','9'] or int(playerNumber)>9 or int(playerNumber)<2:
                    playerNumber=input("\nEither that's not a number or you're lying about how many friends you have. Try again. ")



                #Picks a random pair of words from the lists representing the difficulty that they chose
                gameStart,gameEnd=(random.choice(useDifficulty)).split(' ')
                #Clears the screen
                os.system("CLS")


                #Animates a loading bar
                for i in range(1,9):
                    print("\t\t\t╔═══════════╗\n\t\t\t Multiplayer\n\t\t\t╚═══════════╝\n\n\n\t\t     Loading your game...\n")
                    print("\t\t     ┌────────────────┐\n\t\t     │"+"/"*(i*2)+" "*((8-i)*2)+'╠'+"\n\t\t     └────────────────┘",flush=open)
                    time.sleep(random.choice(loadingBar))
                    os.system("CLS")
                multiplayerPoints=[]
                for player in range(int(playerNumber)):

                    
                    #Sets up the lists that the user will be using based on the difficulty. Then sets the total amount of points that they start with
                    if multiplayerDifficulty[0]=='1':
                        totalpoints=8
                    elif multiplayerDifficulty[0]=='2':
                        totalpoints=10
                    elif multiplayerDifficulty[0]=='3':
                        totalpoints=12
                    elif multiplayerDifficulty[0]=='4':
                        totalpoints=14
                    else:
                        totalpoints=16


                    #Sets up the variables turns and errors      
                    turns=0
                    errors=0
                    #Sets up lists for later use    
                    listStart=[]
                    listEnd=[]
                    #Places every character of the starting word into a list as it's own object
                    for i in gameStart:
                        listStart.append(i)
                    #Places every character of the ending word into a list as it's own object
                    for i in gameEnd:
                        listEnd.append(i)
                    #Joins the lists with 5 spaces in between each element *important for printing the spaces in between on the actual game
                    spacedStart='     '.join(listStart)
                    spacedEnd='     '.join(listEnd)
                    #Sets up numberStart list
                    numberStart=[]
                    #Loop that puts 1 number per character of the start word into a list
                    for i in range(len(gameStart)):
                        numberStart.append(str(i+1))
                    #Joins numbers with 5 spaces between each element *important for lining up the numbers with the letters of the word
                    spacedNumberstart='     '.join(numberStart)
                    #Sets up boolean to check if an inputed word is real or not

                                                                                                                 
                    #Loop while the original word is not the ending word (aka they haven't beaten the game yet)
                    while spacedStart!=spacedEnd:

                    
                        #Sets up stringStart variable that is the created word without spaces in between to use for regularly outputting the new words being created
                        stringStart=''
                        for a in listStart:
                            stringStart+=a

                            
                        #Clears the screen
                        os.system("CLS")
                        #Prints title, introduction, game board (letters and numbers with spaces separating them)
                        print("\t\t\t╔═══════════╗\n\t\t\t Multiplayer\n\t\t\t╚═══════════╝\n\nPLAYER",player+1,"Your words are:",gameStart,"and",gameEnd+"\n\nSolve the puzzle by turning the word",gameStart,"to the word",gameEnd,'''one letter at a time!\n\n\n'''+'\t'+'-     '*len(gameStart)+'\n\t'+spacedStart+'\n\t'+'-     '*len(gameStart)+'\n\t'+'^     '*len(gameStart)+'\n\t'+spacedNumberstart+'\n')                   
                        #Asks the user for the number corresponding to the letter they want to change. Uses stringStart to print the current word
                        replace=input("\nEnter the number corresponding to the letter in %s would you like to change. "%stringStart).upper()
                        #Bulletproofs replace
                        while replace=='' or (replace[0] not in spacedNumberstart) or (replace[0]==' ') or (replace[0].find(' ')!=-1) or len(replace)>1:
                            replace=input("\nSorry, we didn't recognize that input. Try again. ")



                        #Clears the screen
                        os.system("CLS")
                        #Prints title and introduction and:
                        #If they chose to replace a character after the first one
                        if int(replace)>1:
                            #Formats a box around the character they chose and reprints the replace input and their choice
                            print("\t\t\t╔═══════════╗\n\t\t\t Multiplayer\n\t\t\t╚═══════════╝\n\nPLAYER",player+1,"Your words are:",gameStart,"and",gameEnd+"\n\nSolve the puzzle by turning the word",gameStart,"to the word",gameEnd,"one letter at a time!\n\n\n"+'\t'+'-     '*(int(replace)-2)+'-    '+'┌ ┐    '+'-     '*(len(gameStart)-int(replace))+'\n\t'+spacedStart+'\n\t'+'-     '*(int(replace)-2)+'-    '+'└ ┘    '+'-     '*(len(gameStart)-int(replace))+'\n\t'+'^     '*len(gameStart)+'\n\t'+spacedNumberstart+"\n\n\nEnter the number corresponding to the letter in %s would you like to change. %s "%(stringStart,replace))
                        #If they chose to replace the first character and reprints the replace input and their choice
                        else:
                            #Formats a box around specifically the first one *this is required because having the box there messes with the spacing
                            print("\t\t\t╔═══════════╗\n\t\t\t Multiplayer\n\t\t\t╚═══════════╝\n\nPLAYER",player+1,"Your words are:",gameStart,"and",gameEnd+"\n\nSolve the puzzle by turning the word",gameStart,"to the word",gameEnd,"one letter at a time!\n\n\n"+'       '+'┌ ┐    '+'-     '*(len(gameStart)-int(replace))+'\n\t'+spacedStart+'\n       '+'└ ┘    '+'-     '*(len(gameStart)-int(replace))+'\n\t'+'^     '*len(gameStart)+'\n\t'+spacedNumberstart+"\n\n\nEnter the number corresponding to the letter in %s would you like to change. %s "%(stringStart,replace))
                        

                        #Asks the user what letter they would like to replace their character option with
                        replaceWith=input("\nWhat letter of the alphabet would you like to replace it with? ").upper()
                        #Bulletproofs replaceWith
                        while len(replaceWith)!=1:
                            replaceWith=input("\nSorry, that input wasn't understood. Try again with a single character answer. ").upper()


                        #Replaces the index that they chose (subtracting 1 because it starts at 0) with what they wanted to replace it with    
                        listStart[int(replace)-1]=str(replaceWith)
                        #If the joined list containing the new word isn't in the dictionary:
                        if ''.join(listStart) not in dictionary:
                            #Based on the mode that they are playing on, gives them the appropriate message, adds to error, subtracts 1 point where required
                            if mode=='MULTIPLAYER':
                                input("\n%s is not in the dictionary!\nBecause you are playing MULTIPLAYER mode, we have deducted one point from your total.\nPress enter to try again! "%(''.join(listStart)))
                                errors+=1
                                totalpoints-=1
                                os.system("CLS")
                          
                            #Resets the word to the most recent correct word that they entered
                            listStart=[]
                            for i in spacedStart:
                                if i!=' ':
                                    listStart.append(i)
                        #If the new word is in the dictionary:
                        else:
                            #Sets the printable word on the game screen with the spaces in the middle
                            spacedStart='     '.join(listStart)
                            #Subtract a point from the total
                            totalpoints-=1
                            #Adds to the turn number
                            turns+=1
                            #Clears the screen
                            os.system("CLS")

                                                                                                                
                    #Prints title and congratulations message. Displays the amount of turns they took, amount of errors they made, and their final score
                    print("\t\t\t╔═══════════╗\n\t\t\t Multiplayer\n\t\t\t╚═══════════╝\n\nPLAYER",player+1,"Your words are:",gameStart,"and",gameEnd+"\n\nSolve the puzzle by turning the word",gameStart,"to the word",gameEnd,"one letter at a time!\n\n\n"+'\t'+'-     '*len(gameStart)+'\n\t'+spacedStart+'\n\t'+'-     '*len(gameStart)+'\n\t'+'^     '*len(gameStart)+'\n\t'+spacedNumberstart+'\n'+"\n\nCongratulations! You solved the puzzle by turning the word",gameStart,"to",gameEnd+" on",mode,"mode!\nBecause it took you",turns,"turns and you made",errors,"error(s), your final score is:",totalpoints,"points!")
                    #Asks the user if they want to add their score to the leaderboard
                    leaderboardQuestion=input("\nPlayer %i, would you like to add your score to the leaderboard? [Y/N].  "%(player+1)).upper()
                    #Bulletproofs leaderboardQuestion
                    while leaderboardQuestion=='' or leaderboardQuestion[0] not in ['Y','N']:
                        leaderboardQuestion=input("\nSorry that isn't a valid input. Try again typing Yes or No. ").upper()
                    #If they chose to add their score to the leaderboard
                    if leaderboardQuestion[0]=='Y':
                        #Sets up the leaderboard lists: Cheat, Points, Mode, Words Given, and Name to use when setting up the leaderboard in the menu
                        if cheat==True:
                            leaderboardCheat.append('Yes')
                        else:
                            leaderboardCheat.append('No')
                        leaderboardPoints.append(totalpoints)
                        leaderboardMode.append(mode)
                        onlyWords=gameStart+' to '+gameEnd
                        leaderboardWords.append(onlyWords)
                        name=input("\nPlease enter your name for the leaderboard. [Under 13 characters]. ")
                        while name=='' or len(name)>12:
                            name=input("\nSorry, names must be between 1-12 letters long. Enter another name, please. ")
                        leaderboardName.append(name)
                        print("You have been added to the leaderboard. To look at the leaderboard, select it on the main menu. ")


                    multiplayerPoints.append(totalpoints)
                    if (player+1)!=int(playerNumber):
                        input("\nPlayer %i, press enter to begin your round!"%(player+2))
                    else:
                        input("\nPress enter to get the final results!")
                os.system("CLS")
                print("\t\t\t╔═══════════╗\n\t\t\t Multiplayer\n\t\t\t╚═══════════╝\n\nAnd the results are:")
                time.sleep(2)
                topScore=0
                for score in multiplayerPoints:
                    if score==max(multiplayerPoints):
                        topScore+=1
                if topScore==1:
                    print("\nPlayer",multiplayerPoints.index(max(multiplayerPoints))+1,"wins with a score of:",max(multiplayerPoints))
                else:
                    print('\n'+str(topScore),"players tied with a score of:",max(multiplayerPoints))
                #Asks the user if they would like to go back to the menu                
                menuAgain=input("\nWould you like to go back to the menu (Y) or exit the game (N)? [Y/N]. ").upper()
                #Bulletproofs choice
                while menuAgain=='' or menuAgain[0] not in ['Y','N']:
                    menuAgain=input("\nSorry, that isn't a valid input. Try again typing Yes or No. ").upper()
                #If they want to go back to the menu:
                if menuAgain=='Y':
                    os.system("CLS")
                    #Runs through loading bar animation
                    for i in range(1,9):
                        print("\t\t\t╔═══════════╗\n\t\t\t Multiplayer\n\t\t\t╚═══════════╝\n\n\n\t\tSending you back to the menu...\n")
                        print("\t\t     ┌────────────────┐\n\t\t     │"+"/"*(i*2)+" "*((8-i)*2)+'╠'+"\n\t\t     └────────────────┘",flush=open)
                        time.sleep(random.choice(loadingBar))
                        os.system("CLS")             
                    #Breaks back to main menu
                    break
                #If they don't want to go back to the menu:
                else:
                    #Sets variables into a configuration in which none of the loop conditions will be met
                    keepPlaying=False
                    endGame=True
                    diction=False
                    #Breaks from all loops because of the above
                    break           


        #If they chose the 3rd option (Leaderboard):
        elif menuSelection=='3':
            #Clears the screen
            os.system("CLS")
            #Prints title
            print("\t\t\t╔═══════════════╗\n\t\t\t The Leaderboard\n\t\t\t╚═══════════════╝\n")
            #If there is no info in the leaderboard
            if leaderboardPoints==[]:
                #Tells the user that there is no information to display
                input("Sorry!\nAs of right now in your game session, no players have been added to the leaderboard! ")
                #Outputs loading animation back to menu after user inputs anything
                os.system("CLS")
                for i in range(1,9):
                    print("\t\t\t╔═══════════════╗\n\t\t\t The Leaderboard\n\t\t\t╚═══════════════╝\n\nSorry!\nAs of right now in your game session, no players have been added to the leaderboard!")
                    print("\n\n\t\t  Sending you back to the menu.\n\n\t\t       ┌────────────────┐\n\t\t       │"+"/"*(i*2)+" "*((8-i)*2)+'╠'+"\n\t\t       └────────────────┘",flush=open)
                    time.sleep(random.choice(loadingBar))
                    os.system("CLS")
                keepPlaying=True
                os.system("CLS")
                break
            #If there is information to be displayed
            else:
                #Sets up a list that is the exact copy of leaderboardPoints *this is required because we need to be able to manipulate the points list and still be able to load it up again if they pick to enter the leaderboard more than once
                leaderboardIndex=list(leaderboardPoints)
                #Prints the leaderboard title and formatting
                print("The following are the top games for this game session:\n\nCheating?\tPoints\t\tMode\t\tWords\t\tName\n---------       ------     --------------  ---------------  ------------\n")
                #Prints the info of the person on the leaderboard with the most points, sets that to negative quadrillion and then looks for the next highest amount, etc.
                for i in range(len(leaderboardPoints)):
                    indexShortcut=leaderboardIndex.index(max(leaderboardIndex))
                    print('%-9s       %-4i       %-15s %-16s %-s\n'%(leaderboardCheat[indexShortcut],(max(leaderboardIndex)),leaderboardMode[indexShortcut],leaderboardWords[indexShortcut],leaderboardName[indexShortcut]))
                    leaderboardIndex[indexShortcut]=-1000000000000000
                input("\n\n\nPress enter to go back to the menu. ")
                #Clears the screen
                os.system("CLS")
                #Prints loading bar animation for going back to the menu
                for i in range(1,9):
                    print("\t\t\t╔═══════════════╗\n\t\t\t The Leaderboard\n\t\t\t╚═══════════════╝\n")
                    print("\n\n\t\t  Sending you back to the menu.\n\n\t\t       ┌────────────────┐\n\t\t       │"+"/"*(i*2)+" "*((8-i)*2)+'╠'+"\n\t\t       └────────────────┘",flush=open)
                    time.sleep(random.choice(loadingBar))
                    os.system("CLS")
                keepPlaying=True
                os.system("CLS")
                break

                                    
        #If they chose the 4th option (adding to the dictionary):
        elif menuSelection=='4':

            
            #Clear screen
            os.system("CLS")
            #Print title
            print("\t\t\t╔════════════════════════╗\n\t\t\t Adding To The Dictionary\n\t\t\t╚════════════════════════╝\n")
            #Gives users disclaimer about cheating. Asks if they would still like to continue
            dictionaryContinue=input('In the "Add to The Dictionary" option you can add as many words as you require.\n\nNote that adding to the dictionary this session is only temporary until you close this window.\nAlso, adding to the dictionary is technically cheating so be warned.\nWould you like to continue [Y/N]? ').upper()
            #Bulletproofs the continue input
            while dictionaryContinue=='' or dictionaryContinue[0] not in ['Y','N']:
                dictionaryContinue=input("\nSorry, that isn't a valid input. Try again typing Yes or No. ").upper()
            #If they don't want to continue
            if dictionaryContinue[0]=='N':
                #Clear the screen, prints animation for going back to the menu, sends them back
                os.system("CLS")
                for i in range(1,9):
                    print("\t\t\t╔════════════════════════╗\n\t\t\t Adding To The Dictionary\n\t\t\t╚════════════════════════╝\n\n\t\t      Sending you back to the menu.\n\n")
                    print("\t\t\t    ┌────────────────┐\n\t\t\t    │"+"/"*(i*2)+" "*((8-i)*2)+'╠'+"\n\t\t\t    └────────────────┘",flush=open)
                    time.sleep(random.choice(loadingBar))
                    os.system("CLS")
                break


            #If they want to continue
            else:
                #Clears the screet, prints title, sets cheat to True to use for the leaderboard
                os.system("CLS")
                print("\t\t\t╔════════════════════════╗\n\t\t\t Adding To The Dictionary\n\t\t\t╚════════════════════════╝\n")
                cheat=True
                #Asks them what they would like to add to the dictionary
                dictionaryAdd=input("What word would you like to add to the dictionary? ").upper()
                #Adds the uppercased word to the dictionary
                dictionary.append(dictionaryAdd)

                
                #Asks if that is all they would like to add
                addMorequestion=input("\nIs that all you would like to add? [Y/N]. ").upper()
                #Bulletproofs response
                while addMorequestion=='' or addMorequestion[0] not in ['Y','N']:
                    addMorequestion=input("\nSorry, that isn't a valid input. Try again by typing Yes or No. ").upper()
                #If they want to add more
                if addMorequestion=='N':
                    #While loop of adding words until they input 'exit'
                    addMore='zzzzzzzzzzzz'
                    while addMore!='EXIT':
                        addMore=input("\nWhat word would you like to add to the dictionary? (type 'EXIT' when you would like to stop adding). ").upper()
                        dictionary.append(addMore)
                    #Clears screen and prints going back to menu animation
                    os.system("CLS")
                    for i in range(1,9):
                        print("\t\t\t╔════════════════════════╗\n\t\t\t Adding To The Dictionary\n\t\t\t╚════════════════════════╝\n\n\t\t      Sending you back to the menu.\n\n")
                        print("\t\t\t    ┌────────────────┐\n\t\t\t    │"+"/"*(i*2)+" "*((8-i)*2)+'╠'+"\n\t\t\t    └────────────────┘",flush=open)
                        time.sleep(random.choice(loadingBar))
                        os.system("CLS")
                    break


                #If they don't want to add more
                else:                    
                    #Clears screen, prints back to menu animation
                    os.system("CLS")
                    for i in range(1,9):
                        print("\t\t\t╔════════════════════════╗\n\t\t\t Adding To The Dictionary\n\t\t\t╚════════════════════════╝\n\n\t\t      Sending you back to the menu.\n\n")
                        print("\t\t\t    ┌────────────────┐\n\t\t\t    │"+"/"*(i*2)+" "*((8-i)*2)+'╠'+"\n\t\t\t    └────────────────┘",flush=open)
                        time.sleep(random.choice(loadingBar))
                        os.system("CLS")
                    break


        #If they chose the 5th option (exiting the game)
        else:

            
            #Sets up variables into a configuration that won't fit any of the while loop conditions after break
            keepPlaying=False
            endGame=True
            break

        
os.system("CLS")
print("\t\t\t╔═════════╗\n\t\t\t Thank You\n\t\t\t╚═════════╝\n\nThank you for playing the game! Please close this window now.\n\nBlack to White\tv7.1434234234\nby New Borleans Productions")               
input()
