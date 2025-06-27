
# sampling does not support reasoning/COT models
'''
async def review_prompt(context: Context, file_to_review: FileToReview, prompt: str) -> list[ViolationItem]:
    message_result = await context.session.create_message(
        messages = [
            SamplingMessage(
                role="user",
                content=TextContent(
                    type="text",
                    text=prompt
                )
            )
        ],
        max_tokens=DataManager.get_max_tokens(),
    )

    logging.info(f"Received response for file {file_to_review.file_name}")

    text = message_result.content.text
    text = text[text.index('['): text.rindex(']') + 1]
    parsed_data = json.loads(text)
    result = []
    for item in parsed_data:
        if isinstance(item, dict) and 'line_no' in item and 'rule_name' in item and 'message' in item:
            violation_item = ViolationItem(
                file_name=file_to_review.file_name,
                line_no=item['line_no'],
                rule=item['rule_name'],
                message=item['message']
            )
            result.append(violation_item)
        else:
            logging.warning(f"Invalid item format: {item}")
    
    logging.info(f"Found {len(result)} violations in file {file_to_review.file_name}")
    return result


async def review_file(context: Context, file_to_review: FileToReview) -> list[ViolationItem]:
    rules = DataManager.get_instance().get_rules_by_file_type(file_to_review.file_type)
    max_length_rule = max(rules, key=len)
    max_chunk_size = DataManager.get_max_prompt_length() - len(prompt_template.format(rules=max_length_rule, content_to_review=""))

    file_chunks = generate_file_chunks(file_to_review.content, max_chunk_size)

    prompts = []
    for chunk in file_chunks:
         for rule in rules:
            prompts.append(prompt_template.format(rules=rule, content_to_review=chunk))

    
    logging.info(f"Reviewing file {file_to_review.file_name} with {len(prompts)} prompts")

    result = []
    for prompt in prompts:
         result.extend(await review_prompt(context, file_to_review, prompt))
       
    return result

@mcp.tool()
async def review_file(file_path: str) -> list[ViolationItem]:
    """review a file and return the review results.

    Args:
        file_path: Path to the file containing the state code (e.g., '/path/to/xxx.go', '/path/to/xxx.html.markdown')

    Returns:
        A list of ViolationItem objects containing the file name, line number, and error message
    """
    try:
        if not any(file_path.endswith(ext) for ext in ['.go', '.html.markdown']):
            raise_error(f"Unsupported file type for {file_path}. Supported types are .go and .html.markdown")

        logging.info(f"Reviewing file: {file_path}")
        with open(file_path, 'r') as file:
            return await reviewer.review_file(mcp.get_context(), FileToReview(file_name=file_path, file_type=FileType.from_filename(file_path), content=file.read()))
    except Exception as e:
        error = f"Error reviewing file {file_path}: {str(e)}"
        logging.error(error)
        return error
    

@mcp.tool()
async def review_pull_request(pull_request_url: str) -> list[ViolationItem]:
    """review a pull request and return the review results.

    Args:
        pull_request_url: URL of the pull request to review (e.g., 'https://github.com/xxx/yyy/pull/12345')

    Returns:
        A list of ViolationItem objects containing the file name, line number, and error message
    """
    try:
        files = get_files_to_review(pull_request_url)
    except Exception as e:
        error = f"Error fetching pull request files from {pull_request_url}: {str(e)}"
        logging.error(error)
        return error
    
    result = []
    for file in files:
        try:
            logging.info(f"Reviewing file {file.file_name}")
            violations = await reviewer.review_file(mcp.get_context(), file)
            result.extend(violations)
        except Exception as e:
            logging.error(f"Error reviewing file {file.file_name}: {str(e)}")
            
    return result

'''