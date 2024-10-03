import numpy as np
import tensorflow as tf
from data import text_data_arr

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential

# Tokenize the text
tokenizer = Tokenizer(char_level=True)
tokenizer.fit_on_texts(text_data_arr)
vocab_size = len(tokenizer.word_index) + 1

# Prepare input and target sequences
input_sequences = []
for line in text_data_arr:
    sequences = tokenizer.texts_to_sequences([line])[0]
    for i in range(1, len(sequences)):
        input_sequences.append(sequences[:i + 1])

max_sequence_length = max([len(x) for x in input_sequences])
input_sequences = pad_sequences(input_sequences, maxlen=max_sequence_length, padding='pre')

# Define the model architecture:
model = Sequential([
    Embedding(vocab_size, 32),
    LSTM(128, return_sequences=True, dropout=0.2, recurrent_dropout=0.2),
    LSTM(128, dropout=0.2, recurrent_dropout=0.2),
    Dense(vocab_size, activation="softmax"),
])

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
model.summary()

x, y = input_sequences[:, :-1], input_sequences[:, -1]
y = tf.keras.utils.to_categorical(y, num_classes=vocab_size)

# Train the model
epochs = 150  # Increase the number of epochs to give the model more time to learn
batch_size = 32
model.fit(x, y, epochs=epochs, batch_size=batch_size)

model.save('custom_llm_model.keras')
