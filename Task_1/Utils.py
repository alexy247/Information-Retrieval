
def parse_text(text):
    if not text:
        return ''
    result = ' '
    for t in text:
        result = result + " " + t.text
    return result


def parse_tags(tags, DATA_TAG):
    if not tags:
        return []
    result = []
    for tag in tags:
        tag_data = tag.attrs.get(DATA_TAG)
        if tag_data:
            result.append(tag.attrs[DATA_TAG])
    return result

# Сохранило 988 человек
def parse_saves(saves_str):
    splitted = saves_str.split(" ")
    if len(splitted) == 3:
        try:
            return int(splitted[1])
        except ValueError:
            return None

# 169368 просмотров
def parse_views(views_str, DATA_AUTHOR_ID):
    splitted = views_str.split(" ")
    if len(splitted) == 2:
        try:
            return int(splitted[0])
        except ValueError:
            return None

# Реклама?
def is_ads(attr, DATA_AUTHOR_ID):
    return attr.get(DATA_AUTHOR_ID) is None