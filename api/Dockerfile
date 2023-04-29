FROM python:3.11.2-slim-buster AS base

LABEL maintainer="Yulia Panaseiko <nishtayulia@gmail.com>"

# стоврення користувача, який не є рутом

ARG UID=1000
ARG GID=1000
ENV UID=${UID}
ENV GID=${GID}
# сворюємо користувача з ім'м docker_user, який не є рутом, і його UID за
# замовченням буде 1000 (раніше тут було ARG UID=1000 ENV UID=${UID}), він може бути
# замінений при старті контейнера передачою змінної або в файлі docker-compose.yaml
# або як аргумент команди docker
RUN useradd -m -u $UID docker_user
USER docker_user

# Инициализация проекта
WORKDIR /home/docker_user/app

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
COPY requirements.txt ./
RUN  pip install -r requirements.txt
COPY . .
CMD ["python3", "-m", "main"]