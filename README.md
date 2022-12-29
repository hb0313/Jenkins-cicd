## Model Description

This model is based on the QuartzNet architecture [1]. The pre-trained models here can be used immediately for fine-tuning or dataset evaluation.

It utilizes a character encoding scheme, and transcribes text in the standard character set that is provided in the French portion of Common Voice from Mozilla (MCV) [2].
## Model Architecture

The Quartznet model is composed of multiple blocks with residual connections between them, trained with CTC loss. Each block consists of one or more modules with 1D time-channel separable convolutional layers, batch normalization, and ReLU layers.

The Quartznet 15x5 model consists of 79 layers and has a total of 18.9 million parameters, with five blocks that repeat fifteen times plus four additional convolutional layers [1].

## Performance

The performance of Automatic Speech Recognition models is measuring using Word Error Rate.

The model obtains the following scores on the following evaluation datasets -

14 % on the dev set from French MCV dataset.
Note that these scores on this evaluation sets are not particularly indicative of the quality of transcriptions that models trained on ASR Set will achieve, but they are a useful proxy.

## Input

This model accepts 16000 KHz Mono-channel Audio (wav files) as input.

## Output

This model provides transcribed speech as a string for a given audio sample.

## Machine specification

CPU 8GB, GPU optional

## How to use

Click try it out under 'POST' method. This will enable an option to upload image.

Upload the image. Next, click execute to produce the output.

The response will be a JSON.


   JSON Formate:

    {
        "content": base64 audio encoded string,
        "sampleRate": 22050 ,
        "encoding": "WAV",
        "languageCode": "English",
    }


Decoder for audio file genrator:

```
import base64

wav_file = open("temp.wav", "wb")
decode_string = base64.b64decode(audio_encoded_json_content)
wav_file.write(decode_string)
```