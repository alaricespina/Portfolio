import fbchat
from getpass import getpass 

username = "your pass"
psw = "your pass"
print("Username set:" + username)
print("Password set:" + psw)

client = fbchat.Client(username, psw) 
no_of_friends = int(input("Number of friends: ")) 
for i in range(no_of_friends): 
    name = str(input("Name: "))
    friends = client.searchForUsers(name)
    print(friends.name)
    whichone = int(input("Return a number:")) - 1
    friend = friends[whichone]
    msg = str(input("Message:"))
    sent = client.send(fbchat.models.Message(msg),friend.uid)
    if sent:
    	print("Message sent succesfully")
    '''
    friend = friends[0] 
    msg = str(raw_input("Message: ")) 
    sent = client.send(friend.uid, msg) 
    if sent: 
        print("Message sent successfully!") 
    '''
