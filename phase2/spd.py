import random
import time

# List of sample sentences for typing practice
sample_sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "This is a sample sentence for typing practice.",
    "The only way to do great work is to love what you do.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "In the middle of every difficulty lies opportunity."
]

def get_random_sentence():
    # Choose a random sentence from the list
    return random.choice(sample_sentences)

def calculate_wpm(start_time, end_time, typed_text):
    # Calculate the time taken in seconds
    elapsed_time = end_time - start_time
    
    # Calculate the number of words typed
    typed_words = len(typed_text.split())
    
    # Calculate words per minute (WPM)
    wpm = (typed_words / elapsed_time) * 60
    
    return wpm

def main():
    print("Typing Speed Tester")

    # Get a random sentence for typing practice
    random_sentence = get_random_sentence()

    print("Type the following sentence:")
    print(random_sentence)
    input("Press Enter when you're ready to start typing...")

    start_time = time.time()
    
    typed_text = input("Start typing here: ")
    
    end_time = time.time()
    
    wpm = calculate_wpm(start_time, end_time, typed_text)

    print(f"Your typing speed: {wpm:.2f} WPM")

if __name__ == "__main__":
    main()

