import glob
import os
import re

def get_pipeline_path(name: str) -> str:
    dirname = os.path.dirname(__file__)
    path = os.path.join(dirname, name) + ".json"
    if os.path.exists(path):
        return path
    else:
        raise ValueError(f"File '{path}' is not part of valid pipelines!")

def get_pipeline_name(path: str) -> str:
    """
    Input "path" is the str for the pipeline's full path.
    """
    dirname = os.path.dirname(__file__)
    if os.path.dirname(path) != dirname or not os.path.exists(path):
        raise ValueError(f"File {path} is not a pipeline from ({dirname})")
    return os.path.basename(path).split(".")[0]

def get_pipelines_paths(names: set = None) -> set:
    """
    Return pipelines' path.
    By default return all pipelines' paths in the RestingfMRI_Denoise pipeline folder.
    """
    dirname = os.path.dirname(__file__)
    if names is None:
        return set(glob.glob(os.path.join(dirname, "*.json")))
    elif names is not None and names <= get_pipelines_names():
        return set(map(get_pipeline_path, names))
    else:
        raise ValueError("Unknown pipelines names: " + str(names))

def get_pipelines_names() -> set:
    """
    Return all pipelines' names in the RestingfMRI_Denoise pipeline folder.
    """
    return set(map(get_pipeline_name , get_pipelines_paths()))


def is_valid_name(name: str) -> bool:
    return True if name in get_pipelines_names() else False
