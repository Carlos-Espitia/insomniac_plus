# importing the required libraries 

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import * 
import sys

import os
from os.path import expanduser
import time
import datetime

#user dir
home = expanduser("~")

# 1. Subclass QRunnable thread 
# The main class for running long functions
class Runnable(QRunnable):
    def __init__(self):
        super().__init__()

    # Your long-running task goes here ...
    def run(self):
        ################
        bots = 2
        wait_time = 72000
        wait_time2 = datetime.timedelta(seconds=wait_time)
        device = ["emulator-5554", "emulator-5556", "emulator-5558", "emulator-5560"]
        usernames = ["carlos_.espitia", "emily.ricoo", "alec.lopez_", "nico.dimeo"]
        num_users = len(usernames)

        num_sessions = [2, 2, 2, 2]

        #
        #"interact", "clean", "interact/clean"
        #
        bot_mode = ["interact/clean", "interact/clean", "interact/clean", "interact/clean"]

        #interacting
        interact = ["@sydney.barker", "@chloebuchholtz", "@guthrie.richardson", "@hannahmharris1212"]
        interaction_count = "1000"
        successful_interactions_limit_per_source = "1000"
        interactions_limit_per_source = ["1000", "1000", "1000", "1000"]
        total_succesful_interactions_limit = ["300", "300", "300", "300"]
        follow_percentage = "100"
        follow_limit = ["300", "300", "300", "300"]
        likes_count = ["0", "0", "0", "0"]
        total_likes_limit = ["0", "0", "0", "0"]
        #cleaning
        #
        #"--unfollow", "--unfollow-followed-by-anyone", "--unfollow-non-followers"
        #
        UNF_mode = ["--unfollow", "--unfollow-non-followers", "--unfollow", "--unfollow-non-followers"]
        unfollow_limit = ["200", "200", "200", "200"]
        #following sort order
        #
        #"defualt", "latest", "earliest"
        #
        unfollow_sort = ["latest", "latest", "latest", "latest"]

        ###################
        #Account configs
        if bots == 1:
            ACC1_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[0]} --device {device[0]} --interact {interact[0]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[0]} --total-successful-interactions-limit {total_succesful_interactions_limit[0]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[0]} --likes-count {likes_count[0]} --total-likes-limit {total_likes_limit[0]}"
            ACC1_config_clean = f"python start.py --wait-for-device --no-speed-check --username {usernames[0]} --device {device[0]} --following-sort-order {unfollow_sort[0]} {UNF_mode[0]} {unfollow_limit[0]}"

            ACC2_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[1]} --device {device[0]} --interact {interact[1]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[1]} --total-successful-interactions-limit {total_succesful_interactions_limit[1]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[1]} --likes-count {likes_count[1]} --total-likes-limit {total_likes_limit[1]}"
            ACC2_config_clean = f"python start.py --wait-for-device --no-speed-check --username {usernames[1]} --device {device[0]} --following-sort-order {unfollow_sort[1]} {UNF_mode[1]} {unfollow_limit[1]}"

            ACC3_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[2]} --device {device[0]} --interact {interact[2]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[2]} --total-successful-interactions-limit {total_succesful_interactions_limit[2]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[2]} --likes-count {likes_count[2]} --total-likes-limit {total_likes_limit[2]}"
            ACC3_config_clean = f"python start.py --wait-for-device --no-speed-check --username {usernames[2]} --device {device[0]} --following-sort-order {unfollow_sort[2]} {UNF_mode[2]} {unfollow_limit[2]}"

            ACC4_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[3]} --device {device[0]} --interact {interact[3]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[3]} --total-successful-interactions-limit {total_succesful_interactions_limit[3]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[3]} --likes-count {likes_count[3]} --total-likes-limit {total_likes_limit[3]}"
            ACC4_config_clean = f"python start.py --wait-for-device --no-speed-check --username {usernames[3]} --device {device[0]} --following-sort-order {unfollow_sort[3]} {UNF_mode[3]} {unfollow_limit[3]}"

        if bots == 2:
            if num_users > 1:
                if num_users == 2:
                    ACC1_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[0]} --device {device[0]} --interact {interact[0]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[0]} --total-successful-interactions-limit {total_succesful_interactions_limit[0]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[0]} --likes-count {likes_count[0]} --total-likes-limit {total_likes_limit[0]}"
                    ACC1_config_clean = f"python start.py --wait-for-device --no-speed-check --username {usernames[0]} --device {device[0]} --following-sort-order {unfollow_sort[0]} {UNF_mode[0]} {unfollow_limit[0]}"

                    ACC2_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[1]} --device {device[1]} --interact {interact[1]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[1]} --total-successful-interactions-limit {total_succesful_interactions_limit[1]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[1]} --likes-count {likes_count[1]} --total-likes-limit {total_likes_limit[1]}"
                    ACC2_config_clean = f"python start.py --wait-for-device --no-speed-check --username {usernames[1]} --device {device[1]} --following-sort-order {unfollow_sort[1]} {UNF_mode[1]} {unfollow_limit[1]}"

                if num_users > 2:
                    ACC1_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[0]} --device {device[0]} --interact {interact[0]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[0]} --total-successful-interactions-limit {total_succesful_interactions_limit[0]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[0]} --likes-count {likes_count[0]} --total-likes-limit {total_likes_limit[0]}"
                    ACC1_config_clean = f"python start.py --wait-for-device --no-speed-check --username {usernames[0]} --device {device[0]} --following-sort-order {unfollow_sort[0]} {UNF_mode[0]} {unfollow_limit[0]}"

                    ACC2_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[1]} --device {device[0]} --interact {interact[1]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[1]} --total-successful-interactions-limit {total_succesful_interactions_limit[1]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[1]} --likes-count {likes_count[1]} --total-likes-limit {total_likes_limit[1]}"
                    ACC2_config_clean = f"python start.py --wait-for-device --no-speed-check --username {usernames[1]} --device {device[0]} --following-sort-order {unfollow_sort[1]} {UNF_mode[1]} {unfollow_limit[1]}"

                    ACC3_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[2]} --device {device[1]} --interact {interact[2]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[2]} --total-successful-interactions-limit {total_succesful_interactions_limit[2]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[2]} --likes-count {likes_count[2]} --total-likes-limit {total_likes_limit[2]}"
                    ACC3_config_clean = f"python start.py --wait-for-device --no-speed-check --username {usernames[2]} --device {device[1]} --following-sort-order {unfollow_sort[2]} {UNF_mode[2]} {unfollow_limit[2]}"

                    ACC4_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[3]} --device {device[1]} --interact {interact[3]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[3]} --total-successful-interactions-limit {total_succesful_interactions_limit[3]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[3]} --likes-count {likes_count[3]} --total-likes-limit {total_likes_limit[3]}"
                    ACC4_config_clean = f"python start.py --wait-for-device --no-speed-check --username {usernames[3]} --device {device[1]} --following-sort-order {unfollow_sort[3]} {UNF_mode[3]} {unfollow_limit[3]}"
            else:
                print("You must bot atleast 2 or more accounts to use 2 bots!")
                exit()

        if bots == 4:
            if num_users > 2:
                ACC1_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[0]} --device {device[0]} --interact {interact[0]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[0]} --total-successful-interactions-limit {total_succesful_interactions_limit[0]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[0]} --likes-count {likes_count[0]} --total-likes-limit {total_likes_limit[0]}"
                ACC1_config_clean = f"python start.py --wait-for-device --no-speed-check --username {usernames[0]} --device {device[0]} --following-sort-order {unfollow_sort[0]} {UNF_mode[0]} {unfollow_limit[0]}"

                ACC2_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[1]} --device {device[1]} --interact {interact[1]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[1]} --total-successful-interactions-limit {total_succesful_interactions_limit[1]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[1]} --likes-count {likes_count[1]} --total-likes-limit {total_likes_limit[1]}"
                ACC2_config_clean = f"python start.py --wait-for-device --no-speed-check --username {usernames[1]} --device {device[1]} --following-sort-order {unfollow_sort[1]} {UNF_mode[1]} {unfollow_limit[1]}"

                ACC3_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[2]} --device {device[2]} --interact {interact[2]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[2]} --total-successful-interactions-limit {total_succesful_interactions_limit[2]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[2]} --likes-count {likes_count[2]} --total-likes-limit {total_likes_limit[2]}"
                ACC3_config_clean = f"python start.py --wait-for-device --no-speed-check --username {usernames[2]} --device {device[2]} --following-sort-order {unfollow_sort[2]} {UNF_mode[2]} {unfollow_limit[2]}"

                ACC4_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[3]} --device {device[3]} --interact {interact[3]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[3]} --total-successful-interactions-limit {total_succesful_interactions_limit[3]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[3]} --likes-count {likes_count[3]} --total-likes-limit {total_likes_limit[3]}"
                ACC4_config_clean = f"python start.py --wait-for-device --no-speed-check --username {usernames[3]} --device {device[3]} --following-sort-order {unfollow_sort[3]} {UNF_mode[3]} {unfollow_limit[3]}"
            else:
                print("You must bot atleast 3 or more accounts to use 4 bots!")
                exit()

        #6 sessions
        max_sessions = 5
        S = 0

        def bot1():
            #Startup emulators
            os.chdir("C:\\LDPlayer\\LDPlayer4.0")
            if bots == 1:
                os.system("dnconsole.exe launch --index 0")
            if bots == 2:
                os.system("dnconsole.exe launch --index 0")
                os.system("dnconsole.exe launch --index 1")
            if bots == 4:
                os.system("dnconsole.exe launch --index 0")
                os.system("dnconsole.exe launch --index 1")
                os.system("dnconsole.exe launch --index 2")
                os.system("dnconsole.exe launch --index 3")
            #wait for emus to open
            print("sleeping for 10 seconds")
            time.sleep(10)
            ############

            os.chdir(f"{home}\\Insomniac-master")
            print(ACC1_config_interact)

            ################

            global S, max_sessions
            while S < max_sessions:
                if bots == 1:    
                    #######################################
                    if num_sessions[0] > S:
                        if bot_mode[0] == "interact":
                            os.system(ACC1_config_interact)

                        if bot_mode[0] == "clean":
                            os.system(ACC1_config_clean)

                        if bot_mode[0] == "interact/clean":
                            os.system(ACC1_config_interact)
                    #######################################
                    if num_sessions[1] > S:
                        if bot_mode[1] == "interact":
                            os.system(ACC2_config_interact)

                        if bot_mode[1] == "clean":
                            os.system(ACC2_config_clean)

                        if bot_mode[1] == "interact/clean":
                            os.system(ACC2_config_interact)
                    #######################################
                    if num_sessions[2] > S:
                        if bot_mode[2] == "interact":
                            os.system(ACC3_config_interact)

                        if bot_mode[2] == "clean":
                            os.system(ACC3_config_clean)

                        if bot_mode[2] == "interact/clean":
                            os.system(ACC3_config_interact)
                    #######################################
                    if num_sessions[3] > S:
                        if bot_mode[3] == "interact":
                            os.system(ACC4_config_interact)

                        if bot_mode[3] == "clean":
                            os.system(ACC4_config_clean)

                        if bot_mode[3] == "interact/clean":
                            os.system(ACC4_config_interact)
                    #######################################

                    output_S = S
                    output_S += 1
                    print(f"ALL ACCS session {output_S} done!")
                    S += 1
                    print(f"Sleeping for {wait_time2}")
                    os.system(f"TIMEOUT /T {wait_time} /NOBREAK")

                    #######################################
                    if num_sessions[0] > S:
                        if bot_mode[0] == "interact":
                            os.system(ACC1_config_interact)

                        if bot_mode[0] == "clean":
                            os.system(ACC1_config_clean)

                        if bot_mode[0] == "interact/clean":
                            os.system(ACC1_config_clean)
                    #######################################
                    if num_sessions[1] > S:
                        if bot_mode[1] == "interact":
                            os.system(ACC2_config_interact)

                        if bot_mode[1] == "clean":
                            os.system(ACC2_config_clean)

                        if bot_mode[1] == "interact/clean":
                            os.system(ACC2_config_clean)
                    #######################################
                    if num_sessions[2] > S:
                        if bot_mode[2] == "interact":
                            os.system(ACC3_config_interact)

                        if bot_mode[2] == "clean":
                            os.system(ACC3_config_clean)

                        if bot_mode[2] == "interact/clean":
                            os.system(ACC3_config_clean)
                    #######################################
                    if num_sessions[3] > S:
                        if bot_mode[3] == "interact":
                            os.system(ACC4_config_interact)

                        if bot_mode[3] == "clean":
                            os.system(ACC4_config_clean)

                        if bot_mode[3] == "interact/clean":
                            os.system(ACC4_config_clean)
                    #######################################

                    output_S = S
                    output_S += 1
                    print(f"ALL ACCS session {output_S} done!")
                    S += 1
                    print(f"Sleeping for {wait_time2}")
                    os.system(f"TIMEOUT /T {wait_time} /NOBREAK")


        ############################
        #2BOTS ##################### 
        ############################

                if bots == 2:
                    if S == 0:
                        os.chdir(f"{home}\\Insomniac++")
                        os.system("start cmd.exe /c python bot2.py")
                        os.chdir(f"{home}\\Insomniac-master")

                    if num_users == 2:
                        #######################################
                        if num_sessions[0] > S:
                            if bot_mode[0] == "interact":
                                os.system(ACC1_config_interact)

                            if bot_mode[0] == "clean":
                                os.system(ACC1_config_clean)

                            if bot_mode[0] == "interact/clean":
                                os.system(ACC1_config_interact)
                        #######################################

                        output_S = S
                        output_S += 1
                        print(f"ACC1 session {output_S} done!")
                        S += 1
                        print(f"Sleeping for {wait_time2}")
                        os.system(f"TIMEOUT /T {wait_time} /NOBREAK")

                        #######################################
                        if num_sessions[0] > S:
                            if bot_mode[0] == "interact":
                                os.system(ACC1_config_interact)

                            if bot_mode[0] == "clean":
                                os.system(ACC1_config_clean)

                            if bot_mode[0] == "interact/clean":
                                os.system(ACC1_config_clean)
                        #######################################

                        output_S = S
                        output_S += 1
                        print(f"ACC1 session {output_S} done!")
                        S += 1
                        print(f"Sleeping for {wait_time2}")
                        os.system(f"TIMEOUT /T {wait_time} /NOBREAK")

                    else:
                        if num_sessions[0] > S:
                            if bot_mode[0] == "interact":
                                os.system(ACC1_config_interact)

                            if bot_mode[0] == "clean":
                                os.system(ACC1_config_clean)

                            if bot_mode[0] == "interact/clean":
                                os.system(ACC1_config_interact)
                        #######################################
                        if num_sessions[1] > S:
                            if bot_mode[1] == "interact":
                                os.system(ACC2_config_interact)

                            if bot_mode[1] == "clean":
                                os.system(ACC2_config_clean)

                            if bot_mode[1] == "interact/clean":
                                os.system(ACC2_config_interact)
                        #######################################

                        output_S = S
                        output_S += 1
                        print(f"1st and 2nd ACCS session {output_S} done!")
                        S += 1
                        print(f"Sleeping for {wait_time2}")
                        os.system(f"TIMEOUT /T {wait_time} /NOBREAK")

                        #######################################
                        if num_sessions[0] > S:
                            if bot_mode[0] == "interact":
                                os.system(ACC1_config_interact)

                            if bot_mode[0] == "clean":
                                os.system(ACC1_config_clean)

                            if bot_mode[0] == "interact/clean":
                                os.system(ACC1_config_clean)
                        #######################################
                        if num_sessions[1] > S:
                            if bot_mode[1] == "interact":
                                os.system(ACC2_config_interact)

                            if bot_mode[1] == "clean":
                                os.system(ACC2_config_clean)

                            if bot_mode[1] == "interact/clean":
                                os.system(ACC2_config_clean)
                        #######################################

                        output_S = S
                        output_S += 1
                        print(f"1st and 2nd ACCS session {output_S} done!")
                        S += 1
                        print(f"Sleeping for {wait_time2}")
                        os.system(f"TIMEOUT /T {wait_time} /NOBREAK")


        ############################
        #4BOTS ##################### 
        ############################

                if bots == 4:
                    if S == 0:
                        os.chdir(f"{home}\\Insomniac++")
                        os.system("start cmd.exe /c python bot2.py")
                        os.system("start cmd.exe /c python bot3.py")
                        os.system("start cmd.exe /c python bot4.py")
                        os.chdir(f"{home}\\Insomniac-master")

                    #######################################
                    if num_sessions[0] > S:
                        if bot_mode[0] == "interact":
                            os.system(ACC1_config_interact)

                        if bot_mode[0] == "clean":
                            os.system(ACC1_config_clean)

                        if bot_mode[0] == "interact/clean":
                            os.system(ACC1_config_interact)
                    #######################################

                    output_S = S
                    output_S += 1
                    print(f"1st and 2nd ACCS session {output_S} done!")
                    S += 1
                    print(f"Sleeping for {wait_time2}")
                    os.system(f"TIMEOUT /T {wait_time} /NOBREAK")

                    #######################################
                    if num_sessions[0] > S:
                        if bot_mode[0] == "interact":
                            os.system(ACC1_config_interact)

                        if bot_mode[0] == "clean":
                            os.system(ACC1_config_clean)

                        if bot_mode[0] == "interact/clean":
                            os.system(ACC1_config_clean)
                    #######################################

                    output_S = S
                    output_S += 1
                    print(f"1st and 2nd ACCS session {output_S} done!")
                    S += 1
                    print(f"Sleeping for {wait_time2}")
                    os.system(f"TIMEOUT /T {wait_time} /NOBREAK")

            print("Bot finished")

