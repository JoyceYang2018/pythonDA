def simplifyPath(self, path: str) -> str:
    a_list = path.split("/")
    result = []
    for i in a_list:
        if i == "..":
            if result:
                result.pop()
        elif i not in [".", ""]:
            result.append(i)
    return "/" + "/".join(result)