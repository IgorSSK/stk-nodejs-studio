import os

def run(meta):
  meta.global_inputs["project_name"] = os.path.basename(os.getcwd())
  return meta