import csv
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CNS11643.settings')
django.setup()
from word_api.models import CharMap

# with open('CNS2UNICODE_Unicode BMP.txt', 'r', encoding='utf-8') as f:
#     reader = csv.reader(f, delimiter='\t')
#     for row in reader:
#         cns, unicode = row
#         character = CharMap(cns_code=cns, unicode_code=unicode)

with open('CNS2BIG5.txt', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        cns, big5 = row
        CharMap.objects.filter(cns_code=cns).update(big5_code=big5)
