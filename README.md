# YarrrTube

YarrrTube allows you to download videos and audio from YouTube as MP4/MP3 files.

## Installation

To clone the repo, run:

```
git clone https://github.com/chacei/YarrrTube.git
```

Once cloned, you'll need to install `yt-dlp`, which is a tool for downloading content from YouTube and other websites. You can either just run `pip install yt-dlp`, or alternatively install it in a virtual environment with the steps below:

```
cd YarrrTube
python3 -m venv venv
source venv/bin/activate
pip install yt-dlp
```

You can run `deactivate` to exit out of the virtual environment after you've finished downloading your videos. If you wish to download more at a later date, run `source venv/bin/activate` from the repo home directory to re-enter the virtual environment before running scripts.

## Usage

Simply run:

```
python3 YarrrTube.py
```

and follow the instructions to download your content.
