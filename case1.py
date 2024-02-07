import re

#TODO
#1. Case 2 logic (classify, then just get right and left vars and add throw them into vars array)
#2. Untranslated statements: eqangle, coll, cyclic, eqratio, perp, para
translate = {
    "segment": lambda l: f"Construct 2 distinct points {l[0]}, {l[1]}",
    "on_tline": lambda l: f"Construct {l[0]} such that {l[0]}{l[1]} is perpendicular to {l[2]}{l[3]}",
    "on_circle": lambda l: f"Construct {l[0]} on circle such that {l[1]}{l[2]} = {l[1]}{l[0]}",
    "on_pline": lambda l: f"Construct {l[0]} such that {l[0]}{l[1]} is parallel to {l[2]}{l[3]}",
    "on_line": lambda l: f"Construct {l[0]} such that line {l[1]}{l[2]}",
    "cong": lambda l: f"Show that {l[0]}{l[1]} = {l[2]}{l[3]}",
    "angle_bisector": lambda l: f"Construct point {l[0]} on the angle bisector of ∠{l[1]}{l[2]}{l[3]}",
    "angle_mirror": lambda l: f"Construct point {l[0]} such that {l[2]}{l[3]} is the bisector of ∠{l[1]}{l[2]}{l[0]}",
    "circle": lambda l: f"Construct point {l[0]} as the circumcenter of {l[1]}{l[2]}{l[3]}",
    "eq_quadrilateral": lambda l: f"Construct quadrilateral {l[0]}{l[1]}{l[2]}{l[3]} with {l[0]}{l[3]} = {l[1]}{l[2]}",
    "eq_trapezoid": lambda l: f"Construct trapezoid {l[0]}{l[1]}{l[2]}{l[3]} with {l[0]}{l[3]} = {l[1]}{l[2]}",
    "eqtriangle": lambda l: f"Construct {l[0]} such that {l[0]}{l[1]}{l[2]} is an equilateral triangle",
    "eqangle2": lambda l: f"Construct {l[0]} such that ∠{l[2]}{l[1]}{l[0]} = ∠{l[0]}{l[3]}{l[2]}",
    "eqdia_equadrilateral": lambda l: f"Construct quadrilateral {l[0]}{l[1]}{l[2]}{l[3]} with {l[0]}{l[2]} = {l[1]}{l[3]}",
    "eqdistance": lambda l: f"Construct {l[0]} such that {l[0]}{l[1]} = {l[2]}{l[3]}",
    "foot": lambda l: f"Construct {l[0]} on the foot of {l[1]} on {l[2]}{l[3]}",
    "free": lambda l: f"Construct a free point {l[0]}",
    "incenter": lambda l: f"Construct {l[0]} as the incenter of {l[1]}{l[2]}{l[3]}",
    "incenter2": lambda l: f"Construct {l[3]} as the incenter of {l[4]}{l[5]}{l[6]} with touchpoints {l[0]}, {l[1]}, {l[2]}",
    "excenter": lambda l: f"Construct {l[0]} as the excenter of {l[1]}{l[2]}{l[3]}",
    "excenter2": lambda l: f"Construct {l[3]} as the excenter of {l[4]}{l[5]}{l[6]} with touchpoints {l[0]}, {l[1]}, {l[2]}",
    "centroid": lambda l: f"Construct {l[0]} as the centroid of {l[1]}{l[2]}{l[3]}",
    "midpointcircle": lambda l: f"Construct {l[0]}, {l[1]}, {l[2]} as the midpoints of triangle {l[4]}{l[5]}{l[6]}, and {l[3]} as the circumcenter of {l[0]}{l[1]}{l[2]}",
    "iso_triangle": lambda l: f"Construct {l[0]}, {l[1]}, {l[2]} such that {l[0]}{l[1]}={l[0]}{l[2]}", #table uses isos, but example uses iso_triangle
    "tangent": lambda l: tangent(l),
    "midpoint": lambda l: f"Construct {l[0]} as the midpoint of {l[1]}{l[2]}",
    "mirror": lambda l: f"Construct {l[0]} such that {l[2]} is the midpoint of {l[1]}{l[0]}",
    "rotate90": lambda l: f"Construct {l[0]} such that {l[1]}{l[0]}{l[2]} is a right isosceles triangle", #?
    "on_aline": lambda l: f"Construct {l[0]} such that ∠{l[0]}{l[1]}{l[2]} = ∠{l[3]}{l[4]}{l[5]}",
    "on_bline": lambda l: f"Construct {l[0]} on the perpendicular bisector of {l[1]}{l[2]}",
    "orthocenter": lambda l: f"Construct {l[0]} as the orthocenter of {l[1]}{l[2]}{l[3]}",
    "parallelogram": lambda l: f"Construct {l[0]} such that {l[1]}{l[2]}{l[3]}{l[0]} is a parallelogram",
    "pentagon": lambda l: f"Construct pentagon {l[0]}{l[1]}{l[2]}{l[3]}{l[4]}",
    "quadrilateral": lambda l: f"Construct quadrilateral {l[0]}{l[1]}{l[2]}{l[3]}",
    "trapezoid": lambda l: f"Construct right trapezoid {l[0]}{l[1]}{l[2]}{l[3]}",
    "r_triangle": lambda l: f"Construct right triangle {l[0]}{l[1]}{l[2]}",
    "rectangle": lambda l: f"Construct rectangle {l[0]}{l[1]}{l[2]}{l[3]}",
    "reflect": lambda l: f"Construct {l[0]} as the reflection of {l[1]} about {l[2]}{l[3]}",
    "risos": lambda l: f"Construct right isosceles triangle {l[0]}{l[1]}{l[2]}",
    "angle": lambda l: f"Construct {l[0]} such that ∠{l[1]}{l[2]}{l[0]} = {l[3]}",
    "shift": lambda l: f"Construct point {l[0]} such that {l[0]}{l[1]}={l[2]}{l[3]} and {l[0]}{l[2]}={l[1]}{l[3]}",
    "square": lambda l: f"Construct {l[0]}, {l[1]} such that {l[0]}{l[1]}{l[2]}{l[3]} is a square",
    "init_square": lambda l: f"Construct square {l[0]}{l[1]}{l[2]}{l[3]}",
    "trapezoid": lambda l: f"Construct trapezoid {l[0]}{l[1]}{l[2]}{l[3]}",
    "triangle": lambda l: f"Construct triangle {l[0]}{l[1]}{l[2]}",
    "triangle12": lambda l: f"Construct triangle {l[0]}{l[1]}{l[2]} such that {l[0]}{l[1]}:{l[0]}{l[2]} = 1:2",
    "21LC": lambda l: f"Construct circle center {l[3]} that touches line {l[4]}{l[6]} and line {l[5]}{l[6]} and circle({l[7]}, {l[4]}) at {l[0]}, {l[1]}, {l[2]}",
    "3PEQ": lambda l: f"Construct {l[0]}, {l[1]}, {l[2]} on three sides of triangle {l[3]}{l[4]}{l[5]} such that {l[1]} is the midpoint of {l[0]}{l[2]}",
    "trisect": lambda l: f"Construct {l[0]}, {l[1]} on {l[2]}{l[4]} such that {l[3]}{l[0]} and {l[3]}{l[1]} trisect ∠{l[2]}{l[3]}{l[4]}",
    "trisegment": lambda l: f"Construct {l[0]}, {l[1]} on segment {l[2]}{l[3]} such that {l[2]}{l[0]}={l[0]}{l[1]}={l[1]}{l[3]}",
    "on_dia": lambda l: f"Construct point {l[0]} such that {l[1]}{l[0]} is perpendicular to {l[2]}{l[0]}",
    "ieqtriangle": lambda l: f"Construct equilateral triangle {l[0]}{l[1]}{l[2]}",
    "cc_tangent": lambda l: f"Construct common tangents of circles ({l[4]}, {l[5]}) and ({l[6]}, {l[7]}) with touchpoints {l[0]}, {l[1]} for one tangent and {l[2]}, {l[3]} for the other",
    "eqangle3": lambda l: f"Construct point {l[0]} such that ∠{l[1]}{l[0]}{l[2]} = ∠{l[4]}{l[3]}{l[5]}"
            }

