class Messages:
    
    def inputData(self,messages):
        self.__messages = messages
        new_files = open("messages.txt","w", encoding='utf-8')

        new_files.writelines(messages)

        new_files.close()
    
    def outputData(self):
        files = open("messages.txt","r", encoding='utf-8')
        messages = []
        messages = files.readlines()
        self.__messages = messages[0]
        return self.__messages

if __name__ == "__main__":
    news = Messages()
    news.inputData("測試用")
    print(news.outputData())