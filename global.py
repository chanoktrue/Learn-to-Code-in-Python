# การกำหนดตัวแปลแบบ Local และ Global

global_var = 20

def myFunction():
    # กำหนดตัวแปล Local
    local_var = 10
    print(f"Inside the function : local_val = {local_var}")
    print(f"Inside the function : gloabl_var = {global_var}")
        
myFunction()