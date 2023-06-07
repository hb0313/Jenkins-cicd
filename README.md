# Model description

The Vision Transformer (ViT) is a transformer encoder model (BERT-like) pretrained on a large collection of images in a supervised fashion, namely ImageNet-21k, at a resolution of 224x224 pixels. Next, the model was fine-tuned on ImageNet (also referred to as ILSVRC2012), a dataset comprising 1 million images and 1,000 classes, also at resolution 224x224.


## Machine specifications

CPU 4GB, Optional

## How to use

Click try it out under 'POST' method. This will enable an option to upload image.

Upload any image in png or jpg formate, model uses multipart/form-data to process image. Next, click execute to produce the output.

The response will be a JSON with image classification label.

### Example

When a dog image is passed to model, below response is generated

```JSON
[
  {
    "label": "German shepherd, German shepherd dog, German police dog, alsatian",
    "model": "Vissl - RegnetY-40"
  }
]
```
