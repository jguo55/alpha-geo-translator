string = "A"
points = ["B", "C"]
points2 = ["D", "E"]
key = {"point": f"Free floating point {string} ", "segment": f"Construct two distinct points {points[0]} + {points[1]}", "on_pline":"a", "on_circle":"chat"}
#so basically the type will be the key to the dictionary, dictionary will have the representation of the key in natural language
print(key["segment"])

'''import re
inp = "a b = segment a b; g1 = on_tline g1 a a b; g2 = on_tline g2 b b a; m = on_circle m g1 a, on_circle m g2 b; n = on_circle n g1 a, on_circle n g2 b; c = on_pline c m a b, on_circle c g1 a; d = on_pline d m a b, on_circle d g2 b; e = on_line e a c, on_line e b d; p = on_line p a n, on_line p c d; q = on_line q b n, on_line q c d ? cong e p e q"
parts = re.split(r",|;", inp)

print(parts)'''