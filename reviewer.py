import logging
import os

from datetime import datetime
from utils import FileToReview, Constants, create_uuid
from data_manager import DataManager

json_format = """\
[
    {
        "rule": "array_dictionary_init_with_make",
        "file": "/home/user/code/review/test/test.go",
        "line": 123,
        "message": "array and dictionary should be initialized with make..."
    }
]
"""

md_format = """\
# Code Review Results
### File: D:\code\code_review\test\test.go
| Rule Name | Line Number | Error Message |
|-----------|-------------|---------------|
| tags_type_definition | 45 | `Tags` fields must be defined as `map[string]string` for type safety. Avoid `map[string]interface{}`. |
| prefer_name_validation | 108 | Define `ValidateFunc` for the `name` field and do not simply use `validation.StringIsNotEmpty` to validate `name`. Use a proper validation function with regex pattern or specific validation logic. |\
""" 

prompt_template = """
<Role>You are an expert in Terraform Provider for Azure.</Role>
<Task>Your task is to: review the content between <file_to_review> tags below to find out all places where violate the rules defined in <rules/> tags below. You should use the rules to check the content between <file_to_review> tags and output a violation list. The element in the list should contain the rule_name, file_path, line_number and error_message. If there is no error, return an empty list: '[]'.</Task>

<rules>
{rules}
</rules>

<file_to_review>
# file: {file_name}
{content_to_review}
</file_to_review>
"""

def add_line_number(line_no: int, line: str) -> str:
    return f"{line_no} {line}"

def generate_file_chunks(file_content: str, max_chunk_size: int) -> list[str]:
    result = []
    lines = file_content.splitlines()
    idx = 0

    current_chunk = ''
    while idx < len(lines):
        line = add_line_number(idx + 1, lines[idx]) + '\n'
        if len(current_chunk) + len(line) > max_chunk_size:
            result.append(current_chunk)
            current_chunk = ''
            overlap_size = int(DataManager.get_chunk_overlap_ratio()* max_chunk_size)
            while overlap_size > 0 and idx >= 0:
                overlap_size -= len(lines[idx])
                idx -= 1

            continue
            
        current_chunk += line
        idx += 1
    
    if current_chunk:
        result.append(current_chunk)

    return result

def create_prompts(file: FileToReview) -> list[str]:
    rules = DataManager.get_instance().get_rules_by_file_type(file.file_type)
    max_length_rule = max(rules, key=len)
    max_chunk_size = DataManager.get_max_prompt_length() - len(prompt_template.format(file_name=file.file_name, rules=max_length_rule, content_to_review=""))
    file_chunks = generate_file_chunks(file.content, max_chunk_size)

    prompts = []
    for chunk in file_chunks:
        for rule in rules:
            prompts.append(prompt_template.format(file_name=file.file_name, rules=rule, content_to_review=chunk))
    
    logging.info(f"Generated {len(prompts)} prompts for file {file.file_name}")
    return prompts
     
def create_review_task(files: list[FileToReview]) -> str:
    prompts: list[str] = []
    for file in files:        
        prompts.extend(create_prompts(file))

    task_id = create_uuid()
    directory = os.path.join(os.getenv(Constants.RESULT_DIRECTORY), datetime.now().strftime("%Y-%m-%d_%H-%M-%S")+f".{task_id}")
    logging.info(f"Creating review task in directory: {directory}")   
    os.makedirs(directory, exist_ok=True)

    json_format_file_path = os.path.join(directory, Constants.JSON_FORMAT_FILE)
    with open(json_format_file_path, 'w') as f:
        f.write(json_format)

    with open(os.path.join(directory, Constants.MD_FORMAT_FILE), 'w') as f:
        f.write(md_format)

    idx = 1
    for prompt in prompts:
        prompt_file_path = f"{directory}/prompt_{idx}.txt"
        with open(prompt_file_path, 'w') as f:
            f.write(prompt)
        
        result_file_path = f"{directory}/result_{idx}.txt"
        content = f'read and complete all instructions in `{prompt_file_path}` from line 1 to line {len(prompt.splitlines())} and save the result into `{result_file_path}` with the same format in `{json_format_file_path}`. The `message` field should contain not only the details of the problem, but also contain the details of how to fix the problem.'

        task_file_path = f"{directory}/task_{idx}.txt"
        with open(task_file_path, 'w') as f:
            f.write(content)

        idx += 1
    
    return f"Repeatedly invoke #{get_next_review_task.__name__} with task_id={task_id} and complete the given task until there are no more tasks."

   
def get_next_review_task(task_id: str) -> str:
    task_directories = [item for item in os.listdir(os.getenv(Constants.RESULT_DIRECTORY)) if item.endswith(task_id) and os.path.isdir(os.path.join(os.getenv(Constants.RESULT_DIRECTORY), item))]
    if not task_directories:
        return f"Task with ID {task_id} not found."
    
    target_directory: str = os.path.join(os.getenv(Constants.RESULT_DIRECTORY), task_directories[0])
    entries = os.listdir(target_directory)

    if Constants.REVIEW_RESULT_FILE in entries:
        return f"All tasks are completed. The review result is available in {os.path.join(target_directory, Constants.REVIEW_RESULT_FILE)}."

    tasks = [item for item in entries if item.startswith('task_') and item.endswith('.txt')]
    task_results = [item for item in entries if item.startswith('result_') and item.endswith('.txt')]

    for i in range(len(tasks)):
        if f'result_{i + 1}.txt' not in task_results:
            task_file = os.path.join(target_directory, f'task_{i + 1}.txt')
            with open(task_file, 'r') as f:
                return f'Next task: {f.read()}'
    
    review_draft_file_path = os.path.join(target_directory, Constants.REVIEW_DRAFT_FILE)
    if not os.path.exists(review_draft_file_path):
        content = ""
        for result in task_results:
            result_file = os.path.join(target_directory, result)
            with open(result_file, 'r') as f:
                content += f.read() + '\n\n'
        
        with open(review_draft_file_path, 'w') as f:
            f.write(content)
    

    md_format_file_path = os.path.join(target_directory, Constants.MD_FORMAT_FILE)
    review_result_file_path = os.path.join(target_directory, Constants.REVIEW_RESULT_FILE)
    return f'Next task: arrange the content in `{review_draft_file_path}` by your own knowledge and output the result to `{review_result_file_path}` with the same format as `{md_format_file_path}`'
