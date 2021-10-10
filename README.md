<p align="center">
  <img src="https://github.com/igudesman/linkbrary/blob/master/logos/linkbrary_logo_with_text.png" />
</p>

# Linkbrary Bot #
![Tests Passing](https://github.com/igudesman/linkbrary/actions/workflows/test-github-actions.yml/badge.svg)
[![Telegram Bot](https://img.shields.io/badge/bot-%20%20on%20Telegram-2ba2d9.svg)](https://t.me/linkbrary_bot)

Welcome to **Linkbrary Bot** project!

Want to collect all your links, articles and videos in one place for future reading? Try out **Linkbrary**!

Linkbrary helps you to collect links and videos you want to go through later in one place. As easy as sending link to the bot.
Have time for reading? Just ask the bot - it will send you random link! Or specify topic, estimated time of difficulty to get what you want!

## Table of Contents
* [Demo](#demo)
* [Features](#features)
* [Technology Stack](#technology-stack)
* [Code Best Practices](#code-best-practices)
* [Materials for SSAD Course](#materials-for-ssad-course)
* [Credits](#credits)

## Demo <a name="demo"></a>
![til](https://github.com/igudesman/linkbrary/blob/master/demo/demoLinkbrary.gif)

## Features <a name="features"></a>
* Universal link storage accessible from any platform
* Automatic links tagging
* Automatic time to read/view estimation
* Getting random unread links

## Technology Stack <a name="technology-stack"></a>
* TelegramAPI
* Python
* MongoDB

## Code Best Practices <a name="code-best-practices"></a>
1. SOLID Principles:
    * **Single Responsibility Principle**
    
      The principle of single duty requires that one class does only one job. Thus, if a class has more than one job, it becomes dependent. Changing the behavior of one class job leads to a change in another. Link Analyzer is an example of such a class.
    * **Liskov Substitution Principle**
    
      The main idea behind the Liskov Substitution Principle is that for any class, the client should be able to use any subclass of the base class without noticing the        difference between them, and therefore without any changes in the behavior of the program during execution. This means that the client is completely isolated and unaware of  changes in the class hierarchy. For example, we used InvalidUrl, which inherits from BaseException and uses all its methods.
    * **Interface Segregation Principle**
    
      Create thin interfaces that are customer-centric. Clients should not depend on interfaces that they do not use. This principle eliminates the disadvantages of implementing   large interfaces. An example in our project is the Analyzer interface.

2. Using Linter:
<img src="https://github.com/igudesman/linkbrary/blob/master/demo/pylint.png" />
We use Pylint that is a plugin of PyCharm. We have a small amount of warnings, which is fine; but a lot of conventions notice - this is due to tests and import issues that we did not manage to overcome. We will shortly try to conform all conventions practices so that our code looks nice.

3. Using PyTest:
<img src="https://github.com/igudesman/linkbrary/blob/master/demo/pytest-coverage.png" />
We set up PyTest with GitHub Actions (you can see badge above), and managed to provide very high coverage. Our next step in testing our product is setting up not only class tests, but interactions tests, where interaction with bot could be fully simulated. However, this requires some cloud environemnts setup and API keys safe management, which was out of this MVP scope.

## Materials for SSAD Course <a name="materials-for-ssad-course"></a>
* [RUP Artifact](https://docs.google.com/document/d/1NvzGc7YgpdCWJnEomHVriLlVA9wztOa5/edit?usp=sharing&ouid=106934281615236387751&rtpof=true&sd=true)
* [Diagrams](https://github.com/igudesman/linkbrary/blob/master/diagrams)

## Credits <a name="credits"></a>
[Innopolis University](https://innopolis.university/en/) students, Data Science track:
* Daniil [@igudesman](https://github.com/igudesman) Igudesman
* Mikhail [@Glemhel](https://github.com/Glemhel) Rudakov
* Anna [@asleepann](https://github.com/asleepann) Startseva
