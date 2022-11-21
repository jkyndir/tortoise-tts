# this script should be run from the root folder of this whole repository so that we here make references to modules from the perspective of this repository's root
import torchaudio
import argparse
import os
from datetime import datetime
# #print out sys.path to see the paths python uses to search for modules when importing.
# import sys
# print(sys.path)
from tortoise.api import TextToSpeech
from tortoise.utils.audio import load_audio, load_voice, load_voices


# utils
def txtFl_2_str(txtFlPth):
    with open(txtFlPth, "r") as f:
        read_str = f.read()
        return read_str


def get_timestamp():
    timestamp = datetime.now().timestamp()
    date_time = datetime.fromtimestamp(timestamp)
    stimestamp_str = date_time.strftime("%d-%m-%Y-%H-%M-%S")
    return stimestamp_str


# Main Functions -------------------------------------------------------------------------------------
# get a tts instance
def init_tts():
    # This will download all the models used by Tortoise from the HuggingFace hub.
    tts = TextToSpeech()
    return tts


# Load it and send it through Tortoise.
def vocalize_txt(tts, txt_2b_voiced, voice_name, preset_mode, o_audio_flnm, extra_voice_dirs=[]):
    """_summary_

    Args:
        tts: tts instance
        txt_2b_voiced (_type_): This is the text that will be spoken.
        voice_name (_type_): choose a voice name, i.e. a subfolder name in the tortoise/voices
        preset_mode (_type_): Pick a "preset mode" to determine quality. Options: {"ultra_fast", "fast" (default), "standard", "high_quality"}. See docs in api.py
        o_audio_flnm (_type_): the output audio's name with extension
    """
    voice_samples, conditioning_latents = load_voice(
        voice_name, extra_voice_dirs)
    gen = tts.tts_with_preset(txt_2b_voiced, voice_samples=voice_samples, conditioning_latents=conditioning_latents,
                              preset=preset_mode)
    torchaudio.save(o_audio_flnm, gen.squeeze(0).cpu(), 24000)

    # run system cmd to launch the file.
    run_audio_cmd = f"start {o_audio_flnm}"
    os.system(run_audio_cmd)


# Main Action ----------------------------------------------------------------------------------------------------------
def main():

    default_oDir = os.path.join(
        os.environ['USERPROFILE'], f"downloads/tts_results")

    parser = argparse.ArgumentParser()
    parser.add_argument('--txt', type=str, help='Either the path to the a .txt file or the plain string to be vocalized.',
                        default="One ring to rule them all. One ring to find them. One ring to bring them all, and in the darkness bind them.")
    parser.add_argument(
        '--voice', type=str, help="Selects the voice to use for generation. Default is the built-in voice named 'rainbow'", default='rainbow')
    parser.add_argument('--extra_voices_dir', type=str,
                        help='The path to the folder where your extra voices are stored. Subfolder names are considered as voice names.', default='')
    parser.add_argument('--preset', type=str,
                        help='Which voice preset to use. Can be "ultra_fast", "fast", "standard", "high_quality"', default='fast')
    parser.add_argument('--oDir', type=str,
                        help='Where to store outputs.', default=default_oDir)
    args = parser.parse_args()

    # get the text to be voiced
    if os.path.isfile(args.txt):
        txt_2b_voiced = txtFl_2_str(args.txt)
    else:
        txt_2b_voiced = args.txt

    # get the extra voice dirs
    extra_voice_dirs = [args.extra_voices_dir]

    # init a tts
    my_tts = init_tts()

    # create the output folder if it does not exist already
    os.makedirs(args.oDir, exist_ok=True)

    print("Ready. Vocalizing initiated...")
    # vocalize
    vocalize_txt(my_tts, txt_2b_voiced, args.voice, args.preset,
                 os.path.join(args.oDir, f"{args.voice}_{get_timestamp()}.wav"), extra_voice_dirs)


if __name__ == "__main__":
    main()
