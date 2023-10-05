# FF_SHOT - Video Snapshot Generator

FF_SHOT is a Python script that allows you to easily capture screenshots from multiple video sources. It is designed to be user-friendly and provides a command-line interface to specify the video sources, the number of screenshots to capture, and the output folder.

## Features

- Capture screenshots from multiple video sources effortlessly.
- Specify the desired number of screenshots to capture for each video source.
- Automatic installation of required packages (FFmpeg and tqdm) if not already installed.
- Progress visualization with a detailed progress bar, providing real-time feedback on the screenshot capture process.
- Error handling and logging of any encountered errors during the process.

## Usage

1. Specify the number of video sources you want to capture screenshots from.
2. Provide the path of each video source file and assign a descriptive name for each source.
3. Specify the number of screenshots you want to capture for each video source.
4. The script will automatically install the necessary packages if they are not already installed.
5. Screenshots will be saved in the "FF_SHOT" folder in PNG format.

### Output File Format

The script will save the screenshots with the following naming convention:

```
Screenshot {index} [{source}].png
```

Where `{index}` represents the sequential number of the screenshot, and `{source}` represents the name of the video source.

## Requirements

- FFmpeg: Ensure FFmpeg is installed and added to your system's PATH environment variable.
- Python 3.x: Make sure you have Python 3.x installed on your system.

## Installation

1. Clone this repository or download the script file to your local machine.
2. Install the required packages by running the following command:

```
pip install -r requirements.txt
```

Note: This will install FFmpeg and tqdm if they are not already installed.

## Example

Here's an example usage of the script:
```
$ python ff_shot.py

Enter the number of video sources: 2
Enter the video 1 path: /path/to/video1.mp4
Enter the source 1 name: Source 1
Enter the video 2 path: /path/to/video2.mp4
Enter the source 2 name: Source 2
Enter the number of screenshots you want: 5

Screenshot generation completed!
```

## Notes

- It is recommended to have FFmpeg installed and added to your system's PATH environment variable for the script to work properly.
- Make sure you have the necessary permissions to write to the output folder.

## SUMMARISED THAT I PROMPT USED TO CREATE THIS SCRIPT IN GHAT GPT

To generate the FF_SHOT script with all the features and prompts using ChatGPT, you can use the following GPT prompt:

```
Create a Python script named "ff_shot.py" that allows users to capture screenshots from multiple video sources. The script should have the following features:

1. Prompt the user to enter the number of video sources.
2. For each video source, prompt the user to enter the video path and a descriptive name.
3. Prompt the user to enter the number of screenshots to capture.
4. Install the required packages (FFmpeg and tqdm) if not already installed.
5. Show a progress bar during the screenshot capture process to indicate the status of the screenshot generation.
6. Handle errors gracefully and log any encountered errors to a log file.
7. Save the screenshots in the "FF_SHOT" folder in PNG format.
8. Ensure FFmpeg is installed and added to the system's PATH environment variable to enable video processing.
9. Display clear instructions and usage examples in the script and README.md file to guide users on how to use the script effectively.

The script should follow these steps to capture the screenshots:
1. Validate and parse the user inputs to obtain the number of video sources, video paths, source names, and number of screenshots.
2. Check if the required packages (FFmpeg and tqdm) are installed and install them if necessary.
3. Create the "FF_SHOT" folder if it doesn't exist.
4. For each video source, calculate the duration of the video using FFprobe, and determine the time interval between each screenshot based on the desired number of screenshots.
5. Initialize a progress bar to track the screenshot generation process for each video source.
6. Use FFmpeg to capture screenshots at the specified time intervals and save them in the "FF_SHOT" folder with appropriate filenames.
7. Update the progress bar after capturing each screenshot and display the current status of the process.
8. Handle any errors that occur during the screenshot generation and log them to a log file for debugging purposes.
9. Once all screenshots have been captured for all video sources, display a completion message.

The script should provide a clear and user-friendly command-line interface, guiding users through the process of capturing screenshots and handling any errors that may occur. Additionally, it should include comprehensive instructions and usage examples in both the script and the README.md file to assist users in understanding and using the script effectively.

Please generate the script with the provided features and prompts, ensuring that the core mechanism of the script is explained in detail.

```

Using this prompt, ChatGPT will generate a Python script for you with all the features and prompts mentioned. Feel free to modify and adapt the generated code as needed.

Feel free to modify the script and README.md to suit your specific needs or integrate it into your own projects.

Enjoy capturing screenshots from your video sources with FF_SHOT!
