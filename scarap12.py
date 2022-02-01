# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scrapping1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import requests,time,random
from bs4 import BeautifulSoup
from selenium import webdriver
import sys
import os

class Ui_MainWindow1(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-1, -1, 801, 601))
        self.frame.setStyleSheet("background-color: rgb(215, 203, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(180, 30, 371, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(100, 100, 551, 421))
        self.frame_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(0, 0, 0, 124));")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(170, 40, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:20px;")
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(150, 340, 91, 31))
        self.pushButton.setStyleSheet("background-color: rgb(0, 255, 255);\n"
"border-radius:5px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 340, 91, 31))
        self.pushButton_2.setStyleSheet("background-color: rgb(85, 255, 127);\n"
"border-radius:5px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setGeometry(QtCore.QRect(390, 340, 91, 31))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"border-radius:5px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 90, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:20px;")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(40, 50, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(0, 0, 0, 0));\n"
"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(0, 0, 0, 0));\n"
"color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 160, 311, 41))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 210, 311, 41))
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(80, 280, 421, 31))
        self.label_4.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(171, 86, 86, 0));\n"
"color: rgb(255, 85, 0);")
        self.label_4.setText("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Linkedin Web Scrapper"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "ENTER THE USERNAME"))
        self.pushButton.setText(_translate("MainWindow", "SCRAP"))
        self.pushButton_2.setText(_translate("MainWindow", "OPEN CSV"))
        self.pushButton_3.setText(_translate("MainWindow", "EXIT"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "ENTER THE PASSWORD"))
        self.label_2.setText(_translate("MainWindow", "Email  :"))
        self.label_3.setText(_translate("MainWindow", "Password :"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "ENTER WHAT BASES YOU ARE SEACHING"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "ENTER TTHE NUMBER OF PROFILES"))


    def scrap(self):
       browser=webdriver.Chrome('C:/Users/AtharvKulkarni/chromedriver_win32/chromedriver.exe')
       browser.get('https://www.linkedin.com/uas/login')
       username = self.lineEdit.text()
       password = self.lineEdit_2.text()

       elementID=browser.find_element_by_id('username')
       elementID.send_keys(username)

       elementID=browser.find_element_by_id('password')
       elementID.send_keys(password)

       elementID.submit()

       #Scraping the Profile links
       dev = self.lineEdit_3.text()
       dev = dev.replace(' ','%20')
       #Use below four lines only for first time
       #f = open(dev+'Employee_info_Database.csv', 'w')
       #writer = csv.writer(f)
       #writer.writerow(["Link to profile","Name","Location","Job","Connections on linkedin","Company name & Job type","Job Title","Date from Active in company","Experience","College name","Degree name","Stream name","College years","Phone Number","Email ID",	"Website link"])
       #f.close()
       count = self.lineEdit_4.text()
       count = int(count)
       if count%10 != 0:
          page_count = count//10 +1
       else:
          page_count = count//10
       page_count = int(page_count)+1
       count = int(count)*2+1

       for j in range(1,page_count,1):
        link = 'https://www.linkedin.com/search/results/people/?keywords='+dev+'&origin=SWITCH_SEARCH_VERTICAL&page='+str(j)+'&sid=HN4'
        browser.get(link)

        SCROLL_PAUSE_TIME=5

        last_height=browser.execute_script("return document.body.scrollHeight")

        for i in range(3):
          browser.execute_script("window.scrollTo(0, document.body.scroll.Height);")

          time.sleep(SCROLL_PAUSE_TIME)

          new_height = browser.execute_script("return document.body.scrollHeight")
          if new_height == last_height:
            break
            last_height==new_height
        src = browser.page_source
        soup = BeautifulSoup(src,'html.parser')
        soup
        links = soup.find('div', {'class':'ph0 pv2 artdeco-card mb2'})
        f = open(dev+".txt", "a")
    # traverse paragraphs from soup
        if link != None:
         for link in links.find_all("a"):
            data = link.get('href')
            f.write(data)
            f.write("\n")

        f.close()
       browser.close()
       time.sleep(2)
       browser=webdriver.Chrome('C:/Users/AtharvKulkarni/chromedriver_win32/chromedriver.exe')
       browser.get('https://www.linkedin.com/uas/login')
       username = self.lineEdit.text()
       password = self.lineEdit_2.text()

       elementID=browser.find_element_by_id('username')
       elementID.send_keys(username)

       elementID=browser.find_element_by_id('password')
       elementID.send_keys(password)

       elementID.submit()


