"""
71. Simplify Path
link: https://leetcode.com/problems/simplify-path/
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        directories = []

        for item in path:
            if item == "" or item == ".":
                continue

            if item == "..":
                if len(directories) > 0:
                    directories.pop()
            else:
                directories.append(item)

        return "/" + "/".join(directories)

    def simplifyPath(self, path: str) -> str:
        directories = []
        i, n = 0, len(path)

        while i < n:
            while i < n and path[i] == "/":
                i += 1  # Skipping slashes

            start = i
            while i < n and path[i] != "/":
                i += 1  # Finding end of directory

            new_dir = path[start:i]

            if new_dir == "..":
                if directories:  # Not []
                    directories.pop()  # Moving up one level

            elif new_dir and new_dir != ".":  # not empty and "."
                directories.append(new_dir)

        return "/" + "/".join(directories)


unix_path = Solution().simplifyPath("/...///a/../b/c/../d/./")
print(f"Absolute path: {unix_path}")
