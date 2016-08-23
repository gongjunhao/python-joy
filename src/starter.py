import subprocess
import _thread

taskList = [
    'D:\Program Files\VPS\\Shadowsocks.exe',
    'D:\\Program Files\\QQ\\Bin\\QQ.exe',
    'D:\\Program Files\\JetBrains\\IntelliJ IDEA 14.1.4\\bin\\idea.exe'
    ]

def startProcess(task):
   subprocess.call([task], shell=True)


def main():
    for index, task in enumerate(taskList):
       _thread .start_new_thread(startProcess, (task,))
 
if __name__ == '__main__':
   main()
   input("Press Enter to exit...")
