import os
import logging

from utils import FileType, Rules, raise_error,Constants

class DataManager:
    _instance = None
    _initialized = False

    def __init__(self):
        if not self._initialized:
            self._rules = DataManager._load_rules()
            DataManager._initialized = True
        
    def get_rules_by_file_type(self, file_type: FileType) -> list[str]:
        if file_type == FileType.GO_RESOURCE:
            return self._rules.go_resource
        elif file_type == FileType.GO_TEST:
            return self._rules.go_test
        elif file_type == FileType.MARKDOWN_DOC:
            return self._rules.markdown_doc
        else:
            raise_error(f"Unknown file type: {file_type}")

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    @staticmethod
    def _load_rules_from(directory: str) -> list[str]:
        md_files = [item for item in os.listdir(directory) if item.endswith('.md')]
        logging.info(f"Loading rules from {directory}, found {len(md_files)} files")
        rules = []
        for md_file in md_files:
            file_path = os.path.join(directory, md_file)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                rule_name = md_file[:-len('.md')]
                rules.append(f'<Rule>## rule name: {rule_name}\n{content}</Rule>')
        
        rules_str = '\n\n'.join(rules)
        max_rule_length = DataManager.get_max_rule_length()

        if len(rules_str) <= max_rule_length:
            result = [rules_str]
        else:
            # Calculate number of elements needed
            num_elements = (len(rules_str) + max_rule_length - 1) // max_rule_length
            
            # Create empty strings in result
            result = [''] * num_elements
            
            # Distribute rules one by one into the shortest string
            for rule in rules:
                # Find the index of the shortest string
                shortest_index = min(range(len(result)), key=lambda i: len(result[i]))
                
                # Add separator if the string is not empty
                if result[shortest_index]:
                    result[shortest_index] += '\n\n'
                
                # Add the current rule to the shortest string
                result[shortest_index] += rule

        logging.info(f"Loaded {len(result)} rules from {directory}")
        return result

    @staticmethod
    def _load_rules() -> Rules:
        try:
            rules = Rules(go_resource=[], go_test=[], markdown_doc=[])
            rules_directory = os.path.join(os.path.dirname(__file__), 'rules')
            rules.go_resource = DataManager._load_rules_from(os.path.join(rules_directory, FileType.GO_RESOURCE.value))
            rules.go_test = DataManager._load_rules_from(os.path.join(rules_directory, FileType.GO_TEST.value))
            rules.markdown_doc = DataManager._load_rules_from(os.path.join(rules_directory, FileType.MARKDOWN_DOC.value))
        except Exception as e:
            raise_error(f"Failed to load rules: {str(e)}")

        return rules
    
    @staticmethod
    def get_max_prompt_length() -> int:
        return int(os.getenv('MAX_TOKENS')) << 2 # suppose max_prompt_length is four times of max_tokens

    @staticmethod
    def get_max_rule_length() -> int:
        max_rule_length_per_prompt = os.getenv(Constants.MAX_RULE_LENGTH_PER_PROMPT, '')
        if max_rule_length_per_prompt:
            return int(max_rule_length_per_prompt)
        
        return DataManager.get_max_prompt_length() >> 1 # use half of max_prompt_length for rules

    @staticmethod
    def get_max_tokens() -> int:
        return int(os.getenv('MAX_TOKENS'))
    
    @staticmethod
    def get_chunk_overlap_ratio() -> float:
        return 0.1
