class Dictionary:
    def __init__(self, words):
        cleaned = [w.strip() for w in words if w.strip()]
        self.words = sorted(cleaned)

    def get_words(self):
        return self.words

    def binary_search_first(self, prefix):
        low = 0
        high = len(self.words) - 1
        result = -1

        while low <= high:
            mid = (low + high) // 2
            word = self.words[mid]

            if word.startswith(prefix):
                result = mid
                high = mid - 1
            elif word < prefix:
                low = mid + 1
            else:
                high = mid - 1

        return result

    def prefix_matches(self, prefix):
        matches = []
        start = self.binary_search_first(prefix)

        if start == -1:
            return matches

        for i in range(start, len(self.words)):
            if self.words[i].startswith(prefix):
                matches.append(self.words[i])
            else:
                break

        return matches


class PrefixSuggester:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def suggest(self, prefix):
        return self.dictionary.prefix_matches(prefix)


class App:
    def show_prefixes(self):
        try:
            with open("prefixes.txt", "r") as f:
                prefixes = [p.strip() for p in f.readlines() if p.strip()]
        except FileNotFoundError:
            print("Error: prefixes.txt not found.")
            return

        print("\nAvailable Prefixes:")
        for p in sorted(prefixes):
            print(" -", p)

    def run(self):
        try:
            with open("words.txt", "r") as f:
                word_list = f.readlines()
        except FileNotFoundError:
            print("Error: words.txt not found.")
            return

        dictionary = Dictionary(word_list)
        suggester = PrefixSuggester(dictionary)

        print("Autocomplete System (type 'prefixes' to view prefix list, 'exit' to quit)")

        while True:
            prefix = input("\nEnter prefix: ").strip()

            if prefix.lower() == "exit":
                print("Goodbye.")
                break

            if prefix.lower() == "prefixes":
                self.show_prefixes()
                continue

            suggestions = suggester.suggest(prefix)

            if suggestions:
                print("Suggestions:")
                for word in suggestions:
                    print(" -", word)

                choice = input("\nMatch found! Type 'exit' to quit or press Enter to search again: ").strip().lower()

                if choice == "exit":
                    print("Goodbye!")
                    break
                else:
                    continue

            else:
                print("No matches found.")


def main():
    app = App()
    app.run()


if __name__ == "__main__":
    main()