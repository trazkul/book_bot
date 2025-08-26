import logging
from pathlib import Path

path = Path('book') / 'book.txt'

logger = logging.getLogger(__name__)

def _get_part_text(text: str, start: int, page_size: int) -> tuple[str, int]:
    end = start + page_size
    part = text[start:end]

    punct = {'.', ',', '!', '?', ':', ';'}
    last_safe_end = -1
    i = 0

    while i < len(part):
        ch = part[i]
        if ch in punct:
            # 1) Вычисляем ПОЛНУЮ длину последовательности пунктуации в исходном тексте
            seq_start_in_text = start + i
            j = seq_start_in_text
            while j < len(text) and text[j] in punct:
                j += 1
            full_seq_len = j - seq_start_in_text   # напр., для '...' это 3

            # 2) Проверяем, влезает ли вся последовательность в окно
            if i + full_seq_len <= len(part):
                # ВЛЕЗАЕТ → принимаем целиком как корректный конец
                last_safe_end = i + full_seq_len - 1
                i += full_seq_len                  # перепрыгиваем всю последовательность
                continue
            else:
                # НЕ ВЛЕЗАЕТ → НЕ трогаем last_safe_end (откатываемся к прежнему безопасному)
                # просто двигаемся дальше по окну, не принимая обрубок ('..' из '...')
                pass
        i += 1

    page_text = part[: last_safe_end + 1]
    page_len  = len(page_text)
    return page_text, page_len

def prepare_book(path: str, page_size: int = 1050) -> dict[int, str]:
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()

    book = {}
    start = 0
    page_num = 1

    while start < len(text):
        page_text, length = _get_part_text(text, start, page_size)

        if length == 0:  # фолбэк, чтобы не зависнуть
            page_text = text[start:start + page_size]
            length = len(page_text)

        book[page_num] = page_text.lstrip()
        start += length
        page_num += 1

    return book