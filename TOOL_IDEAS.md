# 🧰 tool ideas

a running wishlist of small, useful tools that fit the OpenGarage spirit:
practical, offline-first, no ads, no sign-ups, no forced arbitration. things
you'd otherwise paste into a sketchy website. pick whatever looks fun — none of
this is set in stone, and ideas/PRs are welcome.

> loose priority tags: 🟢 easy starter · 🟡 medium · 🔴 chunky project

---

## 📁 file & media converters

these slot right next to the existing `video_convertors/` tools.

- 🟢 **image converter** — png ↔ jpg ↔ webp ↔ avif, with a quality flag (Pillow)
- 🟢 **image resizer / thumbnailer** — resize/crop by max dimension, keep aspect ratio
- 🟡 **gif ↔ mp4** — the reverse of the existing mp4→gif tool
- 🟡 **audio converter** — mp3 ↔ wav ↔ flac ↔ m4a (ffmpeg, same pattern as yt tool)
- 🟡 **pdf toolkit** — merge, split, rotate, extract pages (pypdf)
- 🟡 **document converter** — markdown → html / pdf, docx → pdf (pandoc wrapper)
- 🔴 **image → pdf / pdf → images** — scan-style bundling and page extraction

## ⬇️ downloaders

siblings for the new `downloaders/` folder.

- 🟢 **youtube video downloader** — same yt-dlp base, keep video + pick resolution
- 🟡 **playlist / channel batch download** — reuse `YTConvertor`, loop over entries
- 🟡 **generic media grabber** — hand any yt-dlp-supported site a url
- 🟡 **subtitle downloader** — pull `.srt`/`.vtt` captions for a video

## 🔤 encoding & text tools

extend the existing `encoders/` folder.

- 🟢 **base64 encode/decode** — text and files, both directions
- 🟢 **hash generator** — md5 / sha1 / sha256 for a string or file
- 🟢 **url encode/decode** — percent-encoding helper
- 🟢 **case / slug converter** — snake ↔ camel ↔ kebab ↔ title, and url slugs
- 🟡 **qr code generator** — text/url → png (qrcode lib)
- 🟡 **json ↔ yaml ↔ toml converter** — round-trip config formats
- 🟡 **csv ↔ json converter** — with a pretty-print / flatten option

## 🖼️ image manipulation

the "image manipulation" bucket mentioned in the readme.

- 🟢 **exif viewer / stripper** — read metadata or scrub it for privacy
- 🟡 **watermark tool** — overlay text/logo with position + opacity
- 🟡 **color palette extractor** — dominant colors from an image
- 🔴 **background remover** — cutout via `rembg` (heavier dependency)

## 🧮 everyday utilities

small quality-of-life scripts.

- 🟢 **unit converter** — length / weight / temperature / data sizes
- 🟢 **password generator** — length + character-class flags
- 🟢 **stopwatch / countdown timer** — cli with sound on finish
- 🟡 **bulk file renamer** — regex / sequential / date-based patterns
- 🟡 **duplicate file finder** — by content hash, report or delete
- 🟡 **directory tree printer** — export a folder structure to markdown

---

## 🌱 project-wide "nice to haves"

not tools, but things that would make the repo nicer for everyone:

- **shared cli scaffolding** — a tiny helper so every tool gets consistent
  `argparse` setup, an `output/` resolver, and a dependency-check (like the
  ffmpeg check in `youtube_to_mp3`) without copy-pasting.
- **tests** — even a couple of smoke tests per tool would build confidence.
- **a proper `[project]` table in `pyproject.toml`** — migrate off the
  deprecated `[tool.poetry]` metadata that `poetry check` warns about.
- **per-tool README snippets** — a one-liner usage example living next to each
  tool.

---

*have an idea that isn't here? open an issue or add it to this list in a PR.* 🚪
