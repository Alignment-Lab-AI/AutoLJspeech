# AutoAudioPipeline

AutoAudioPipeline is a comprehensive script that automates the process of transcribing, diarizing, and cleaning audio or video files. It generates speaker-aware transcripts and creates an LJ Speech-like dataset for each speaker, making it easy to work with the processed audio data.

## Features

- Supports various audio and video formats, including online URLs
- Performs vocal isolation using source separation
- Transcribes the audio using the Faster Whisper library
- Aligns the transcription with the audio using WhisperX (for supported languages)
- Performs speaker diarization using NVIDIA NeMo MSDD
- Restores punctuation in the transcript using DeepMultilingualPunctuation
- Generates an SRT file with the diarized transcript
- Creates an LJ Speech-like dataset with separate directories for each speaker

## Major Cleaning Stages

1. **Audio Conversion**: The script converts the input audio or video file to WAV format using the `pydub` library. If a URL is provided, it downloads the audio using `yt-dlp` and `ffmpeg`.

2. **Vocal Isolation** (optional): The script uses the `demucs` library to isolate the vocals from the audio, separating them from background noise and music. This stage is enabled by default but can be disabled using the `--no-stem` flag.

3. **Transcription**: The audio is transcribed using the Faster Whisper library, which provides efficient and accurate speech recognition. The script supports various Whisper models and allows for language detection or specifying a particular language.

4. **Alignment** (optional): If the detected language is supported by WhisperX, the script aligns the transcription with the audio using the wav2vec2 model. This step improves the timing accuracy of the transcribed words.

5. **Speaker Diarization**: The script performs speaker diarization using the NVIDIA NeMo MSDD (Multi-Scale Diarization Decoder) model. It identifies and labels different speakers in the audio, assigning a unique speaker label to each segment.

6. **Punctuation Restoration**: The DeepMultilingualPunctuation library is used to restore punctuation in the transcript. This step enhances the readability and coherence of the transcribed text.

7. **SRT Generation**: The script generates an SRT file with the diarized transcript, providing synchronized subtitles for the audio. Each subtitle entry includes the start and end timestamps along with the corresponding speaker label and text.

8. **LJ Speech-like Dataset Creation**: The script creates a directory structure similar to the LJ Speech dataset, with separate directories for each speaker. Each speaker directory contains the segmented audio files and a metadata file that maps the audio filenames to their respective transcripts.

## Usage

1. Install the required dependencies listed in the `requirements.txt` file:

```
pip install -r requirements.txt
```
2. Run the script with the desired options:
```
python script.py -i <input_file> [--no-stem] [--suppress_numerals] [--whisper-model <model_name>] [--batch-size <batch_size>] [--language <language>] [--device <device>]
```
- `<input_file>`: Path to the input audio or video file, or a URL.
- `--no-stem` (optional): Disables vocal isolation (enabled by default).
- `--suppress_numerals` (optional): Suppresses numerical digits in the transcription.
- `--whisper-model <model_name>` (optional): Specifies the Whisper model to use for transcription (default: "medium.en").
- `--batch-size <batch_size>` (optional): Sets the batch size for inference (default: 8).
- `--language <language>` (optional): Specifies the language spoken in the audio (default: None, auto-detection).
- `--device <device>` (optional): Specifies the device to use for computation (default: "cuda" if available, else "cpu").

3. The script will process the input file and generate the following outputs:
- An SRT file with the diarized transcript, saved as `<input_file_name>.srt`.
- An `LJ_Speech_dataset` directory containing separate directories for each speaker, along with their respective audio segments and metadata files.

## Example
```
python script.py -i audio.wav --language en --device cuda
```

This command processes the `audio.wav` file, assuming the spoken language is English, and uses CUDA for computation. The generated outputs will be saved in the same directory as the input file.

## License
This script is released under the [MIT License](https://opensource.org/licenses/MIT).

## Acknowledgements
AutoAudioPipeline utilizes the following libraries and models:
- [Faster Whisper](https://github.com/guillaumekln/faster-whisper)
- [WhisperX](https://github.com/m-bain/whisperX)
- [NVIDIA NeMo](https://github.com/NVIDIA/NeMo)
- [DeepMultilingualPunctuation](https://github.com/oliverguhr/deepmultilingualpunctuation)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [Demucs](https://github.com/facebookresearch/demucs)

We acknowledge the excellent work of the respective authors and contributors of these projects.

