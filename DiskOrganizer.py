import os
import shutil
import time

class DiskOrganizer:
    def __init__(self, target_drive):
        self.target_drive = target_drive

    def analyze_space(self):
        """Analyze disk space and return free and used space."""
        total, used, free = shutil.disk_usage(self.target_drive)
        print(f"Total: {total // (2**30)} GiB")
        print(f"Used: {used // (2**30)} GiB")
        print(f"Free: {free // (2**30)} GiB")
        return total, used, free

    def defragment_drive(self):
        """A placeholder for defragmentation logic."""
        print("Defragmenting drive... (This is a placeholder operation)")
        time.sleep(2)  # simulate time delay
        print("Defragmentation completed.")

    def organize_files(self):
        """Organize files into subdirectories based on their extensions."""
        print("Organizing files...")
        for root, dirs, files in os.walk(self.target_drive):
            for file in files:
                file_path = os.path.join(root, file)
                file_extension = file.split('.')[-1]
                destination_dir = os.path.join(self.target_drive, file_extension)

                if not os.path.exists(destination_dir):
                    os.makedirs(destination_dir)

                try:
                    shutil.move(file_path, destination_dir)
                    print(f"Moved {file} to {destination_dir}")
                except Exception as e:
                    print(f"Error moving file {file}: {e}")

    def run(self):
        """Run the disk organizer tasks."""
        print(f"Starting DiskOrganizer on {self.target_drive}")
        self.analyze_space()
        self.defragment_drive()
        self.organize_files()
        self.analyze_space()
        print("DiskOrganizer completed.")

if __name__ == "__main__":
    target_drive = "C:\\"  # Change this to the target drive you want to organize
    organizer = DiskOrganizer(target_drive)
    organizer.run()