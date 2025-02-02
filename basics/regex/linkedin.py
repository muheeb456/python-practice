import re

url = input("URL: ").strip()

# username = url.replace("http://linkedin.com/","")
# print(f"username {username}")

# username = url.removeprefix("http://linkedin.com/")
# print(f"username {username}")

# re.sub(pattern,replacement,string,count=0,flags=0) # substitue|replace based in pattern or regex
# username = re.sub(r"^(https?://)?(www\.)?linkedin\.com/","",url)
# print(f"username {username}")

if matches := re.search(r"^(?:https?://)?(?:www\.)?linkedin\.com/([a-z0-9_]+)",url,re.IGNORECASE): #(?:...) --> non capturing group
    print(f"username: {matches.group(1)}")
else:
    print("Your link is broken please check again!")


'''
    re.split(pattern,string,maxsplit=0,flags=0)
    re.findall(patter,string,flags=0)
'''

#   used to validate , cleanup, extract data
