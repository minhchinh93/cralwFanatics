import requests
import re
from thuvien import *

file2 = String_Interact() 
proxies = {
  "http": "http://pnbbraog:vv1uw2pljaxp@94.131.58.139:6395",
  "https": "http://pnbbraog:vv1uw2pljaxp@94.131.58.139:6395",
#   94.131.58.139:6395:pnbbraog:vv1uw2pljaxp

}

def cralwDetail(link):

  # url = "https://www.fanatics.com/college/fdu-florham-devils/fdu-florham-devils-under-armour-primary-performance-t-shirt-navy/o-27+t-90619533+p-265044582190+z-9-4291043011?_ref=p-TLP:m-GRID:i-r0c1:po-1"
  url = link
  payload = {}
  headers = {
    'authority': 'www.fanatics.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
    'cache-control': 'max-age=0',
    'cookie': 'platform1=e; mc=; u_loc=en-US; st=510005; ac=USD; uc=USD; priv=%7B%22acc%22%3Afalse%2C%22fcc%22%3Afalse%2C%22tcc%22%3Afalse%2C%22pc%22%3Atrue%2C%22ecc%22%3Afalse%7D; _s=www.fanatics.com; vid=e3a69010-fde7-11ed-b276-e30d315d4ad3; akacd_PR_Iris_permanent=2177452799~rv=32~id=e02e48794c60c577f8345cdffd9c57eb; akacd_PR_Iris_Assets=2177452799~rv=53~id=1c81d9a23e47e44dcf80c3f38d4da413; bm_sz=BF8A9D11948B5D96A17CDEA8AD3CF092~YAAQTzErF6V7MzuIAQAANKkjZhOJ17ayI1zySAac8jSNgZYDu60OlUqjG6giO0LGmSauJ2k4U5CUwqNsUYFD+GQ4XWqgsPVOvnW2qfCpc4Ed4P2W6GEwKchmlXKehR1aWyRoMoZPVdJRHzFIACuG/d4xZnvxXp71D/SmXcByD1U6fx0giKDxzw/gxFZ5aawNrd/vC5d4j0bMPuo0kZoZXa1jmXIDHK6KXdtLuy2lv46RcBFSRG9mBo//TdbTYJ8nR7QvR8bqz/QiAf0dIwlf7BlSYrHsaDgU56QZx+GMkUHqj7k00Q==~4273478~3159621; civ=1.1.0-rc-20230524.67956; va=%7B%22cc%22%3A0%2C%22ct%22%3A0%2C%22cpi%22%3A%5B%5D%2C%22nv%22%3Afalse%2C%22el%22%3Afalse%2C%22ch%22%3A%22%22%2C%22ci%22%3A%22dir%22%2C%22lic%22%3A%22dir%22%7D; s_fid=03B27B7338198A92-345A3BD12B27571C; s_cc=true; _gcl_au=1.1.1689534545.1685340794; s_fuid=2664110627609340343772393407434413852; fs.bot.check=true; ak_bmsc=0F6B9CAB68DB6B1216BD8F5270BD4535~000000000000000000000000000000~YAAQTzErF6h7MzuIAQAAebEjZhNO3CuIpwxPqN97GiNOVkPRP8nlRpfAYY16xUb2ZAs3IAKgdl8qHTwr/q8XMER9GrCvn791AJ6JTTM876GYDT2tInSGvxSdB6G2lv8bc4sLCb4PqUlH7/7hmkRF8pULqzkGLuMXkUocUzqsuEFY3F38AXqCoRzP2bpgEDUQS3RTEiKblgh5lnBZ71aetFi8FB4EO08LQ+qXpgUaGjUHxwaQhviQraLeLP7H69y3DUarvwUjYvfIOdB1Y6e9/Pe8/EAe0b2CQ/rLNcBtmr31HU3INOmI6XeonA36xrXu1h2Q/gHtNIZvg5j+bTh098Fnh8yrSeLZBOIDW65X21FBg0rJ1wPkFCRpSJ1+CmfaPGv3AjlMiFkcglocTak44FV7HAFC4niwFlZ94SVXhofSQjjIyHzSwpzyXXHtcby5C7bfQH6Y5FRqkDwVdLCylfOCnGOhNQ8xoA0yO3+3/LCLR4rOYiezbIIo96k=; fs.session.id=65b1a96b-476a-46c6-904a-e764921adb33; _pbjs_userid_consent_data=3524755945110770; cookie=6d0feb7f-a940-42e8-bb03-60edf46aab5c; _lr_retry_request=true; _lr_env_src_ats=false; __qca=P0-1364129056-1685340796739; _abck=493D983DB20D7106B9C40E3BE4B422BF~0~YAAQTzErF06DMzuIAQAA8kwpZgm1rB3hhy1k/G5uECMmvFS2A7m+zag55ECRzI6KT2srclWnhimm710tvLxnEivD3FJ/NnpFwxt9AMjM5PA+OhpQ8R70JmGT3eMbvBy4/figjrA4KdNfqNIG4D2Vq8i9iUSk74KmtYUB9b1zX67tuseMM/ssvZwjOAJF0jB9ZyW4RqsNQHEaxPxfvojyJVh6Wd+PGS7M6oIExQkcbhyaRQx4cMBS7yaQxOJj4u8llMTpWSr3SqVwO/MSYwMdCe53xzl4ZbbA4V+EsFnGBiFyUbuJKWKEjkfoRYXL7zHPyCFZK/MS7fSDDqbR9gSruJSrzzEed31AO6fnaWrlGF9wrPpsveSnsBKZ31AqAsRQwngIMox5YrlHDFxE7ClLnSYVmmGjB443nhQ=~-1~-1~-1; _fbp=fb.1.1685341195691.688109630; ist=a5c95680-fdef-11ed-8d2a-d35f18bc0a1c; ura=%7B%22fac%22%3A0%2C%22bds%22%3Afalse%7D; sa=sid%3Da5c95680-fdef-11ed-8d2a-d35f18bc0a1c%7Cfpr%3D0; __gads=ID=e8abbb505f733af3:T=1685340797:RT=1685344127:S=ALNI_MbbM6V-Q5H44Uv37gEbL5GVHkO3yg; __gpi=UID=00000c0c2852083a:T=1685340797:RT=1685344127:S=ALNI_MZsy6jY9zApBOlQwQRGuZmp6_vAKA; csl=/college/fairleigh-dickinson-florham-devils/o-38+t-4544645669+z-94411-3369440334; cqe=%5B%2210129%3AA%3A0%3A1%22%2C%2210287%3AB%3A1%3A1%22%2C%2210299%3AB%3A1%3A1%22%2C%2210318%3AA%3A0%3A1%22%5D; eci=9df55511deaf3b88; cqh=%5B%2210129%3AA%3A0%3A1%22%2C%2210287%3AB%3A1%3A1%22%2C%2210299%3AB%3A1%3A1%22%2C%2210318%3AA%3A0%3A1%22%5D; bm_sv=09423A2E1396C1FDA9B661EFEA9E7994~YAAQHzArF7mqFwaIAQAAjRJXZhNSZ6sArcshzRg7enw5UUVElxJyx5MPLXPZr+tPzmH/J+UEQQagWRVEfs9mCgkziUcbh2bM+Xzt1CSXNOcKnQ222RjDNmb0RkAXFucNyuBXLn60jXpRxAag8/Gl4VAk9aiEsPXh9M6jQdQMb3B9Rlm1DISaIghdgnm/xfDdgZteA/SOD/dzJV3mxPGZYNZ9LSY5rVowY98lP8pNa2eOOMTEZckHHF9CnARQmFCZ0Z4=~1; s_sq=%5B%5BB%5D%5D; AWSALB=L5UkTLxVSY152kBMYzY+sTdQSndIJhOqKdQfgo2vy+IM1vB1tYvUTjP6PwL/3cIa+bV8n8sRao1oE2i5xhQiJT0+EZxsTmKEGotXX5xsWV+N6zQzm7v+L4CZmdbQ; xsrft=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyZXFIb3N0Ijoid3d3LmZhbmF0aWNzLmNvbSIsInZpc2l0b3JJZCI6ImUzYTY5MDEwLWZkZTctMTFlZC1iMjc2LWUzMGQzMTVkNGFkMyIsImlhdCI6MTY4NTM0NDE2MywiZXhwIjoxNjg3MDI5MjA3NDAyfQ.dIjJTOuwfptuQy_OVUekwV9s5bSHfBYRJdJ5DxHnzro; xsrfp=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyZXFIb3N0Ijoid3d3LmZhbmF0aWNzLmNvbSIsInZpc2l0b3JJZCI6ImUzYTY5MDEwLWZkZTctMTFlZC1iMjc2LWUzMGQzMTVkNGFkMyIsImlhdCI6MTY4NTM0NDE2MywiZXhwIjoxNjg3MDI5MjA3NDAyfQ.old5vxRC7VKNpVdymrD5fDssNcMk4GemjvxtdwjEDnw; vrc=58343b1eea0b7ebd; AWSALBCORS=L5UkTLxVSY152kBMYzY+sTdQSndIJhOqKdQfgo2vy+IM1vB1tYvUTjP6PwL/3cIa+bV8n8sRao1oE2i5xhQiJT0+EZxsTmKEGotXX5xsWV+N6zQzm7v+L4CZmdbQ; ajs_anonymous_id=3d0fa119e5f76da7610b9096720c1d2a-0e09f2db7067a0295b1cd78924aae50b4665f37a9dcb7cb32b1ff1fa0dd005c6; cto_bidid=7iSkP19KbWJ2cUJORVBIc1lYUGU2dHI1RHJUTmk4dkxpYk8lMkZpT3IyNXZoOHFpODZxNnhxdE1PbGNGNmlyb3FiZUNUdzNVb2VrNFJtSTlsZWJzNVhCREQ3ckQ2NFRScCUyRkVmcWtTTjhCZ3ZCbmM2WjQlM0Q; cto_bundle=DBzlal9keSUyRkJSJTJCeHJUOWxmdW91MGhpQ2RjbGlLJTJGS0Z3YVlIc0IxM2I2R09DNEdUTUNyU2NXVVhqd2g2NTklMkZQWlF6QzhEJTJGdkU3OFVYTXQyQ0JBS2xGVzFMTTlJSmFxV3hRUUx2NXV6QXVTRVF5eTgyS0NGZ1pDcGZQN1l2UTJ5M1FLMlRGbiUyQmF6UkM5aU9UUzZZQTdsMDkxZWclM0QlM0Q; RT="z=1&dm=www.fanatics.com&si=0911c64e-fded-4c00-bbc5-42b0ec6aa5b4&ss=li8ge4xo&sl=d&tt=2f61&bcn=%2F%2F684d0d47.akstat.io%2F&ld=20a7a&ul=20rvj"; _4c_=%7B%22_4c_s_%22%3A%22fVTbbtswDP2Vwg99qmPLki8KUAxJ2mEd2rpN0u0x8IWJjdqSIcnNsiL%2FPsmXtGuH%2BcU6h4ekSIl6tfYFMGuKgsjHhKAo8ILwwnqGg7Smr5Yoc%2FN7saZW5LlpiHBqAyWpTYDmduRBZiOabXFEEfHz0LqwfplYFCMUhBRT4h4vrKwZYrxaGc9Bx0J0gsgEYXsrtYv6rSniuXrZCJ63mdqoQ2N0e0jPZP6sDTm8lBls9mWuii5AJx%2FYAspdoQztRh3dCAP0al%2BynO8%2Fug3syY16VLOp4HsJxnNRCF7DGUJY01w3wvrZeZjNCtiCEJ1MI1kqs89twhJVZnKS8XpgdQc%2FG%2BK79XIzv54t4nttLJRq5NRxTiKEvInHwwkD5aSOlCeLrtNBzveVjSaBI11P95v6mAY%2BpejL7HF%2Bic63ZX7p4rkXzkOMI0SjGfVsTPwZnl8hT%2FN%2BiBbns8frS9OXW0h2LcRiDUn90IqsSCTkfUmxyEHcXL0DP5KqhR4%2FJDtY92dj0GrULUG1gpVst2il0r0T72MpqBe8Zarn7ts67UlZskUiDH2vebMcMxl8LQQXdyClTjlQ37hULKlHeMMUCJZUK0h0BWsQ9WDoqxsB3%2B0gv2ED7LeUD8jUs3w70ZF6Wt6e0KEGpu5AFfzkVCUsbtVsPmJ9W7gqOYvZqr8PhpUbfSRfSyHVg66sa5ShV7oiLX3DRdk0pnGmQ%2BLwgf0rrzmsYfnUSKiquDFZr0rZVMkBRlljphURvap4llRmP3rCj8NoRj7Brh94HiF68lRlTaOAuOY79q7dpCLySY4%2Fy%2FuJscdbagP7X4B%2F5JNSjfru%2FXHNm%2BH7H18R3z8ej38A%22%7D; AWSALB=zNcq3ltVfy7m6iwrfhUx4fRa9OjRCN685ZUpyCcPM3+cq8tT7okyqFgTJzasFS8d0lur+u1FZ4jqDuwErKriWSFX11U1cotetSd/iNKqVnW4GPLGEi+0EwiBPimD; AWSALBCORS=zNcq3ltVfy7m6iwrfhUx4fRa9OjRCN685ZUpyCcPM3+cq8tT7okyqFgTJzasFS8d0lur+u1FZ4jqDuwErKriWSFX11U1cotetSd/iNKqVnW4GPLGEi+0EwiBPimD; _s=www.fanatics.com; ac=USD; cqe=%5B%2210129%3AA%3A0%3A1%22%2C%2210287%3AB%3A1%3A1%22%2C%2210299%3AB%3A1%3A1%22%2C%2210318%3AA%3A0%3A1%22%5D; mc=; priv=%7B%22acc%22%3Afalse%2C%22fcc%22%3Afalse%2C%22tcc%22%3Afalse%2C%22pc%22%3Atrue%2C%22ecc%22%3Afalse%7D; st=510005; u_loc=en-US; uc=USD; vrc=af4e95cb8be63aaf; xsrfp=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyZXFIb3N0Ijoid3d3LmZhbmF0aWNzLmNvbSIsInZpc2l0b3JJZCI6ImUzYTY5MDEwLWZkZTctMTFlZC1iMjc2LWUzMGQzMTVkNGFkMyIsImlhdCI6MTY4NTM0NDMzOSwiZXhwIjoxNjg3MDI5Mzg0MjA0fQ.h43t1GJzd1Cf4QoJFqcEbkh8YtqQb7srXze2PG23OE8; xsrft=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyZXFIb3N0Ijoid3d3LmZhbmF0aWNzLmNvbSIsInZpc2l0b3JJZCI6ImUzYTY5MDEwLWZkZTctMTFlZC1iMjc2LWUzMGQzMTVkNGFkMyIsImlhdCI6MTY4NTM0NDMzOSwiZXhwIjoxNjg3MDI5Mzg0MjA0fQ.RsH0jme8blneFqaJAD_4kHT8S6uZD_Esoa3_bzCsfSY',
    'referer': 'https://www.fanatics.com/college/fairleigh-dickinson-florham-devils/o-38+t-4544645669+z-94411-3369440334',
    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1'
  }

  response = requests.request("GET", url, headers=headers, data=payload).text

  regex = r"(?<=addAllPageVariables\().+?(?=\);triggerOmniture\(\))"

  test_str = response

  matches = re.finditer(regex, test_str, re.MULTILINE)

  for matchNum, match in enumerate(matches, start=1):

      print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))

      for groupNum in range(0, len(match.groups())):
          groupNum = groupNum + 1

          print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

link ='https://www.fanatics.com/college/fdu-florham-devils/fdu-florham-devils-under-armour-primary-performance-t-shirt-navy/o-27+t-90619533+p-265044582190+z-9-4291043011?_ref=p-TLP:m-GRID:i-r0c1:po-1'
cralwDetail(link)