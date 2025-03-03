import yt_dlp
import os
import re

def sanitize_filename(filename):
    """Removes special characters from the filename to ensure it's filesystem-safe."""
    return re.sub(r'[\/:*?"<>|]', '', filename)  # Removes invalid characters

def download_youtube_media(youtube_urls, download_type, output_dir):
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    if download_type == "audio":
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),  # Uses video title
        }
    else:  # Video
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4',  # Ensures video and audio are merged
            'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),  # Uses video title
        }

    for youtube_url in youtube_urls:
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(youtube_url, download=True)  # Extract info and download
                title = info.get('title', 'Unknown')  # Get video title
                safe_title = sanitize_filename(title)  # Sanitize title

                # Rename file to sanitized version
                file_ext = "mp3" if download_type == "audio" else "mp4"
                old_filename = os.path.join(output_dir, f"{title}.{file_ext}")
                new_filename = os.path.join(output_dir, f"{safe_title}.{file_ext}")

                if old_filename != new_filename and os.path.exists(old_filename):
                    os.rename(old_filename, new_filename)

                print(f"✅ Downloaded and saved as: {new_filename}\n")

        except Exception as e:
            print(f"❌ Error downloading {youtube_url}: {e}")

if __name__ == "__main__":
    # YarrrTube Welcome Message 🏴‍☠️

    print("🏴‍☠️  Welcome to YarrrTube!  🏴‍☠️\n")
    print("🎵 Download YouTube videos or audio to your heart’s content! 🎥\n")

    # Prompt for download type first
    print("📥 Choose download type:")
    print("  [1] Video (MP4)")
    print("  [2] Audio (MP3)")

    download_choice = input("➡️ Enter choice (1/2): ").strip()
    while download_choice not in ["1", "2"]:
        download_choice = input("⚠️ Invalid choice. Enter '1' for video or '2' for audio: ").strip()

    download_type = "video" if download_choice == "1" else "audio"
    output_dir = "Videos" if download_type == "video" else "Audios"

    # Collect YouTube URLs
    youtube_urls = []
    print("\n🎥 Enter YouTube URLs. Press Enter on an empty line when done.")
    while True:
        youtube_url = input("🔗 Enter YouTube URL: ").strip()
        if not youtube_url:
            break  # Stop collecting URLs if input is empty
        youtube_urls.append(youtube_url)

    if youtube_urls:
        print(f"\n🚀 Starting {download_type} downloads...\n")
        download_youtube_media(youtube_urls, download_type, output_dir)
    else:
        print("👋 No URLs entered. Exiting...")
