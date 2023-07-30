import os
import subprocess
import sys
import logging
import json
from tqdm import tqdm
import colorama
from colorama import Fore, Style

SETTINGS_FILE = 'settings.json'

# Colorama initialization for colored text
colorama.init()


def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def show_home_menu():
    clear_screen()
    print(Fore.CYAN + "=== Home Menu ===")
    print("1. Settings")
    print("2. Take Screenshots")
    print("0. Exit" + Style.RESET_ALL)


def show_settings_menu():
    clear_screen()
    print(Fore.CYAN + "=== Settings ===")
    print("1. Toggle Output Image Format (PNG/JPG)")
    print("2. Set Output Folder Name")
    print("0. Back to Home Menu" + Style.RESET_ALL)


def handle_settings():
    while True:
        show_settings_menu()
        user_input = input(Fore.GREEN + "Enter your choice: " + Style.RESET_ALL)

        if user_input == '0':
            break
        elif user_input == '1':
            toggle_output_image_format()
        elif user_input == '2':
            handle_output_folder_name()


def toggle_output_image_format():
    global output_image_format
    if output_image_format == 'PNG':
        output_image_format = 'JPG'
    else:
        output_image_format = 'PNG'
    print(Fore.YELLOW + f"Output image format set to: {output_image_format}" + Style.RESET_ALL)
    input("Press Enter to continue...")


def handle_output_folder_name():
    global output_folder
    output_folder = input(Fore.YELLOW + "Enter the output folder name: " + Style.RESET_ALL).strip()


def take_screenshots():
    clear_screen()
    print(Fore.CYAN + "=== Take Screenshots ===" + Style.RESET_ALL)

    # Set variables
    num_sources = int(input(Fore.YELLOW + "Enter the number of video sources: " + Style.RESET_ALL).strip())

    sources = []
    videos = []

    # Prompt the user for video sources and inputs
    for i in range(num_sources):
        video_path = input(Fore.YELLOW + f"Enter the video {i + 1} path: " + Style.RESET_ALL).strip('"')
        source_name = input(Fore.YELLOW + f"Enter the source {i + 1} name: " + Style.RESET_ALL)
        sources.append(source_name)
        videos.append(video_path)

    # Prompt the user for the number of screenshots they want
    num_screenshots = int(input(Fore.YELLOW + "Enter the number of screenshots you want: " + Style.RESET_ALL).strip())

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
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package, '--user'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
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
            screenshot_name = f"Screenshot {i + 1} [{source}].{output_image_format}"
            screenshot_path = os.path.join(output_folder, screenshot_name)
            try:
                subprocess.run(
                    ["ffmpeg", "-y", "-ss", str(time_offset), "-i", video, "-vframes", "1", "-q:v", "1",
                     "-loglevel", "quiet", screenshot_path], shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
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
    input("Screenshots generated successfully! Press Enter to continue...")


def load_settings():
    global output_image_format, output_folder

    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, 'r') as f:
            settings = json.load(f)
            output_image_format = settings.get('output_image_format', 'PNG')
            output_folder = settings.get('output_folder', 'FF_SHOT')
    else:
        output_image_format = 'PNG'
        output_folder = 'FF_SHOT'


def save_settings():
    settings = {
        'output_image_format': output_image_format,
        'output_folder': output_folder
    }

    with open(SETTINGS_FILE, 'w') as f:
        json.dump(settings, f)


def main():
    load_settings()

    while True:
        show_home_menu()
        user_input = input(Fore.GREEN + "Enter your choice: " + Style.RESET_ALL)

        if user_input == '0':
            save_settings()
            clear_screen()
            print(Fore.CYAN + "Thank you for using FF_Shot! Goodbye!" + Style.RESET_ALL)
            break
        elif user_input == '1':
            handle_settings()
        elif user_input == '2':
            take_screenshots()


if __name__ == "__main__":
    main()
