import os
import subprocess
import sys
import logging
from tqdm import tqdm

# Set variables
output_folder = 'FF_SHOT'
num_sources = int(input("Enter the number of video sources: ").strip())

sources = []
videos = []

# Prompt the user for video sources and inputs
for i in range(num_sources):
    video_path = input(f"Enter the video {i + 1} path: ").strip('"')
    source_name = input(f"Enter the source {i + 1} name: ")
    sources.append(source_name)
    videos.append(video_path)

# Prompt the user for the number of screenshots they want
num_screenshots = int(input("Enter the number of screenshots you want: ").strip())

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Configure logging
log_filename = 'ff_shot.log'
logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Check if required packages are installed, and install them if necessary
required_packages = ['tqdm', 'ffmpeg-python']

for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package, '--user'])
        logging.info(f"Installed package: {package}")

def get_video_duration(video_path):
    cmd = ['ffprobe', '-i', video_path, '-show_entries', 'format=duration', '-v', 'quiet', '-of', 'csv=p=0']
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT).decode().strip()
        duration = float(output)
        return duration
    except subprocess.CalledProcessError as e:
        logging.error(f"Error getting video duration for {video_path}: {e.output.decode().strip()}")
        return None
    except ValueError:
        logging.error(f"Invalid video duration for {video_path}. Please ensure the video file is valid.")
        return None

# Remove existing files in the output folder
for file in os.listdir(output_folder):
    file_path = os.path.join(output_folder, file)
    if os.path.isfile(file_path):
        os.remove(file_path)

# Iterate over each video source
for source, video in zip(sources, videos):
    logging.info(f"Processing screenshots for {source}")

    duration = get_video_duration(video)

    if duration is None:
        logging.error(f"Error processing {source}. Skipping to the next source.")
        print()
        continue

    interval = duration / num_screenshots

    # Set up progress indicator for each video source
    progress_bar = tqdm(total=num_screenshots, desc=f"Processing - {source}")

    # Generate screenshots for the current video source
    for i in range(num_screenshots):
        time_offset = interval * i
        screenshot_name = f"Screenshot {i + 1} [{source}].png"
        screenshot_path = os.path.join(output_folder, screenshot_name)
        try:
            subprocess.run(["ffmpeg", "-y", "-ss", str(time_offset), "-i", video, "-vframes", "1", "-q:v", "1", "-loglevel", "quiet", screenshot_path], shell=True, check=True)
        except subprocess.CalledProcessError as e:
            logging.error(f"Error capturing screenshot {i+1} for {source}: {e}")
        except Exception as e:
            logging.error(f"Unknown error occurred while capturing screenshot {i+1} for {source}: {e}")

        # Update the progress bar with the current video name and completion percentage
        progress_bar.set_postfix(video=source, completed=f"{(i+1)/num_screenshots*100:.2f}%")
        progress_bar.update()

    # Close the progress bar for the current video source
    progress_bar.close()

    logging.info(f"Screenshots for {source} completed.")
    print()

logging.info("Screenshot generation completed!")
