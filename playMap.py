import Stores
import csv
import Messages
class playMap:

    __mapEmpty = "　"
    __mapWall = "｜"
    __mapLine = "－"
    myStores = None

    def printMap(self,userPo):
        self.myStores = Stores.Stores()
        # 新程式區塊
        for k in range(1,28):
            # 印出第一、二、三行
            if (( k == 1 ) or (k == 2) or ( k == 3)):
                self.printmap1(k,0,7,userPo)
            
            # 印出第四行，以及第二十四行
            if (( k == 4 ) or ( k == 24 )):
                print(48*self.__mapLine)

            # 印出第五、六、七行，九、十、十一行，十三、十四、十五行，十七、十八、十九行，二十一、二十二、二十三行    
            if (( k == 5 ) or (k == 6) or ( k == 7)):
                self.printmap2(k,23,7,userPo)
            if (( k == 9 ) or (k == 10) or ( k == 11)):
                self.printmap2(k,22,8,userPo)
            if (( k == 13 ) or (k == 14) or ( k == 15)):
                self.printmap2(k,21,9,userPo)
            if (( k == 17 ) or (k == 18) or ( k == 19)):
                self.printmap2(k,20,10,userPo)
            if (( k == 21 ) or (k == 22) or ( k == 23)):
                self.printmap2(k,19,11,userPo)        
            # 印出第八、十二、十六、二十行
            if (( k == 8 ) or (k == 12) or ( k == 16) or ( k == 20)):
                print(7*self.__mapLine + 34*self.__mapEmpty + 7*self.__mapLine)
            # 印出第二十五、二十六、二十七行    
            if (( k == 25 ) or (k == 26) or ( k == 27)):
                self.printmap1(k,18,11,userPo)

        self.myStores = None
            
    # 列印地圖程式
    def printmap1(self,k,min,max,userPo):
        if (max-min) > 0 :
            j = 1
        else:
            j = -1
        if ((k == 1) or (k == 25)):
            for i in range(min,max,j):
                if (self.myStores.getStoreData(str(i))[2] == "-1"):
                    owner = "　"
                else:
                    owner = self.transferNo(self.myStores.getStoreData(str(i))[2])
                print(self.__mapEmpty + self.getStoreName(self.myStores.getStoreData(str(i))[1]) + owner,end = '')
                if ((i < 6) or (i > 12)):
                    print(self.__mapWall,end = '')
                else:
                    print()

        elif (( k == 2) or (k == 26)):
            for i in range(min,max,j):
                print(self.__mapEmpty + self.getStoreName(self.transferNo(self.myStores.getStoreData(str(i))[3])) + self.__mapEmpty,end = '')
                if ((i < 6) or (i > 12)):
                    print(self.__mapWall,end='')
                else:
                    print()

        elif (( k == 3) or (k == 27)):
            po_tmp = ""
            for i in range(min,max,j):
                po_tmp = self.__mapEmpty
                for l in range(len(userPo)):
                    if (userPo[l] == str(i)):
                        po_tmp = po_tmp + self.transferNo(str(l+1))
                    else:
                        po_tmp = po_tmp + self.__mapEmpty

                # 若人數不足四人則補足其它空間
                if (len(userPo)<4):
                    po_tmp = po_tmp + (4-len(userPo))*self.__mapEmpty

                po_tmp = po_tmp + self.__mapEmpty
                if ((i < 6) or (i > 12)):
                    print(po_tmp + self.__mapWall,end = '')
                else:
                    print(po_tmp,end = '')
            print()

    def printmap2(self,k,min,max,userPo):
        for i in (min,max):
                if (self.myStores.getStoreData(str(i))[2] == "-1"):
                    owner = "　"
                else:
                    owner = self.transferNo(self.myStores.getStoreData(str(i))[2])
        if (( k == 5) or ( k == 9) or( k == 13) or( k == 17) or( k == 21)):
            lines = ""
            lines = lines + self.__mapEmpty + self.getStoreName(self.myStores.getStoreData(str(min))[1]) + owner + self.__mapWall
            if (( k == 9) or ( k == 13)):
              messages = self.getUserData(k)
              lines = lines + 6*self.__mapEmpty + messages + 6*self.__mapEmpty
            else:
              lines = lines + 34*self.__mapEmpty
            lines = lines + self.__mapWall + self.__mapEmpty + self.getStoreName(self.myStores.getStoreData(str(max))[1]) + owner
            print(lines)

        elif (( k == 6) or ( k == 10) or( k == 14) or( k == 18) or( k == 22)):
            lines = ""
            lines = lines + self.__mapEmpty + self.getStoreName(self.transferNo(self.myStores.getStoreData(str(min))[3])) + self.__mapEmpty + self.__mapWall
            if (k == 6):
                lines = lines + 6*self.__mapEmpty + "歡迎參加大富翁文字桌遊　請儘量嫌棄畫面太醜！" + 6*self.__mapEmpty
            else:
                lines = lines + 34*self.__mapEmpty

            lines = lines + self.__mapWall + self.__mapEmpty + self.getStoreName(self.transferNo(self.myStores.getStoreData(str(max))[3])) + self.__mapEmpty
            print(lines)

        elif (( k == 7) or ( k == 11) or( k == 15) or( k == 19) or( k == 23)):
            po_tmp = ""
            lines = self.__mapEmpty
            for j in range(len(userPo)):
                if (userPo[j] == str(str(min))):
                    po_tmp = po_tmp + self.transferNo(str(j+1))
                else:
                    po_tmp = po_tmp + self.__mapEmpty
            # 若人數不足四人則補足其它空間
            if (len(userPo)<4):
                po_tmp = po_tmp + (4-len(userPo))*self.__mapEmpty
            po_tmp = po_tmp + self.__mapEmpty
            lines = lines + po_tmp + self.__mapWall
            po_tmp = ""
            if (( k == 11) or ( k == 15)):
              messages = self.getUserData(k)
              lines = lines + 6*self.__mapEmpty + messages + 6*self.__mapEmpty
            elif ((k == 23)):
                news = self.getMessages()
                lines = lines + 6*self.__mapEmpty + news + 6*self.__mapEmpty
            else:
                lines = lines + 34*self.__mapEmpty
            for j in range(len(userPo)):
                if (userPo[j] == str(str(max))):
                    po_tmp = po_tmp + self.transferNo(str(j+1))
                else:
                    po_tmp = po_tmp + self.__mapEmpty
            po_tmp = po_tmp + self.__mapEmpty
            lines =  lines + self.__mapWall + self.__mapEmpty + po_tmp
            print(lines)

    # 控制每一行的格式大小
    def getStoreName(self,data):
        storeName = ""
        if (len(data) <= 4):
            storeName = data + (4-len(data))*"　"
        return storeName

    # 半形全形轉換功能
    def transferNo(self,data):
        nums = (0,"０",1,"１",2,"２",3,"３",4,"４",5,"５",6,"６",7,"７",8,"８",9,"９")
        tmp = []
        dataleng = len(data)
        for j in range(0,dataleng):
            tmp.append(0)

        newdata = ""
        for i in range(1,dataleng+1):
            tmp[(dataleng-i)] = int(data)%10
            data = int(int(data) / 10)

        for i in range(0,len(tmp)):
            newdata += nums[nums.index(tmp[i])+1]

        return newdata

    # 取得玩家資料內容
    def getUserData(self,k):
        messages = ""
        with open('players.csv', newline='') as csvfile:
            players = csv.DictReader(csvfile)
            for player in players:
                if (k == 9):
                   if (player.get('id') == '0'):
                       money = self.transferNo(str(player.get('money')))
                       messages = "１號玩家：　" + money
                if ( k == 11):
                   if (player.get('id') == '1'):
                       money = self.transferNo(str(player.get('money')))
                       messages = "２號玩家：　" + money
                if ( k == 13):
                   if (player.get('id') == '2'):
                       money = self.transferNo(str(player.get('money')))
                       messages = "３號玩家：　" + money
                if ( k == 15):
                   if (player.get('id') == '3'):
                       money = self.transferNo(str(player.get('money')))
                       messages = "４號玩家：　" + money       
            if len(messages) < 22:
                messages = messages + (22-len(messages))*self.__mapEmpty
            return messages

    # 取得訊息行的資料
    def getMessages(self):
        news = Messages.Messages()
        messages = news.outputData()
        if (len(messages) < 22):
           hello = messages + (22-len(messages))*self.__mapEmpty 
        return hello

if __name__ == "__main__":
    myMap = playMap()
    userPo = ['11']
    myMap.printMap(userPo)
