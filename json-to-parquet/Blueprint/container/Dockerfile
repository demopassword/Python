FROM public.ecr.aws/lambda/python:3.8
COPY app.py .
RUN pip3 install pandas && pip3 install pyarrow
CMD ["app.lambda_handler"]