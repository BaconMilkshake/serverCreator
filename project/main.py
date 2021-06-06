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

server = cloud.create(spec)

#Get IP and details

print(server)
#point docker at EC2



#run the docker compose file

os.system("docker compose -f ./compose/terrariacompose.yml up -d")

#tail the log then attach console to the server
