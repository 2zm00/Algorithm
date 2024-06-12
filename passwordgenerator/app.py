
#대소문자 구분 / 숫자 포함 / 특수문자 포함

site = input("Password Generator\n사이트 주소를 입력하세요: ")

if "http://" in site:
    site = site.replace("http://", "")
if "https://" in site:
    site = site.replace("https://", "")
if "www." in site:
    site = site.replace("www.", "")
if ".com" in site:
    site = site[:site.index(".")]

site = site[:3]+str(len(site))+str(site.count("a"))+"!"

print(site[0].upper()+site[1:])
