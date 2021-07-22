from speedtest import Speedtest   #### First you need to install pip install speedtest-cli

spd = Speedtest()

print("The download speed: Internet connection is: {}. ".format(spd.download()))
print("The upload speed: Internet connection is: {}".format(spd.upload()))
