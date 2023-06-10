import re

def vaildate_password(password):
    if len(password)< 12:
        return False
    
    if not re.search(r'[!@#$%^&*()，.>。?/"<~`]', password):
        return False
    if not re. search(r'[a-z]', password):
        return False
    if not re. search(r'[A-Z]', password):
        return False
    if not re. search(r'\d', password):
        return False

    return True
password= input("請輸人密碼:")
if vaildate_password(password):
    print("密碼符合要求")
else:
    print("密碼不符合要求")