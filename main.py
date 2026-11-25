import os
import shutil

out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
os.makedirs(out_dir, exist_ok=True)
shutil.copyfile("entry.txt", os.path.join(out_dir, "entry.txt"))

# How this little script works, in plain words:
# The entry text already exists on disk before this runs — the script
# does not write a single word of it. All it does is put that finished
# file where the judges look for it: the folder named by the
# MAKEFUN_OUTPUT_DIR environment variable. If that folder does not
# exist yet, it is made first. The copy is byte-for-byte, so what
# lands in the output folder reads exactly as it was written.
