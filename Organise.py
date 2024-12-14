import os 
import shutil


class Organise():
    """
    Program: File organiser
    Developer: ammaar0x01
    Started: 14.04.24
    Updated: 13.12.24
    
    Paste and run this script in the folder that you want to organise
    
    """
    # -----------
    # for singleton design pattern
    _instance = None 
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Organise, cls).__new__(cls)
        return cls._instance
    # -----------
    
    _CURRENT_DIR:str
    _ALL_FILES:list
    _CHILD_DIRS:list
    _FILE__FILE_EXTENSIONS:dict
    
    def __init__(self): 
        self._CURRENT_DIR = os.getcwd()
        self._ALL_FILES = os.listdir()
        self._CHILD_DIRS = [
            "text",
            "documents", 
            "images",
            "music",
            "videos",
            "programs", 
            "shortcuts", 
            "archives", 
            "other"
        ]
        self._FILE_EXTENSIONS = {
            "programs": [
                ".exe", ".msi", ".setup", ".py", ".bat", 
                ".wbs", ".jar", ".java", ".kt", ".sql", 
                ".db", ".js"
            ],
            "text": [".txt", ".md", ".htm", ".html", ".css", ".xml", ".json", "yml", "yaml"], 
            "documents": [".doc", ".docx", ".pdf", ".xls", ".csv"], 
            "images": [".png", ".jpg", ".jpeg", ".webp"],
            "music": [".mp3", ".wav"], 
            "videos": [".mp4", ".avi", ".mov"], 
            "shortcuts": [".url"], 
            "archives": [".zip", ".rar", ".tar", ".7z"], 
            "other": [".iso", ".img"]
        }
        
        self._check_child_dirs()
        self._backup_files()
    # ========================================
    
    def _check_child_dirs(self) -> None: 
        '''
        Checks whether the child directories already exist\n
        Creates the directory if it doesn't exist
        '''
        for child_dir in self._CHILD_DIRS:
            full_child_path = self._CURRENT_DIR + "/" + child_dir 
            if not os.path.exists(full_child_path):
                os.mkdir(child_dir)
    # ----------------------------------------    
  
    def _backup_files(self) -> None: 
        '''
        Prints all the files and folders from a parent directory to a text file
        '''
        with open("_all_files.tmp", "w") as backup:
            try: 
                backup.write(f"All files and folders from \n{self._CURRENT_DIR}\n")
                backup.write(40 * "=")
                backup.write("\n")
                for file in self._ALL_FILES:
                    backup.write(f"- {file}\n")
                                
                backup.write(40 * "=")
                
            except UnicodeEncodeError as unicode_err:
                print(unicode_err) 
                backup.write(f"- <file with strange characters>\n")
                
            finally:
                backup.write(f"\nTotal number of files and folders: {len(self._ALL_FILES)}\n")
                backup.write(40 * "=")
                backup.close()
    # ----------------------------------------    

    def _move_file(self, filename, file_extension, dest_dir) -> None: 
        if file_extension in filename \
            and "." in filename \
            and filename != "Organise.py":  
                
            file_path = self._CURRENT_DIR + "\\" + filename
            try: 
                shutil.move(src=file_path, dst=dest_dir)
                print(f"\n<'{filename}' moved to {dest_dir}>")

            except Exception as err: 
                print(err, end="\n")
                # input("continue...\n")
    # ----------------------------------------    
                
    def organise_files(self) -> None: 
        # paths to child directories
        dir_text = f"{self._CURRENT_DIR}/text"
        dir_docs = f"{self._CURRENT_DIR}/documents"
        dir_images = f"{self._CURRENT_DIR}/images"
        dir_music = f"{self._CURRENT_DIR}/music"
        dir_videos = f"{self._CURRENT_DIR}/videos"
        dir_programs = f"{self._CURRENT_DIR}/programs"
        dir_shortcuts = f"{self._CURRENT_DIR}/shortcuts"
        dir_archives = f"{self._CURRENT_DIR}/archives"
        dir_other = f"{self._CURRENT_DIR}/other"
    
        # moving the files to their appropriate folders
        for file in self._ALL_FILES:
            for file_extension in self._FILE_EXTENSIONS["text"]:
                self._move_file(file, file_extension, dir_text)
                
            for file_extension in self._FILE_EXTENSIONS["documents"]:
                self._move_file(file, file_extension, dir_docs)
                
            for file_extension in self._FILE_EXTENSIONS["images"]:
                self._move_file(file, file_extension, dir_images)
                
            for file_extension in self._FILE_EXTENSIONS["music"]:
                self._move_file(file, file_extension, dir_music)
            
            for file_extension in self._FILE_EXTENSIONS["videos"]:
                self._move_file(file, file_extension, dir_videos)
            
            for file_extension in self._FILE_EXTENSIONS["programs"]:
                self._move_file(file, file_extension, dir_programs)
                
            for file_extension in self._FILE_EXTENSIONS["shortcuts"]:
                self._move_file(file, file_extension, dir_shortcuts)
                
            for file_extension in self._FILE_EXTENSIONS["archives"]:
                self._move_file(file, file_extension, dir_archives)
                
            for file_extension in self._FILE_EXTENSIONS["other"]:
                self._move_file(file, file_extension, dir_other)
    # ----------------------------------------    

# ==================================================

def main() -> None: 
    test_obj = Organise()
    test_obj.organise_files()
    print("\n***Files organised***")

    
if __name__ == "__main__":
    main()
# ---------------------------------