import numpy as np
import tensorflow as tf
from data import text_data_arr

Tokenizer = tf.keras.preprocessing.text.Tokenizer
pad_sequences = tf.keras.preprocessing.sequence.pad_sequences

# Tokenize the text
tokenizer = Tokenizer(char_level=True, lower=True)
tokenizer.fit_on_texts(text_data_arr)
vocab_size = len(tokenizer.word_index) + 1

# Prepare input and target sequences
input_sequences = []
for line in text_data_arr:
    sequences = tokenizer.texts_to_sequences([line])[0]
    for i in range(1, len(sequences)):
        input_sequences.append(sequences[:i + 1])

max_sequence_length = max([len(x) for x in input_sequences])

model = tf.keras.models.load_model('custom_llm_model.keras')

# Evaluate the model and generate text:
def generate_text(seed_text, model, tokenizer, sequence_length, num_chars_to_generate):
    generated_text = seed_text

    for _ in range(num_chars_to_generate):
        token_list = tokenizer.texts_to_sequences([generated_text])
        token_list = pad_sequences(token_list, maxlen=max_sequence_length-1, padding="pre")
        predicted_probs = model.predict(token_list, verbose=0)
        predicted_token = np.argmax(predicted_probs, axis=-1)[0]  # Get the index of the predicted token

        output_word = ""
        for word, index in tokenizer.word_index.items():
            if index == predicted_token:
                output_word = word
                break

        generated_text += output_word

    return generated_text

seed_text = "Hello?"

generated_text = generate_text(seed_text, model, tokenizer, max_sequence_length, num_chars_to_generate=20)
print(generated_text)