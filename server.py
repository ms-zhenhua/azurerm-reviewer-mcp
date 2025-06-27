import logging
import os

import reviewer
from mcp.server.fastmcp import FastMCP
from utils import FileType, FileToReview, raise_error, Constants, is_valid_uuid
from data_manager import DataManager
from pull_request_manager import get_files_to_review

mcp = FastMCP("azurerm-reviewer")

@mcp.prompt()
def review_file(file_path: str) -> str:
    try:
        file_type = FileType.from_filename(file_path)
        if file_type == FileType.UNKNOWN:
            return f"File extension is not supported: {file_path}. Supported file extesnions are: .go, .html.markdown"
        with open(file_path, 'r') as file:
            return reviewer.create_review_task([FileToReview(file_name=file_path, file_type=file_type, content=file.read())])
    except Exception as e:
        logging.error(f"Error reviewing file {file_path}: {str(e)}")
        return "Failed to generate the prompt for the file review. Please check the logs for more details."
        
@mcp.prompt()
def review_pull_request(pull_request_url: str) -> str:
    try:
        return reviewer.create_review_task(get_files_to_review(pull_request_url))
    except Exception as e:
        logging.error(f"Error reviewing pull request {pull_request_url}: {str(e)}")
        return "Failed to generate the prompt for the pull request review. Please check the logs for more details."

@mcp.tool()
def get_next_review_task(task_id: str) -> str:
    """Retrieves the next review task based on the provided task UUID.
    Args:
        task_id (str): The UUID of the task. (e.g. "123e4567-e89b-12d3-a456-426614174000")
    Returns:
        str: A message indicating the next task to be completed. If all tasks are completed, it returns a message indicating that there are no more tasks. If the task ID is not found, it returns an error message.
    """
    try:
        split_items = task_id.split('.')
        if len(split_items) > 1:
            task_id = split_items[1] # workaround for the issue that the MCP client may set task_id as `2025-07-10_12-28-46.90086377-1872-47c7-9927-0627317623b9`.
            
        if not is_valid_uuid(task_id):
            return 'Invalid format for the value of input parameter `task_id`. `task_id` must be a valid UUID. (e.g. "123e4567-e89b-12d3-a456-426614174000")'
                
        return reviewer.get_next_review_task(task_id)
    except Exception as e:
        logging.error(f"Error retrieving task {task_id}: {str(e)}")
        return "Failed to retrieve the next review task. Please check the logs for more details."

def initialization():
    logging.basicConfig(level=logging.INFO)
    if not os.getenv(Constants.GITHUB_TOKEN, ''):
        logging.warning(f"{Constants.GITHUB_TOKEN} environment variable is not set. Rate limits may be lower for GitHub API requests.")
    
    if not os.getenv(Constants.MAX_TOKENS, ''):
        raise_error(f"{Constants.MAX_TOKENS} environment variable is required to set the maximum number of tokens for the model.")

    max_rule_length_per_prompt = os.getenv(Constants.MAX_RULE_LENGTH_PER_PROMPT, '')
    if max_rule_length_per_prompt:
        logging.warning(f"{Constants.MAX_RULE_LENGTH_PER_PROMPT} is set to {max_rule_length_per_prompt}")

    result_directory = os.getenv(Constants.RESULT_DIRECTORY, '')
    if not result_directory:
        raise_error(f"{Constants.RESULT_DIRECTORY} environment variable is required to set the directory for storing results.")
    else:
        os.makedirs(result_directory, exist_ok=True)
        logging.info(f"Results will be stored in {result_directory}")
    
    DataManager.get_instance()


if __name__ == "__main__":
    initialization()
    mcp.run(transport='stdio')