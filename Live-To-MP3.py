import yt_dlp
import os
import re

def sanitize_filename(filename):
    """Removes special characters from the filename to ensure it's filesystem-safe."""
    return re.sub(r'[\/:*?"<>|]', '', filename)  # Removes invalid characters

def download_live_audio(youtube_url, output_dir="Live-to-MP3"):
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),  # Uses video title
    }

    # Download the audio and get metadata
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(youtube_url, download=True)  # Extract info and download
        title = info.get('title', 'Unknown')  # Get video title
        safe_title = sanitize_filename(title)  # Sanitize title

        # Rename the file to sanitized version
        old_filename = os.path.join(output_dir, f"{title}.mp3")
        new_filename = os.path.join(output_dir, f"{safe_title}.mp3")
        if old_filename != new_filename and os.path.exists(old_filename):
            os.rename(old_filename, new_filename)

        print(f"Downloaded and saved as: {new_filename}")

if __name__ == "__main__":
    youtube_url = input("Enter YouTube Live URL: ")
    download_live_audio(youtube_url)
