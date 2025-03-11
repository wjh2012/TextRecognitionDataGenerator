import random as rnd
import string
from typing import List

import wikipedia


def create_strings_from_file(filename: str, count: int) -> List[str]:
    """
    Create all strings by reading lines in specified files
    """

    strings = []

    with open(filename, "r", encoding="utf8") as f:
        lines = [l[0:200] for l in f.read().splitlines() if len(l) > 0]
        if len(lines) == 0:
            raise Exception("No lines could be read in file")
        while len(strings) < count:
            if len(lines) >= count - len(strings):
                strings.extend(lines[0 : count - len(strings)])
            else:
                strings.extend(lines)

    return strings


def create_strings_from_dict(
    length: int, allow_variable: bool, count: int, lang_dict: List[str]
) -> List[str]:
    """
    Create all strings by picking X random word in the dictionary
    """

    dict_len = len(lang_dict)
    strings = []
    for _ in range(0, count):
        current_string = ""
        for _ in range(0, rnd.randint(1, length) if allow_variable else length):
            current_string += lang_dict[rnd.randrange(dict_len)]
            current_string += " "
        strings.append(current_string[:-1])
    return strings


def get_random_page_content() -> str:
    page_title = wikipedia.random(1)
    try:
        page_content = wikipedia.page(page_title).summary
    except (wikipedia.DisambiguationError, wikipedia.PageError):
        return get_random_page_content()
    return page_content


def create_strings_from_wikipedia(
    minimum_length: int, count: int, lang: str
) -> List[str]:
    """
    Create all string by randomly picking Wikipedia articles and taking sentences from them.
    """
    wikipedia.set_lang(lang)
    sentences = []

    while len(sentences) < count:
        page_content = get_random_page_content()
        processed_content = page_content.replace("\n", " ").split(". ")
        sentence_candidates = [
            s.strip() for s in processed_content if len(s.split()) > minimum_length
        ]
        sentences.extend(sentence_candidates)

    return sentences[0:count]


def create_strings_randomly(
    length: int,
    allow_variable: bool,
    count: int,
    let: bool,
    num: bool,
    sym: bool,
    lang: str,
) -> List[str]:
    """
    Create all strings by randomly sampling from a pool of characters.
    """

    # If none specified, use all three
    if True not in (let, num, sym):
        let, num, sym = True, True, True

    pool = ""
    if let:
        if lang == "cn":
            pool += "".join(
                [chr(i) for i in range(19968, 40908)]
            )  # Unicode range of CHK characters
        elif lang == "ja":
            pool += "".join(
                [chr(i) for i in range(12288, 12351)]
            )  # unicode range for japanese-style punctuation
            pool += "".join(
                [chr(i) for i in range(12352, 12447)]
            )  # unicode range for Hiragana
            pool += "".join(
                [chr(i) for i in range(12448, 12543)]
            )  # unicode range for Katakana
            pool += "".join(
                [chr(i) for i in range(65280, 65519)]
            )  # unicode range for Full-width roman characters and half-width katakana
            pool += "".join(
                [chr(i) for i in range(19968, 40908)]
            )  # unicode range for common and uncommon kanji
            # https://stackoverflow.com/questions/19899554/unicode-range-for-japanese
        elif lang=="mc":
            pool += "".join(
                [chr(i) for i in range(65, 68)]
            )
        elif lang=="ko":
            hangul_2350 = "가각간갇갈감갑값갓강개객갱갹거건걸검겁것게겨격결경계고곡곤골공과광괴굉교구국군굴궁권귀규균그극근글금급기긴길김까깎깐깔깜깝깨꺾껌껑껏껐껑껒껓꼬꼭꽂꽃꾀꿀꿇꿈끈끌끓끝끼낀낄낌나난날남납낭낮내냄냇냉너넌널넘넣네넷녀년념렵령례로록론롤료룡루류르른름릉리린림립마막만많말맘망맞맡매맥맨맬맴맹머먹먼멋메며멱면멸명모목몬몰몸못무문물미민믿밀빛빠빨빼뻗뻘뽀뿌쁘삐사삭산살삼삽상새색생서석선설섬섭성세센셔소속손솔솜송수숙순술숨숫숲쉬스슨슬슴습승시식신실심싫싯싱싶싸싹쌀쏘쑤쓰쓴쓸씌씨씩신싶쌀씨쑥아악안알암앞애액야약얄양어억언얼엄업없에여역연열염엽영예오옥온올옴옷완왕왜외요욕용우욱운울움웅원월위유육윤율융으은을음읍응의이익인일임입잉자작잔잘잠잡장재잴쟁저적전절점접정제젯젯조족존졸좁종좋주죽준줄중즉즐증지직진질짐집짝쪽쫓찜차착찬찰참찹창채책처척천철첨첩청체초촉촌총최추축춘출충취측층치칙친칠침칩칭카칸칼캄캡캐컸커컨컬컴컵케켜코콘콜콤콩쾌쾡쿠쿡쿤쿨쿵크큰클큼키킨킬킴타탁탄탈탐탑탕태택터턱턴털텀텁테텍텐텔토통퇴투툭툴퉁트특틈티틱팀파판팔팝패퍼편펼평폐포폭표푸풀풍피픽핀필품핏하학한할함합항해햄허헌험혁현혈협형혜호혹혼홀홍화확환활황회효후훈훌훔훤휘휴휼흉흐흑흔흘흠흥희히힘"
            pool += string.ascii_letters + string.digits + string.punctuation  # 영어 + 숫자 + 특수문자
            pool += hangul_2350
        else:
            pool += string.ascii_letters
    if num:
        pool += "0123456789*,."
    if sym:
        pool += "!\"#$%&'()*+,-./:;?@[\\]^_`{|}~"

    if lang == "cn":
        min_seq_len = 1
        max_seq_len = 2
    elif lang == "ja":
        min_seq_len = 1
        max_seq_len = 2
    else:
        min_seq_len = 2
        max_seq_len = 10

    strings = []
    for _ in range(0, count):
        current_string = ""
        for _ in range(0, rnd.randint(1, length) if allow_variable else length):
            seq_len = rnd.randint(min_seq_len, max_seq_len)
            current_string += "".join([rnd.choice(pool) for _ in range(seq_len)])
            current_string += " "
        strings.append(current_string[:-1])
    return strings
