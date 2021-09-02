import pickle
import numpy as np
import textCleaner
import AttentionLayer as att
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences

# Hàm decoder
def decode_sequence(input_seq, target_word_index, reverse_target_word_index):
    encoder_model = load_model('encoder_model.h5')
    decoder_model = load_model('decoder_model.h5', custom_objects={'AttentionLayer': att.AttentionLayer})

    # endcode input
    e_out, e_h, e_c = encoder_model.predict(input_seq)
    target_seq = np.zeros((1, 1))
    target_seq[0, 0] = target_word_index['sostok']

    stop_condition = False
    decoded_sentence = ''
    while not stop_condition:
        output_tokens, h, c = decoder_model.predict([target_seq] + [e_out, e_h, e_c])

        sampled_token_index = np.argmax(output_tokens[0, -1, :])
        sampled_token = reverse_target_word_index[sampled_token_index]

        if (sampled_token != 'eostok'):
            decoded_sentence += ' ' + sampled_token

        if (sampled_token == 'eostok' or len(decoded_sentence.split()) >= 29):
            stop_condition = True

        target_seq = np.zeros((1, 1))
        target_seq[0, 0] = sampled_token_index
        e_h, e_c = h, c

    return decoded_sentence

def solve(s):
    cleaned_text = []
    cleaned_text.append(textCleaner.text_cleaner(s, 0))

    with open('tokenizer.pickle', 'rb') as handle:
        x_tokenizer = pickle.load(handle)
    with open('y_tokenizer.pickle', 'rb') as handle:
        y_tokenizer = pickle.load(handle)

    max_text_len = 30
    x = np.array(cleaned_text)
    x_seq = x_tokenizer.texts_to_sequences(x)
    x = pad_sequences(x_seq, maxlen=max_text_len, padding='post')
    reverse_target_word_index = y_tokenizer.index_word
    target_word_index = y_tokenizer.word_index

    sumText = decode_sequence(x[0].reshape(1, max_text_len), target_word_index, reverse_target_word_index)

    return sumText


# s = "I always buy chips and candy at UTC's store everyday because this store always try it best to make product. I love it very much."
# print("Review original:", s)
# print("Predicted summary:", solve(s))

