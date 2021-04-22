# importing the required libraries 

import os
from os.path import expanduser
import time
import datetime

#user dir
home = expanduser("~")

################
bots = 2
wait_time = 72000
wait_time2 = datetime.timedelta(seconds=wait_time)
device = ["emulator-5554", "emulator-5556", "emulator-5558", "emulator-5560"]
#only add users you will be botting
usernames = ["carlos_.espitia", "emily.ricoo"]
num_users = len(usernames)

#each sessions
num_sessions = [2, 2, 0, 0]

#Max Sessions
max_S_list = num_sessions
max_S_list.sort(reverse=True)
max_S = max_S_list[0]

#
#"interact", "clean", "interact/clean"
#
bot_mode = ["clean", "interact/clean", "interact/clean", "interact/clean"]

#interacting
interact = [["@sydney.barker", "@test", "@test2"], ["@aidanmthorne", "@test", "@test2"], ["@guthrie.richardson", "@test", "@test2"], ["@hannahmharris1212", "@test", "@test2"]]
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
#"--unfollow-followed-by-anyone" "--unfollow-non-followers"
#
UNF_mode = ["--unfollow-followed-by-anyone", "--unfollow-non-followers", "", "--unfollow-non-followers"]
unfollow_limit = ["300", "300", "200", "200"]
#following sort order
#
#"defualt", "latest", "earliest"
#
unfollow_sort = ["latest", "latest", "latest", "latest"]

###################
#Account configs
if bots == 1:
    #ACC1_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[0]} --device {device[0]} --interact {interact[0][0]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[0]} --total-successful-interactions-limit {total_succesful_interactions_limit[0]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[0]} --likes-count {likes_count[0]} --total-likes-limit {total_likes_limit[0]}"
    ACC1_config_clean = f"python start.py --wait-for-device --no-speed-check --username {usernames[0]} --device {device[0]} --following-sort-order {unfollow_sort[0]} --unfollow {unfollow_limit[0]} {UNF_mode[0]}"

    #ACC2_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[1]} --device {device[0]} --interact {interact[1][0]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[1]} --total-successful-interactions-limit {total_succesful_interactions_limit[1]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[1]} --likes-count {likes_count[1]} --total-likes-limit {total_likes_limit[1]}"
    ACC2_config_clean = f"python start.py --wait-for-device --no-speed-check --username {usernames[1]} --device {device[0]} --following-sort-order {unfollow_sort[1]} --unfollow {unfollow_limit[1]} {UNF_mode[1]}"

    #ACC3_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[2]} --device {device[0]} --interact {interact[2][0]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[2]} --total-successful-interactions-limit {total_succesful_interactions_limit[2]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[2]} --likes-count {likes_count[2]} --total-likes-limit {total_likes_limit[2]}"
    ACC3_config_clean = f"python start.py --wait-for-device --no-speed-check --username {usernames[2]} --device {device[0]} --following-sort-order {unfollow_sort[2]} --unfollow {unfollow_limit[2]} {UNF_mode[2]}"

    #ACC4_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[3]} --device {device[0]} --interact {interact[3][0]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[3]} --total-successful-interactions-limit {total_succesful_interactions_limit[3]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[3]} --likes-count {likes_count[3]} --total-likes-limit {total_likes_limit[3]}"
    ACC4_config_clean = f"python start.py --wait-for-device --no-speed-check --username {usernames[3]} --device {device[0]} --following-sort-order {unfollow_sort[3]} --unfollow {unfollow_limit[3]} {UNF_mode[3]}"

