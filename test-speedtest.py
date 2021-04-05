# SOURCE https://python.plainenglish.io/test-internet-connection-speed-using-python-3a1b5a84028

import time
import random
import logging as lgg
from statistics import mean

lgg.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', filename='logs/speedtest.log', level=lgg.DEBUG)

import speedtest # if not installed: pip install speedtest-cli
speed = speedtest.Speedtest()

def get_int_val():
    question = "Check Your Connection Speed\n\t"
    question += "1) Download Speed\n\t"
    question += "2) Upload Speed\n\t"
    question += "3) Full test with all information\n\t"
    question += "4) Full test with all information then exit\n\t"
    question += "5) Full test with all information (5 times) then exit\n\t"
    question += "6) Full test with all information (10 times) then exit\n\t"
    question += "7) Exit\n"
    question += "Your choice is: "

    try:
        choice = int(input(question))
    except:
        choice = "n/a"
    return choice

def main():

    global speedtest

    while True:
        print('\a')

        choice = get_int_val()
        while (choice == "n/a"):
            print("Please choose the correct options")
            choice = get_int_val()

        if choice == 1:
            print('Counting...')
            speed_now = '{:.2f}'.format(speed.download()/1024/1024)
            print(f"Download speed: {speed_now} Mb/s")
            lgg.info('Download speed has been tested ' + speed_now + " Mb/s")
        elif choice == 2:
            print('Counting...')
            speed_now = '{:.2f}'.format(speed.upload()/1024/1024)
            print(f"Upload speed: {speed_now} Mb/s")
            lgg.info('Upload speed has been tested ' + speed_now + " Mb/s")

        elif choice == 3 or choice == 4:
            print('Counting...')

            local_settings = speed.config
            print(f"Testing from: {local_settings['client']['ip']} ({local_settings['client']['isp']}, {local_settings['client']['country']})")
            lgg.info(f"Testing from: {local_settings['client']['ip']} ({local_settings['client']['isp']}, {local_settings['client']['country']})")

            best_server = speed.get_best_server()
            print(f"Best server: {best_server['sponsor']} ({best_server['name']}, {best_server['cc']}), Latency: {best_server['latency']}")
            lgg.info(f"Best server: {best_server['sponsor']} ({best_server['name']}, {best_server['cc']}), Latency: {best_server['latency']}")

            speed_down = '{:.2f}'.format(speed.download() / 1024 / 1024)
            print(f"Download speed: {speed_down} Mb/s")
            lgg.info('Download speed has been tested ' + speed_down + " Mb/s")

            speed_up = '{:.2f}'.format(speed.upload() / 1024 / 1024)
            print(f"Upload speed: {speed_up} Mb/s")
            lgg.info('Upload speed has been tested ' + speed_up + " Mb/s")
            # speedtest.shell()
            if choice == 4:
                print('Thank you for the speedtest, program exits.')
                break

        elif choice == 5 or choice == 6:
            speed_up_list = []
            speed_down_list = []
            end_num = (choice - 4) * 5
            for i in range(0, end_num):

                try:
                    speedy = speedtest.Speedtest()
                    print(f'Counting ({i+1})...')
                    lgg.info(f"Speedtest cycle {i+1} / {end_num} starts. ")
                except:
                    lgg.error(f"Speedtest cycle {i + 1} / {end_num} starts. ")
                try:
                    local_settings = speedy.config
                    print(f"Testing from: {local_settings['client']['ip']} ({local_settings['client']['isp']}, {local_settings['client']['country']})")
                    lgg.info(f"Testing from: {local_settings['client']['ip']} ({local_settings['client']['isp']}, {local_settings['client']['country']})")
                except:
                    lgg.error(f"Test info print.")

                try:
                    best_server = speedy.get_best_server()
                    print(f"Best server: {best_server['sponsor']} ({best_server['name']}, {best_server['cc']}), Latency: {best_server['latency']}")
                    lgg.info(f"Best server: {best_server['sponsor']} ({best_server['name']}, {best_server['cc']}), Latency: {best_server['latency']}")
                except:
                    lgg.error(f"Test best server.")

                try:
                    speed_down = '{:.2f}'.format(speedy.download() / 1024 / 1024)
                    speed_down_list.append(float(speed_down))
                    print(f"Download speed: {speed_down} Mb/s")
                    lgg.info('Download speed has been tested ' + speed_down + " Mb/s")
                except:
                    lgg.error(f"Test download speed.")

                try:
                    speed_up = '{:.2f}'.format(speedy.upload() / 1024 / 1024)
                    speed_up_list.append(float(speed_up))
                    print(f"Upload speed: {speed_up} Mb/s")
                    lgg.info('Upload speed has been tested ' + speed_up + " Mb/s")
                except:
                    lgg.error(f"Test upload speed.")

                if i != (end_num-1):
                    rnd_int = random.randrange(2, 20)
                    time.sleep(rnd_int)
                    print(f"<< wait {rnd_int} seconds before continue >>.")

                del speedy

            print(f"Download speed (mean): {'{:.2f}'.format(mean(speed_down_list))} Mb/s, Upload speed (mean): {'{:.2f}'.format(mean(speed_up_list))} Mb/s")
            lgg.info(f"Download speed (mean): {'{:.2f}'.format(mean(speed_down_list))} Mb/s, Upload speed (mean): {'{:.2f}'.format(mean(speed_up_list))} Mb/s")
            break
        elif choice == 7:
            quit()
        else:
            print("Please choose the correct options")

if __name__ == '__main__':
    main()


