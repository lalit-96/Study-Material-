FROM continuumio/anaconda3:4.4.0
MAINTAINER UNP, https://unp.education
COPY ./flask_demo C:/Users/myapp
EXPOSE 5000
WORKDIR C:/Users/myapp
RUN pip install -r requirements.txt
CMD python flask_predict_api.py
