import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from sklearn.preprocessing import LabelEncoder

from classifier_data import class_data_arr

texts = []
labels = []
for entry in class_data_arr:
    texts.append(entry[0])
    labels.append(entry[1])

# Preprocess the text data using a Tokenizer
max_words = 100
num_classes = 3
tokenizer = Tokenizer(num_words=max_words)
tokenizer.fit_on_texts(texts)
label_encoder =  LabelEncoder()

sequences = tokenizer.texts_to_sequences(texts)

data = pad_sequences(sequences, maxlen=max_words, padding='pre')
labels = label_encoder.fit_transform(labels)
labels = to_categorical(labels, num_classes=num_classes)

data = np.asarray(data)
labels = np.asarray(labels)

# Build the model
model = Sequential([
    Embedding(max_words, 128, input_length=max_words),
    LSTM(128, return_sequences=True, dropout=0.2, recurrent_dropout=0.2),
    LSTM(128, dropout=0.2, recurrent_dropout=0.2),
    Dense(num_classes, activation="softmax"),
])

# Compile and train the model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(data, labels, validation_split=0.5, epochs=100)

# Predict the class of a new text
new_text = ['positive']
new_sequences = tokenizer.texts_to_sequences(new_text)
new_data = pad_sequences(new_sequences, maxlen=max_words)
prediction = model.predict(new_data)
print(prediction) 

model.save('text_classifier_model.keras')
