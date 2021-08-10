import os


class Path:

    @staticmethod
    def get_root_dir() -> str:
        current_file_path = os.path.abspath(__file__)
        spitted = os.path.split(current_file_path)
        root_path = os.path.join(spitted[0], '..')
        return root_path
