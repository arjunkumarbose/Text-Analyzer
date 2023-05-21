import json

def analyze_text(text):
    # Count number of characters
    length = len(text)

    # Count number of words
    words = text.split()
    num_words = len(words)

    # Count number of vowels and consonants
    vowels = 'aeiouAEIOU'
    num_vowels = len([char for char in text if char in vowels])
    num_consonants = length - num_vowels

    # Build dictionary with analysis results
    analysis = {
        'content': text,
        'word': num_words,
        'length': length,
        'vowel': num_vowels,
        'consonant': num_consonants
    }
    return analysis

def load_text_file(filename):
    with open(filename, 'r') as file:
        text = file.read()
        analysis = analyze_text(text)
        return analysis

def save_to_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    analysis = load_text_file('example.txt')
    save_to_json(analysis, 'analysis.json')
    print(json.dumps(analysis, indent=4))

if __name__ == '__main__':
    main()
