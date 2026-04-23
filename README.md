How to run the program: 
Run the program from a terminal using Python (I personally use PyCharm), with the required text files: prefixes.txt and words.txt in the same directory. When the program starts, you can type any prefix to search for matching words, type 'prefixes' to display all available prefixes from prefixes.txt or type 'exit' to quit.

Required input files: 
prefixes.txt, words.txt and autocomplete.py

Algorithm implemented: 
The autocomplete system uses binary search to find the first matching word and sequential search to collect remaining matches.

Runtime complexity:
O(log n + k) -> The binary search runs in: O(log ⁡n) where n is the number of words in the dictionary. The sequential search runs in: O(k) where k is the number of words that share the prefix.
