import menu
import cloud
import os



#user login:
#credentials = menu.user_log_in()

#retrieve user id user id 

    #userID = db.getuserID(credentials)

#choose game and spec 
game = menu.getSelectedGameDict()
#spec = menu.getSelectedServerSpec() # eg 't2.micro'

#create the EC2 server tagged with user id

cloud.create('t2.micro')

#Get IP and details


#point docker at EC2

#run the docker compose file
#os.system("docker compose -f ./compose/terrariacompose.yml up")
#attach console to the server
