# this script should be run from the root folder of this whole repository so that we here make references to modules from the perspective of this repository's root

import torchaudio

import os

# #print out sys.path to see the paths python uses to search for modules when importing.
# import sys
# print(sys.path)


from tortoise.api import TextToSpeech
from tortoise.utils.audio import load_audio, load_voice, load_voices


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
    voice_samples, conditioning_latents = load_voice(voice_name, extra_voice_dirs)
    gen = tts.tts_with_preset(txt_2b_voiced, voice_samples=voice_samples, conditioning_latents=conditioning_latents,
                              preset=preset_mode)
    torchaudio.save(o_audio_flnm, gen.squeeze(0).cpu(), 24000)


# Main Action ----------------------------------------------------------------------------------------------------------

txt_2b_voiced = "Joining two modalities results in a surprising increase in generalization! What would happen if we combined them all?"
# get my custome voices dir
MY_EXTRA_VOICES_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'voices')
extra_voice_dirs=[MY_EXTRA_VOICES_DIR]


vocalize_txt(init_tts(), txt_2b_voiced, "venti", "fast", os.path.join(os.environ['USERPROFILE'],f"downloads/venti_ai.wav"), extra_voice_dirs)
