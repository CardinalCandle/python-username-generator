import pandas as pd
import random

def generate_usernames(max_len=7, name_count=10, initials=False):
    wordlist_path = "./english.txt"
    reader = pd.read_csv(wordlist_path, delimiter='\t', index_col=None, names=["Name"])
    filtered_df = reader.loc[reader['Name'].str.len() < max_len]
    filtered_df = filtered_df.loc[filtered_df['Name'].str.fullmatch("\w*")]
    # Extracting the wordlist
    words = filtered_df['Name'].tolist()
    
    for i in range(name_count):
        for i in range(4):
            random.seed()
            first_word = random.choice(words).capitalize()
            if initials == False:
                random.seed()
                second_word = random.choice(words).capitalize()
            else:
                temp = filtered_df[filtered_df['Name'].str.lower().str.startswith(first_word[0].lower())]
                second_words = temp['Name'].tolist()
                second_word = random.choice(second_words).capitalize()
            print(first_word + second_word, end="   \t")
        print(" ", end="\n")
    return(first_word + second_word)

generate_usernames(initials=True)