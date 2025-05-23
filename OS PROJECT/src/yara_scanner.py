import yara

def scan_file_with_yara(file_path, rules_path="rules/fake_rules.yar"):
    rules = yara.compile(filepath=rules_path)
    matches = rules.match(filepath=file_path)
    return matches
