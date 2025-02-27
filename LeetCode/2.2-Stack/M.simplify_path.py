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


unix_path = Solution().simplifyPath("/...///a/../b/c/../d/./")
print(f"Absolute path: {unix_path}")
