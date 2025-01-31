import os
import re

def replace_every_odd_occurrence(text, pattern, replacement):
    def replace(match):
        replace.counter += 1
        if replace.counter % 2 != 0:
            return replacement
        else:
            return match.group(0)

    replace.counter = 0
    return re.sub(pattern, replace, text)

def replace_every_even_occurrence(text, pattern, replacement):
    def replace(match):
        replace.counter += 1
        if replace.counter % 2 == 0:
            return replacement
        else:
            return match.group(0)

    replace.counter = 0
    return re.sub(pattern, replace, text)

def process_markdown(text):
    # Escape the dollar sign in the pattern
    pattern1 = r"\$"  # Escaped `$` character for matching

    # Step 2: Replace every odd occurrence of $ with $` (and every even occurrence of $ with `$)
    text = replace_every_odd_occurrence(text, pattern1, "$` ")
    text = replace_every_even_occurrence(text, pattern1, " `$")

    return text

def process_all_markdown_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            # Process the file content
            updated_content = process_markdown(content)

            # Save the processed content back into the file
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(updated_content)

            print(f"Processed {file_path}")

# Run the processing for all markdown files in the 'docs' directory
if __name__ == "__main__":
    process_all_markdown_files("docs")  # 'docs' is the folder containing your .md files
