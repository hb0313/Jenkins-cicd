import tempfile

import fastapi
import gluoncv
import mxnet as mx
from gluoncv.data.transforms.presets.segmentation import test_transform
from gluoncv.utils.viz import get_color_pallete
from mxnet import image

import schemas

# using cpu
ctx = mx.cpu(0)
model = gluoncv.model_zoo.get_model("psp_resnet101_ade", pretrained=True)

router = fastapi.APIRouter()


@router.post(
    "/segment",
    responses={
        400: {"model": schemas.InvalidMediaError},
        500: {"model": schemas.MLModelNotFoundError},
    },
)
async def image_segmentation(
    file: fastapi.UploadFile = fastapi.File(...),
) -> fastapi.responses.FileResponse:
    with tempfile.NamedTemporaryFile(mode="w+b", suffix=".png", delete=False) as pic:
        content = file.file.read()
        pic.write(content)
        read_img = image.imread(pic.name)
        img = test_transform(read_img, ctx)

    output = model.predict(img)
    predict = mx.nd.squeeze(mx.nd.argmax(output, 1)).asnumpy()

    with tempfile.NamedTemporaryFile(mode="w+b", suffix=".png", delete=False) as img:
        mask = get_color_pallete(predict, "ade20k")
        mask.save(img)
        return fastapi.responses.FileResponse(img.name)
