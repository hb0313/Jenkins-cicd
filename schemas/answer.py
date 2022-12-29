import pydantic


class AnswerOut(pydantic.BaseModel):
    content: str
    sampleRate: str
    encoding: str
    languageCode: str