#Scraping the Final Data
       file_object = open(dev+".txt","r")
       links_list = []
       for fo in file_object:
           site = fo.strip()
           links_list.append(site)
       for q in range(1,count,2):
        if links_list[q][25:31] != 'search':
          link = links_list[q]
          c = '?'
          k = link.find(c)
          print(k)
          m = link[:k]+'/'
          print(m)
          browser.get(m)

          SCROLL_PAUSE_TIME=5

          last_height=browser.execute_script("return document.body.scrollHeight")

          for i in range(3):
            browser.execute_script("window.scrollTo(0, document.body.scroll.Height);")

            time.sleep(SCROLL_PAUSE_TIME)

            new_height = browser.execute_script("return document.body.scrollHeight")

            if new_height == last_height:
                break
                last_height==new_height
          src = browser.page_source
          soup = BeautifulSoup(src,'html.parser')
          soup

          name_div = soup.find('div' , {'class':'ph5 pb5'})

          if soup.find('div' , {'class':'ph5 pb5'})  != None:
            name_div = soup.find('div' , {'class':'ph5 pb5'})
          elif soup.find('div' , {'class':'mt2 relative'})  != None:
            name_div = soup.find('div' , {'class':'mt2 relative'})
          else:
            name_div = '-'
          name_div

          if name_div == "-":
            name_loc = '-'
          else:
            name_loc=name_div.find_all('ul')
          name_loc

          if name_div == "-":
            name = "-"
          else:
            name = name_div.find('h1' , attrs={'class':'text-heading-xlarge inline t-24 v-align-middle break-words'}).get_text().strip()
          name

          if name_div == "-":
            loc = "-"
          else:
            loc = name_div.find('span' , attrs={'class':'text-body-small inline t-black--light break-words'}).get_text().strip()
          loc


          if name_div == "-":
            job_title = "-"
          else:
            job_title = name_div.find('div' , attrs={'class':'text-body-medium break-words'}).get_text().strip()
          job_title

          if name_div == "-":
            connections = "-"
          elif name_div.find('span' , attrs={'class':'t-bold'}) == None:
            connections = "500+"
          else:
            connections = name_div.find('span' , attrs={'class':'t-bold'}).get_text().strip()
          connections



          info=[]
          info.append(link)
          info.append(name)
          info.append(loc)
          info.append(job_title)
          info.append(connections)
          info
          if soup.find('section', attrs={'id':'experience-section'}) != None:
            exp_section = soup.find('section', attrs={'id':'experience-section'})
          else:
            exp_section = "-"
          exp_section

          exp_section


          if exp_section == "-":
            a_tags = "-"
            if exp_section.find('ul') == None:
                a_tags = "-"
            elif exp_section == -1:
                a_tags = "-"
          else:
            exp_section = exp_section.find('ul')
            li_tags = exp_section.find('div')
            a_tags = li_tags.find('a')
          a_tags


          if a_tags.find('h3') == None:
            work_title = "-"
          elif a_tags == "-":
            work_title = "-"
          else:
            work_title = a_tags.find('h3').get_text().strip()
          work_title
          if a_tags == "-":
            company_name = "-"
          elif a_tags.find('p',{'class':'pv-entity__secondary-title t-14 t-black t-normal'}) == None:
            company_name = "-"
          else:
            company_name = a_tags.find('p',{'class':'pv-entity__secondary-title t-14 t-black t-normal'}).get_text().strip()
            company_name = company_name.replace('\n',' ')
          company_name


          if a_tags == "-":
            joining_date = "-"
          elif a_tags.find('h4',{'class':'pv-entity__date-range t-14 t-black--light t-normal'}) == None:
            joining_date = "-"
          else:
            joining_date = a_tags.find('h4',{'class':'pv-entity__date-range t-14 t-black--light t-normal'}).get_text().strip()
          joining_date

          if a_tags == "-":
            exp = "-"
          elif a_tags.find('span',{'class':'pv-entity__bullet-item-v2'}) == None:
            exp = "-"
          else:
            exp = a_tags.find('span',{'class':'pv-entity__bullet-item-v2'}).get_text().strip()
          exp

          info.append(company_name)
          info.append(work_title)
          info.append(joining_date)
          info.append(exp)
          info
          if soup.find('section', attrs={'id':'education-section'}) == None:
            edu_section = "-"
          else:
            edu_section = soup.find('section', attrs={'id':'education-section'})
          edu_section


          if edu_section == "-":
            college_name = "-"
          elif edu_section.find('h3') == None:
            college_name = "-"
          elif edu_section.find('h3') == -1:
            college_name = "-"
          else:
            college_name = edu_section.find('h3').get_text().strip()
          college_name


          if edu_section == "-":
            degree_name = "-"
          elif edu_section.find('p',{'class':'pv-entity__secondary-title pv-entity__degree-name t-14 t-black t-normal'}) == None:
            degree_name = "-"
          elif edu_section.find('p',{'class':'pv-entity__secondary-title pv-entity__degree-name t-14 t-black t-normal'}) == -1:
            degree_name = "-"
          else:
            degree_name = edu_section.find('p',{'class':'pv-entity__secondary-title pv-entity__degree-name t-14 t-black t-normal'}).find_all('span')[1].get_text().strip()
          degree_name


          if edu_section == "-":
            stream_name = "-"
          elif edu_section.find('p',{'class':'pv-entity__secondary-title pv-entity__fos t-14 t-black t-normal'}) == None:
            stream_name = "-"
          else:
            stream_name = edu_section.find('span',{'class':'pv-entity__comma-item'}).get_text().strip()



          if edu_section == "-":
            degree_year = "-"
          elif edu_section.find('p',{'class':'pv-entity__dates t-14 t-black--light t-normal'}) == None:
            degree_year = "-"
          else:
            degree_year = edu_section.find('p',{'class':'pv-entity__dates t-14 t-black--light t-normal'}).find_all('span')[1].get_text().strip()
          degree_year



          info.append(college_name)
          info.append(degree_name)
          info.append(stream_name)
          info.append(degree_year)


          info


          contact_link = m+'detail/contact-info/'
          browser.get(contact_link)


          src = browser.page_source
          soup = BeautifulSoup(src,'lxml')
          soup


          if soup.find('span',{'class':'t-14 t-black t-normal'}) == None:
            number ="-"
          else:
            number = soup.find('span',{'class':'t-14 t-black t-normal'}).get_text().strip()
          number


          if soup.find('a',{'class':'pv-contact-info__contact-link link-without-visited-state t-14','rel':'noopener noreferrer'}) == None:
            email = "-"
          else:
            email = soup.find('a',{'class':'pv-contact-info__contact-link link-without-visited-state t-14','rel':'noopener noreferrer'}).get_text().strip()
          email


          if soup.find('a',{'class':'pv-contact-info__contact-link link-without-visited-state','rel':'noopener noreferrer'}) == None:
            website = "-"
          else:
            website = soup.find('a',{'class':'pv-contact-info__contact-link link-without-visited-state','rel':'noopener noreferrer'}).get_text().strip()
          website


          info.append(number)
          info.append(email)
          info.append(website)
          info
          from csv import writer

          # List
          List=[link,name,loc,job_title.encode('utf-8'),connections,company_name,work_title.encode('utf-8'),joining_date,exp,college_name,degree_name,stream_name,degree_year,number,email,website]

        # Open our existing CSV file in append mode
        # Create a file object for this file
          with open('Employee_info_Database.csv', 'a',newline = "") as f_object:

            # Pass this file object to csv.writer()
            # and get a writer object
            writer_object = writer(f_object)

            # Pass the list as an argument into
            # the writerow()
            writer_object.writerow(List)

            #Close the file object
            f_object.close()
       browser.close
       self.lineEdit.setText("")
       self.lineEdit_2.setText("")
       self.lineEdit_3.setText("")
       self.lineEdit_4.setText("")
       self.label_4.setText("CSV File is Ready")

    def ope1(self):
       self.filee=os.getcwd()+"\Employee_info_Database.csv"
       os.startfile(self.filee)
    def exs(self):
        sys.exit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.pushButton.clicked.connect(ui.scrap)
    ui.pushButton_2.clicked.connect(ui.ope1)
    ui.pushButton_3.clicked.connect(ui.exs)
    sys.exit(app.exec_())
