# sudo apt-get install rolldice
#  sudo apt-get remove rolldice

import json

import subprocess

#subprocess.Popen( 'sudo apt-get -y install rolldice',  shell=True,  stdin=subprocess.PIPE ).communicate()

#subprocess.call("(sudo apt-get install rolldice)", shell=True)

installerVars = json.load(open('hypervisor.json'))

for dependency in installerVars["dependencies"]:
	installString = 'sudo apt-get -y install ' +  dependency
	uninstallString = 'sudo apt-get -y remove ' +  dependency
	
	#package
	print dependency
	print installString
	#subprocess.Popen( uninstallString,  shell=True,  stdin=subprocess.PIPE ).communicate()
	subprocess.Popen( installString,  shell=True,  stdin=subprocess.PIPE ).communicate()
	
	#version
	#print installerVars["dependencies"][dependency]



