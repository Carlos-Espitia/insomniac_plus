import os
from os.path import expanduser
import time
#from Main import *
from Main2 import *
os.chdir(f"{home}\\Insomniac-master")


############################
#2BOTS ##################### 
############################

while S < max_sessions:
    if bots == 2:
        if num_users == 2:
            #######################################
            if num_sessions[1] > S:
                if bot_mode[1] == "interact":
                    ACC2_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[1]} --device {device[1]} --interact {interact[1][S]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[1]} --total-successful-interactions-limit {total_succesful_interactions_limit[1]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[1]} --likes-count {likes_count[1]} --total-likes-limit {total_likes_limit[1]}"
                    os.system(ACC2_config_interact)

                if bot_mode[1] == "clean":
                    os.system(ACC2_config_clean)

                if bot_mode[1] == "interact/clean":
                    ACC2_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[1]} --device {device[1]} --interact {interact[1][S_fix_interact]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[1]} --total-successful-interactions-limit {total_succesful_interactions_limit[1]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[1]} --likes-count {likes_count[1]} --total-likes-limit {total_likes_limit[1]}"
                    os.system(ACC2_config_interact)
            #######################################

            output_S = S
            output_S += 1
            print(f"ACC2 session {output_S} done!")
            print(f"Sleeping for {wait_time2}")
            os.system(f"TIMEOUT /T {wait_time} /NOBREAK")
            if S == max_S:
                exit("Bot finished")
            S += 1

            #######################################
            if num_sessions[1] > S:
                if bot_mode[1] == "interact":
                    ACC2_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[1]} --device {device[1]} --interact {interact[1][S]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[1]} --total-successful-interactions-limit {total_succesful_interactions_limit[1]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[1]} --likes-count {likes_count[1]} --total-likes-limit {total_likes_limit[1]}"
                    os.system(ACC2_config_interact)

                if bot_mode[1] == "clean":
                    os.system(ACC2_config_clean)

                if bot_mode[1] == "interact/clean":
                    os.system(ACC2_config_clean)
            #######################################
            
            output_S = S
            output_S += 1
            print(f"ACC2 session {output_S} done!")
            print(f"Sleeping for {wait_time2}")
            os.system(f"TIMEOUT /T {wait_time} /NOBREAK")
            if S == max_S:
                exit("Bot finished")
            S += 1
            S_fix_interact += 1

        else:
            #######################################
            if num_sessions[2] > S:
                if bot_mode[2] == "interact":
                    ACC3_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[2]} --device {device[1]} --interact {interact[2][S]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[2]} --total-successful-interactions-limit {total_succesful_interactions_limit[2]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[2]} --likes-count {likes_count[2]} --total-likes-limit {total_likes_limit[2]}"
                    os.system(ACC3_config_interact)

                if bot_mode[2] == "clean":
                    os.system(ACC3_config_clean)

                if bot_mode[2] == "interact/clean":
                    ACC3_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[2]} --device {device[1]} --interact {interact[2][S_fix_interact]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[2]} --total-successful-interactions-limit {total_succesful_interactions_limit[2]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[2]} --likes-count {likes_count[2]} --total-likes-limit {total_likes_limit[2]}"
                    os.system(ACC3_config_interact)
            #######################################
            if num_sessions[3] > S:
                if bot_mode[3] == "interact":
                    ACC4_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[3]} --device {device[1]} --interact {interact[3][S]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[3]} --total-successful-interactions-limit {total_succesful_interactions_limit[3]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[3]} --likes-count {likes_count[3]} --total-likes-limit {total_likes_limit[3]}"
                    os.system(ACC4_config_interact)

                if bot_mode[3] == "clean":
                    os.system(ACC4_config_clean)

                if bot_mode[3] == "interact/clean":
                    ACC4_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[3]} --device {device[1]} --interact {interact[3][S_fix_interact]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[3]} --total-successful-interactions-limit {total_succesful_interactions_limit[3]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[3]} --likes-count {likes_count[3]} --total-likes-limit {total_likes_limit[3]}"
                    os.system(ACC4_config_interact)
            #######################################

            output_S = S
            output_S += 1
            print(f"3rd and 4th ACCS session {output_S} done!")
            print(f"Sleeping for {wait_time2}")
            os.system(f"TIMEOUT /T {wait_time} /NOBREAK")
            if S == max_S:
                exit("Bot finished")
            S += 1

            #######################################
            if num_sessions[2] > S:
                if bot_mode[2] == "interact":
                    ACC3_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[2]} --device {device[1]} --interact {interact[2][S]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[2]} --total-successful-interactions-limit {total_succesful_interactions_limit[2]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[2]} --likes-count {likes_count[2]} --total-likes-limit {total_likes_limit[2]}"
                    os.system(ACC3_config_interact)

                if bot_mode[2] == "clean":
                    os.system(ACC3_config_clean)

                if bot_mode[2] == "interact/clean":
                    os.system(ACC3_config_clean)
            #######################################
            if num_sessions[3] > S:
                if bot_mode[3] == "interact":
                    ACC4_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[3]} --device {device[1]} --interact {interact[3][S]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[3]} --total-successful-interactions-limit {total_succesful_interactions_limit[3]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[3]} --likes-count {likes_count[3]} --total-likes-limit {total_likes_limit[3]}"
                    os.system(ACC4_config_interact)

                if bot_mode[3] == "clean":
                    os.system(ACC4_config_clean)

                if bot_mode[3] == "interact/clean":
                    os.system(ACC4_config_clean)
            #######################################

            output_S = S
            output_S += 1
            print(f"3rd and 4th ACCS session {output_S} done!")
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
        #######################################
        if num_sessions[1] > S:
            if bot_mode[1] == "interact":
                ACC2_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[1]} --device {device[1]} --interact {interact[1][S]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[1]} --total-successful-interactions-limit {total_succesful_interactions_limit[1]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[1]} --likes-count {likes_count[1]} --total-likes-limit {total_likes_limit[1]}"
                os.system(ACC2_config_interact)

            if bot_mode[1] == "clean":
                os.system(ACC2_config_clean)

            if bot_mode[1] == "interact/clean":
                ACC2_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[1]} --device {device[1]} --interact {interact[1][S_fix_interact]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[1]} --total-successful-interactions-limit {total_succesful_interactions_limit[1]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[1]} --likes-count {likes_count[1]} --total-likes-limit {total_likes_limit[1]}"
                os.system(ACC2_config_interact)
        #######################################

        output_S = S
        output_S += 1
        print(f"ACC2 session {output_S} done!")
        print(f"Sleeping for {wait_time2}")
        os.system(f"TIMEOUT /T {wait_time} /NOBREAK")
        if S == max_S:
            exit("Bot finished")
        S += 1

        #######################################
        if num_sessions[1] > S:
            if bot_mode[1] == "interact":
                ACC2_config_interact = f"python start.py --wait-for-device --no-speed-check --username {usernames[1]} --device {device[1]} --interact {interact[1][S]} --successful-interactions-limit-per-source {successful_interactions_limit_per_source} --interactions-limit-per-source {interactions_limit_per_source[1]} --total-successful-interactions-limit {total_succesful_interactions_limit[1]} --interactions-count {interaction_count} --follow-percentage {follow_percentage} --total-follow-limit {follow_limit[1]} --likes-count {likes_count[1]} --total-likes-limit {total_likes_limit[1]}"
                os.system(ACC2_config_interact)

            if bot_mode[1] == "clean":
                os.system(ACC2_config_clean)

            if bot_mode[1] == "interact/clean":
                os.system(ACC2_config_clean)
        #######################################

        output_S = S
        output_S += 1
        print(f"ACC2 session {output_S} done!")
        print(f"Sleeping for {wait_time2}")
        os.system(f"TIMEOUT /T {wait_time} /NOBREAK")
        if S == max_S:
            exit("Bot finished")
        S += 1
        S_fix_interact += 1

print("Bot finished")
os.system("pause")