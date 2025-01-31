celery -A app.api.search.celery.tasks worker --loglevel=info

The trigger of postgresql

CREATE OR REPLACE FUNCTION update_search_vector()
RETURNS TRIGGER AS $$
DECLARE
  words TEXT[];
  word TEXT;
  prefixes TEXT[];
  prefix TEXT;
  stemmed_words TEXT[];
BEGIN
  -- Разбиваем текст на слова и очищаем его
  words := regexp_split_to_array(
    regexp_replace(
      CONCAT_WS(' ', NEW.name, NEW.description, NEW.house_number), 
      '[^A-Za-zА-Яа-я0-9 ]', '', 'g'
    ), 
    '\s+'
  );

  prefixes := '{}';

  -- Генерируем n-граммы + стемминг
  FOREACH word IN ARRAY words LOOP
    -- Приведение слова к основе (стемминг)
    SELECT ARRAY(SELECT unnest(ts_lexize('russian_stem', word)) LIMIT 1) 
    INTO stemmed_words;
    
    IF stemmed_words IS NULL OR array_length(stemmed_words, 1) = 0 THEN
      stemmed_words := ARRAY[word]; -- Если стемминг не найден, оставляем слово как есть
    END IF;

    -- Добавляем стеммированные слова и n-граммы
    FOREACH word IN ARRAY stemmed_words LOOP
      FOR i IN 1 .. length(word) LOOP
        prefix := substr(word, 1, i);
        prefixes := array_append(prefixes, prefix);
      END LOOP;
    END LOOP;
  END LOOP;

  -- Записываем в search_vector
  NEW.search_vector := to_tsvector('russian', array_to_string(prefixes, ' '));

  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_update_search_vector
BEFORE INSERT OR UPDATE ON houses
FOR EACH ROW
EXECUTE FUNCTION update_search_vector();




