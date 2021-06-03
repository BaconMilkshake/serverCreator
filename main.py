import menu
import os
import docker

game = menu.getSelectedGameDict()

#user login:

#retrieve user id user id 

#start the EC2 server tagged with user id

#Get IP and details

#point docker at EC2

#run the docker compose file
os.system("docker compose -f ./compose/terrariacompose.yml up")
#attach console to the server
