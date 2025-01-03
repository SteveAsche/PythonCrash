"""Testing the file not found exception """

filename = 'alice.txt'
def count_words(filename, wordsearch):
    try:
        with open(filename, encoding='utf-8') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "sorry, the file "+ filename + " does not exist."
        print(msg)
    else:
        # Count the words in the file
        words = contents.split()
        num_words = len(words)
        print("The file contains "+ str(num_words) + " words.")
        wordcount = 0
        for word in words:
            if word.lower() == wordsearch:
                wordcount += 1
        print("There are " + str(wordcount) + " instances of the word " + wordsearch +" mentioned.")
        # print("There are " + str(dog_counter) + " rabbits mentioned.")

filename = 'alice.txt'
searchfor = input("What word would you like me to find? ")
count_words(filename, searchfor)