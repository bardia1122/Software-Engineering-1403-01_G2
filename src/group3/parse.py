import re

def find_word_boundary(text, index):
    """Find the start index of the word containing the current index."""
    # Move left until a space or start of the text
    while index > 0 and text[index - 1] not in (' ', '\n'):
        index -= 1
    return index

def generate_suggestions(input_text, corrected_text):
    input_index = 0
    corrected_index = 0
    suggestions = []

    while input_index < len(input_text) and corrected_index < len(corrected_text):
        input_char = input_text[input_index]
        corrected_char = corrected_text[corrected_index]

        # Match, move both pointers
        if input_char == corrected_char:
            input_index += 1
            corrected_index += 1
            continue

        # Detect Consecutive Spaces (merged into one suggestion)
        if input_char == " " and corrected_char != " ":
            start_index = find_word_boundary(input_text, input_index)
            while input_index < len(input_text) and input_text[input_index] == " ":
                input_index += 1
            suggestions.append({
                "start": start_index,
                "end": input_index,
                "original": input_text[start_index:input_index],
                "suggestion": corrected_text[start_index:corrected_index + 1]
            })
            continue

        # Detect Half-Space Insertions
        if corrected_char == "‌" and input_char != "‌":
            start_index = find_word_boundary(input_text, input_index)
            suggestions.append({
                "start": start_index,
                "end": input_index + 1,
                "original": input_text[start_index:input_index + 1],
                "suggestion": corrected_text[start_index:corrected_index + 1]
            })
            corrected_index += 1
            continue

        # Handle Simple Character Replacements (Adjusted to Word Boundary)
        start_index = find_word_boundary(input_text, input_index)
        suggestions.append({
            "start": start_index,
            "end": input_index + 1,
            "original": input_text[start_index:input_index + 1],
            "suggestion": corrected_text[start_index:corrected_index + 1]
        })

        input_index += 1
        corrected_index += 1

    # Handle Remaining Characters in Input (Deletions)
    while input_index < len(input_text):
        start_index = find_word_boundary(input_text, input_index)
        suggestions.append({
            "start": start_index,
            "end": len(input_text),
            "original": input_text[start_index:],
            "suggestion": ""
        })
        break

    # Handle Remaining Characters in Corrected Text (Insertions)
    while corrected_index < len(corrected_text):
        start_index = find_word_boundary(corrected_text, corrected_index)
        suggestions.append({
            "start": start_index,
            "end": len(corrected_text),
            "original": "",
            "suggestion": corrected_text[start_index:]
        })
        break

    return suggestions

input_text = "من میتوانم    یا می توانم   ."
output_text = "من می‌توانم یا می‌توانم."
print(generate_suggestions(input_text,output_text))
print(f"word is: {input_text[20:28]} end of word")