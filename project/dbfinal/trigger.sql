create or replace function new_model()
returns trigger
language plpgsql
    as
    $$
begin
    if new.model_id = old.model_id and new.model_name = old.model_name then
        raise notice 'Model exists';
    end if;
    raise notice 'Done';
    return new;
end;$$;

create trigger
    model_creation
    before update
    on model
    for each row
    execute procedure new_model();

update model
set model_name='Model Hayabusa'
where model_id=2001;


create or replace function new_region()
returns trigger
language plpgsql
    as
    $$
begin
    if new.region_name is NULL then
        raise exception 'Region cant be empty';
        end if;
    return new;
end;$$;

create trigger
    region_trigger
    after update
    on region
    for each statement
    execute procedure new_region();

update region
set region_name = ''
where region_id = 11;

