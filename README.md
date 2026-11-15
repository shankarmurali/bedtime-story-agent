# Bedtime Story Agent

An AI agent that writes one original short story every evening and narrates it to an MP3, so there is something new to listen to before sleep.

Each night it picks a genre, finds one small real detail in the day's news, grows a piece of fiction from it, and reads the result aloud in a single narrator voice. It ends with one line saying which part was real.

## What you get each night

- An MP3 of about seven minutes, read word for word.
- The story text.
- A "What was real" line with the source of the seed.

## How it works

1. **Genre.** Chosen by weekday: far-future science fiction, the paranormal, lesser-told Indian mythology, a tale about an undeciphered script, near-future fiction from the news, folklore, and one free night.
2. **Seed.** A few web searches for the day's news in science, technology, space, archaeology or nature. One concrete detail becomes the starting point.
3. **Story.** 900 to 1,100 words, written for the ear, calm enough for bedtime.
4. **Narration.** The open-source [Kokoro](https://github.com/thewh1teagle/kokoro-onnx) speech model renders the text to audio locally in the agent's sandbox. No text is sent to a speech service.
5. **Delivery.** The MP3 and text are returned in the agent's session. Nothing is written to cloud storage.

## Files

| File | Purpose |
|---|---|
| `task-prompt.md` | The full instruction for the nightly run. This is the part you paste into your agent's scheduler. |
| `setup.sh` | Installs pinned packages and downloads the voice model, verifying checksums. |
| `narrate.py` | Turns a plain-text story into an MP3. |
| `SECURITY.md` | Risks of running this unattended, and how the design limits them. |

## Set it up

You need an AI agent that can run on a schedule, search the web, run shell commands and send you a file. This was built with Claude's scheduled tasks; other agents with the same abilities should work.

1. Read `SECURITY.md`.
2. Create a daily scheduled task about half an hour before you want to listen.
3. Paste the contents of `task-prompt.md` as the task's instruction.
4. Change the genre list and content rules to your taste.
5. Run it once by hand and listen before leaving it on.

## Use the narrator on its own

```bash
bash setup.sh
python3 narrate.py story.txt story.mp3            # British male voice (default)
python3 narrate.py story.txt story.mp3 af_heart   # American female voice
```

Requirements: Python 3.10 or newer, `ffmpeg`, about 150 MB of disk for the model. Rendering runs on a CPU and takes roughly one and a half times the audio length.

Text tips for good narration: separate paragraphs with a blank line, put the title alone as the first paragraph, spell out years and numbers, and avoid symbols and abbreviations.

## Limits

- The agent does not remember earlier nights. Variety comes from the weekday rotation and the daily news seed, so an occasional echo of an older story is possible.
- The narrator has one voice and no sound design.
- The stories are fiction. They are not predictions.

## Credits

Narration uses the Kokoro voice model through the `kokoro-onnx` package. Check their licenses before reusing audio commercially.
