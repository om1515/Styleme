from PIL import Image
import requests

url = 'https://media.istockphoto.com/id/697913308/photo/orange-men-shorts-for-swimming.jpg?s=612x612&w=0&k=20&c=Ta47ejxSIVtknPGGZ92BB_KGI9bLLZuU_C0EaOXl0AA='
image = Image.open(requests.get(url, stream=True).raw)



from transformers import AutoModelForImageClassification, AutoImageProcessor

repo_name = "samokosik/finetuned-clothes"

image_processor = AutoImageProcessor.from_pretrained(repo_name)
model = AutoModelForImageClassification.from_pretrained(repo_name)


encoding = image_processor(image.convert("RGB"), return_tensors="pt")
print(encoding.pixel_values.shape)


import torch
with torch.no_grad():
  outputs = model(**encoding)
  logits = outputs.logits



predicted_class_idx = logits.argmax(-1).item()
print("Predicted class:", model.config.id2label[predicted_class_idx])
