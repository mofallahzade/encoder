#Developer : Mohammad Fallahzade
import random
class codec:
    valDicN = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o'          #Value , Character
                    ,16:'p',17:'q',18:'r',19:'s',20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',26:'z',27:'A',28:'B'
                    ,29:'C',30:'D',31:'E',32:'F',33:'G',34:'H',35:'I',36:'J',37:'K',38:'L',39:'M',40:'N',41:'O'
                    ,42:'P',43:'Q',44:'R',45:'S',46:'T',47:'U',48:'V',49:'W',50:'X',51:'Y',52:'Z',53:'1',54:'2'
                    ,55:'3',56:'4',57:'5',58:'6',59:'7',60:'8',61:'9',62:'.',63:'?',64:'!',65:'0',66:'-',67:'_'
                    ,68:'@',69:'(',70:')',71:','}
    valDicS = {v: k for k, v in valDicN.items()}                                                                        #Character , Value
    seperatorCharacters = ['/','[',']','&','$','<','>','=','~','*','^','{','}']                                         #Seperator Characters                                   
    allChars = list(valDicS.keys())                                                                                     #All of the Characters
    for char in seperatorCharacters:
        allChars.append(char)
    def __init__(self,string):
        self.mainString = string
    def encode(self):
        """
            *This method will encode every character in the main string to a code mixed by valDicN values depends on unicode code of the character
            *The resalt code is a string made by all of this codes.
            *Seperator Characters are used to seperate this code that can be decodeable
        """                                            
        self.encodedString = ""
        count = 0
        for char in self.mainString:
            encodedChar = ""
            asciiVal = ord(char)
            encodedCharVal = 0
            dif = asciiVal - encodedCharVal
            while dif > 0:
                keyList = []
                for key in self.valDicN:
                    if key <= dif:
                        keyList.append(key)
                    else:
                        break;
                chosenKey = int(random.choice(keyList))
                encodedChar += self.valDicN.get(chosenKey)
                encodedCharVal += chosenKey
                dif = asciiVal - encodedCharVal
            if count != 0:
                self.encodedString += random.choice(self.seperatorCharacters) + encodedChar
            else:
                self.encodedString += encodedChar
            count += 1
        return self.encodedString
    def decode(self):
        """
            *This method tries to break the main string to seperated code depended on seperator characters
            *After that it will check every character in those seperations to find the value in valDicS dictionary
            *The summary of values shows the unicode of a character,that's where chr method will return the exact character
        """
        self.decodedString = ""
        count = 0
        for char in self.mainString:
            if char not in self.allChars:
                count += 1
                break;
        if count == 1:
            return "Wrong Code!"
        temp = self.mainString
        while temp != "":
            undecodedChar = ''
            for char in temp:
                if char in self.seperatorCharacters:
                    deletText = undecodedChar + char
                    break
                else:
                    undecodedChar += char
            else:
                deletText = undecodedChar
            temp = temp.replace(deletText, "", 1)
            value = 0
            for char in undecodedChar:
                value = value + self.valDicS.get(char)
            self.decodedString += chr(value)
        if self.decodedString == "Wrong Code!":
            self.decodedString = "Nice Job,Your text is: " + self.decodedString
        return self.decodedString
        
while True:
    mainString = input("Enter the String : ")
    code = codec(mainString)
    theAction = int(input("1:Encode\n2:Decode\n0:Exit : "))
    if theAction == 1:
        print(code.encode())
    elif theAction == 2:
        print(code.decode())
    elif theAction == 0:
        break
    else:
        print("Wrong Entry")
