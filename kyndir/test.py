# this script should be run from the root folder of this whole repository so that we here make references to modules from the perspective of this repository's root

import torchaudio

#print out sys.path to see the paths python uses to search for modules when importing.
import sys
print(sys.path)


from tortoise.api import TextToSpeech
from tortoise.utils.audio import load_audio, load_voice, load_voices


# This will download all the models used by Tortoise from the HuggingFace hub.
tts = TextToSpeech()


# Load it and send it through Tortoise.
def vocalize_txt(txt_2b_voiced, voice_name, preset_mode, o_audio_flnm):
    """_summary_

    Args:
        txt_2b_voiced (_type_): _description_
        voice_name (_type_): choose a voice name, i.e. a subfolder name in the tortoise/voices
        preset_mode (_type_): Pick a "preset mode" to determine quality. Options: {"ultra_fast", "fast" (default), "standard", "high_quality"}. See docs in api.py
        o_audio_flnm (_type_): the output audio's name with extension
    """
    voice_samples, conditioning_latents = load_voice(voice_name)
    gen = tts.tts_with_preset(txt_2b_voiced, voice_samples=voice_samples, conditioning_latents=conditioning_latents,
                              preset=preset_mode)
    torchaudio.save(o_audio_flnm, gen.squeeze(0).cpu(), 24000)


# This is the text that will be spoken.
txt_2b_voiced = "Joining two modalities results in a surprising increase in generalization! What would happen if we combined them all?"
# Pick a "preset mode" to determine quality. Options: {"ultra_fast", "fast" (default), "standard", "high_quality"}. See docs in api.py
preset_mode = "fast"
# choose a voice name, i.e. a subfolder name in the tortoise/voices
voice_name = "tom"
vocalize_txt(txt_2b_voiced, voice_name, preset_mode, "venti_test.wav")
