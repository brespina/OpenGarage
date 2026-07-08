# 🚪 OpenGarage

*my first step into free and open-source software—welcome to the journey!*

[![mit license](https://img.shields.io/badge/license-mit-green.svg)](https://opensource.org/licenses/mit)
[![issues](https://img.shields.io/github/issues/brespina/OpenGarage)](https://github.com/brespina/OpenGarage/issues)
[![prs welcome](https://img.shields.io/badge/prs-welcome-brightgreen.svg?style=flat)](https://github.com/brespina/OpenGarage/pulls)

---

## 🎉 welcome

hello there! 👋 welcome to **OpenGarage**, my very first attempted contribution to the world of **free and open-source software**. i am building this project to provide simple tools that everyone can use freely, modify, and share. this journey marks the beginning of my adventure into creating software for the community. i hope you'll find these tools helpful and maybe even join me in improving them as well as our skills as developers! 🚀

**OpenGarage** is all about practicality, freedom, ... and no ads! it will offer small, useful tools for common tasks, such as video conversion, encoding text, and image manipulation, and anything i learn along the way. all software here is provided under the mit license—because software should be free, accessible, and shareable.

**adhd yapping**
for some reason, i often forget that i have the knowledge and tools available for a certain issue. yet, i find myself looking up websites to convert .mp4 to .gif, then i have to sign up, agree to their terms of service, agree to forced arbitration... it's exhausting. this is me, a fresh college graduate, who everyday realizes how much i do not know, fighting back against this modern idea of learned helplessness that has slightly been creeping in. i will make mistakes and i encourage anyone to correct and teach me, whether you be a high school competitive programmer, or an elderly beginner programmer. anyone can provide you with a learning opportunity <3

---

## ✨ what's inside?

OpenGarage currently plans to offer a collection of simple utilities that i already have used:

- **video file converters:**
  - mp4 to gif converter
  - webm to mp4 converter
- **downloaders:**
  - youtube to mp3 (audio extractor)
- **encoding tools:**
  - run-length encoding (rle) utility
- **..coming soon!**

---

## 🚀 how to get started

i've tried to make this project as easy as possible to use!

### 1. clone the repository

```bash
git clone https://github.com/brespina/OpenGarage.git
cd OpenGarage
```

### 2. set up a virtual environment

it's recommended to use a virtual environment to manage dependencies for this project. here's how to set it up:

#### for windows

```bash
python -m venv venv
venv\scripts\activate
```

#### for macOS and linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### FIXME: EXPLAIN CHOCO -> SCOOP -> PIPX -> PIPX INSTALL POETRY vs PIP INSTALL POETRY TOMORROw 10/13/2024

### X. install dependencies - note

***note: i am learning how to use pyproject.toml and its proving difficult for me but it seems vastly worth it.***

- **(i still am unsure if i set this up properly. i am reading poetry documentation, along with pre-commit, pre-commit-ci, black, and flake8)**
now that your virtual environment is activated, install the required packages:

```bash
# good bye requirements.txt pip install -r requirements.txt
poetry install
```

### 4. run a tool

heads up: these tools use relative imports, so run them **as modules from the repo root** (don't `cd` into the tool folder). on windows use `python`, on macOS/linux use `python3`. the result lands in that tool's own `output/` folder.

> **ffmpeg required:** the audio/video tools shell out to [ffmpeg](https://ffmpeg.org/download.html), so it needs to be installed and on your PATH. check with `ffmpeg -version`.

#### convert a .webm to .mp4

```bash
python -m tools.video_convertors.webm_to_mp4.webm_to_mp4 -ip /absolute/path/to/input/video.webm -of output_name.mp4
```

#### extract audio from a youtube video to .mp3

```bash
python -m tools.downloaders.youtube_to_mp3.youtube_to_mp3 "https://www.youtube.com/watch?v=VIDEO_ID" -q 192
```

the mp3 saves into the tool's own `output/` folder by default; pass `-o /some/dir` to pick a different one, and `-q` sets the bitrate in kbps (e.g. 128, 192, 320). run any tool with `-h` to see all its options.

---

## 📂 project structure

```plaintext
OpenGarage/
│
├── tools/
│    ├── downloaders/
│    │   ├── yt_convertor.py
│    │   └── youtube_to_mp3/
│    │       ├── youtube_to_mp3.py
│    │       └── output/
│    │
│    ├── encoders/
│    │   └── rle_encoder/
│    │       ├── rle_encoder.py
│    │       └── output/
│    │
│    └── video_convertors/
│        ├── ffm_convertor.py
│        ├── mp4_to_gif/
│        │   ├── mp4_to_gif.py
│        │   └── output/
│        │
│        └── webm_to_mp4/
│            ├── webm_to_mp4.py
│            └── output/
│
├── .venv/                      # virtual environment folder
│
├── LICENSE                     # mit license
├── README.md
├── pyproject.toml
├── poetry.lock
├── .gitignore
└── .pre-commit-config.yaml
```

---

## 🛠️ contributing

i am a certified newbie, so do not hesitate to critique and offer suggestions. if you have ideas for new tools or find a bug, feel free to:

1. **open an issue** for bugs or suggestions.
2. **submit a pull request** to share your improvements or new tools.

no contribution is too small. your help will not only improve the project but also teach me a lot along the way!

---

## 📝 license

this project is released under the mit license. you're free to use, modify, and distribute the software however you like. see the [license](license) file for more details.

---

## ❤️ acknowledgments

unfortunately, only recently did i become aware of what free and open-source software even was. but it is so heartwarming to see that it brandishes a huge community that gives back to each other. this project is my introduction to the free and open-source software community. thanks to everyone who makes software free, accessible, and shared. your work inspired me to create **OpenGarage**.

---

## 🙌 join me on this journey

if you found this project useful or have ideas for improvement, **please star this repository** (⭐) to show your support! every bit of feedback helps me grow as a developer and makes **OpenGarage** even better.

this is only the beginning—thanks for stopping by. let's build, make mistakes, learn, and share!  🚀
