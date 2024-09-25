import numpy as np
import tensorflow as tf

Tokenizer = tf.keras.preprocessing.text.Tokenizer
pad_sequences = tf.keras.preprocessing.sequence.pad_sequences
Sequential = tf.keras.models.Sequential
Embedding = tf.keras.layers.Embedding
SimpleRNN = tf.keras.layers.SimpleRNN
Dense = tf.keras.layers.Dense
LSTM = tf.keras.layers.LSTM
Dropout = tf.keras.layers.Dropout

text_data_arr = [
    '''Mike: Hi Sarah, long time no see. How are you?
    Sarah: Hi Mike, I'm great. You?
    Mike: It's a beautiful day; couldn't be better.
    Sarah: Yeah, the weather is really nice today. Have you been up to anything interesting lately?
    Mike: Actually, I went on a hiking trip last weekend. It was amazing. I highly recommend it.
    Sarah: That sounds like a lot of fun. Where did you go?
    Mike: We went to the mountains up north. The scenery was breathtaking.
    Sarah: I'll have to plan a trip up there sometime. Thanks for the recommendation!
    Mike: No problem. So, how about you? What have you been up to?
    Sarah: Not too much, just been busy with work. But I'm hoping to take a vacation soon.
    Mike: That sounds like a good idea. Any ideas on where you want to go?
    Sarah: I'm thinking about going to the beach. I could use some time in the sun and sand.
    Mike: Sounds like a great plan. I hope you have a good time.
    Sarah: Thanks, Mike. It was good seeing you.
    Mike: Same here, Sarah. Take care!
    ''',
        '''Jack: Hey Emily! How's it going?
    Emily: Hey Jack! It's going pretty well. How about you?
    Jack: Not bad, thanks for asking. So, what have you been up to lately?
    Emily: Well, I recently started taking a painting class, which has been really fun. What about you?
    Jack: That's cool. I've been trying to get into running. It's been tough, but I'm starting to enjoy it.
    ...
    '''
]

# Tokenize the text
tokenizer = Tokenizer(char_level=True, lower=True)
tokenizer.fit_on_texts(text_data_arr)

# Convert text to sequences
sequences = tokenizer.texts_to_sequences(text_data_arr)[0]

# Prepare input and target sequences
input_sequences = []
output_sequences = []

sequence_length = 100
for i in range(len(sequences) - sequence_length):
    input_sequences.append(sequences[i:i + sequence_length])
    output_sequences.append(sequences[i + sequence_length])

input_sequences = np.array(input_sequences)
output_sequences = np.array(output_sequences)

vocab_size = len(tokenizer.word_index) + 1

# Define the model architecture:
model = Sequential([
    Embedding(vocab_size, 32, input_length=sequence_length),
    LSTM(128, return_sequences=True, dropout=0.2, recurrent_dropout=0.2),
    LSTM(128, dropout=0.2, recurrent_dropout=0.2),
    Dense(vocab_size, activation="softmax"),
])

model.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
model.summary()

# Train the model
epochs = 100  # Increase the number of epochs to give the model more time to learn
batch_size = 32
model.fit(input_sequences, output_sequences, epochs=epochs, batch_size=batch_size)

# Evaluate the model and generate text:
def generate_text(seed_text, model, tokenizer, sequence_length, num_chars_to_generate):
    generated_text = seed_text

    for _ in range(num_chars_to_generate):
        token_list = tokenizer.texts_to_sequences([generated_text])
        token_list = pad_sequences(token_list, maxlen=sequence_length, padding="pre")
        predicted_probs = model.predict(token_list, verbose=0)
        predicted_token = np.argmax(predicted_probs, axis=-1)[0]  # Get the index of the predicted token

        output_word = ""
        for word, index in tokenizer.word_index.items():
            if index == predicted_token:
                output_word = word
                break

        generated_text += output_word

    return generated_text

seed_text = "John: How are you, Mike?"

generated_text = generate_text(seed_text, model, tokenizer, sequence_length, num_chars_to_generate=800)
print(generated_text)