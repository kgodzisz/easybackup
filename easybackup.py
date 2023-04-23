import os
import time

def backup_files(source, destination, compression):
    timestamp = time.strftime('%Y-%m-%d-%H-%M-%S')
    filename = f"backup-{timestamp}.tar.{compression}"
    tar_command = f"tar -czvf {destination}/{filename} {source}"
    if compression == "bz2":
        tar_command = f"tar -cjvf {destination}/{filename} {source}"
    os.system(tar_command)
    print(f"Backup created: {destination}/{filename}")

backup_files("/data", "/backups", "gz")