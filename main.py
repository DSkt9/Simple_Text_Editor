from collections import Counter
import glob
import re

# Function to read and store the file
def read_file():
    path = 'Data/TextFile01.txt'
    all_files = glob.glob(path + "TextFile01.txt")
    text = []
    with open('TextFile01.txt', 'r', encoding='ISO-8859-1') as f:
        text.append(f.read())
    return text


# Function to save the updated text to a new file
def saveTextFile(text):
    with open('TextFile02.txt', 'w', encoding='ISO-8859-1') as f:
        f.writelines(text)
    print("Changes saved to TextFile02.txt")


# Function to display the menu
def display_menu():
    print("\nMenu:")
    print("1. All Word Count")
    print("2. Single Word Count")
    print("3. Replace a Word")
    print("4. Add Text")
    print("5. Delete Text")
    print("6. HighLight")
    print("7. Reverse Text")
    choice = input("Choose an option: ")
    return choice


# Function for the all word count menu item
def AllWordCount(text):
    word_counts = Counter(" ".join(text).split())
    print(word_counts.most_common(5))


# Function for the single word count menu item with word boundaries
def SingleWordCount(text):
    word_to_check = input("Enter a word to check its count: ").strip().lower()
    # Checking if input is > one word
    if len(word_to_check.split()) > 1:
        print("Error: Please enter only one word.")
        return
    pattern = r'\b' + re.escape(word_to_check) + r'\b'  # Word boundary
    word_counts = Counter(" ".join(text).split())
    count = len(re.findall(pattern, " ".join(text).lower()))  # Count exact word matches
    print(f"The word '{word_to_check}' appears {count} time(s) in the text.")


# Function for replacing a word with word boundaries
def ReplaceWord(text):
    word_to_replace = input("Enter a word to replace: ").strip().lower()
    replacement_word = input("Enter a replacement word: ").strip().lower()
    pattern = r'\b' + re.escape(word_to_replace) + r'\b'  # Word boundary

    updated_text = []
    for line in text:
        updated_line = re.sub(pattern, replacement_word, line, flags=re.IGNORECASE)
        updated_text.append(updated_line)

    print(f"The word '{word_to_replace}' was replaced with '{replacement_word}'.\n")
    for line in updated_text:
        print(line)

    return updated_text


# Function for adding new text at the end of the current text
def AddText(text):
    additional_text = input("Enter text to add: ")
    text.append(additional_text)
    print("\nUpdated text:")
    for line in text:
        print(line)
    return text


# Function for deleting the first instance of a text (with whole word matching)
def DeleteText(text):
    deleted_text = input("Enter text to delete: ").strip().lower()
    pattern = r'\b' + re.escape(deleted_text) + r'\b'  # Word boundary

    updated_text = []
    deleted = False
    for line in text:
        if not deleted:
            line = re.sub(pattern, '', line, flags=re.IGNORECASE, count=1)  # Delete the first match
            deleted = True
        updated_text.append(line)

    print(f"The first instance of the word '{deleted_text}' has been deleted.\n")
    for line in updated_text:
        print(line)

    return updated_text


# Function for highlighting all occurrences of a word
def HighLight(text):
    highlighted_word = input("Enter a word to highlight: ").strip().lower()
    if len(highlighted_word.split()) > 1:
        print("Error: Please enter only one word.")
        return
    pattern = r'\b' + re.escape(highlighted_word) + r'\b'  # Word boundary

    updated_text = []
    for line in text:
        highlighted_line = re.sub(pattern, f"**{highlighted_word}**", line, flags=re.IGNORECASE)
        updated_text.append(highlighted_line)

    print("\nUpdated text with highlighted word:")
    for line in updated_text:
        print(line)

    return updated_text


# Function to reverse all text
def ReverseText(text):
    reversed_text = [line[::-1] for line in text]
    print("\nReversed text:")
    for line in reversed_text:
        print(line)


# Main function to open the file, display the menu, and handle user input
def main():
    # Read the file when the program starts
    text = read_file()
    print("File content loaded successfully!")

    # Menu loop
    while True:
        choice = display_menu()

        if choice == "1":
            AllWordCount(text)
        elif choice == "2":
            SingleWordCount(text)
        elif choice == "3":
            ReplaceWord(text)
        elif choice == "4":
            AddText(text)
        elif choice == "5":
            DeleteText(text)
        elif choice == "6":
            HighLight(text)
        elif choice == "7":
            ReverseText(text)
        else:
            print("Invalid choice. Please try again.")

        # Ask user if they want to continue or save
        continue_choice = input("\nWould you like to perform another action? (y/n): ").strip().lower()
        if continue_choice != 'y':
            save_choice = input("Do you want to save the changes? (y/n): ").strip().lower()
            if save_choice == 'y':
                saveTextFile(text)
            break


# Run the program
if __name__ == "__main__":
    main()
