FROM node:20.9.0-alpine as build

WORKDIR /app

# Копируем package.json для установки зависимостей
COPY package*.json ./

# Устанавливаем зависимости с использованием npm ci
RUN npm ci

# Копируем остальные файлы проекта
COPY . .

# Устанавливаем переменную окружения для увеличения памяти
ENV NODE_OPTIONS="--max-old-space-size=4096"

# Выполняем сборку проекта
RUN npm run build

# Копируем результат сборки в папку для дальнейшего использования
CMD cp -r build result_build
