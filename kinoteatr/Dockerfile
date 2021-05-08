FROM python:3.9.4-alpine

WORKDIR /usr/src/kinoteatr

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN apk add --update --no-cache tiff-dev jpeg-dev openjpeg-dev zlib-dev freetype-dev lcms2-dev \
libwebp-dev tcl-dev tk-dev harfbuzz-dev fribidi-dev libimagequant-dev libxcb-dev libpng-dev \
gcc build-base freetype-dev libpng-dev openblas-dev \
postgresql-dev gcc python3-dev musl-dev


RUN pip install --upgrade pip
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .