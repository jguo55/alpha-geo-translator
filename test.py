string = "A"
points = ["B", "C"]
key = {"point": "Free floating point " + string, "segment": "Construct two distinct points " + ''.join(points)}
#ngl this works p well but we need to strip the vars still
print (key["segment"])