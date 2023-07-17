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

## CODE TO GET THIS IN GHAT GPT

To generate the FF_SHOT script with all the features and prompts using ChatGPT, you can use the following GPT prompt:

```
Create a Python script named "ff_shot.py" that allows users to capture screenshots from multiple video sources. The script should have the following features:

Prompt the user to enter the number of video sources.
For each video source, prompt the user to enter the video path and a descriptive name.
Prompt the user to enter the number of screenshots to capture.
Install the required packages (FFmpeg and tqdm) if not already installed.
Show a progress bar during the screenshot capture process.
Handle errors and log any encountered errors.
Save the screenshots in the "FF_SHOT" folder in PNG format.
Ensure FFmpeg is installed and added to the system's PATH environment variable.
Display clear instructions and usage examples in the script and README.md file.
Please generate the script with the provided features and prompts.
```

Using this prompt, ChatGPT will generate a Python script for you with all the features and prompts mentioned. Feel free to modify and adapt the generated code as needed.

Feel free to modify the script and README.md to suit your specific needs or integrate it into your own projects.

Enjoy capturing screenshots from your video sources with FF_SHOT!
