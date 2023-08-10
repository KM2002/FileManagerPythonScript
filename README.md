# FileManagerPythonScript

The File Organizer Script is a Python script that automatically organizes files in a specified directory based on their file types. 
It monitors the directory for newly created files and categorizes them into different destination folders based on their extensions.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
- [Configuration](#configuration)
- [Supported File Types](#supported-file-types)

## Features

- Automatically organizes files into specific folders based on their extensions.
- Automatically creates the destination directory if it doesn't exist already.
- Monitors a specified directory for new files and moves them to the appropriate folders.
- Supports various file types including images, videos, audios, documents, and installers.
- Easy-to-configure: You can set your source and destination paths along with supported file extensions.


## Requirements

- Python 3.x
- Watchdog library (`pip install watchdog`)


## Usage

1. Clone or download this repository to your local machine.
2. Install the required packages using `pip` if you haven't already:

    ```sh
    pip install watchdog
    ```
3. Edit the script to configure your source and destination paths, and supported file extensions.
4. Open a terminal and navigate to the directory containing the script.
5. Run the script:

    ```sh
    python file_manager.py
    ```
   The script will start monitoring the specified directory and organizing files automatically.

6. To stop the script, press `Ctrl+C` in the terminal.

## Configuration

You can customize the behavior of the script by modifying the following variables in the script:

- `source_path`: The directory to monitor for new files.
- `dest_image`, `dest_audio`, `dest_files`, `dest_installers`, etc.: Destination directories for different file types.
- `image_extensions`, `audio_extensions`, `document_extensions`, `installer_extensions`, etc.: Lists of supported file extensions for each category.

## Supported File Types

The script supports the following file types for automatic organization:

- Images (e.g., jpg, png, gif)
- Videos (e.g., mp4, avi, mov)
- Audios (e.g., mp3, wav, m4a)
- Documents (e.g., pdf, docx, xls)
- Installers (e.g., pkg, dmg, app)

You can extend or modify the lists of supported file extensions as needed.