class Window(QMainWindow): 
    def __init__(self): 
        super().__init__()
        # set the title 
        self.setWindowTitle("Insomniac Bot Tool")

        #window size
        height = 541
        width = 731
        self.setFixedHeight(height) 
        self.setFixedWidth(width)

        #Background color
        self.setStyleSheet(u"background-color: rgb(72, 72, 72);")
        
        #insomniac title
        self.label = QLabel(self)
        self.label.setGeometry(QRect(-4, 0, 741, 41))
        self.label.setStyleSheet(u"background-color: rgb(255, 163, 160);")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Insomniac Bot</span></p></body></html>", None))

        #links widget
        self.widget = QWidget(self)
        self.widget.setGeometry(QRect(500, 50, 221, 111))
        self.widget.setStyleSheet(u"background-color: rgb(76, 76, 76);")
        self.label_40 = QLabel(self.widget)
        self.label_40.setGeometry(QRect(0, 0, 221, 31))
        self.label_40.setStyleSheet(u"background-color: rgb(255, 163, 160);")
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Community</span></p></body></html>", None))
        #Discord link
        self.label_41 = QLabel(self.widget)
        self.label_41.setGeometry(QRect(20, 40, 71, 31))
        font = QFont()
        font.setUnderline(False)
        self.label_41.setFont(font)
        self.label_41.setOpenExternalLinks(True)
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><a href=\"https://discord.gg/t5u5uM5y\"><span style=\" font-size:14pt; text-decoration: underline; color:#ffffff;\">Discord</span></p></a></body></html>", None))
        #telegram link
        self.label_42 = QLabel(self.widget)
        self.label_42.setGeometry(QRect(10, 70, 91, 31))
        self.label_42.setFont(font)
        self.label_42.setOpenExternalLinks(True)
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><a href=\"https://t.me/insomniac_chat\"><span style=\" font-size:14pt; text-decoration: underline; color:#ffffff;\">Telegram</span></p></a></body></html>", None))
        #website
        self.label_43 = QLabel(self.widget)
        self.label_43.setGeometry(QRect(120, 40, 71, 31))
        self.label_43.setFont(font)
        self.label_43.setOpenExternalLinks(True)
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><a href=\"https://insomniac-bot.com\"><span style=\" font-size:14pt; text-decoration: underline; color:#ffffff;\">Website</span></p></a></body></html>", None))
        #Github
        self.label_44 = QLabel(self.widget)
        self.label_44.setGeometry(QRect(120, 70, 71, 31))
        self.label_44.setFont(font)
        self.label_44.setOpenExternalLinks(True)
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><a href=\"https://github.com/alexal1/Insomniac\"><span style=\" font-size:14pt; text-decoration: underline; color:#ffffff;\">GitHub</span></p></a></body></html>", None))
        
        #start button
        self.pushButton_3 = QPushButton(self)
        self.pushButton_3.setGeometry(QRect(270, 80, 191, 51))
        font2 = QFont()
        font2.setPointSize(16)
        self.pushButton_3.setFont(font2)
        self.pushButton_3.setStyleSheet(u"color: rgb(255, 163, 160);")
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Start Bot", None))

        #settings widget
        self.widget_3 = QWidget(self)
        self.widget_3.setGeometry(QRect(10, 50, 221, 111))
        self.widget_3.setStyleSheet(u"background-color: rgb(76, 76, 76);")

        #settings title
        self.label_4 = QLabel(self.widget_3)
        self.label_4.setGeometry(QRect(0, 0, 221, 31))
        self.label_4.setStyleSheet(u"background-color: rgb(255, 163, 160);")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Settings</span></p></body></html>", None))
    
        #Bots label and input
        self.label_5 = QLabel(self.widget_3)
        self.label_5.setGeometry(QRect(10, 40, 31, 16))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt; color:#ffffff;\">Bots:</span></p></body></html>", None))
        self.comboBox = QComboBox(self.widget_3)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox.setGeometry(QRect(40, 38, 31, 21))
        self.comboBox.setMinimumSize(QSize(0, 21))
        self.comboBox.setStyleSheet(u"color: rgb(255, 255, 255);")

        #bots amount
        self.label_39 = QLabel(self.widget_3)
        self.label_39.setGeometry(QRect(10, 60, 41, 16))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt; color:#ffffff;\">Users:</span></p></body></html>", None))
        self.spinBox_20 = QSpinBox(self.widget_3)
        self.spinBox_20.setGeometry(QRect(50, 59, 61, 22))
        self.spinBox_20.setStyleSheet(u"color: rgb(255, 255, 255);\n" "border-color: rgb(0, 0, 0);")
        self.spinBox_20.setMinimum(1)
        self.spinBox_20.setMaximum(4)

        #time wait label and input 
        self.label_6 = QLabel(self.widget_3)
        self.label_6.setGeometry(QRect(10, 82, 141, 20))
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Wait sec after each session:</p></body></html>", None))
        self.spinBox = QSpinBox(self.widget_3)
        self.spinBox.setGeometry(QRect(155, 80, 61, 22))
        self.spinBox.setStyleSheet(u"color: rgb(255, 255, 255);\n""border-color: rgb(0, 0, 0);")
        self.spinBox.setMaximum(86400)

        #configs widget
        self.widget_2 = QWidget(self)
        self.widget_2.setGeometry(QRect(10, 170, 711, 361))
        self.widget_2.setStyleSheet(u"background-color: rgb(80, 80, 80);")

        #tabs widget
        self.tabWidget = QTabWidget(self.widget_2)
        self.tabWidget.setGeometry(QRect(0, 30, 711, 331))
        self.tabWidget.setStyleSheet(u"background-color: rgb(80, 80, 80);")
        self.tab = QWidget()
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tabWidget.addTab(self.tab_4, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"User 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"User 2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"User 3", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"User 4", None))
        
        #config title
        self.label_3 = QLabel(self.widget_2)
        self.label_3.setGeometry(QRect(0, 0, 711, 31))
        self.label_3.setStyleSheet(u"background-color: rgb(255, 163, 160);")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Configs</span></p></body></html>", None))

        #################################################
        #Config 1 GUI code
        #################################################

        ##User 1 widget
        self.widget_4 = QWidget(self.tab)
        self.widget_4.setGeometry(QRect(0, 0, 701, 411))

        #username label and input
        self.label_7 = QLabel(self.widget_4)
        self.label_7.setGeometry(QRect(40, 10, 61, 21))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Username:</span></p></body></html>", None))
        self.lineEdit = QLineEdit(self.widget_4)
        self.lineEdit.setGeometry(QRect(110, 10, 191, 20))
        self.lineEdit.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lineEdit.setMaxLength(30)

        #session label and input 
        self.label_8 = QLabel(self.widget_4)
        self.label_8.setGeometry(QRect(340, 10, 51, 21))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Sessions</span></p></body></html>", None))
        self.spinBox_2 = QSpinBox(self.widget_4)
        self.spinBox_2.setGeometry(QRect(340, 40, 51, 22))
        self.spinBox_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setMaximum(6)

        #bot mode label and input
        self.label_9 = QLabel(self.widget_4)
        self.label_9.setGeometry(QRect(40, 40, 61, 21))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Bot Mode:</span></p></body></html>", None))
        self.comboBox_2 = QComboBox(self.widget_4)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"interact", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"clean", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"interact/clean", None))
        self.comboBox_2.setGeometry(QRect(110, 40, 191, 22))
        self.comboBox_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        #targets label and input
        self.label_10 = QLabel(self.widget_4)
        self.label_10.setGeometry(QRect(50, 70, 51, 21))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Targets:</span></p></body></html>", None))
        self.lineEdit_3 = QLineEdit(self.widget_4)
        self.lineEdit_3.setGeometry(QRect(110, 70, 191, 20))
        self.lineEdit_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        #unfollow mode label and input 
        self.label_17 = QLabel(self.widget_4)
        self.label_17.setGeometry(QRect(530, 10, 91, 21))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#ffffff;\">Unfollow Mode</span></p></body></html>", None))
        self.comboBox_3 = QComboBox(self.widget_4)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"Unfollow", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"Unfollow non followers", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"Unfollow followed by anyone", None))
        self.comboBox_3.setGeometry(QRect(490, 40, 171, 22))
        self.comboBox_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        #interaction settings widget
        self.widget_5 = QWidget(self.widget_4)
        self.widget_5.setGeometry(QRect(20, 110, 441, 181))
        self.widget_5.setStyleSheet(u"background-color: rgb(76, 76, 76);")

        #title interaction settings
        self.label_19 = QLabel(self.widget_5)
        self.label_19.setGeometry(QRect(0, 0, 441, 21))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Interaction Settings</span></p></body></html>", None))
        self.label_19.setStyleSheet(u"background-color: rgb(255, 163, 160);")

        #succesful interactions label and input
        self.label_12 = QLabel(self.widget_5)
        self.label_12.setGeometry(QRect(10, 30, 141, 21))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Total Succesful Actions:</span></p></body></html>", None))
        self.spinBox_4 = QSpinBox(self.widget_5)
        self.spinBox_4.setGeometry(QRect(150, 30, 51, 22))
        self.spinBox_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_4.setMaximum(1000)

        #Actions per target label and input
        self.label_11 = QLabel(self.widget_5)
        self.label_11.setGeometry(QRect(10, 60, 121, 21))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Actions Per Target: </span></p></body></html>", None))        
        self.spinBox_3 = QSpinBox(self.widget_5)
        self.spinBox_3.setGeometry(QRect(130, 60, 51, 22))
        self.spinBox_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_3.setMaximum(1000)

        #Total follow limit label and input 
        self.label_13 = QLabel(self.widget_5)
        self.label_13.setGeometry(QRect(10, 90, 111, 21))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Total Follows Limit: </span></p></body></html>", None))
        self.spinBox_5 = QSpinBox(self.widget_5)
        self.spinBox_5.setGeometry(QRect(130, 90, 51, 22))
        self.spinBox_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_5.setMaximum(1000)

        #total likes limit label and input
        self.label_15 = QLabel(self.widget_5)
        self.label_15.setGeometry(QRect(10, 120, 101, 21))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Total Likes Limit:</span></p></body></html>", None))
        self.spinBox_7 = QSpinBox(self.widget_5)
        self.spinBox_7.setGeometry(QRect(110, 120, 51, 22))
        self.spinBox_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_7.setMaximum(1000)

        #Likes Per IG label and input
        self.label_14 = QLabel(self.widget_5)
        self.label_14.setGeometry(QRect(10, 150, 111, 21))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Likes Per IG Profile:</span></p></body></html>", None))
        self.spinBox_6 = QSpinBox(self.widget_5)
        self.spinBox_6.setGeometry(QRect(130, 150, 51, 22))
        self.spinBox_6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_6.setMaximum(1000)

        #Total Comment Limit label and input
        self.label_20 = QLabel(self.widget_5)
        self.label_20.setGeometry(QRect(220, 30, 141, 21))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Total Comments Limit: </span></p></body></html>", None))
        self.spinBox_9 = QSpinBox(self.widget_5)
        self.spinBox_9.setGeometry(QRect(360, 30, 51, 22))
        self.spinBox_9.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_9.setMaximum(1000)

        #comment file button
        self.pushButton = QPushButton(self.widget_5)
        self.pushButton.setGeometry(QRect(250, 100, 121, 31))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Comments List File", None))
        font = QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setKerning(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"color: rgb(255, 255, 255);")

        #succeful comment percentage label and input 
        self.label_21 = QLabel(self.widget_5)
        self.label_21.setGeometry(QRect(190, 60, 191, 21))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Succesful Comment Percentage:</span></p></body></html>", None))
        self.spinBox_10 = QSpinBox(self.widget_5)
        self.spinBox_10.setGeometry(QRect(380, 60, 51, 22))
        self.spinBox_10.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_10.setMaximum(100)

        #cleaning settings widget
        self.widget_6 = QWidget(self.widget_4)
        self.widget_6.setGeometry(QRect(470, 110, 211, 181))
        self.widget_6.setStyleSheet(u"background-color: rgb(76, 76, 76);")

        #cleaning setigns title
        self.label_22 = QLabel(self.widget_6)
        self.label_22.setGeometry(QRect(0, 0, 211, 21))
        self.label_22.setStyleSheet(u"background-color: rgb(255, 163, 160);")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Cleaning Settings</span></p></body></html>", None))

        #unfollows label and input 
        self.label_16 = QLabel(self.widget_6)
        self.label_16.setGeometry(QRect(50, 40, 61, 21))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Unfollows:</span></p></body></html>", None))
        self.spinBox_8 = QSpinBox(self.widget_6)
        self.spinBox_8.setGeometry(QRect(120, 40, 51, 22))
        self.spinBox_8.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_8.setMaximum(1000)

        #unfollow sort list label and input 
        self.label_18 = QLabel(self.widget_6)
        self.label_18.setGeometry(QRect(50, 80, 111, 21))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Unfollow Sort List</span></p></body></html>", None))
        self.comboBox_4 = QComboBox(self.widget_6)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"default", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", u"latest", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("MainWindow", u"earliest", None))
        self.comboBox_4.setGeometry(QRect(60, 110, 91, 22))
        self.comboBox_4.setStyleSheet(u"color: rgb(255, 255, 255);")


        #################################################
        #Config 2 GUI code
        #################################################

        ##User 2 widget
        self.widget_7 = QWidget(self.tab_2)
        self.widget_7.setGeometry(QRect(0, 0, 701, 411))

        #username label and input
        self.label_45 = QLabel(self.widget_7)
        self.label_45.setGeometry(QRect(40, 10, 61, 21))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Username:</span></p></body></html>", None))
        self.lineEdit_5 = QLineEdit(self.widget_7)
        self.lineEdit_5.setGeometry(QRect(110, 10, 191, 20))
        self.lineEdit_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lineEdit_5.setMaxLength(30)
        
        #session label and input 
        self.label_46 = QLabel(self.widget_7)
        self.label_46.setGeometry(QRect(340, 10, 51, 21))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Sessions</span></p></body></html>", None))
        self.spinBox_21 = QSpinBox(self.widget_7)
        self.spinBox_21.setGeometry(QRect(340, 40, 51, 22))
        self.spinBox_21.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_21.setMinimum(1)
        self.spinBox_21.setMaximum(6)

        #bot mode label and input
        self.label_47 = QLabel(self.widget_7)
        self.label_47.setGeometry(QRect(40, 40, 61, 21))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Bot Mode:</span></p></body></html>", None))
        self.comboBox_8 = QComboBox(self.widget_7)
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.setItemText(0, QCoreApplication.translate("MainWindow", u"interact", None))
        self.comboBox_8.setItemText(1, QCoreApplication.translate("MainWindow", u"clean", None))
        self.comboBox_8.setItemText(2, QCoreApplication.translate("MainWindow", u"interact/clean", None))
        self.comboBox_8.setGeometry(QRect(110, 40, 191, 22))
        self.comboBox_8.setStyleSheet(u"color: rgb(255, 255, 255);")

        #targets label and input
        self.label_48 = QLabel(self.widget_7)
        self.label_48.setGeometry(QRect(50, 70, 51, 21))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Targets:</span></p></body></html>", None))
        self.lineEdit_6 = QLineEdit(self.widget_7)
        self.lineEdit_6.setGeometry(QRect(110, 70, 191, 20))
        self.lineEdit_6.setStyleSheet(u"color: rgb(255, 255, 255);")

        #unfollow mode label and input 
        self.label_49 = QLabel(self.widget_7)
        self.label_49.setGeometry(QRect(530, 10, 91, 21))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#ffffff;\">Unfollow Mode</span></p></body></html>", None))
        self.comboBox_9 = QComboBox(self.widget_7)
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.setItemText(0, QCoreApplication.translate("MainWindow", u"Unfollow", None))
        self.comboBox_9.setItemText(1, QCoreApplication.translate("MainWindow", u"Unfollow non followers", None))
        self.comboBox_9.setItemText(2, QCoreApplication.translate("MainWindow", u"Unfollow followed by anyone", None))
        self.comboBox_9.setGeometry(QRect(490, 40, 171, 22))
        self.comboBox_9.setStyleSheet(u"color: rgb(255, 255, 255);")

        #interaction settings widget
        self.widget_10 = QWidget(self.widget_7)
        self.widget_10.setGeometry(QRect(20, 110, 441, 181))
        self.widget_10.setStyleSheet(u"background-color: rgb(76, 76, 76);")

        #title interaction settings
        self.label_50 = QLabel(self.widget_10)
        self.label_50.setGeometry(QRect(0, 0, 441, 21))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Interaction Settings</span></p></body></html>", None))
        self.label_50.setStyleSheet(u"background-color: rgb(255, 163, 160);")

        #succesful interactions label and input
        self.label_51 = QLabel(self.widget_10)
        self.label_51.setGeometry(QRect(10, 30, 141, 21))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Total Succesful Actions:</span></p></body></html>", None))
        self.spinBox_22 = QSpinBox(self.widget_10)
        self.spinBox_22.setGeometry(QRect(150, 30, 51, 22))
        self.spinBox_22.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_22.setMaximum(1000)

        #Actions per target label and input
        self.label_52 = QLabel(self.widget_10)
        self.label_52.setGeometry(QRect(10, 60, 121, 21))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Actions Per Target: </span></p></body></html>", None))        
        self.spinBox_23 = QSpinBox(self.widget_10)
        self.spinBox_23.setGeometry(QRect(130, 60, 51, 22))
        self.spinBox_23.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_23.setMaximum(1000)

        #Total follow limit label and input 
        self.label_53 = QLabel(self.widget_10)
        self.label_53.setGeometry(QRect(10, 90, 111, 21))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Total Follows Limit: </span></p></body></html>", None))
        self.spinBox_24 = QSpinBox(self.widget_10)
        self.spinBox_24.setGeometry(QRect(130, 90, 51, 22))
        self.spinBox_24.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_24.setMaximum(1000)

        #total likes limit label and input
        self.label_54 = QLabel(self.widget_10)
        self.label_54.setGeometry(QRect(10, 120, 101, 21))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Total Likes Limit:</span></p></body></html>", None))
        self.spinBox_25 = QSpinBox(self.widget_10)
        self.spinBox_25.setGeometry(QRect(110, 120, 51, 22))
        self.spinBox_25.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_25.setMaximum(1000)

        #Likes Per IG label and input
        self.label_55 = QLabel(self.widget_10)
        self.label_55.setGeometry(QRect(10, 150, 111, 21))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Likes Per IG Profile:</span></p></body></html>", None))
        self.spinBox_26 = QSpinBox(self.widget_10)
        self.spinBox_26.setGeometry(QRect(130, 150, 51, 22))
        self.spinBox_26.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_26.setMaximum(1000)

        #Total Comment Limit label and input
        self.label_56 = QLabel(self.widget_10)
        self.label_56.setGeometry(QRect(220, 30, 141, 21))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Total Comments Limit: </span></p></body></html>", None))
        self.spinBox_27 = QSpinBox(self.widget_10)
        self.spinBox_27.setGeometry(QRect(360, 30, 51, 22))
        self.spinBox_27.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_27.setMaximum(1000)

        #succeful comment percentage label and input 
        self.label_57 = QLabel(self.widget_10)
        self.label_57.setGeometry(QRect(190, 60, 191, 21))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Succesful Comment Percentage:</span></p></body></html>", None))
        self.spinBox_28 = QSpinBox(self.widget_10)
        self.spinBox_28.setGeometry(QRect(380, 60, 51, 22))
        self.spinBox_28.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_28.setMaximum(100)

        #comment file button
        self.pushButton_4 = QPushButton(self.widget_10)
        self.pushButton_4.setGeometry(QRect(250, 100, 121, 31))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Comments List File", None))
        font = QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setKerning(True)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(u"color: rgb(255, 255, 255);")

        #cleaning settings widget
        self.widget_11 = QWidget(self.widget_7)
        self.widget_11.setGeometry(QRect(470, 110, 211, 181))
        self.widget_11.setStyleSheet(u"background-color: rgb(76, 76, 76);")

        #cleaning settings title
        self.label_60 = QLabel(self.widget_11)
        self.label_60.setGeometry(QRect(0, 0, 211, 21))
        self.label_60.setStyleSheet(u"background-color: rgb(255, 163, 160);")
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Cleaning Settings</span></p></body></html>", None))

        #unfollows label and input 
        self.label_58 = QLabel(self.widget_11)
        self.label_58.setGeometry(QRect(50, 40, 61, 21))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Unfollows:</span></p></body></html>", None))
        self.spinBox_29 = QSpinBox(self.widget_11)
        self.spinBox_29.setGeometry(QRect(120, 40, 51, 22))
        self.spinBox_29.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_29.setMaximum(1000)

        #unfollow sort list label and input 
        self.label_59 = QLabel(self.widget_11)
        self.label_59.setGeometry(QRect(50, 80, 111, 21))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Unfollow Sort List</span></p></body></html>", None))
        self.comboBox_10 = QComboBox(self.widget_11)
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.setItemText(0, QCoreApplication.translate("MainWindow", u"default", None))
        self.comboBox_10.setItemText(1, QCoreApplication.translate("MainWindow", u"latest", None))
        self.comboBox_10.setItemText(2, QCoreApplication.translate("MainWindow", u"earliest", None))
        self.comboBox_10.setGeometry(QRect(60, 110, 91, 22))
        self.comboBox_10.setStyleSheet(u"color: rgb(255, 255, 255);")

        #################################################
        #Config 3 GUI code
        #################################################

        ##User 3 widget
        self.widget_12 = QWidget(self.tab_3)
        self.widget_12.setGeometry(QRect(0, 0, 701, 411))

        #username label and input
        self.label_61 = QLabel(self.widget_12)
        self.label_61.setGeometry(QRect(40, 10, 61, 21))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Username:</span></p></body></html>", None))
        self.lineEdit_7 = QLineEdit(self.widget_12)
        self.lineEdit_7.setGeometry(QRect(110, 10, 191, 20))
        self.lineEdit_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lineEdit_7.setMaxLength(30)
        
        #session label and input 
        self.label_62 = QLabel(self.widget_12)
        self.label_62.setGeometry(QRect(340, 10, 51, 21))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Sessions</span></p></body></html>", None))
        self.spinBox_30 = QSpinBox(self.widget_12)
        self.spinBox_30.setGeometry(QRect(340, 40, 51, 22))
        self.spinBox_30.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_30.setMinimum(1)
        self.spinBox_30.setMaximum(6)

        #bot mode label and input
        self.label_63 = QLabel(self.widget_12)
        self.label_63.setGeometry(QRect(40, 40, 61, 21))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Bot Mode:</span></p></body></html>", None))
        self.comboBox_11 = QComboBox(self.widget_12)
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.setItemText(0, QCoreApplication.translate("MainWindow", u"interact", None))
        self.comboBox_11.setItemText(1, QCoreApplication.translate("MainWindow", u"clean", None))
        self.comboBox_11.setItemText(2, QCoreApplication.translate("MainWindow", u"interact/clean", None))
        self.comboBox_11.setGeometry(QRect(110, 40, 191, 22))
        self.comboBox_11.setStyleSheet(u"color: rgb(255, 255, 255);")

        #targets label and input
        self.label_64 = QLabel(self.widget_12)
        self.label_64.setGeometry(QRect(50, 70, 51, 21))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Targets:</span></p></body></html>", None))
        self.lineEdit_8 = QLineEdit(self.widget_12)
        self.lineEdit_8.setGeometry(QRect(110, 70, 191, 20))
        self.lineEdit_8.setStyleSheet(u"color: rgb(255, 255, 255);")

        #unfollow mode label and input 
        self.label_65 = QLabel(self.widget_12)
        self.label_65.setGeometry(QRect(530, 10, 91, 21))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#ffffff;\">Unfollow Mode</span></p></body></html>", None))
        self.comboBox_12 = QComboBox(self.widget_12)
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.setItemText(0, QCoreApplication.translate("MainWindow", u"Unfollow", None))
        self.comboBox_12.setItemText(1, QCoreApplication.translate("MainWindow", u"Unfollow non followers", None))
        self.comboBox_12.setItemText(2, QCoreApplication.translate("MainWindow", u"Unfollow followed by anyone", None))
        self.comboBox_12.setGeometry(QRect(490, 40, 171, 22))
        self.comboBox_12.setStyleSheet(u"color: rgb(255, 255, 255);")

        #interaction settings widget
        self.widget_13 = QWidget(self.widget_12)
        self.widget_13.setGeometry(QRect(20, 110, 441, 181))
        self.widget_13.setStyleSheet(u"background-color: rgb(76, 76, 76);")

        #title interaction settings
        self.label_66 = QLabel(self.widget_13)
        self.label_66.setGeometry(QRect(0, 0, 441, 21))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Interaction Settings</span></p></body></html>", None))
        self.label_66.setStyleSheet(u"background-color: rgb(255, 163, 160);")

        #succesful interactions label and input
        self.label_67 = QLabel(self.widget_13)
        self.label_67.setGeometry(QRect(10, 30, 141, 21))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Total Succesful Actions:</span></p></body></html>", None))
        self.spinBox_31 = QSpinBox(self.widget_13)
        self.spinBox_31.setGeometry(QRect(150, 30, 51, 22))
        self.spinBox_31.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_31.setMaximum(1000)

        #Actions per target label and input
        self.label_68 = QLabel(self.widget_13)
        self.label_68.setGeometry(QRect(10, 60, 121, 21))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Actions Per Target: </span></p></body></html>", None))        
        self.spinBox_32 = QSpinBox(self.widget_13)
        self.spinBox_32.setGeometry(QRect(130, 60, 51, 22))
        self.spinBox_32.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_32.setMaximum(1000)

        #Total follow limit label and input 
        self.label_69 = QLabel(self.widget_13)
        self.label_69.setGeometry(QRect(10, 90, 111, 21))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Total Follows Limit: </span></p></body></html>", None))
        self.spinBox_33 = QSpinBox(self.widget_13)
        self.spinBox_33.setGeometry(QRect(130, 90, 51, 22))
        self.spinBox_33.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_33.setMaximum(1000)

        #total likes limit label and input
        self.label_70 = QLabel(self.widget_13)
        self.label_70.setGeometry(QRect(10, 120, 101, 21))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Total Likes Limit:</span></p></body></html>", None))
        self.spinBox_34 = QSpinBox(self.widget_13)
        self.spinBox_34.setGeometry(QRect(110, 120, 51, 22))
        self.spinBox_34.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_34.setMaximum(1000)

        #Likes Per IG label and input
        self.label_71 = QLabel(self.widget_13)
        self.label_71.setGeometry(QRect(10, 150, 111, 21))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Likes Per IG Profile:</span></p></body></html>", None))
        self.spinBox_35 = QSpinBox(self.widget_13)
        self.spinBox_35.setGeometry(QRect(130, 150, 51, 22))
        self.spinBox_35.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_35.setMaximum(1000)

        #Total Comment Limit label and input
        self.label_72 = QLabel(self.widget_13)
        self.label_72.setGeometry(QRect(220, 30, 141, 21))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Total Comments Limit: </span></p></body></html>", None))
        self.spinBox_36 = QSpinBox(self.widget_13)
        self.spinBox_36.setGeometry(QRect(360, 30, 51, 22))
        self.spinBox_36.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_36.setMaximum(1000)

        #succeful comment percentage label and input 
        self.label_73 = QLabel(self.widget_13)
        self.label_73.setGeometry(QRect(190, 60, 191, 21))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Succesful Comment Percentage:</span></p></body></html>", None))
        self.spinBox_37 = QSpinBox(self.widget_13)
        self.spinBox_37.setGeometry(QRect(380, 60, 51, 22))
        self.spinBox_37.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_37.setMaximum(100)

        #comment file button
        self.pushButton_5 = QPushButton(self.widget_13)
        self.pushButton_5.setGeometry(QRect(250, 100, 121, 31))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Comments List File", None))
        font = QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setKerning(True)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet(u"color: rgb(255, 255, 255);")

        #cleaning settings widget
        self.widget_14 = QWidget(self.widget_12)
        self.widget_14.setGeometry(QRect(470, 110, 211, 181))
        self.widget_14.setStyleSheet(u"background-color: rgb(76, 76, 76);")

        #cleaning settings title
        self.label_76 = QLabel(self.widget_14)
        self.label_76.setGeometry(QRect(0, 0, 211, 21))
        self.label_76.setStyleSheet(u"background-color: rgb(255, 163, 160);")
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Cleaning Settings</span></p></body></html>", None))

        #unfollows label and input 
        self.label_74 = QLabel(self.widget_14)
        self.label_74.setGeometry(QRect(50, 40, 61, 21))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Unfollows:</span></p></body></html>", None))
        self.spinBox_38 = QSpinBox(self.widget_14)
        self.spinBox_38.setGeometry(QRect(120, 40, 51, 22))
        self.spinBox_38.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_38.setMaximum(1000)

        #unfollow sort list label and input 
        self.label_75 = QLabel(self.widget_14)
        self.label_75.setGeometry(QRect(50, 80, 111, 21))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Unfollow Sort List</span></p></body></html>", None))
        self.comboBox_13 = QComboBox(self.widget_14)
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.setItemText(0, QCoreApplication.translate("MainWindow", u"default", None))
        self.comboBox_13.setItemText(1, QCoreApplication.translate("MainWindow", u"latest", None))
        self.comboBox_13.setItemText(2, QCoreApplication.translate("MainWindow", u"earliest", None))
        self.comboBox_13.setGeometry(QRect(60, 110, 91, 22))
        self.comboBox_13.setStyleSheet(u"color: rgb(255, 255, 255);")

        #################################################
        #Config 4 GUI code
        #################################################

        ##User 4 widget
        self.widget_15 = QWidget(self.tab_4)
        self.widget_15.setGeometry(QRect(0, 0, 701, 411))

        #username label and input
        self.label_77 = QLabel(self.widget_15)
        self.label_77.setGeometry(QRect(40, 10, 61, 21))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Username:</span></p></body></html>", None))
        self.lineEdit_9 = QLineEdit(self.widget_15)
        self.lineEdit_9.setGeometry(QRect(110, 10, 191, 20))
        self.lineEdit_9.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lineEdit_9.setMaxLength(30)
        
        #session label and input 
        self.label_78 = QLabel(self.widget_15)
        self.label_78.setGeometry(QRect(340, 10, 51, 21))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Sessions</span></p></body></html>", None))
        self.spinBox_39 = QSpinBox(self.widget_15)
        self.spinBox_39.setGeometry(QRect(340, 40, 51, 22))
        self.spinBox_39.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_39.setMinimum(1)
        self.spinBox_39.setMaximum(6)

        #bot mode label and input
        self.label_79 = QLabel(self.widget_15)
        self.label_79.setGeometry(QRect(40, 40, 61, 21))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Bot Mode:</span></p></body></html>", None))
        self.comboBox_14 = QComboBox(self.widget_15)
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.setItemText(0, QCoreApplication.translate("MainWindow", u"interact", None))
        self.comboBox_14.setItemText(1, QCoreApplication.translate("MainWindow", u"clean", None))
        self.comboBox_14.setItemText(2, QCoreApplication.translate("MainWindow", u"interact/clean", None))
        self.comboBox_14.setGeometry(QRect(110, 40, 191, 22))
        self.comboBox_14.setStyleSheet(u"color: rgb(255, 255, 255);")

        #targets label and input
        self.label_80 = QLabel(self.widget_15)
        self.label_80.setGeometry(QRect(50, 70, 51, 21))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Targets:</span></p></body></html>", None))
        self.lineEdit_10 = QLineEdit(self.widget_15)
        self.lineEdit_10.setGeometry(QRect(110, 70, 191, 20))
        self.lineEdit_10.setStyleSheet(u"color: rgb(255, 255, 255);")

        #unfollow mode label and input 
        self.label_81 = QLabel(self.widget_15)
        self.label_81.setGeometry(QRect(530, 10, 91, 21))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; color:#ffffff;\">Unfollow Mode</span></p></body></html>", None))
        self.comboBox_15 = QComboBox(self.widget_15)
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.setItemText(0, QCoreApplication.translate("MainWindow", u"Unfollow", None))
        self.comboBox_15.setItemText(1, QCoreApplication.translate("MainWindow", u"Unfollow non followers", None))
        self.comboBox_15.setItemText(2, QCoreApplication.translate("MainWindow", u"Unfollow followed by anyone", None))
        self.comboBox_15.setGeometry(QRect(490, 40, 171, 22))
        self.comboBox_15.setStyleSheet(u"color: rgb(255, 255, 255);")

        #interaction settings widget
        self.widget_16 = QWidget(self.widget_15)
        self.widget_16.setGeometry(QRect(20, 110, 441, 181))
        self.widget_16.setStyleSheet(u"background-color: rgb(76, 76, 76);")

        #title interaction settings
        self.label_82 = QLabel(self.widget_16)
        self.label_82.setGeometry(QRect(0, 0, 441, 21))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Interaction Settings</span></p></body></html>", None))
        self.label_82.setStyleSheet(u"background-color: rgb(255, 163, 160);")

        #succesful interactions label and input
        self.label_83 = QLabel(self.widget_16)
        self.label_83.setGeometry(QRect(10, 30, 141, 21))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Total Succesful Actions:</span></p></body></html>", None))
        self.spinBox_40 = QSpinBox(self.widget_16)
        self.spinBox_40.setGeometry(QRect(150, 30, 51, 22))
        self.spinBox_40.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_40.setMaximum(1000)

        #Actions per target label and input
        self.label_84 = QLabel(self.widget_16)
        self.label_84.setGeometry(QRect(10, 60, 121, 21))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Actions Per Target: </span></p></body></html>", None))        
        self.spinBox_41 = QSpinBox(self.widget_16)
        self.spinBox_41.setGeometry(QRect(130, 60, 51, 22))
        self.spinBox_41.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_41.setMaximum(1000)

        #Total follow limit label and input 
        self.label_85 = QLabel(self.widget_16)
        self.label_85.setGeometry(QRect(10, 90, 111, 21))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Total Follows Limit: </span></p></body></html>", None))
        self.spinBox_42 = QSpinBox(self.widget_16)
        self.spinBox_42.setGeometry(QRect(130, 90, 51, 22))
        self.spinBox_42.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_42.setMaximum(1000)

        #total likes limit label and input
        self.label_86 = QLabel(self.widget_16)
        self.label_86.setGeometry(QRect(10, 120, 101, 21))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Total Likes Limit:</span></p></body></html>", None))
        self.spinBox_43 = QSpinBox(self.widget_16)
        self.spinBox_43.setGeometry(QRect(110, 120, 51, 22))
        self.spinBox_43.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_43.setMaximum(1000)

        #Likes Per IG label and input
        self.label_87 = QLabel(self.widget_16)
        self.label_87.setGeometry(QRect(10, 150, 111, 21))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Likes Per IG Profile:</span></p></body></html>", None))
        self.spinBox_44 = QSpinBox(self.widget_16)
        self.spinBox_44.setGeometry(QRect(130, 150, 51, 22))
        self.spinBox_44.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_44.setMaximum(1000)

        #Total Comment Limit label and input
        self.label_88 = QLabel(self.widget_16)
        self.label_88.setGeometry(QRect(220, 30, 141, 21))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Total Comments Limit: </span></p></body></html>", None))
        self.spinBox_45 = QSpinBox(self.widget_16)
        self.spinBox_45.setGeometry(QRect(360, 30, 51, 22))
        self.spinBox_45.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_45.setMaximum(1000)

        #succeful comment percentage label and input 
        self.label_89 = QLabel(self.widget_16)
        self.label_89.setGeometry(QRect(190, 60, 191, 21))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Succesful Comment Percentage:</span></p></body></html>", None))
        self.spinBox_46 = QSpinBox(self.widget_16)
        self.spinBox_46.setGeometry(QRect(380, 60, 51, 22))
        self.spinBox_46.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_46.setMaximum(100)

        #comment file button
        self.pushButton_6 = QPushButton(self.widget_16)
        self.pushButton_6.setGeometry(QRect(250, 100, 121, 31))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Comments List File", None))
        font = QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setKerning(True)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet(u"color: rgb(255, 255, 255);")

        #cleaning settings widget
        self.widget_17 = QWidget(self.widget_15)
        self.widget_17.setGeometry(QRect(470, 110, 211, 181))
        self.widget_17.setStyleSheet(u"background-color: rgb(76, 76, 76);")

        #cleaning settings title
        self.label_92 = QLabel(self.widget_17)
        self.label_92.setGeometry(QRect(0, 0, 211, 21))
        self.label_92.setStyleSheet(u"background-color: rgb(255, 163, 160);")
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Cleaning Settings</span></p></body></html>", None))

        #unfollows label and input 
        self.label_90 = QLabel(self.widget_17)
        self.label_90.setGeometry(QRect(50, 40, 61, 21))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Unfollows:</span></p></body></html>", None))
        self.spinBox_47 = QSpinBox(self.widget_17)
        self.spinBox_47.setGeometry(QRect(120, 40, 51, 22))
        self.spinBox_47.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.spinBox_47.setMaximum(1000)

        #unfollow sort list label and input 
        self.label_91 = QLabel(self.widget_17)
        self.label_91.setGeometry(QRect(50, 80, 111, 21))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#ffffff;\">Unfollow Sort List</span></p></body></html>", None))
        self.comboBox_16 = QComboBox(self.widget_17)
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.setItemText(0, QCoreApplication.translate("MainWindow", u"default", None))
        self.comboBox_16.setItemText(1, QCoreApplication.translate("MainWindow", u"latest", None))
        self.comboBox_16.setItemText(2, QCoreApplication.translate("MainWindow", u"earliest", None))
        self.comboBox_16.setGeometry(QRect(60, 110, 91, 22))
        self.comboBox_16.setStyleSheet(u"color: rgb(255, 255, 255);")

        ##########################################
        ##########################################
        #self.tabWidget.setTabEnabled(1, False)
        #self.tabWidget.setTabEnabled(2, False)
        #self.tabWidget.setTabEnabled(3, False)

        
    def start(self):

        #########################################################################
        #Qthread code 
        pool = QThreadPool.globalInstance()
        # 2. Instantiate the subclass of QRunnable
        runnable = Runnable()
        # 3. Call start()
        pool.start(runnable)
        

if __name__ == '__main__':
    # create pyqt5 app 
    App = QApplication(sys.argv)
    # create the instance of our Window 
    window = Window()
    window.show() 

    # start the app 
    sys.exit(App.exec())