def tangent(l): #this one has 2 definitions
    if len(l) == 3:
        return f"Construct {l[0]} such that {l[1]}{l[2]} is perpendicular to {l[2]}{l[0]}"
    elif len(l) == 5:
        return f"Construct points {l[0]}, {l[1]} as the tangent touch points from {l[2]} to circle ({l[3]}, {l[4]})"
    else:
        return "tangent (untranslated)"
    
class Statement:
    def __init__(self, s):
        #classifies the statement on init
        self.vars = s.split(" ") #[b,c,=,segment]
        try: #if there's no equals sign then it's just a comma case
            ei = self.vars.index("=") + 1
            for i in range(ei):
                del i
                self.vars.pop(0)
        except:
            pass
        self.type = self.vars.pop(0)
        self.vars = [i.upper() for i in self.vars]

    def getVars(self):
        return self.vars
    
    def getType(self):
        return self.type


inpfile = open(r"input.txt", "r")
input = inpfile.readlines()
outfile = open("translated.txt", "w", encoding='utf-8')


for linect in range(len(input)):
    output = ""
    if linect % 2 == 1:
        prob = input[linect]
        parts = re.split('[;,?]', prob)
        parts = [p.strip() for p in parts] #couldn't figure out how to get re to strip the whitespace automatically, easy optimization if possible

        sparts = [Statement(p) for p in parts] #convert string to statement object

        for i in sparts: #translate each statement object into string
            try:
                output += translate[i.getType()](i.getVars()) + ". "
            except:
                output += i.getType() + " " +   ' '.join(i.getVars()) + " (function untranslated). "
        output += "\n"
    else:
        output = input[linect]
    outfile.write(output)

inpfile.close()
outfile.close()