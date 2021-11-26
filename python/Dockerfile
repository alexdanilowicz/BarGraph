FROM python:3.7

# run this before copying requirements for cache efficiency
RUN pip install --upgrade pip

#set work directory early so remaining paths can be relative
WORKDIR /app

# Adding requirements file to current directory
# just this file first to cache the pip install step when code changes
COPY requirements.txt .

#install dependencies
RUN pip install -r requirements.txt

# copy code itself from context to image
COPY . .

CMD ["python", "./main.py", "--force"]