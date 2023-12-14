class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        duplicates = defaultdict(list)
        for path in paths:
            path = path.split()
            directory_path, files_in_path = path[0], path[1:]
            # print(files_in_path)
            for file in files_in_path:
                file_name, file_content = file.split('(')
                duplicates[file_content[:-1]].append(directory_path + '/' + file_name)
        return [duplicates[content] for content in duplicates if len(duplicates[content]) > 1]