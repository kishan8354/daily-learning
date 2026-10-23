import os
import pandas as pd
import spacy
import torch
from pandas.tseries import frequencies
from torch.nn.utils.rnn import pad_sequence
from torch.utils.data import DataLoader,Dataset
from PIL import Image
import torchvision.transforms as transforms
import spacy
from customDataset import  CatsAndDogsDataset
# spacy_eng = spacy.load("en_core_web_sm")
# class Vocabulary:
#     def __init__(self,freq_threshold):
#         self.itos={0:"<PAD>",1:"<SOS>",2:"<EOS>",3:"<UNK>"}
#         self.stoi = {"<PAD>":0, "<SOS>":1,  "<EOS>":2,"<UNK>":3}
#         self.freq_threshold=freq_threshold
#     def __len__(self):
#         return len(self.itos)
#     @staticmethod
#     def tokenizer_eng(text):
#         return [tok.text.lower() for tok in spacy_eng.tokenizer(text)]
#     def build_vocab(self,sentence_list):
#         frequencies={}
#         idx=4
#         for sentence in sentence_list:
#             for word in self.tokenizer_eng(sentence):
#                 if word not in frequencies:
#                     frequencies[word]=1
#                 else:
#                     frequencies[word]+=1
#                 if frequencies[word]==self.freq_threshold:
#                     self.stoi[word]=idx
#                     self.itos[idx]=word
#                     idx+=1
#     def numericalize(self,text):
#         tokenized_text=self.tokenizer_eng(text)
#         return[
#             self.stoi[token] if token in self.stoi else self.stoi["<UNK>"]
#             for token in tokenized_text
#         ]
# class FlickrDataset(Dataset):
#     def __init__(self,root_dir,captions_file,transform=None,freq_threshold=5):
#         super().__init__()
#         self.root_dir=root_dir
#         self.df=pd.read_csv(captions_file)
#         self.transform=transform
#         self.imgs=self.df["image"]
#         self.captions_file=self.df["caption"]
#         self.vocab=Vocabulary(freq_threshold)
#         self.vocab.build_vocab(self.captions_file)
#     #     pytorch expect map style dataset which provided by these two function __len__() and __getitem__() which inherits from parent class Dataset
#     def __len__(self):
#         return len(self.df)
#     def __getitem__(self,index):
#         caption=self.captions_file[index]
#         img_id=self.imgs[index]
#         img=Image.open(os.path.join(self.root_dir,img_id)).convert("RGB")
#         if self.transform is not None:
#             img=self.transform(img)
#         numericalized_caption=[self.vocab.stoi["<SOS>"]]
#         numericalized_caption+=self.vocab.numericalize(caption)
#         numericalized_caption.append(self.vocab.stoi["<EOS>"])
#         return img,torch.tensor(numericalized_caption)
# class MyCollate:
#     def __init__(self,pad_idx):
#         self.pad_idx=pad_idx
#     def __call__(self,batch):
#         imgs=[item[0].unsqueeze(0) for item in batch]
#         imgs=torch.cat(imgs,dim=0)
#         targets=[item[1] for item in batch]
#         targets=pad_sequence(targets,batch_first=False,padding_value=self.pad_idx)
#         return imgs,targets
# def get_loader(
#                    root_folder,annotation_file,transform,batch_size=32,num_workers=8,shuffle=True,pin_memory=False,):
#         dataset=FlickrDataset(root_folder,annotation_file,transform=transform)
#         pad_idx=dataset.vocab.stoi["<PAD>"]
#         loader=DataLoader(dataset=dataset,batch_size=batch_size,shuffle=shuffle,num_workers=num_workers,pin_memory=pin_memory,collate_fn=MyCollate(pad_idx=pad_idx))
#         return loader
# def main():
#     transform=transforms.Compose(
#         [
#             transforms.Resize((224,224)),
#             transforms.ToTensor(),
#         ]
#     )
#     dataloader = get_loader(root_folder="dataset/flicker8k/Images",annotation_file="dataset/flicker8k/captions.txt",transform=transform)
#     for idx,(imgs,caption) in enumerate(dataloader):
#         print(imgs.shape)
#         print(caption.shape)
# if __name__=="__main__":
#     main()
# lecture dataaugmentation
from torchvision.utils import save_image
from customDataset import CatsAndDogsDataset
my_transforms=transforms.Compose([
    transforms.ToPILImage(),
    transforms.RandomHorizontalFlip(p=0.5),
    transforms.ToTensor(),
])
dataset=CatsAndDogsDataset(csv_file='cats_dogs_train.csv',root_dir="dataset/catsAndDogs/PetImages/Cat",transform=my_transforms)
