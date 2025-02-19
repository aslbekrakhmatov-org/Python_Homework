class vectorNd:
    def __init__(self, *args):
        self.args = list(args)
    
    def __repr__(self):
        return f"Vector{tuple(self.args)}"
    def __add__(self, other):
        return vectorNd(*[a+b for a, b in zip(self.args, other.args)])
    def __sub__(self, other):
        return vectorNd(*[a-b for a,b in zip(self.args, other.args)])
    

    
v1 = vectorNd(1, 2, 3, 4)
v2 = vectorNd(1, 1, 2, 5)
v3 = v1 + v2
print(v3)

