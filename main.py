############################
# project : 2021 phyton 1  #          
# Date    :2021/07/16      #        
# Author  :Kenny           #
# ######################## #  
import random
import Player
import Chance
import Dana
import Stores
import playMap
import Messages
area = 24
def playerPo(steps):
    if (steps >= area):
        return (steps % area)
    else:
        return steps

## 清除舊資料
def clearOldData():
    files = open('players.csv','w',encoding='utf-8')
    files.truncate()
    titles = "id,name,money,po,status\n"
    files.writelines(titles)
    files.close()
    files = open('messages.txt','w',encoding='utf-8')
    files.truncate()
    titles = "遊戲即將開始...."
    files.writelines(titles)
    files.close()


if __name__ == "__main__" :
    playernum = eval(input('請輸入玩家人數'))
    players = []
    clearOldData()
    for i in range(playernum):
        players.append(Player.Player())
        # 要求玩家輸入玩家名稱
        players[i].setName(input("請輸入玩家名稱:"),i)
        
    # 設定玩家位置值
    player_po = []
    for i in range(playernum):
        player_po.append(0)
    i=0
    map=playMap.playMap()

#####################################################
    news = Messages.Messages()
    news.inputData("請按下《ＥＮＴＥＲ》進行遊戲")
    map.printMap(player_po)
    input()

#######################################################

    while True :
        ##########################33 計算可遊戲玩家
        new_players_num = 0
        for num in range(len(players)):
            if (players[num].getStatus() != -1):
                new_players_num = new_players_num + 1
        players_num = new_players_num
        if (players_num == 1):
            news.inputData("只剩下一位玩家！遊戲結束！")
            map.printMap(player_po)
            break
        if (players[i].getStatus() == -1):
            news.inputData(map.transferNo(str(i+1)) + "號玩家己破產《ＥＮＴＥＲ》")
            map.printMap(player_po)
            input()
            i = i + 1
            if (i >= players_num):
                i = i - players_num
            continue
        elif (players[i].getStatus() > 0):
            newstatus = players[i].getStatus() - 1
            players[i].setStatus(-1)
            news.inputData(map.transferNo(str(i+1)) + "號玩家休息" + map.transferNo(str(newstatus)) + "次")
            map.printMap(player_po)
            input()
            i = i + 1
            if (i >= players_num):
                i = i - players_num
            continue
        ############     骰子       #############
        oldpo = players[i].getPos()
        newstep = random.randrange(1,6)
        news.inputData(map.transferNo(str(i+1)) + "號玩家擲骰子：" + map.transferNo(str(newstep)) + "點")
        map.printMap(player_po) # 印地圖
        # 設定玩家新的位置
        players[i].setPos(newstep)
    ##### c.) 移動到骰子點數的框格
        newpo = players[i].getPos()
        
        #　I. 可能經過起點
        if ((int(newpo/area) > int(oldpo/area)) and ((newpo % area) != 0)):
            news.inputData(map.transferNo(str(i+1)) + "號玩家越過「開始」位置《ＥＮＴＥＲ》")
            players[i].setMoney(2000,i)
            map.printMap(player_po)
            input()
            news.inputData(map.transferNo(str(i+1)) + "號玩家得２０００《ＥＮＴＥＲ》")

        newpo = playerPo(newpo)
        player_po[i] = str(newpo)
        map.printMap(player_po)
        input()
        news.inputData(map.transferNo(str(i+1)) + "號玩家在新位置：" + map.transferNo(str(newpo)) + "《ＥＮＴＥＲ》")
        map.printMap(player_po)
        input()
        #  II. 可能落在邊角框格
        if (newpo == 0):
            news.inputData(map.transferNo(str(i+1)) + "號玩家回到「開始」位置《ＥＮＴＥＲ》")
            players[i].setMoney(2000,i)
            map.printMap(player_po)
            input()
            news.inputData(map.transferNo(str(i+1)) + "號玩家得２０００《ＥＮＴＥＲ》")
        elif (newpo  == 6):
            players[i].setStatus(3)
            news.inputData(map.transferNo(str(i+1)) + "玩家坐牢,休息三次《ＥＮＴＥＲ》")
            map.printMap(player_po)
            input()
        elif (newpo  == 18):
            players[i].setStatus(1)
            news.inputData(map.transferNo(str(i+1)) + "玩家休息一次《ＥＮＴＥＲ》")
            map.printMap(player_po)
            input()
        elif (newpo == 12):
            players[i].setStatus(0)
            news.inputData(map.transferNo(str(i+1)) + "路過,在玩一次《ＥＮＴＥＲ》")
            map.printMap(player_po)
            input()
        ###########    機會牌    ##################
        elif newpo == 10 or newpo == 21 :
            mychance=Chance.Chance()
            chance=mychance.choice()
            players[i].setMoney(int(chance[1]),i)
            news.inputData(map.transferNo(str(i+1)) + "號玩家中命運：" + chance[0])
            map.printMap(player_po)
            input()


        ###########   命運牌     ####################
        elif newpo == 2 or newpo == 15 :
            mydana = Dana.dana()
            dana=mydana.choice()
            players[i].setMoney(int(dana[1]),i)
            news.inputData(map.transferNo(str(i+1)) + "號玩家中命運：" + dana[0])
            map.printMap(player_po)
            input()
    
        elif newpo == 9 :
            playerStore = Stores.Stores()
            store = playerStore.getStoreData(str(newpo))
            news.inputData(map.transferNo(str(i+1)) + "玩家需要繳電費")
            players[i].setMoney(0-int(store[3]),i)
            input()
        elif newpo == 22 :
            playerStore = Stores.Stores()
            store = playerStore.getStoreData(str(newpo))
            news.inputData(map.transferNo(str(i+1)) + "玩家需要繳稅")
            players[i].setMoney(0-int(store[3]),i)
            input()

        ###########
        #############################################
        ############  地產     ######################  
        else:
            playerStore = Stores.Stores()
            store = playerStore.getStoreData(str(newpo))
            ## 判斷是否有人己取得該地產所有權了
            if store[2] == '-1':
                #print("該地產無人所有！")
                news.inputData("該地產無人所有！是否買進？（Ｙ｜Ｎ）")
                map.printMap(player_po)
                results = input()
                if ((results == 'Y') or (results == 'y')):
                    store[2] = str(i+1)
                    playerStore.setStoreData(store)
                    players[i].setMoney(0-int(store[3]),i)
                    news.inputData(map.transferNo(str(i+1)) + "號玩家買進地產：" + store[1])
                    map.printMap(player_po)
                    input()
                else:
                    news.inputData(map.transferNo(str(i+1)) + "號玩家放棄買進")
                    map.printMap(player_po)
                    input()
            else:
                #print("該地產為：" + str(players[int(store[2])-1].getName()) + "所有")
                news.inputData("該地產為：" + store[2] + "號玩家所有")
                map.printMap(player_po)
                input()
                if  ( int(store[2]) == players[i] ):
                    news.inputData("不需支付費用給自已")
                    map.printMap(player_po)
                    input()

                else:
                    news.inputData("需支付：" + map.transferNo(store[3]))
                    map.printMap(player_po)
                    input()
                    # 需付費玩家
                    players[i].setMoney(0-int(store[3]),i)
                    # 收費玩家
                    players[int(store[2])-1].setMoney(int(store[3]),int(store[2])-1)
                    map.printMap(player_po)
                    input()
                playerStore = None
        ###############################
        i+=1 
        if (i >= playernum):
            i-=playernum
        ##############end
        end = input ('是否結束(Y/N)')
        if (end == 'Y') or (end == 'y'):
            break 