[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/github_username/repo">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">MBO LINE Bot</h3>

  <p align="center">
    A LINE Bot to help you do managements by objects
    <br />
    <br />
    <a href="https://github.com/dextermallo/MBO-Line-Bot/issues">Report Bug</a>
    ·
    <a href="https://github.com/dextermallo/MBO-Line-Bot/issues">Request Feature</a>
  </p>
</p>

<!-- Content -->
# Requirements
1. AWS Account ([Register here](https://portal.aws.amazon.com/billing/signup#/start))
> We Will Use **AWS lambda** and **DynamoDB**
2. LINE Offical Account ([Register here](https://account.line.biz/login?redirectUri=https%3A%2F%2Fmanager.line.biz%2F))  
> You have to also connect LINE Offical Account **with a LINE account** to use Message API.

3. Install Serverless ([See me to install with npm](https://www.npmjs.com/package/serverless)). 
> More about Serverless [here](https://www.serverless.com/)  

# Deployment
1. Clone this repo.
```shell
  $ git clone https://github.com/dextermallo/MBO-Line-Bot.git. 
```

2. Generate a LINE Bot: Remember your **Channel Access Token** and **Channel Secret**

![Alt text](/images/readme/01.png "Channel Access Token")

<p align="center">
<i>(Channel Access Token)</i>
</p>

![Alt text](/images/readme/02.png "Channel Secret")

<p align="center">
<i>(Channel Secret)</i>
</p>

3. Create a dynamoDB in AWS: Remember your **url**

![Alt text](/images/readme/04.png "ARN")

<p align="center">
<i>(Amazon Resource Name)</i>
</p>

4. Make a file in root directory called **.env** for **sensitive keys loading**
  ```markdown
    LINE_CHANNEL_ACCESS_TOKEN=<Your LINE Channel Access Token>
    LINE_CHANNEL_SECRET=<Your LINE Channel Secret>
    DYNAMODB_URL=<Your DyanmoDB URL>
  ```

  or you can also run script below:
  ```shell
    $ source script/env_file_generator.sh
  ```

5. Set your AWS key for global environment, or you can also run script below to set temporary key:
```shell
  $ source script/set_aws_key.sh
```

6. Deploy!
```shell
  $sls deploy
```

7. Set your LINE Bot Webhook url

![Alt text](/images/readme/03.png "Webhook")

<p align="center">
<i>(Amazon Resource Name)</i>
</p>

8. Done! Now you can try to talk with your LINE Bot 🐥

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[stars-shield]: https://img.shields.io/github/stars/dextermallo/MBO-Line-Bot.svg?style=flat-square
[stars-url]: https://github.com/dextermallo/MBO-Line-Bot/stargazers
[issues-shield]: https://img.shields.io/github/issues/dextermallo/MBO-Line-Bot.svg?style=flat-square
[issues-url]: https://github.com/dextermallo/MBO-Line-Bot/issues
[license-shield]: https://img.shields.io/github/license/dextermallo/MBO-Line-Bot.svg?style=flat-square
[license-url]: https://github.com/dextermallo/MBO-Line-Bot/blob/master/LICENSE