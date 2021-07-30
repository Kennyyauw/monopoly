import csv

class Stores:

    def __init__(self):
        self.__id = []
        self.__name = []
        self.__owner = []
        self.__prize = []
        with open('stores.csv',newline='',encoding='utf-8') as csvfile:
            rows = csv.DictReader(csvfile)
            for row in rows:
                self.__id.append(row['ID'])
                self.__name.append(row['name'])
                self.__owner.append(row['owner'])
                self.__prize.append(row['prize'])

    def getStoreData(self,po):
        index = self.__id.index(po)
        return [self.__id[index],self.__name[index],self.__owner[index],self.__prize[index]]

    def setStoreData(self,newdata):
        index = self.__id.index(newdata[0])
        self.__owner[index] = newdata[2]
        with open('stores.csv', 'w', newline='',encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            length = len(self.__id)
            writer.writerow(['ID','name','owner','prize'])
            for i in range(0,length):
                writer.writerow([self.__id[i],self.__name[i],self.__owner[i],self.__prize[i]])

if __name__ == "__main__":
    myStore = Stores()
    result = myStore.getStoreData(str(4))
    print(result)
    result[2] = '1'
    myStore.setStoreData(result)
    newresult = myStore.getStoreData(str(4))
    print(newresult)