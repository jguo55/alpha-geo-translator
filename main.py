inp = "b c = segment; d = free; e = eqdistance d b c; t = on_bline b d, on_bline c e; a = eqangle2 b t e; p = on_line a b, on_line c d; q = on_line a b, on_line c t; r = on_line a e, on_line c d; s = on_line a e, on_line d t ? cyclic p q r s"
parts = inp.split("; ")
funcs = ["segment", "on_tline"]
output = ""
untranslated = ""
# which one is better computationally
#1. classify
#2. strip variables
#3. add
#4. add untranslated
# >>>> OR <<<<
#1. strip variables
#2. classify
#3. add
#4. add untranslated
#if this solution is inefficient then unlucky but im not quite good enough to figure out how to make it better
for p in parts:
    for f in funcs:
        if f in p:
            print(p)
        else:
            output += p
            untranslated = p

class Statement:
    def __init__(s):
        #classifies the statement on init
        for f in funcs:
            if f in s:
                this.type = s
                this.vars = 


