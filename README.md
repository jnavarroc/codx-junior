# codx-junior
Your junior assistant for Full Stack Developers

## Motivation

As a Full Stack Developer, we are supposed to deal with everything, know everything, and fix everything—from front, to back, to database, cloud, DevOps... and I like it, but it's a titan task. I'm developing codx-junior to have an AI that can manage all tedious and repetitive tasks in software development and IT. I want codx-junior to help me deal with projects I don't know and situations where "the last developer left yesterday and there's no doc." I want codx-junior to write better code than me, better tests than me, and, of course, keep documentation updated.

![image](https://github.com/user-attachments/assets/29123838-1b1b-44c6-a92a-c28968238385)


## PNRL: Play now read later

Default setup will run a docker container with codx-junior and will map codx-junior repor parent's path to connect with host's projects. 

### dev environment

#### docker
```sh
  git clone https://github.com/gbrian/codx-junior.git
  cd codx-junior
  # change `.env.dev` as needed
  # Set HOST_PROJECTS_ROOT_PATH to yor host project's path
  ########################################### 
  ## It's important have same path between 
  ## host project's and container 
  ###########################################
  HOST_PROJECTS_ROOT_PATH="$(dirname $PWD)" \
  HOST_USER="$(id -u):$(id -g)" \
  docker-compose -f docker-compose.dev.yaml up -d
```

#### bash
```sh
  git clone https://github.com/gbrian/codx-junior.git
  cd codx-junior
  # change `.env.dev` as needed
  source .env.dev
  bash installer.sh
  bash run_client.sh &
  bash run_api.sh &
```

After you should be able to access codx-junior at: 
http://localhost:9983


## Features

### Tasks

### Knowledge

### Mentions

Mentions allow you to reference specific parts of your project or codebase for easier management and collaboration. Below is a demonstration video on how to use mentions effectively:

[![YouTube](http://i.ytimg.com/vi/CDZzE4Ea6DA/hqdefault.jpg)](https://www.youtube.com/watch?v=CDZzE4Ea6DA)





To use mentions, simply include the `@codx-processing` tag followed by the specific instruction or note you want to add. For example:
```markdown
@codx-processing: --knowledge @codx-junior-api Add a link to webm video from "assets/codx_mentions_demo.webm". And explain about mentions and how to use it
```
This will notify the system to process the mention and make the necessary changes or additions.

### Code generation
Ofc... we are here for this :)

### Codebase knowledge
codx-junior uses RAG techniques to find revelant parts of the code for your tasks or giving support

### Task managent
codx-junior is task based. Create task and polish it with codx-junior until your are ready to generate code

### Chat & Support
Talk with codx-junior to learn about the code base, find ways to improve your code or learn new skills

### Wiki
Don't write more documentation, codx-junior will do for you

### Personalize
Define how do you want codx-junior to perform, code styling, ...

```           _                 _   _             
          (_)               | | (_)            
 _ __ ___  _  __ _ _ __ __ _| |_ _ _ __   __ _ 
| '_ ` _ \| |/ _` | '__/ _` | __| | '_ \ / _` |
| | | | | | | (_| | | | (_| | |_| | | | | (_| |
|_| |_| |_|_|\__, |_|  \__,_|\__|_|_| |_|\__, |
              __/ |                       __/ |
             |___/                       |___/ 
```
This project come from my fork of https://github.com/gpt-engineer-org/gpt-engineer - such a great project! ❤️- ...but that work was never merged to main branch because I followed different approach and ended up rewriting everything. Please try gpt-engineer as well, worth it!

Nowadays codx branch has nothing in common with gpt-enginner master so it's time to create a new project for it.