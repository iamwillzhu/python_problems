from typing import Dict, List
def is_well_formed(parentheses: str) -> bool:
    left_chars: List[str] = []
    lookup_chars: Dict[str, str] = {'(': ')', '[': ']', '{': '}'}

    for char in parentheses:
        if char in lookup_chars:
            left_chars.append(char)
        elif len(left_chars) == 0 or lookup_chars[left_chars.pop()] != char:
            return False

    return len(left_chars) == 0
    
