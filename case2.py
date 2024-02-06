#case 2: rightside doesn't include leftside
import re
inp = "b c = segment; d = free; e = eqdistance d b c; t = on_bline b d, on_bline c e; a = eqangle2 b t e; p = on_line a b, on_line c d; q = on_line a b, on_line c t; r = on_line a e, on_line c d; s = on_line a e, on_line d t ? cyclic p q r s"
parts = re.split('[;,]', inp)
parts = [p.strip() for p in parts] #couldn't figure out how to get re to strip the whitespace automatically, easy optimization if possible
sparts = []

class Statement:
    def __init__(self, s):
        #classifies the statement on init
        self.separated = s.split(" ") #[b,c,=,segment]
        self.equals = False
        self.l = []
        self.r = []
        try:
            self.type = self.separated.pop(self.separated.index("=")+1)
            for i in self.separated:
                if i == "=":
                    self.equals = True
                    continue
                match self.equals:
                    case False:
                        self.l.append(i)
                    case True:
                        self.r.append(i)
        except:
            self.type = self.separated.pop(0)
            for i in self.separated:
                self.r.append(i)
    
    def translate(self):
        translation = {"segment":"Construct two distinct points such that " + self.l[0] + ", " + self.l[1], "on_tline":"b", "on_pline":"c", "on_circle": "d"}
        return(translation[self.getType()])

    def getSeparated(self):
        return self.separated

    def getl(self):
        return self.l
    
    def getr(self):
        return self.r
    
    def getType(self):
        return self.type

    def setl(self, vars):
        self.l = vars

#if this solution is inefficient then unlucky but im not quite good enough to figure out how to make it better
#Issues/todo:
#OK CHAT IT TURNS OUT THAT THE FIRST CHARACTER OF RIGHTSIDE *IS* THE LEFTSIDE except in some cases... wtf
# 1. Comma handling (it's basically 'and')
        # ok the best way to handle it is probably just to handle the comma as another seperate statement
        # the only thing is that l will be the same as the statement before
        # so i think make a check for if the left side is null, then use the same left side as the statement before
# 2. Dictionary/translate function (refer to test file)
        #leave the '?' statements as is, no translations provided ('cyclic' and 'cong')
# 3. File input/output?


for p in parts: #convert string to statement object
    a = Statement(p)
    sparts.append(Statement(p))

for i in range(len(sparts)): #translate each statement object into string
    sm = sparts[i]
    lvar = sm.getl()
    rvar = sm.getr()
    if len(sm.getl()) == 0: #if leftside of the statement is empty
        sm.setl(sparts[i-1].getl()) #it was a comma, get the leftside from previous Statement
    

    print(sm.translate())
