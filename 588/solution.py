class File:
    def __init__(self, name: str, content: str = ""):
        self.name = name
        self.content = content
class Folder:
    def __init__(self, name: str):
        self.name = name
        self.children: dict[str, "Folder | File"] = {}

    def sorted_children(self) -> List[str]:
        return sorted(self.children)
Node = Folder | File
class FileSystem:
    def __init__(self):
        self.root = Folder("")

    def _parse_path(self, path: str) -> list[str]:
        return [part for part in path.split("/") if part]

    def _traverse(self, path: str) -> Node | None:
        curr: Node = self.root
        for name in self._parse_path(path):
            if not isinstance(curr, Folder) or name not in curr.children:
                return None
            curr = curr.children[name]
        return curr

    def _traverse_or_create(self, parts: list[str]) -> Folder:
        curr = self.root
        for name in parts:
            if name not in curr.children:
                curr.children[name] = Folder(name)
            curr = curr.children[name]
        return curr

    def ls(self, path: str) -> List[str]:
        node = self._traverse(path)
        if isinstance(node, Folder):
            return node.sorted_children()
        if isinstance(node, File):
            return [node.name]
        return []

    def mkdir(self, path: str) -> None:
        self._traverse_or_create(self._parse_path(path))

    def addContentToFile(self, filePath: str, content: str) -> None:
        parts = self._parse_path(filePath)
        parent = self._traverse_or_create(parts[:-1])
        file_name = parts[-1]

        if file_name not in parent.children:
            parent.children[file_name] = File(file_name)

        parent.children[file_name].content += content

    def readContentFromFile(self, filePath: str) -> str:
        node = self._traverse(filePath)
        return node.content if isinstance(node, File) else ""
