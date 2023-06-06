tries = 4

while tries >= 1:

    userName = input("pls enter the username here: ")
    
    password = input("pls enter the pass here: ")
    
    if userName=='yossef' and  password=='1234':


        print('login seccessful')

        break

    if userName!='yossef' or  password!='1234':

        print('wrong entey')

        
    tries-=1

    print(f'the tries left :: {tries}')

else :

    print('the the acount is closed try again letter ')
    