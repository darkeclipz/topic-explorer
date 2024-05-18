import os
import json
from openai import OpenAI
from helpers import get_key
client = OpenAI(api_key=get_key())

def to_filename(filename):
    return filename.replace(' ', '-').replace('/', '-').replace('(', '').replace(')', '').replace(',', '').replace('.', '').replace('?', '').replace('\'', '').lower()

subject = "statistics"

if not os.path.exists(subject):
    os.mkdir(subject)

if not os.path.exists(f'{subject}/src'):
    os.mkdir(f'{subject}/src')

if not os.path.exists(f'{subject}/key_topics.json'):

    print(f'Retrieving topics and subtopics for: {subject}...')

    json_format = """
    {
        "key_topics": [
            {"topic", "<TOPIC_NAME>", subtopics: []},
            {"topic", "<TOPIC_NAME>", subtopics: []},
        ]
    }
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        response_format={ "type": "json_object" },
        messages=[
            {"role": "system", "content": "You are a helpful assistant designed to output JSON in the following format:\n\n" + json_format},
            {"role": "user", "content": f"Tell me key topics and subtopics for {subject}."},
        ]
    )

    key_topics_json = response.choices[0].message.content

    with open(f'{subject}/key_topics.json', 'w') as key_topics_file:
        key_topics_file.write(key_topics_json)

else:

    print(f'Reading topics and subtopics from key_topics.json for: {subject}...')

    with open(f'{subject}/key_topics.json', 'r') as key_topics_file:
        key_topics_json = key_topics_file.read()

key_topics = json.loads(key_topics_json)

for topic in key_topics["key_topics"]:
    topic_name = topic["topic"]
    subtopics = topic["subtopics"]
    for subtopic_name in subtopics:
        print(f'  * {topic_name}: {subtopic_name}')

for topic in key_topics["key_topics"]:
    topic_name = topic["topic"]
    subtopics = topic["subtopics"]
    for subtopic_name in subtopics:
        output_file_name = to_filename(f'{topic_name}-{subtopic_name}') + ".md"
        absolute_output_file_name = f'{subject}/src/{output_file_name}'

        if os.path.exists(absolute_output_file_name):
            print(f'Skipping {output_file_name}...')
            continue
        else:
            print(f'Generating {output_file_name}...')
    
        client = OpenAI(api_key=get_key())

        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Tell me key topics for {subject}."},
            {"role": "assistant", "content": key_topics_json},
            {"role": "user", "content": f"Explain {subtopic_name} ({topic_name})."},
        ]

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages
        )

        with open(absolute_output_file_name, 'w', encoding="utf-8") as output_file:
            output_file.write(response.choices[0].message.content)


print('Prepending post headers...')

for topic in key_topics["key_topics"]:
    topic_name = topic["topic"]
    subtopics = topic["subtopics"]
    for subtopic_name in subtopics:
        output_file_name = to_filename(f'{topic_name}-{subtopic_name}') + ".md"
        absolute_output_file_name_orig = f'src/{output_file_name}'
        absolute_output_file_name = f'src/{output_file_name}'
        
        with open(f'{subject}/{absolute_output_file_name_orig}', 'r', encoding='utf-8') as output_file:
            output_file_content = output_file.readlines()

        if output_file_content[0][:3] == '---':
            print(f'Header already found in {output_file_name}, skipping...')
            continue

        prepend = [
            "---\n",
            f"title: {subtopic_name}\n"
            "---\n\n",
            "[Back to index](index.html)\n\n",
            "---\n",
            f"# {topic_name}\n",
            f"## {subtopic_name}\n\n",
            ""
        ]

        append = [
            "\n\n---\n",
            "[Back to index](index.html)\n"
        ]

        with open(f'{subject}/{absolute_output_file_name}', 'w', encoding='utf-8') as output_file:
            output_file.writelines(prepend)
            output_file.writelines(output_file_content)
            output_file.writelines(append)


print('Generating table of contents...')

table_of_contents = []

for topic in key_topics["key_topics"]:
    topic_name = topic["topic"]
    subtopics = topic["subtopics"]
    chapter = []
    table_of_contents.append((topic_name, chapter))
    for subtopic_name in subtopics:
        output_file_name = to_filename(f'{topic_name}-{subtopic_name}')
        absolute_output_file_name = f'{output_file_name}.html'
        chapter.append((subtopic_name, absolute_output_file_name))

index = []

index.append("# Programming\n")
index.append("## Table of Contents\n")

for topic, chapter in table_of_contents:

    index.append(f"### {topic}\n\n")

    for subtopic, path in chapter:

        index.append(f" * [{subtopic}]({path})\n")
    
    index.append("\n")

with open(f"{subject}/src/index.md", "w", encoding="utf-8") as index_file:
    index_file.writelines(index)