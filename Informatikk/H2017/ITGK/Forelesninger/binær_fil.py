db = {"Jo": [10, "Skogata 3"], "Per": [20, "Heigata 2"]}
import pickle
f = open("database.dat", "wb")
pickle.dump(db, f)
f.close()
f = open("database.dat", "rb")
data = pickle.load(f)
print(data)
f.close()
