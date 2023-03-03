myDict = {"Name":"Rohit", "Age":20, "Gender":"Male", "List":[24, 52, 0.26, "Arabic"], "anotherDict":{"Sub":"Maths"}}

print(myDict.items())
print(myDict.keys())
print(myDict.values())

updateDict = {
    "Om":"Brother"
}
myDict.update(updateDict)
print(myDict)