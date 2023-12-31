# Random Username Generator

This simple Python script generates random usernames using a list of English words. You can customize the maximum length of usernames, the number of usernames to generate, and whether to include same initials.

I made this because I wasn't satisfied with using keepassxc's feature of passphrase generation to make up some usernames I could use, mainly because they don't have what I needed : same first initials, also the wordlist was fairly small and I couldn't control the word lengths, which are the features I took care in this small tool.

## Features

- Generates random usernames using English words.
- Customize maximum username length.
- Option to include usernames with same initials.

## Getting Started

To generate random usernames using the Random Username Generator, follow these steps:

### Prerequisites

- Python 3 : Make sure you have Python installed on your system.

### Usage

1. Clone the repository:

```bash
git clone https://github.com/yourusername/random-username-generator.git
cd random-username-generator
```
2. Open the generate_usernames.py script in your favorite Python editor.

3. Customize the script's parameters or keep the default options :

    `max_len`: Maximum length of the usernames.
    
    `name_count`: Number of usernames to generate.
    
    `initials`: Set to True if you want the first letters of each word to match.

Run the script:
```bash
python generate_usernames.py
```
4. View the generated usernames in the terminal.