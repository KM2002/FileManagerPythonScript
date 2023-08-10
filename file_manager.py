import os
import os.path
import time
import shutil
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

source_path = ''
dest_image = ''
dest_audio = ''
dest_video = ''
dest_files = ''
dest_installers = ''


# ? supported image types
image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw", ".avif"
                    ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]
# ? supported Video types
video_extensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
                    ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]
# ? supported Audio types
audio_extensions = [".m4a", ".flac", "mp3", ".wav", ".wma", ".aac"]
# ? supported Document types
document_extensions = [".doc", ".docx", ".odt", ".ipynb", ".java", ".c", ".cpp", ".html"
                       ".pdf", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".css", ".js", ".sh", ".go", ".ts"]
# ? supported installer files in mac os
installer_extensions = [".pkg", ".dmg", ".osx", ".app"]

def move_files(source, dest):
    shutil.move(source, dest)

def check_folder(dest, name):
    if os.path.exists(dest):
        move_files(os.path.join(source_path, name),dest )
    else:
        os.mkdir(dest)
        move_files(os.path.join(source_path, name),dest)
    
                         
class MoveFilesFunc(FileSystemEventHandler):
    def on_created(self, event):
        with os.scandir(source_path) as items:
            for item in items:
                name = item.name
                name = name.lower()
                self.check_images(dest_image, name)
                self.check_files(dest_files, name)
                self.check_audio(dest_audio, name)
                self.check_video(dest_video, name)
                self.check_installers(dest_installers, name)
            
    def check_images(self, dest, name):
        for file in image_extensions:
            if name.endswith(file):
                check_folder(dest_image, name)
                logging.info(f"Moved image file: {name}")
                        
    def check_files(self, dest, name):
        for file in document_extensions:
            if name.endswith(file):
                check_folder(dest_files, name)
                logging.info(f"Moved document file: {name}")
                
    def check_audio(self, dest, name):
        for file in audio_extensions:
            if name.endswith(file):
                check_folder(dest_audio, name)
                logging.info(f"Moved audio file: {name}")
                
    def check_video(self, dest, name):
        for file in video_extensions:
            if name.endswith(file):
                check_folder(dest_audio, name)
                logging.info(f"Moved video file: {name}")
                
    def check_installers(self, dest, name):
        for file in installer_extensions:
            if name.endswith(file):
                check_folder(dest_installers, name)
                logging.info(f"Moved package file: {name}")        
    
        

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source_path
    event_handler = MoveFilesFunc()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()    
