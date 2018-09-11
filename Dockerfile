FROM ubuntu:18.04
ENV PYTHONUNBUFFERED 1
RUN ln -fs /usr/share/zoneinfo/Europe/Paris /etc/localtime
ENV LANG C.UTF-8
RUN apt update && apt install -y python3.6 python3-pip make texlive-latex-base texlive-luatex texlive-lang-french texlive-latex-extra texlive-fonts-recommended texlive-xetex texlive-font-utils
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip3 install -r requirements.txt
ADD . /code/
EXPOSE 8000
WORKDIR /code/project
RUN python3 manage.py migrate
CMD python3 manage.py runserver 0.0.0.0:8000
