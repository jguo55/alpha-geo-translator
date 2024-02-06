#case 1: rightside includes leftside (subject of type) (easier case)
import re
inp = "a b = segment a b; g1 = on_tline g1 a a b; g2 = on_tline g2 b b a; m = on_circle m g1 a, on_circle m g2 b; n = on_circle n g1 a, on_circle n g2 b; c = on_pline c m a b, on_circle c g1 a; d = on_pline d m a b, on_circle d g2 b; e = on_line e a c, on_line e b d; p = on_line p a n, on_line p c d; q = on_line q b n, on_line q c d ? cong e p e q"
parts = re.split('[;,]', inp)
parts = [p.strip() for p in parts] #couldn't figure out how to get re to strip the whitespace automatically, easy optimization if possible
'''
translation = { #idk how to make it so i can define the translation dictionary just one time
                "angle_bisector": "Construct a point " + v[0] + " on the angle bisector of ∠" + v[1] + v[2] + v[3],
                "angle_mirror": "Construct a point " + v[0] + " such that " + v[2] + v[3] + " is the bisector of ∠" + v[1] + v[2] + v[0],
                "circle": "Construct point " + v[0] + " as the circumcenter of " + v[1] + ", " + v[2] + ", " + v[3],
                "eq_quadrilateral": "Construct quadrilateral " + v[0] + v[1] + v[2] + v[3] + " with " + v[0] + v[3] + " = " + v[1] + v[2],
                "eq_trapezoid": "Construct trapezoid " + v[0] + v[1] + v[2] + v[3] + " with " + v[0] + v[3] + " = " + v[1] + v[2],
                "eqtriangle": "Construct " + v[0] + " such that " + v[0] + v[1] + v[2] + " is an equilateral triangle",
                "eqangle2": "Construct " + v[0] + " such that ∠" + v[2] + v[1] + v[0] + " = ∠" + v[0] + v[3] + v[2],
                "eqdia_equadrilateral": "Construct quadrilateral " + v[0] + v[1] + v[2] + v[3] + " with " + v[0] + v[2] + " = " + v[1] + v[3],
                "eqdistance": "Construct " + v[0] + " such that " + v[0] + v[1] + " = " + v[2] + v[3],
                "foot": "Construct " + v[0] + " as the foot of " + v[1] + " on " + v[2] + v[3],
                "free": "Construct a free point " + v[0],
                "incenter": "Construct " + v[0] + " as the incenter of " + v[1] + v[2] + v[3],
                "incenter2": "Construct " + v[3] + " as the incenter of " + v[4] + v[5] + v[6] + " with touchpoints " + v[0] + ", " + v[1] + ", " + v[2],
                "excenter": "Construct " + v[0] + " as the excenter of " + v[1] + v[2] + v[3],
                "excenter2": "Construct " + v[0] + " as the excenter of " + v[4] + v[5] + v[6] + " with touchpoints " + v[0] + ", " + v[1] + ", " + v[2],
                "centroid": "Construct " + v[0] + " as the centroid of " + v[1] + v[2] + v[3],






                "midpointcircle": "Construct " + v[0] + ", " + v[1] + ", " + v[2] + " as the midpoints of triangle " + v[1] + v[2] + v[3] + ", and " + v[5] + " as the circumcenter of " + v[0] + v[1] + v[2],
                "isos": "Construct " + v[0] + ", " + v[1] + ", " + v[2] + " such that " + v[0] + v[1] + " = " + v[0] + v[2],
                "tangent": "Construct " + v[0] + " such that " + v[0] + v[2] + " is perpendicular to " + v[1] + v[2],
                "midpoint": "Construct " + v[0] + " as the midpoint of " + v[1] + v[2],
                "mirror": "Construct " + v[0] + " such that " + v[0] + v[1] + v[2] + " is a right isosceles triangle",
                "rotate90": "Construct " + v[0] + " such that " + v[0] + v[1] + v[2] + " = " + v[3] + v[4] + v[5],
                "on_aline": "Construct " + v[0] + " on the perpendicular bisector of " + v[1] + v[2] + " and " + v[3] + v[4] + v[5],
                "on_bline": "Construct " + v[0] + " on line " + v[1] + v[2] + " such that " + v[0] + v[3] + " = " + v[1] + v[2],
                "on_circle": "Construct " + v[0] + " on circle " + v[1] + v[2] + " such that " + v[0] + v[3] + " = " + v[1] + v[2],
                "on_line": "Construct " + v[0] + " on line " + v[1] + v[2] + " such that " + v[0] + v[3] + " = " + v[1] + v[2],
                "on_pline": "Construct " + v[0] + " such that " + v[0] + v[1] + " is parallel to " + v[2] + v[3],
                "on_tline": "Construct " + v[0] + " such that " + v[0] + v[1] + " is perpendicular to " + v[2] + v[3],
                "orthocenter": "Construct " + v[0] + " as the orthocenter of " + v[1] + v[2] + v[3],
                "parallelogram": "Construct " + v[0] + " such that " + v[1] + v[2] + v[0] + v[3] + " is a parallelogram",
                "pentagon": "Construct pentagon " + v[0] + v[1] + v[2] + v[3] + v[4],
                "rectangle": "Construct rectangle " + v[0] + v[1] + v[2] + v[3],
                "reflect": "Construct " + v[0] + " as the reflection of " + v[1] + " about " + v[2] + v[3],
                "risos": "Construct right isosceles triangle " + v[0] + v[1] + v[2],
                "angle": "Construct " + v[0] + " such that " + v[0] + v[1] + v[2] + " = " + v[3],
                "segment": "Construct two distinct points " + v[0] + ", " + v[1],
                "shift": "Construct point " + v[0] + " such that " + v[0] + v[1] + "=" + v[2] + v[3] + " and " + v[0] + v[2] + "=" + v[1] + v[3],
                "square": "Construct " + v[0] + ", " + v[1] + " such that " + v[0] + v[1] + v[2] + v[3] + " is a square",
                "init_square": "Construct square " + v[0] + v[1] + v[2] + v[3],
                "triangle": "Construct triangle " + v[0] + v[1] + v[2],
                "triangle12": "Construct triangle " + v[0] + v[1] + v[2] + " with " + v[0] + v[1] + ":" + v[0] + v[2] + " = 1:2",
                }
'''
translate = {"segment": lambda l: f"Construct 2 distinct points {l[0]}, {l[1]}"}
class Statement:
    def __init__(self, s):
        #classifies the statement on init
        self.vars = s.split(" ") #[a,b,=,segment,a,b] anything after the equals sign we don't need tbh
        self.equals = False
        try:
            ei = self.vars.index("=") + 1
            for i in range(ei):
                del i #real optimization
                self.vars.pop(0)
        except:
            pass
        self.type = self.vars.pop(0)

    def getVars(self):
        return self.vars
    
    def getType(self):
        return self.type
        

#if this solution is inefficient then unlucky but im not quite good enough to figure out how to make it better
#Issues/todo:
#1. Finish making it work
#2. OPTIMIZATION
#3. File input/output?

sparts = [Statement(p) for p in parts] #convert string to statement object

for i in sparts: #translate each statement object into string
    print(translate[i.getType()](i.getVars()))

'''
output = ""
for i in range(len(sparts)-1): #translate each statement object into string
    output += sparts[i].translate() + "; "
output += parts[-1] #last statement is always question
print(output)
'''