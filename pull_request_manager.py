import os
import logging
import requests

from utils import FileType, FileToReview, raise_error

def get_github_headers():
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    if os.getenv("GITHUB_TOKEN"):
        headers["Authorization"] = f"Bearer {os.getenv('GITHUB_TOKEN')}"

    return headers

def get_file_content(file) -> str:        
    response = requests.get(file["raw_url"])
    if response.status_code == 200:
        return response.text

    file_name = file['file_name']   
    raise_error(f"Failed to fetch file content of {file_name}: {response.status_code} {response.text}")


def get_pull_request_files(pull_request_url: str) -> list[dict]:
    all_files = []
    headers = get_github_headers()
    current_url = pull_request_url.replace("github.com", "api.github.com/repos").replace("/pull/", "/pulls/").rstrip('/') + '/files?per_page=100&page=1'

    max_loop_count = 100
    loop_count = 0
    while current_url and loop_count < max_loop_count:
        loop_count += 1
        logging.info(f"Fetching pull request files from {current_url}")
        response = requests.get(current_url, headers=headers)
        if response.status_code != 200:
            raise_error(f"Failed to fetch pull request files: {response.status_code} {response.text}")
        
        page_files = response.json()
        all_files.extend(page_files)

        current_url = None
        if 'Link' in response.headers:
            links = response.headers['Link']
            for link in links.split(','):
                if 'rel="next"' in link:
                    current_url = link.split('>')[0].split('<')[1]
                    break

    if loop_count >= max_loop_count:
        raise_error("Reached maximum loop count while fetching pull request files. This may indicate an issue with pagination or the number of files in the pull request.")

    logging.info(f"Total files fetched from pull request: {len(all_files)}")    
    return all_files


def get_files_to_review(pull_request_url: str) -> list[FileToReview]:
    files = get_pull_request_files(pull_request_url)
    files_to_review = []
    for file in files:
        file_name : str = file['filename']
        status = file.get("status", "")
        file_type = FileType.from_filename(file_name)
        if not any(file_name.startswith(item) for item in ['internal/services/', 'website/docs']) or file_type == FileType.UNKNOWN or status != "added":
            continue

        # skip test files other than resource test files
        if not file_name.endswith('_resource_test.go') and file_name.endswith('_test.go'):
            continue

        files_to_review.append(FileToReview(file_name=file["filename"], file_type=file_type, content=get_file_content(file)))
    
    logging.info(f"Total files to review: {len(files_to_review)}")
    return files_to_review