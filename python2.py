from importlib import metadata

print("Pip Version : ",metadata.version("pip"))
pip_metadata = metadata.metadata("pip")
print(list(pip_metadata))
print("Homepage: ",pip_metadata["Home-page"])
print("Python requirements",pip_metadata["Requires-Python"])