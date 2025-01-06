from uils.path import project_root


class FileUtil:
    @classmethod
    def generate_by_path(cls, context, file_path):
        file_path = project_root / file_path
        # 确保目标目录存在
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, "w") as f:
            f.write(context)
