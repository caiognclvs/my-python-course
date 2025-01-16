band = {
    "vocals": "Plant",
    "guitar": "Page"
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(type(band))
print(len(band2))

print(band["vocals"])
print(band.get("guitar"))

print(band.keys())

print(band.values())

print(band.items())

print("guitar" in band)
print("triangle" in band)

band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})

print(band)

print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem())
print(band)

band["drums"] = "Bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2

# band2 = band
# print("Bad copy!")
# print(band)
# print(band2)

# band2["drums"] = "Dave"
# print(band)

band2 = band.copy()
band2["drums"] = "Dave"
print(band)
print(band2)
