import sys
sys.path.append('/Users/davidkuchelmeister/Documents/PycharmProjects/Code_Summary/RaspberryPie/')
import WriteTreePathFile

text = """
#!/usr/bin/expect
        spawn scp -r /Users/davidkuchelmeister/Documents/Coding/Blockchain pi@192.168.10.24:/home/pi/Downloads
        set pass "melon"
        expect {
        password: {send "$pass/r"; exp_continue}
                  }
"""

# print(text)



### Get Path
root_dir = "/Users/davidkuchelmeister/Pictures/"
folder = ["Bilder Fotodecke/","Fotos aus Studium","Fotoshooting Mam 60.","Gute alte Zeiten","Klassen Fotos Wi13b","paps Bilder","Sonja"]

WriteTreePathFile.WriteTreePathFile(root_dir,folder)