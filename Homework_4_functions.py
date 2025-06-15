# Homework_4 functions for project Wordle

def get_result(word1, word2):
    result=[]; i=0
    while i < len(word1):
        character = word1[i]
        if character == word2[i]:
            result.append('correct')
        elif character in word2:
            result.append('present')
        else:
            result.append('absent')
        i += 1
    return result

def get_string_from_results(results, word):
    string_parts=[]
    i = 0
    while i < len(results):
        character = word[i]
        result = results[i]
        if result == 'correct':
            string_parts.append("[" + character.upper() + "]")
        elif result == 'present':
            string_parts.append("(" + character + ")")
        else:
            string_parts.append(" " + character + " ")
        i += 1

    junction = "".join(string_parts)
    return junction