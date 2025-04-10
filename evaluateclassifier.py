import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from classifier_data import class_data_arr

texts = []
for entry in class_data_arr:
    texts.append(entry[0])

max_words = 100
tokenizer = Tokenizer(num_words=max_words)
tokenizer.fit_on_texts(texts)
model = tf.keras.models.load_model('text_classifier_model.keras')

# Predict the class of a new text
new_text = ['neutral text']
new_sequences = tokenizer.texts_to_sequences(new_text)
new_data = pad_sequences(new_sequences, maxlen=max_words, padding='pre')
prediction = model.predict(new_data)
print(prediction) 