if bots == 2:
    if num_users > 1:
        if num_users == 2:
            #ACC1_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[0]} --device {device[0]} --interact {interact[0]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[0]} --total-successful-interactions-limit {total_succesful_interactions_limit[0]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[0]} --likes-count {likes_count[0]} --total-likes-limit {total_likes_limit[0]}"
            ACC1_config_clean = f"python start.py --wait-for-device --no-speed-check --username {usernames[0]} --device {device[0]} --following-sort-order {unfollow_sort[0]} --unfollow {unfollow_limit[0]} {UNF_mode[0]}"

            #ACC2_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[1]} --device {device[1]} --interact {interact[1]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[1]} --total-successful-interactions-limit {total_succesful_interactions_limit[1]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[1]} --likes-count {likes_count[1]} --total-likes-limit {total_likes_limit[1]}"
            ACC2_config_clean = f"python start.py --wait-for-device --no-speed-check --username {usernames[1]} --device {device[1]} --following-sort-order {unfollow_sort[1]} --unfollow {unfollow_limit[1]} {UNF_mode[1]}"

        if num_users > 2:
            #ACC1_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[0]} --device {device[0]} --interact {interact[0]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[0]} --total-successful-interactions-limit {total_succesful_interactions_limit[0]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[0]} --likes-count {likes_count[0]} --total-likes-limit {total_likes_limit[0]}"
            ACC1_config_clean = f"python start.py --wait-for-device --no-speed-check --username {usernames[0]} --device {device[0]} --following-sort-order {unfollow_sort[0]} --unfollow {unfollow_limit[0]} {UNF_mode[0]}"

            #ACC2_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[1]} --device {device[0]} --interact {interact[1]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[1]} --total-successful-interactions-limit {total_succesful_interactions_limit[1]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[1]} --likes-count {likes_count[1]} --total-likes-limit {total_likes_limit[1]}"
            ACC2_config_clean = f"python start.py --wait-for-device --no-speed-check --username {usernames[1]} --device {device[0]} --following-sort-order {unfollow_sort[1]} --unfollow {unfollow_limit[1]} {UNF_mode[1]}"

            #ACC3_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[2]} --device {device[1]} --interact {interact[2]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[2]} --total-successful-interactions-limit {total_succesful_interactions_limit[2]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[2]} --likes-count {likes_count[2]} --total-likes-limit {total_likes_limit[2]}"
            ACC3_config_clean = f"python start.py --wait-for-device --no-speed-check --username {usernames[2]} --device {device[1]} --following-sort-order {unfollow_sort[2]} --unfollow {unfollow_limit[2]} {UNF_mode[2]}"

            #ACC4_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[3]} --device {device[1]} --interact {interact[3]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[3]} --total-successful-interactions-limit {total_succesful_interactions_limit[3]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[3]} --likes-count {likes_count[3]} --total-likes-limit {total_likes_limit[3]}"
            ACC4_config_clean = f"python start.py --wait-for-device --no-speed-check --username {usernames[3]} --device {device[1]} --following-sort-order {unfollow_sort[3]} --unfollow {unfollow_limit[3]} {UNF_mode[3]}"
    else:
        print("You must bot atleast 2 or more accounts to use 2 bots!")
        exit()

if bots == 4:
    if num_users > 2:
        #ACC1_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[0]} --device {device[0]} --interact {interact[0]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[0]} --total-successful-interactions-limit {total_succesful_interactions_limit[0]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[0]} --likes-count {likes_count[0]} --total-likes-limit {total_likes_limit[0]}"
        ACC1_config_clean = f"python start.py --wait-for-device --no-speed-check --username {usernames[0]} --device {device[0]} --following-sort-order {unfollow_sort[0]} --unfollow {unfollow_limit[0]} {UNF_mode[0]}"

        #ACC2_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[1]} --device {device[1]} --interact {interact[1]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[1]} --total-successful-interactions-limit {total_succesful_interactions_limit[1]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[1]} --likes-count {likes_count[1]} --total-likes-limit {total_likes_limit[1]}"
        ACC2_config_clean = f"python start.py --wait-for-device --no-speed-check --username {usernames[1]} --device {device[1]} --following-sort-order {unfollow_sort[1]} --unfollow {unfollow_limit[1]} {UNF_mode[3]}"

        #ACC3_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[2]} --device {device[2]} --interact {interact[2]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[2]} --total-successful-interactions-limit {total_succesful_interactions_limit[2]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[2]} --likes-count {likes_count[2]} --total-likes-limit {total_likes_limit[2]}"
        ACC3_config_clean = f"python start.py --wait-for-device --no-speed-check --username {usernames[2]} --device {device[2]} --following-sort-order {unfollow_sort[2]} --unfollow {unfollow_limit[2]} {UNF_mode[2]}"

        #ACC4_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[3]} --device {device[3]} --interact {interact[3]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[3]} --total-successful-interactions-limit {total_succesful_interactions_limit[3]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[3]} --likes-count {likes_count[3]} --total-likes-limit {total_likes_limit[3]}"
        ACC4_config_clean = f"python start.py --wait-for-device --no-speed-check --username {usernames[3]} --device {device[3]} --following-sort-order {unfollow_sort[3]} --unfollow {unfollow_limit[3]} {UNF_mode[3]}"
    else:
        print("You must bot atleast 3 or more accounts to use 4 bots!")
        exit()

