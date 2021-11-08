import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
#from main import * # import the main python file with model from the example
#from main import inference
import time
import tensorflow as tf
import tensorlayer as tl
import numpy as np
from tensorlayer.cost import cross_entropy_seq, cross_entropy_seq_with_mask
from tqdm import tqdm
from sklearn.utils import shuffle
#from data.twitter import data
from chat.data.twitter import data
from tensorlayer.models.seq2seq import Seq2seq
from tensorlayer.models.seq2seq_with_attention import Seq2seqLuongAttention
import os

def initial_setup(data_corpus):
    metadata, idx_q, idx_a = data.load_data(PATH='chat/data/{}/'.format(data_corpus))
    (trainX, trainY), (testX, testY), (validX, validY) = data.split_dataset(idx_q, idx_a)
    trainX = tl.prepro.remove_pad_sequences(trainX.tolist())
    trainY = tl.prepro.remove_pad_sequences(trainY.tolist())
    testX = tl.prepro.remove_pad_sequences(testX.tolist())
    testY = tl.prepro.remove_pad_sequences(testY.tolist())
    validX = tl.prepro.remove_pad_sequences(validX.tolist())
    validY = tl.prepro.remove_pad_sequences(validY.tolist())
    return metadata, trainX, trainY, testX, testY, validX, validY




data_corpus = "twitter"

#data preprocessing
metadata, trainX, trainY, testX, testY, validX, validY = initial_setup(data_corpus)

# Parameters
src_len = len(trainX)
tgt_len = len(trainY)

assert src_len == tgt_len

batch_size = 32
n_step = src_len // batch_size
src_vocab_size = len(metadata['idx2w']) # 8002 (0~8001)
emb_dim = 1024

word2idx = metadata['w2idx']   # dict  word 2 index
idx2word = metadata['idx2w']   # list index 2 word

unk_id = word2idx['unk']   # 1
pad_id = word2idx['_']     # 0

start_id = src_vocab_size  # 8002
end_id = src_vocab_size + 1  # 8003

word2idx.update({'start_id': start_id})
word2idx.update({'end_id': end_id})
idx2word = idx2word + ['start_id', 'end_id']

src_vocab_size = tgt_vocab_size = src_vocab_size + 2

num_epochs = 50
vocabulary_size = src_vocab_size




def inference(seed, top_n):
    model_.eval()
    seed_id = [word2idx.get(w, unk_id) for w in seed.split(" ")]
    sentence_id = model_(inputs=[[seed_id]], seq_length=20, start_token=start_id, top_n = top_n)
    sentence = []
    for w_id in sentence_id[0]:
        w = idx2word[w_id]
        if w == 'end_id':
            break
        sentence = sentence + [w]
    return sentence

decoder_seq_length = 20
model_ = Seq2seq(
    decoder_seq_length = decoder_seq_length,
    cell_enc=tf.keras.layers.GRUCell,
    cell_dec=tf.keras.layers.GRUCell,
    n_layer=3,
    n_units=256,
    embedding_layer=tl.layers.Embedding(vocabulary_size=vocabulary_size, embedding_size=emb_dim),
    )





load_weights = tl.files.load_npz(name='chat/model.npz')
tl.files.assign_weights(load_weights, model_)



def respond(input):
    sentence = inference(input, 3)
    #print(sentence)
    response=' '.join(sentence)

    return response

from googletrans import Translator
tr = Translator()

def jpn2en(text):
    return tr.translate(text=text, src="ja", dest="en").text

def en2jpn(text):
    return tr.translate(text=text, src="en", dest="ja").text

'''
while True:
    userInput=input("user# ")
    userInput=jpn2en(userInput)
    #print(userInput)
    time.sleep(0.5)
    res=respond(userInput)
    print("bot# ",en2jpn(res))
    #print('r:',res)
'''