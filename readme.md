## This application allows a user to 
- log in to a console with their account
- choose a game and have the server be brought up
    - Future may be changed to choose a pre-existing gameserver or create new one
- interact with the server console
-  close their server
-   be billed for the time their server was running
    - Be able to querry ammount of time played on each game in the last month
- save their server image for later use

## How to setup:
You must have docker and docker compose installed and an active AWS account:
- Create a new AWS account 
- Create a aws user with programatic access and full ec2 access
- Enter the aws key and secret key into the /.aws/credentials file
- Example credentials file
- - '''[default]
aws_access_key_id = 
aws_secret_access_key = 
 '''
- Generate and save a key pair called 'id_rsa' using a cmd line tool such as ssh-keygen 
- Select reigion "us-west-2" on amazon console and go to ec2 -> Key Pairs -> Action -> import keypair and import the public key naming the key pair 'defaultec2'
- Put the private id_rsa file in the root of the repo directory
- Create a security group called 'defaultec2' under ec2 -> security groups allowing for ssh into docker deamon and for people to connect to the game server
- Run ''' docker build . -t servercreator ''' from the repo root
- Start the program with docker compose -f ./dockercompose.yml run servercreator
- - This will run the program and its postgres database
## Boto3 is used to interact with AWS 
- https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html

