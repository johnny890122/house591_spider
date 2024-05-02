FROM public.ecr.aws/lambda/python:3.11

COPY requirements.txt ./
RUN python3.11 -m pip install -r requirements.txt -t .

COPY main.py utils.py house591_spider.py ./

CMD ["main.lambda_handler"]
