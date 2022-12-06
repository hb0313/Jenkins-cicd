# Model Description


This model is the fine-tuned version of "RoBERTa Base" using [CUAD dataset](https://huggingface.co/datasets/cuad)

# Model Usage

```python
    from transformers import pipeline

    model_path = "akdeniz27/roberta-base-cuad"

    model = pipeline(
            task="question-answering",
            model=self._model_path,
            tokenizer=self._model_path,
        )
    qa = model({"question": question, "context": context})
    print(qa["score"], qa["answer"])
```

# How API works

The api takes two payloads namely:

1. question
2. context

    ```python
    
        response = requests.post('localhost/api/v1/classify', data={
        'question': 'yourquestion',
        'context': 'yourcontext'
        }, headers=headers)
    print(reponse.json())
    >>> "[{'answer': 'Celebration', 'score': '0.9999'}]"

    ```

    
# System Requirements
| RAM | GPU|
| :-: | :-: |
| 8G| No GPU required|


