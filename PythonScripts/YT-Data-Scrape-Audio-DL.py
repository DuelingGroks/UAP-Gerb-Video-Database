import subprocess
import json
import os
import sys
import re

def sanitize_filename(filename):
    """
    Removes or replaces characters not allowed in filenames for most OSes.
    """
    invalid_chars = r'[<>:"/\\|?*]'
    sanitized = re.sub(invalid_chars, '', filename)
    return sanitized.strip().rstrip('.')

def get_video_title(url):
    """
    Extracts the video title using yt-dlp without downloading the video.
    """
    cmd = ["yt-dlp", "-J", "--skip-download", url]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error extracting title for {url}:\n{result.stderr}")
        return None
    info = json.loads(result.stdout)
    return info.get("title", "Unknown_Title")

def download_audio(url, title, index):
    """
    Downloads the audio of a video using yt-dlp and saves it with a sanitized, sequential filename.
    """
    safe_title = sanitize_filename(title)
    output_template = f"{str(index).zfill(2)}-{safe_title}.%(ext)s"
    cmd = [
        "yt-dlp",
        "-f", "bestaudio",
        "--extract-audio",
        "--audio-format", "m4a",
        "-o", output_template,
        url
    ]
    print(f"Downloading audio for '{title}'...")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error downloading audio for '{title}':\n{result.stderr}")
    else:
        print(f"Audio downloaded successfully as {output_template.split('.')[0]}.m4a")

def download_metadata(url, title, index):
    """
    Downloads metadata of a video using yt-dlp and saves it with a sanitized, sequential filename.
    """
    safe_title = sanitize_filename(title)
    output_file = f"{str(index).zfill(2)}-{safe_title}-metadata.json"
    cmd = ["yt-dlp", "-J", "--skip-download", url]
    print(f"Downloading metadata for '{title}'...")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(result.stdout)
        print(f"Metadata saved as {output_file}")
    else:
        print(f"Error downloading metadata for '{title}':\n{result.stderr}")

def download_thumbnail(url, title, index):
    """
    Downloads the thumbnail of a video using yt-dlp and saves it with a sanitized, sequential filename.
    """
    safe_title = sanitize_filename(title)
    output_template = f"{str(index).zfill(2)}-{safe_title}-thumbnail.%(ext)s"
    cmd = [
        "yt-dlp",
        "--skip-download",
        "--write-thumbnail",
        "--convert-thumbnails", "jpg",
        "-o", output_template,
        url
    ]
    print(f"Downloading thumbnail for '{title}'...")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error downloading thumbnail for '{title}':\n{result.stderr}")
    else:
        print(f"Thumbnail downloaded as {output_template.split('.')[0]}.jpg")

def download_subtitles(url, title, index):
    """
    Downloads subtitles of a video using yt-dlp and saves them with a sanitized, sequential filename.
    """
    safe_title = sanitize_filename(title)
    output_template = f"{str(index).zfill(2)}-{safe_title}-subtitles.%(ext)s"
    cmd = [
        "yt-dlp",
        "--write-auto-subs",
        "--skip-download",
        "--sub-langs", "en",
        "--convert-subs", "vtt",
        "-o", output_template,
        url
    ]
    print(f"Downloading subtitles for '{title}'...")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error downloading subtitles for '{title}':\n{result.stderr}")
    else:
        print(f"Subtitles downloaded as {output_template.split('.')[0]}.vtt")

def process_url(url, index):
    """Helper function to process a single URL."""
    title = get_video_title(url)
    if title:
        download_audio(url, title, index)
        download_metadata(url, title, index)
        download_thumbnail(url, title, index)
        download_subtitles(url, title, index)
    else:
        print(f"Skipping {url} due to title extraction error.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python video_data_scrape.py <url_list.txt> or python video_data_scrape.py <single_url>")
        sys.exit(1)

    arg = sys.argv[1]

    # Simple check to see if the argument looks like a URL
    url_pattern = re.compile(r'^(https?://|www\.)')
    if url_pattern.match(arg):
        # Treat it as a single URL
        process_url(arg, 1)
    else:
        # Treat it as a file path
        try:
            with open(arg, 'r', encoding='utf-8') as f:
                urls = [line.strip() for line in f if line.strip()]
            for index, url in enumerate(urls, start=1):
                process_url(url, index)
        except FileNotFoundError:
            print(f"File not found: {arg}")
            sys.exit(1)

if __name__ == "__main__":
    main()
