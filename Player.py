import csv
import Messages
class Player:
    # 初始化玩家，每人發 20000 遊戲幣以及出發位置為 0
    def __init__(self,money = 20000, po = 0):
        self.__money = money
        self.__po = po
        self.__status = 0

    # 設定玩家名稱
    def setName(self,name,id):
        self.__name = name
        self.__id = id
        with open('players.csv','a',newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow([self.__id,self.__name,self.__money,self.__po,self.__status])

    # 取得玩家名稱
    def getName(self):
        return self.__name
        
    # 修改玩家遊戲幣
    def setMoney(self,money,id):
        news = Messages.Messages()
        self.__money += money
        table = [['id','name','money','po','status']]
        with open('players.csv','r',newline='') as csvfile:
            rows = csv.DictReader(csvfile)
            for row in rows:
                if (row.get('id') == str(id)):
                    newmoney = int(row['money'])+money
                    if (newmoney < 0):
                        news.inputData("玩家破產，出局了！")
                        row['status'] = '-1'
                        self.__status = -1
                        newmoney = 0000
                    row['money'] = str(newmoney)
                table.append([row['id'],row['name'],row['money'],row['po'],row['status']])
        with open('players.csv','w',newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(table)
        
    # 取得玩家遊戲幣
    def getMoney(self):
        return self.__money
        
    # 修改玩家位置
    def setPos(self,move):
        self.__po += move
        
    # 取得玩家位置
    def getPos(self):
        return self.__po

    # 取得玩家狀態
    def getStatus(self):
        return self.__status

    # 設定玩家狀態
    def setStatus(self,status):
        self.__status = self.__status + status


if __name__ == "__main__":
    myplayer = Player()
    myplayer.getStatus()