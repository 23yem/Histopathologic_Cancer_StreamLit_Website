from PIL import Image
import io
import os

import tensorflow as tf
from tensorflow.keras.models import load_model

from data_preprocessing import data_preprocessing


model = tf.keras.models.load_model(os.path.join("Histopathologic_Cancer_StreamLit_Website", "model2_saved.h5"))

preprocessed_img = data_preprocessing()

print(preprocessed_img)