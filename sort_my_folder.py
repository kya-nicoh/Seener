import os

# Every new folder increments the number by 00, 01, 02, 03, 04

def write_to_file(FILE_NAME, x):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(x))
    file_write.close()
    return

while True:
    if os.path.isfile('last_folder_num.txt'):
            with open('last_folder_num.txt', 'r') as f:
                last_folder_num = f.read()
                print("Last folder numbre is " + last_folder_num)
                x = int(last_folder_num)
                print('current value bitch is ' + str(x))
    
    counts = input('Would you like to add another folder?\n')
    if counts == 'y':
        directory = "%s NewFolder" % str(x)
        parent_dir = "D:/00 PassionProjects/02 Seener"
        x += 1
        print('x is incremented to ' + str(x))
        
        mode = 0o666
        path = os.path.join(parent_dir, directory)

        os.mkdir(path, mode)
        print("Directory '%s' created" % directory)

        write_to_file('last_folder_num.txt', x)
    else:
        # os.rmdir(path)
        break
    
# make a gui so whenever I click a button it adds the folder and another to delete using tkinter
# Another for the input of the additional string 
# Automatically detect the folder im in, add the increment inside the folder and close 