inp = "b c = segment; d = free; e = eqdistance d b c; t = on_bline b d, on_bline c e; a = eqangle2 b t e; p = on_line a b, on_line c d; q = on_line a b, on_line c t; r = on_line a e, on_line c d; s = on_line a e, on_line d t ? cyclic p q r s"
parts = inp.split("; ")
sparts = []
funcs = ["segment", "on_tline"]
output = ""
untranslated = ""

class Statement:
    def __init__(self, s):
        #classifies the statement on init
        self.separated = s.split(" ") #[b,c,=,segment]
        self.equals = False
        self.type = self.separated.pop(self.separated.index("=")+1) #type of function is always right after equals sign
        self.lside = []
        self.rside = []
        for i in self.separated:
            if i == "=":
                self.equals = True
                continue
            match self.equals:
                case False:
                    self.lside.append(i)
                case True:
                    self.rside.append(i)

    def getSeparated(self):
        return self.separated

    def getlside(self):
        return self.lside
    
    def getrside(self):
        return self.rside
    
    def getType(self):
        return self.type

#if this solution is inefficient then unlucky but im not quite good enough to figure out how to make it better
#Issues/todo:
# 1. Comma handling (it's basically 'and')
# 2. Dictionary/translate function (refer to test file)
# 3. File input/output?
for p in parts:
    a = Statement(p)
    sparts.append(Statement(p))

for i in sparts:
    print(i.getlside())
    print(i.getType())
    print(i.getrside())
    print()


