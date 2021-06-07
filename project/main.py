import menu
import cloud
import os
import db

db.initialise()


#user login:

userId = menu.sign_in_or_up(db_get_userID = db.getuserID, db_create_user = db.createUser)

#choose game and spec 
game = menu.getSelectedGameDict()
spec = menu.getSelectedServerSpec() # eg 't2.micro'

#create the EC2 server and save server id in users table

instanceid = cloud.create(spec) 
print(instanceid)
#wait for server to be initialised
cloud.wait_until_running(instanceid)
print("restarting")
cloud.reboot_instance(instanceid)

cloud.wait_until_running(instanceid)
print("restarted")
#Get IP and details

ip = cloud.get_public_ip(instanceid)
#point docker at EC2
#os.system(f"export DOCKER_HOST=ssh://ec2-user@{ip}")


#run the docker compose file

#os.system("export COMPOSE_FILE=./compose/terrariacompose.yml")
os.system(f"docker -H ssh://ec2-user@{ip} compose up")

#tail the log then attach console to the server
