import sys

last_tag = sys.argv[1]
last_commit = sys.argv[2]
next_tag = ""
brokenup_tag = last_tag.split(".")

if "major/" in last_commit:
major_version = int(brokenup_tag[0])
next_tag = str(major_version+1)+".0.0"

elif "feature/" in last_commit:
feature_version = int(brokenup_tag[1])
next_tag = brokenup_tag[0]+"."+str(feature_version+1)+".0"

else:
patch_version = int(brokenup_tag[2])
next_tag = brokenup_tag[0]+"."+brokenup_tag[1]+"."+str(patch_version+1)

print(next_tag)