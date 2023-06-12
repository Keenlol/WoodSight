from fastai.vision.all import *
import gradio as gr
import skimage
import pathlib
import os

plt = platform.system()
if plt == 'Linux': pathlib.WindowsPath = pathlib.PosixPath

learn = load_learner('WoodClassification_FastAI_4_1.pkl')
examples = [str(x) for x in get_image_files('images')]

labels = learn.dls.vocab
def predict(img):
    img = PILImage.create(img)
    pred,pred_idx,probs = learn.predict(img)
    val, idx = probs.topk(3)
    pred_labels = labels[idx]
    return {labels[i]: float(probs[i]) for i in range(len(labels))}

examples_list = [['examples/' + image] for image in os.listdir('examples/')]
examples_list

title = "Wood Texture Classification"
description = "<p style='text-align: center; font-size:16px'>Image classification Model trained with images from google"
enable_queue=True
inputs = gr.Image(shape=(224, 224))

gr.Interface(fn=predict,
    inputs=inputs,
    outputs=gr.Label(num_top_classes=3),
    title=title,
    description=description,
    examples=examples_list).launch(inline=False, enable_queue=enable_queue)
