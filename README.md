# Folder Cleaner and Organizer

## Overview

The Folder Cleaner and Organizer is a Python utility designed to automatically organize files into specified directories based on their types. This tool monitors a source directory for new or modified files and sorts them into categories such as Images, PDFs, Videos, and Documents. 

## Features

- **Automatic File Sorting**: Files are automatically moved to designated folders based on their type (Images, PDFs, Videos, Documents).
- **File Renaming**: Handles duplicate files by renaming them to avoid overwriting.
- **Real-Time Monitoring**: Uses file system monitoring to detect changes and organize files as they are added or modified.

## Installation

To set up the Folder Cleaner and Organizer, follow these steps:

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/yourusername/folder-cleaner-organizer.git

2. **Navigate to the Project Directory:**:
   ```sh
   cd Desktop Cleaner

## Configuration

Edit the following variables in the script to match your directory paths:

- `source_dir`: Path to the directory to monitor.
- `dest_dir_image`: Path where image files will be moved.
- `dest_dir_pdf`: Path where PDF files will be moved.
- `dest_dir_videos`: Path where video files will be moved.
- `dest_dir_doc`: Path where document files will be moved.

## Usage

1. **Run the Program**:
   ```sh
   python main.py
   ```
   The script will start monitoring the `source_dir` directory for changes and organize files into the specified directories based on their extensions.

2. **File Categories**
   - **Images**: Files with extensions `.jpg`, `.png`, `.gif`, etc.
   - **PDFs**: Files with the `.pdf` extension.
   - **Videos**: Files with extensions like `.mp4`, `.avi`, `.mov`, etc.
   - **Documents**: Files with extensions like `.doc`, `.xlsx`, `.ppt`, etc.

## Logging

Logs are generated to provide information about the program’s activity. These logs will be available in the console where the script is run.