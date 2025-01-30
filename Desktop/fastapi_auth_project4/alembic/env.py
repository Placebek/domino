from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

# Импортируем Base и модели
from app.database import Base  # Убедитесь, что путь правильный
from app.models import User, Seller  # Импортируем модели

# Получаем объект конфигурации Alembic
config = context.config

# Настройка логирования (по умолчанию)
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Устанавливаем target_metadata для автогенерации миграций
target_metadata = Base.metadata  # Это позволяет Alembic работать с вашими моделями

def run_migrations_offline() -> None:
    """Запуск миграций в режиме 'offline'."""
    url = config.get_main_option("sqlalchemy.url")  # Получаем URL из конфигурации
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Запуск миграций в режиме 'online'."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


# Определение режима работы (offline или online)
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
