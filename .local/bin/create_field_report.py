#!/usr/bin/env python3
import os
from datetime import datetime

# Set directories
recordings_dir = "/home/denis/drive/Daygame/Recordings"
logseq_journal_path = "/home/denis/logseq/journals"

# Step 1: Find the latest directory based on date format (YYYYMMDD)
def get_latest_directory(recordings_dir):
    subdirs = [d for d in os.listdir(recordings_dir) if os.path.isdir(os.path.join(recordings_dir, d))]
    latest_dir = sorted(subdirs, reverse=True)[0]  # Get the latest date-sorted directory
    return latest_dir

# Step 2: Create Logseq block for each audio file
def create_logseq_entry(latest_dir):
    # Convert latest_dir to YYYY_MM_DD format for Logseq journal file
    date = datetime.strptime(latest_dir, "%Y%m%d").strftime("%Y_%m_%d")
    journal_file_path = os.path.join(logseq_journal_path, f"{date}.md")

    # Check if the journal file exists, if not, create it
    if not os.path.exists(journal_file_path):
        with open(journal_file_path, "w") as f:
            f.write(f"# {date}\n\n")  # Basic structure for Logseq journal

    # Step 3: Write Logseq block for each audio file in the latest directory
    with open(journal_file_path, "a") as journal_file:
        journal_file.write("\n- [[field report]]\n")
        journal_file.write("         - location:\n")

        # Loop through each audio file in the latest directory
        full_dir_path = os.path.join(recordings_dir, latest_dir)
        for audiofile in os.listdir(full_dir_path):
            if audiofile.endswith(".mp3"):
                filename = os.path.splitext(audiofile)[0]  # Remove extension to get just the name
                journal_file.write(f"    - {filename}\n")
                journal_file.write(f"         - ![]({os.path.join(full_dir_path, audiofile)})\n")
                journal_file.write("         - notes\n")

# Execute the script
latest_dir = get_latest_directory(recordings_dir)
create_logseq_entry(latest_dir)

print(f"Logseq entries created for audio files in the {latest_dir} directory.")
