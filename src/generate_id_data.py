from itertools import count
import os
import string
import random
from trdg.generators import (
    GeneratorFromStrings
)

id_count = 1000
issue_count = 400

ids = [random.choice( string.ascii_uppercase) + "".join(random.choices(string.octdigits, k=9)) for _ in range(id_count)]
city_texts = ["(北縣)", "(宜縣)", "(桃縣)", " (竹縣)", "(苗縣)", "(中縣)", "(彰縣)", "(投縣)", "(雲縣)", "(嘉縣)", "(南縣)", "(高縣)", "(屏縣)", "(東縣)", "(花縣)", "(澎縣)", "(基市)", "(竹市)", "(嘉市)", "(連江)", "(金門)", "(北市)", "(高市)", "(新北市)", "(中市)", "(南市)", "(桃市)"]

issue_type_texts = ["初發", "補發", "換發"]

year_texts = [f"{i}年" for i in range(90,120)]

month_texts = [f"{i}月" for i in range(1,13)]

day_texts = [f"{i}日" for i in range(1,32)]

combine_issue_texts = [f"民國{random.choice(year_texts)}{random.choice(month_texts)}{random.choice(day_texts)} {random.choice(city_texts)} {random.choice(issue_type_texts)}" for _ in range(issue_count)]

# The generators use the same arguments as the CLI, only as parameters
id_generator = GeneratorFromStrings(
    ids,
    count=id_count,
    blur=1,
    skewing_angle=5,
    random_blur=True,
    random_skew=True,
    fonts=["data/fonts/kaiu.ttf"]
)

os.makedirs("data/id_card_id_only/images", exist_ok=True)

with open("data/id_card_id_only/lexicon.txt","w",encoding="utf8") as f,open("data/id_card_id_only/annotation_train.txt","w",encoding="utf8") as f1,open("data/id_card_id_only/annotation_test.txt","w",encoding="utf8") as f2,open("data/id_card_id_only/annotation_val.txt","w",encoding="utf8") as f3 :
    ind = 0
    for i, (img, lbl) in enumerate(id_generator):        
        filepath = f"images/id_{i}.png"
        img.save(os.path.join('data/id_card_id_only',filepath))
        f.write(f"{lbl}\n")
        ratio = i / id_count 
        if ratio <= 0.7:
          f1.write(f"{filepath} {ind}\n")
        elif ratio > 0.7 and ratio<=0.85:
          f2.write(f"{filepath} {ind}\n")
        else:
          f3.write(f"{filepath} {ind}\n")
        ind+=1

os.makedirs("data/id_card_issue_only/images", exist_ok=True)

issue_generator = GeneratorFromStrings(
    combine_issue_texts,
    count=issue_count,
    blur=1,
    skewing_angle=5,
    random_blur=True,
    random_skew=True,
    language="cn",
    fonts=["data/fonts/PMingLiU-02.ttf"]
)

with open("data/id_card_issue_only/lexicon.txt","w",encoding="utf8") as f,open("data/id_card_issue_only/annotation_train.txt","w",encoding="utf8") as f1,open("data/id_card_issue_only/annotation_test.txt","w",encoding="utf8") as f2,open("data/id_card_issue_only/annotation_val.txt","w",encoding="utf8") as f3 :
    ind = 0
    for i, (img, lbl) in enumerate(issue_generator):
        filepath = f"images/issue_{i}.png"
        img.save(os.path.join('data/id_card_issue_only',filepath))
        f.write("%s\n" % lbl)
        ratio = i / issue_count 
        if ratio <= 0.7:
          f1.write(f"{filepath} {ind}\n")
        elif ratio > 0.7 and ratio<=0.85:
          f2.write(f"{filepath} {ind}\n")
        else:
          f3.write(f"{filepath} {ind}\n")
        ind+=1