class WOFPlayer():
    def __init__(self,name):
        self.name=name
        self.prizeMoney=0
        self.prizes=[]
    def addMoney(self,amt):
        self.prizeMoney=self.prizeMoney+amt
        
    def goBankrupt(self):
        self.prizeMoney=0
    def addPrize(self,prize):
        self.prizes.append(prize)
    def __str__(self):
        return "{} (${})".format(self.name,self.prizeMoney)
class WOFHumanPlayer(WOFPlayer):

    def getMove(self,category,obscuredPhrase,guessed):
        print( """
             {} has (${})
             Category: {}
             Phrase:   {}
             Guessed:  {}

             Guess a letter,phrase,or type 'exit' or 'pass' :""".format(self.name,self.prizeMoney,category,obscuredPhrase,', '.join(sorted(guessed))))
        prompt=input()
        return prompt
        

class WOFComputerPlayer(WOFPlayer):
    def __init__(self,name,difficulty):
        #WOFPlayer.__init__(name,difficulty)
        self.name=name
        self.difficulty=difficulty
        self.SORTED_FREQUENCIES='ZQXJKVBPYGFWMUCLDRHSNIOATE'

    def smartCoinFlip(self):

        rand_number = random.randint(1, 10)
        if rand_number>self.difficulty:
            return True
        elif rand_number <=self.difficulty:
            return False

    def getPossibleLetters(guessed):
        LETTERS='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        lis=[]
        for x in guessed:
            for y in LETTERS:
                if x==y:
                    pass
                else:
                    lis.append(y)
        if self.prizeMoney>250:
            VOWEL_COST=250
        VOWELS='AEIOU'
        return lis
    def getMove(self):
        VOWELS='AEIOU'
        bal=self.getPossibleLetters
        for x in bal:
            for y in LETTERS:
                if x==y:
                    return 'pass'
        move=self.smartCoinFlip
        if move==True:
            maxlen=len(self.SORTED_FREQUENCIES)
            hfi=SORTED_FREQUENCIES[maxlen-1]
            return hfi
        elif move==False:
            letters = [letter for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
            rand_letter = random.choice(letters)
            return letters
        # Write the WOFPlayer class definition (part A) here

# Write the WOFHumanPlayer class definition (part B) here

# Write the WOFComputerPlayer class definition (part C) here