#6 sessions
max_sessions = 5
S = 0
S_fix_interact = 0

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

    ################

    global S, max_sessions, S_fix_interact
    while S < max_sessions:
        if bots == 1:    
            #######################################
            if num_sessions[0] > S:
                if bot_mode[0] == "interact":
                    ACC1_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[0]} --device {device[0]} --interact {interact[0][S]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[0]} --total-successful-interactions-limit {total_succesful_interactions_limit[0]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[0]} --likes-count {likes_count[0]} --total-likes-limit {total_likes_limit[0]}"
                    os.system(ACC1_config_interact)

                if bot_mode[0] == "clean":
                    os.system(ACC1_config_clean)

                if bot_mode[0] == "interact/clean": 
                    ACC1_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[0]} --device {device[0]} --interact {interact[0][S_fix_interact]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[0]} --total-successful-interactions-limit {total_succesful_interactions_limit[0]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[0]} --likes-count {likes_count[0]} --total-likes-limit {total_likes_limit[0]}"
                    os.system(ACC1_config_interact)
            #######################################
            if num_sessions[1] > S:
                if bot_mode[1] == "interact":
                    ACC2_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[1]} --device {device[0]} --interact {interact[1][S]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[1]} --total-successful-interactions-limit {total_succesful_interactions_limit[1]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[1]} --likes-count {likes_count[1]} --total-likes-limit {total_likes_limit[1]}"
                    os.system(ACC2_config_interact)

                if bot_mode[1] == "clean":
                    os.system(ACC2_config_clean)

                if bot_mode[1] == "interact/clean":
                    ACC2_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[1]} --device {device[0]} --interact {interact[1][S_fix_interact]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[1]} --total-successful-interactions-limit {total_succesful_interactions_limit[1]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[1]} --likes-count {likes_count[1]} --total-likes-limit {total_likes_limit[1]}"
                    os.system(ACC2_config_interact)
            #######################################
            if num_sessions[2] > S:
                if bot_mode[2] == "interact":
                    ACC3_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[2]} --device {device[0]} --interact {interact[2][S]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[2]} --total-successful-interactions-limit {total_succesful_interactions_limit[2]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[2]} --likes-count {likes_count[2]} --total-likes-limit {total_likes_limit[2]}"
                    os.system(ACC3_config_interact)

                if bot_mode[2] == "clean":
                    os.system(ACC3_config_clean)

                if bot_mode[2] == "interact/clean":
                    ACC3_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[2]} --device {device[0]} --interact {interact[2][S_fix_interact]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[2]} --total-successful-interactions-limit {total_succesful_interactions_limit[2]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[2]} --likes-count {likes_count[2]} --total-likes-limit {total_likes_limit[2]}"
                    os.system(ACC3_config_interact)
            #######################################
            if num_sessions[3] > S:
                if bot_mode[3] == "interact":
                    ACC4_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[3]} --device {device[0]} --interact {interact[3][S]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[3]} --total-successful-interactions-limit {total_succesful_interactions_limit[3]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[3]} --likes-count {likes_count[3]} --total-likes-limit {total_likes_limit[3]}"
                    os.system(ACC4_config_interact)

                if bot_mode[3] == "clean":
                    os.system(ACC4_config_clean)

                if bot_mode[3] == "interact/clean":
                    ACC4_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[3]} --device {device[0]} --interact {interact[3][S_fix_interact]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[3]} --total-successful-interactions-limit {total_succesful_interactions_limit[3]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[3]} --likes-count {likes_count[3]} --total-likes-limit {total_likes_limit[3]}"
                    os.system(ACC4_config_interact)
            #######################################

            output_S = S
            output_S += 1
            print(f"ALL ACCS session {output_S} done!")
            print(f"Sleeping for {wait_time2}")
            os.system(f"TIMEOUT /T {wait_time} /NOBREAK")
            if S == max_S:
                exit("Bot finished")
            S += 1

            #######################################
            if num_sessions[0] > S:
                if bot_mode[0] == "interact":
                    ACC1_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[0]} --device {device[0]} --interact {interact[0][S]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[0]} --total-successful-interactions-limit {total_succesful_interactions_limit[0]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[0]} --likes-count {likes_count[0]} --total-likes-limit {total_likes_limit[0]}"
                    os.system(ACC1_config_interact)

                if bot_mode[0] == "clean":
                    os.system(ACC1_config_clean)

                if bot_mode[0] == "interact/clean":
                    os.system(ACC1_config_clean)
            #######################################
            if num_sessions[1] > S:
                if bot_mode[1] == "interact":
                    ACC2_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[1]} --device {device[0]} --interact {interact[1][S]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[1]} --total-successful-interactions-limit {total_succesful_interactions_limit[1]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[1]} --likes-count {likes_count[1]} --total-likes-limit {total_likes_limit[1]}"
                    os.system(ACC2_config_interact)

                if bot_mode[1] == "clean":
                    os.system(ACC2_config_clean)

                if bot_mode[1] == "interact/clean":
                    os.system(ACC2_config_clean)
            #######################################
            if num_sessions[2] > S:
                if bot_mode[2] == "interact":
                    ACC3_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[2]} --device {device[0]} --interact {interact[2][S]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[2]} --total-successful-interactions-limit {total_succesful_interactions_limit[2]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[2]} --likes-count {likes_count[2]} --total-likes-limit {total_likes_limit[2]}"
                    os.system(ACC3_config_interact)

                if bot_mode[2] == "clean":
                    os.system(ACC3_config_clean)

                if bot_mode[2] == "interact/clean":
                    os.system(ACC3_config_clean)
            #######################################
            if num_sessions[3] > S:
                if bot_mode[3] == "interact":
                    ACC4_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[3]} --device {device[0]} --interact {interact[3][S]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[3]} --total-successful-interactions-limit {total_succesful_interactions_limit[3]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[3]} --likes-count {likes_count[3]} --total-likes-limit {total_likes_limit[3]}"
                    os.system(ACC4_config_interact)

                if bot_mode[3] == "clean":
                    os.system(ACC4_config_clean)

                if bot_mode[3] == "interact/clean":
                    os.system(ACC4_config_clean)
            #######################################

            output_S = S
            output_S += 1
            print(f"ALL ACCS session {output_S} done!")
            print(f"Sleeping for {wait_time2}")
            os.system(f"TIMEOUT /T {wait_time} /NOBREAK")
            if S == max_S:
                exit("Bot finished")
            S += 1
            S_fix_interact += 1


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
                        ACC1_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[0]} --device {device[0]} --interact {interact[0][S]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[0]} --total-successful-interactions-limit {total_succesful_interactions_limit[0]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[0]} --likes-count {likes_count[0]} --total-likes-limit {total_likes_limit[0]}"
                        os.system(ACC1_config_interact)

                    if bot_mode[0] == "clean":
                        os.system(ACC1_config_clean)

                    if bot_mode[0] == "interact/clean":
                        ACC1_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[0]} --device {device[0]} --interact {interact[0][S_fix_interact]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[0]} --total-successful-interactions-limit {total_succesful_interactions_limit[0]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[0]} --likes-count {likes_count[0]} --total-likes-limit {total_likes_limit[0]}"
                        os.system(ACC1_config_interact)
                #######################################

                output_S = S
                output_S += 1
                print(f"ACC1 session {output_S} done!")
                print(f"Sleeping for {wait_time2}")
                os.system(f"TIMEOUT /T {wait_time} /NOBREAK")
                if S == max_S:
                    exit("Bot finished")
                S += 1

                #######################################
                if num_sessions[0] > S:
                    if bot_mode[0] == "interact":
                        ACC1_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[0]} --device {device[0]} --interact {interact[0][S]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[0]} --total-successful-interactions-limit {total_succesful_interactions_limit[0]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[0]} --likes-count {likes_count[0]} --total-likes-limit {total_likes_limit[0]}"
                        os.system(ACC1_config_interact)

                    if bot_mode[0] == "clean":
                        os.system(ACC1_config_clean)

                    if bot_mode[0] == "interact/clean":
                        os.system(ACC1_config_clean)
                #######################################

                output_S = S
                output_S += 1
                print(f"ACC1 session {output_S} done!")
                print(f"Sleeping for {wait_time2}")
                os.system(f"TIMEOUT /T {wait_time} /NOBREAK")
                if S == max_S:
                    exit("Bot finished")
                S += 1
                S_fix_interact += 1

            else:
                if num_sessions[0] > S:
                    if bot_mode[0] == "interact":
                        ACC1_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[0]} --device {device[0]} --interact {interact[0][S]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[0]} --total-successful-interactions-limit {total_succesful_interactions_limit[0]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[0]} --likes-count {likes_count[0]} --total-likes-limit {total_likes_limit[0]}"
                        os.system(ACC1_config_interact)

                    if bot_mode[0] == "clean":
                        os.system(ACC1_config_clean)

                    if bot_mode[0] == "interact/clean":
                        ACC1_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[0]} --device {device[0]} --interact {interact[0][S_fix_interact]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[0]} --total-successful-interactions-limit {total_succesful_interactions_limit[0]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[0]} --likes-count {likes_count[0]} --total-likes-limit {total_likes_limit[0]}"
                        os.system(ACC1_config_interact)
                #######################################
                if num_sessions[1] > S:
                    if bot_mode[1] == "interact":
                        ACC2_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[1]} --device {device[0]} --interact {interact[1][S]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[1]} --total-successful-interactions-limit {total_succesful_interactions_limit[1]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[1]} --likes-count {likes_count[1]} --total-likes-limit {total_likes_limit[1]}"
                        os.system(ACC2_config_interact)

                    if bot_mode[1] == "clean":
                        os.system(ACC2_config_clean)

                    if bot_mode[1] == "interact/clean":
                        ACC2_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[1]} --device {device[0]} --interact {interact[1][S_fix_interact]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[1]} --total-successful-interactions-limit {total_succesful_interactions_limit[1]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[1]} --likes-count {likes_count[1]} --total-likes-limit {total_likes_limit[1]}"
                        os.system(ACC2_config_interact)
                #######################################

                output_S = S
                output_S += 1
                print(f"1st and 2nd ACCS session {output_S} done!")
                print(f"Sleeping for {wait_time2}")
                os.system(f"TIMEOUT /T {wait_time} /NOBREAK")
                if S == max_S:
                    exit("Bot finished")
                S += 1

                #######################################
                if num_sessions[0] > S:
                    if bot_mode[0] == "interact":
                        ACC1_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[0]} --device {device[0]} --interact {interact[0][S]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[0]} --total-successful-interactions-limit {total_succesful_interactions_limit[0]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[0]} --likes-count {likes_count[0]} --total-likes-limit {total_likes_limit[0]}"
                        os.system(ACC1_config_interact)

                    if bot_mode[0] == "clean":
                        os.system(ACC1_config_clean)

                    if bot_mode[0] == "interact/clean":
                        os.system(ACC1_config_clean)
                #######################################
                if num_sessions[1] > S:
                    if bot_mode[1] == "interact":
                        ACC2_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[1]} --device {device[0]} --interact {interact[1][S]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[1]} --total-successful-interactions-limit {total_succesful_interactions_limit[1]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[1]} --likes-count {likes_count[1]} --total-likes-limit {total_likes_limit[1]}"
                        os.system(ACC2_config_interact)

                    if bot_mode[1] == "clean":
                        os.system(ACC2_config_clean)

                    if bot_mode[1] == "interact/clean":
                        os.system(ACC2_config_clean)
                #######################################

                output_S = S
                output_S += 1
                print(f"1st and 2nd ACCS session {output_S} done!")
                print(f"Sleeping for {wait_time2}")
                os.system(f"TIMEOUT /T {wait_time} /NOBREAK")
                if S == max_S:
                    exit("Bot finished")
                S += 1
                S_fix_interact += 1

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
                    ACC1_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[0]} --device {device[0]} --interact {interact[0][S]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[0]} --total-successful-interactions-limit {total_succesful_interactions_limit[0]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[0]} --likes-count {likes_count[0]} --total-likes-limit {total_likes_limit[0]}"
                    os.system(ACC1_config_interact)

                if bot_mode[0] == "clean":
                    os.system(ACC1_config_clean)

                if bot_mode[0] == "interact/clean":
                    ACC1_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[0]} --device {device[0]} --interact {interact[0][S_fix_interact]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[0]} --total-successful-interactions-limit {total_succesful_interactions_limit[0]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[0]} --likes-count {likes_count[0]} --total-likes-limit {total_likes_limit[0]}"
                    os.system(ACC1_config_interact)
            #######################################

            output_S = S
            output_S += 1
            print(f"1st ACC session {output_S} done!")
            print(f"Sleeping for {wait_time2}")
            os.system(f"TIMEOUT /T {wait_time} /NOBREAK")
            if S == max_S:
                exit("Bot finished")
            S += 1

            #######################################
            if num_sessions[0] > S:
                if bot_mode[0] == "interact":
                    ACC1_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[0]} --device {device[0]} --interact {interact[0][S]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[0]} --total-successful-interactions-limit {total_succesful_interactions_limit[0]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[0]} --likes-count {likes_count[0]} --total-likes-limit {total_likes_limit[0]}"
                    os.system(ACC1_config_interact)

                if bot_mode[0] == "clean":
                    os.system(ACC1_config_clean)

                if bot_mode[0] == "interact/clean":
                    os.system(ACC1_config_clean)
            #######################################

            output_S = S
            output_S += 1
            print(f"1st ACC session {output_S} done!")
            print(f"Sleeping for {wait_time2}")
            os.system(f"TIMEOUT /T {wait_time} /NOBREAK")
            if S == max_S:
                exit("Bot finished")
            S += 1
            S_fix_interact += 1

print("Bot finished")

if __name__ == '__main__':
    bot1()
