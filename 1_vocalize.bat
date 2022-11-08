@echo off

echo This script vocalizes input texts with a chosen voice
echo.

@REM activate env
echo Activating env tts...
call conda activate tts
echo.

set txt="One ring to rule them all. One ring to find them. One ring to bring them all, and in the darkness bind them."
set /p txt="Set input text (.txt flpth or plain txt, default is the Ring Verse): "
echo txt is set as %txt%
echo.

set extra_voices_dir=""
set /p extra_voices_dir="Set the folder path to your custom voices (default is empty): "
echo extra_voices_dir is set as %extra_voices_dir%
echo.

set voice="rainbow"
set /p voice="Set the voice to clone (default is the built-in voice named 'rainbow'): "
echo voice is set as %voice%
echo.

set preset="fast"
set /p preset="Set the preset mode for generation (Can be ultra_fast, fast(default), standard, high_quality): "
echo preset is set as %preset%
echo.

set oDir="%USERPROFILE%/downloads/tts_results"
set /p oDir="Set the output folder (default is the windows' downloads folder): "
echo oDir is set as %oDir%
echo.

python -m kyndir.vocalize --txt %txt% --voice %voice% --extra_voices_dir %extra_voices_dir% --preset %preset% --oDir %oDir%

echo.
echo All Finished!
@REM deactivate env
echo Deactivating env tts...
call conda deactivate
PAUSE