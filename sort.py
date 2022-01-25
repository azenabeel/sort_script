import os, shutil # os: deal with folders; shutil move file into folder

folders={
    'videos':['.mp4'],
    'audios':['.wav','.mp3'],
    'images':['.jpg', '.jpeg', '.png'],
    'documents':['.txt', '.doc', '.xlsx', '.xls', '.pdf', '.zip', '.rar', '.html'],
}


def rename_folder():
    for folder in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, folder)) == True:
            os.rename(os.path.join(directory, folder), os.path.join(directory, folder.lower()))

def create_move(ext, file_name):
    find = False
    for folder_name in folders:
        if "."+ext in folders[folder_name]:
            if folder_name not in os.listdir(directory):
                os.mkdir(os.path.join(directory, folder_name)) #(src(path,filename),dst(path,dest folder))
            shutil.move(os.path.join(directory, file_name), os.path.join(directory,folder_name))#(src,dst)
            find = True
            break
    if find != True:
        if other_files not in os.listdir(directory):
            os.mkdir(os.path.join(directory, other_files))
        shutil.move(os.path.join(directory, file_name), os.path.join(directory, other_files))



directory = "/home/nabeel/downloads"
all_files = os.listdir(directory)
length=len(all_files)
count = 1
other_files = input("Enter the Folder name for unknown files: ") 
rename_folder()


for file in all_files:  
    if os.path.isfile(os.path.join(directory, file)) == True:   # os.path.join(directory, i) == (directory + "/" +i)
        extension = file.split(".")[-1]
        create_move(extension, file)
    print(f"Total Files: {length}| Done: {count} | Left:{length-count}")
    count += 1
