import os
from os.path import expanduser
import time
#from Main import *
from Main2 import *

os.chdir(f"{home}\\Insomniac-master")

############################
#4BOTS ##################### 
############################

while S < max_sessions:
    if bots == 4:
        #######################################
        if num_sessions[3] > S:
            if bot_mode[3] == "interact":
                ACC4_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[3]} --device {device[3]} --interact {interact[3][S]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[3]} --total-successful-interactions-limit {total_succesful_interactions_limit[3]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[3]} --likes-count {likes_count[3]} --total-likes-limit {total_likes_limit[3]}"
                os.system(ACC4_config_interact)

            if bot_mode[3] == "clean":
                os.system(ACC4_config_clean)

            if bot_mode[3] == "interact/clean":
                ACC4_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[3]} --device {device[3]} --interact {interact[3][S_fix_interact]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[3]} --total-successful-interactions-limit {total_succesful_interactions_limit[3]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[3]} --likes-count {likes_count[3]} --total-likes-limit {total_likes_limit[3]}"
                os.system(ACC4_config_interact)
        #######################################

        output_S = S
        output_S += 1
        print(f"ACC4 session {output_S} done!")
        print(f"Sleeping for {wait_time2}")
        os.system(f"TIMEOUT /T {wait_time} /NOBREAK")
        if S == max_S:
            exit("Bot finished")
        S += 1

        #######################################
        if num_sessions[3] > S:
            if bot_mode[3] == "interact":
                ACC4_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[3]} --device {device[3]} --interact {interact[3][S]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[3]} --total-successful-interactions-limit {total_succesful_interactions_limit[3]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[3]} --likes-count {likes_count[3]} --total-likes-limit {total_likes_limit[3]}"
                os.system(ACC4_config_interact)

            if bot_mode[3] == "clean":
                os.system(ACC4_config_clean)

            if bot_mode[3] == "interact/clean":
                os.system(ACC4_config_clean)
        #######################################

        output_S = S
        output_S += 1
        print(f"ACC4 session {output_S} done!")
        print(f"Sleeping for {wait_time2}")
        os.system(f"TIMEOUT /T {wait_time} /NOBREAK")
        if S == max_S:
            exit("Bot finished")
        S += 1
        S_fix_interact += 1

print("Bot finished")
os.system("pause")