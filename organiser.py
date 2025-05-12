import os
import shutil
from colorama import Fore,Style,init
from datetime import datetime

init(autoreset=True)

file_type={
    "Images":[".jpg",".png",".jpeg",".gif"],
    "Documents":[".pdf",".docx",".txt",".pptx"],
    "Videos":[".mp4",".mkv",".mov"],
    "Audio":[".mp3",".wav"],
    "Archives":[".zip",".rar",".tar",".gz"]
}
def checkFolder(directory):
    Folder_list=["Images", "Documents", "Videos", "Audio", "Archives", "Others"]
    for folder in Folder_list:
        folder_path=os.path.join(directory,folder)
        if not(os.path.isdir(folder_path)):
            os.mkdir(folder_path)
            print(Fore.GREEN+f"[+] Created folder :\t{folder_path}")
        else:
            print(Fore.YELLOW+f"[!] Folder Already Exists :\t{folder_path}")

def classify_move(directory):
    log_path = os.path.join(directory, "log.txt")
    with open(log_path,"a") as log_file:
        for file in os.listdir(directory):
            file_path=os.path.join(directory,file)
            if os.path.isdir(file_path):
                continue
            if os.path.isfile(file_path):
                ext= os.path.splitext(file)[1].lower()
                moved=False
                for Folder,Extensions in file_type.items():
                    if ext in Extensions:
                        dest_folder=os.path.join(directory,Folder)
                        try:
                            shutil.move(file_path, os.path.join(dest_folder, file))
                            timestamp=datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
                            log_file.write(f"{timestamp} Moved: {file} -> {Folder}\n")
                            print(Fore.CYAN+f"Moved: {file} -> {Folder}")
                        except PermissionError:
                            print(Fore.MAGENTA+f"Permission denied: {file} (maybe open in another app)")
                        except FileNotFoundError:
                            print(Fore.RED+f"Folder not found: {dest_folder}")
                        except Exception as e:
                            print(Fore.LIGHTRED_EX + f"Error moving {file}: {e}")
                        moved = True
                        break
                if not moved:
                    other_folder= os.path.join(directory,"Others")
                    try:
                        shutil.move(file_path, os.path.join(other_folder, file))
                        timestamp=datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
                        print(f"Moved: {file} -> Others")
                        log_file.write(f"{timestamp} Moved {file} to Others Folder\n")
                    except Exception as e:
                        print(f"Error moving {file} to Others: {e}")


def main():
    directory=input("Enter the directory that is to be sorted\t")
    if os.path.exists(directory):
        print(Fore.CYAN+"Starting the file organization process......\n")
        
        checkFolder(directory)

        classify_move(directory)

        print(Fore.GREEN+"\nFile Organization Completed\n")
    else:
        print(Fore.RED+"Invalid path.Please Check the Path and try again")

if __name__=="__main__":
    main()