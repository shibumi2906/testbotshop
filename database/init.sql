-- init.sql

-- Создаем расширение для поддержки UUID, если оно еще не установлено.
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Создаем базу данных (если необходимо).
CREATE DATABASE testbotshop_db;

-- Создаем схему, если требуется определенная структура.
CREATE SCHEMA IF NOT EXISTS public;

-- Пример создания таблицы (для тестирования, если нужно).
-- В реальном проекте создание таблиц лучше выполнять через миграции Django.
CREATE TABLE IF NOT EXISTS sample_table (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Пример вставки тестовых данных.
-- Эти данные можно удалить после запуска.
INSERT INTO sample_table (name) VALUES ('Test Data 1'), ('Test Data 2');

-- Добавляем роли или пользователя (если нужно).
-- В реальном проекте обычно пользователи и роли задаются через docker-compose.yml.
DO
$$
BEGIN
    IF NOT EXISTS (
        SELECT FROM pg_catalog.pg_roles WHERE rolname = 'your_db_user'
    ) THEN
        CREATE ROLE your_db_user LOGIN PASSWORD 'your_db_password';
        GRANT ALL PRIVILEGES ON DATABASE testbotshop_db TO your_db_user;
    END IF;
END
$$;
