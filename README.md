celery -A app.api.search.celery.tasks worker --loglevel=info

The trigger of postgresql

CREATE OR REPLACE FUNCTION update_search_vector()
RETURNS TRIGGER AS $$
BEGIN
  NEW.search_vector := to_tsvector('russian', 
    CONCAT_WS(' ', 
              regexp_replace(NEW.name, '[^A-Za-zА-Яа-я0-9 ]', '', 'g'),
              regexp_replace(NEW.description, '[^A-Za-zА-Яа-я0-9 ]', '', 'g'),
              regexp_replace(NEW.house_number, '[^A-Za-zА-Яа-я0-9 ]', '', 'g')
    )
  );
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_update_search_vector
BEFORE INSERT OR UPDATE ON houses
FOR EACH ROW
EXECUTE FUNCTION update_search_vector();

CREATE TRIGGER trg_update_search_vector
BEFORE INSERT OR UPDATE ON houses
FOR EACH ROW
EXECUTE FUNCTION update_search_vector();
