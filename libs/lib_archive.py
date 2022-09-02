def load(cd, ad):
    print("loading archive")
    import glob
    import json
    all_shows=[]
    z=(glob.glob(ad  + cd+"/*"))
    #print (z)
    for i in range(len(z)):
        with open(z[i]) as d:
            dictData = json.load(d)
            all_shows.append(dictData)



    return all_shows


if __name__ == "__main__":


    x=load("future_shows","C:/Users/kw/AppData/Roaming/demo3/")
    print (x)