phrases = [
    "Ogre",
    "Jungle",
    "Pickly",
    "Large",
    "Orange",
    "Cake",
    "Walk",
    "Green"
]

def is_not_punctuation(ch):
    punctuation = "'\"!@#$%^&*()_+,./?;:[]{}\|~`"
    return ch not in punctuation

def remove_punctuation(chs):
    return list(filter(is_not_punctuation, chs))

def format_string(string):
    lower_case_chs = list(string.lower())
    chs_with_no_puncation = remove_punctuation(lower_case_chs)
    return "".join(chs_with_no_puncation)

def validate_input(func):
    def wrapper_func(_, string):
        if not isinstance(string, str):
            raise TypeError("Invalid type, expected string.")
        
        return func(_, string)

    return wrapper_func

class Node:
    def __init__(self):
        self.is_word_complete = False
        self.children = {}

class AutoCompleteSystem:
    def __init__(self, strings):
        self.root = Node()

        # This map is used to map the formatted string to the actual string
        # This is needed since the string is formatted before it is inserted into the trie
        self.actual_strings = {}

        if isinstance(strings, list):
            for string in strings:
                self.add(string)
        
    @validate_input
    def add(self, string):
        formatted_string = format_string(string)

        curr = self.root

        for letter in formatted_string:
            if letter not in curr.children:
                curr.children[letter] = Node()
            
            curr = curr.children[letter]

        curr.is_word_complete = True
        self.actual_strings[formatted_string] = string

    @validate_input
    def find(self, string):
        curr = self.root

        for letter in string:
            if letter not in curr.children:
                return None

            curr = curr.children[letter]

        return curr

    @validate_input
    def auto_complete(self, prefix):
        strings = []

        formatted_prefix = format_string(prefix)

        start_node = self.find(formatted_prefix)

        def auto_complete_helper(node, string):
            if node.is_word_complete and string != formatted_prefix:
                strings.append(self.actual_strings[string])
                
            for ch, node in node.children.items():
                auto_complete_helper(node, string + ch)

        if start_node != None:
            auto_complete_helper(start_node, formatted_prefix)

        return strings
