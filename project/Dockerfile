FROM python:3.12-alpine

ARG usergroup=paradox
ARG username=paradox

# Create a group and user
RUN addgroup -S $usergroup && adduser -S ${username} -G ${usergroup}

# Tell docker that all future commands should run as the appuser user
USER ${username}

RUN mkdir ~/.local/bin -p
RUN echo "export PATH=$PATH:/home/${username}/.local/bin" >> ~/.bashrc

WORKDIR /home/${username}/project

COPY . .


RUN pip install --upgrade pip && pip install -r requirements.txt

ENTRYPOINT [ "sh", "run.sh" ]