from AutoCompleteSystem import AutoCompleteSystem
from phrases import phrases

autoCompleteSystem = AutoCompleteSystem(phrases)

def auto_complete(prefix):
    messages = autoCompleteSystem.auto_complete(prefix)
    return messages