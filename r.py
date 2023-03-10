from transformers import pipeline
class Model:
    def a(self):
        sentiment_model = pipeline(model="federicopascual/finetuning-sentiment-model-3000-samples")
        return sentiment_model

m_obj = Model()
model = m_obj.a()
list_of_dict = model(["I love  this move", "This movie sucks!"])
print(list_of_dict)