# PROMPT_FOR_ANY_AI — Celentrail (ZERO QUESTIONS CONTRACT)

Ты работаешь ТОЛЬКО по этому репозиторию Celentrail. Репозиторий — единственный источник правды.

## SOURCE OF TRUTH (машинный контекст)
1) `data/AI_CONTEXT.json` — главный источник размеров/углов/массы/материалов/дефолтов
2) `CANONICAL.md` — каноническое описание системы
3) Файлы узлов в корне репозитория:
   - `00_MASTER_CONTEXT.md`
   - `01_SYSTEM_OVERVIEW.md`
   - `10_BALKA.md`
   - `20_TROLLEY.md`
   - `30_TRACK_AND_ROLLERS.md`
   - `40_LOADS_AND_TARGETS.md`

## ZERO QUESTIONS CONTRACT
- Запрещено задавать вопросы про размеры/массу/углы/геометрию/материалы.
- Если параметра нет в `data/AI_CONTEXT.json` — НЕ спрашивай пользователя.
- Используй `DEFAULTS_IF_NOT_SPECIFIED` из JSON.
- Любой отсутствующий параметр добавляй списком в конце ответа:
  `MISSING_TO_ADD_TO_AI_CONTEXT.json`

## Разрешены только 2 вопроса пользователю
1) “что посчитать/сравнить?”
2) “что изменить (какой параметр/узел)?”

## Обязательный алгоритм ответа
1) Загрузи `data/AI_CONTEXT.json`
2) Выполни задачу, используя данные репозитория
3) В конце выведи `MISSING_TO_ADD_TO_AI_CONTEXT.json`
