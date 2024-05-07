<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With Python</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

Here's a blank template to get started: To avoid retyping too much info. Do a search and replace with your text editor for the following: `Leenoose`, `FastAPI-Kafka-SQL-Example`, `twitter_handle`, `linkedin_username`, `elfzity@hotmail.com`, `elfzity@hotmail.com`, `Kafka with FastAPI for SQL changes`, `Simple project using Kafka to trigger REST calls to FastAPI (Python REST framework) to make changes to Database`

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python]][Python-url]
* [![FastAPI][FastAPI]][FastAPI-url]
* [![PostgreSQL][PostgreSQL]][PostgreSQL-url]
 
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* Ensure Python is installed and of version >3.7
  ```sh
    python --version
    Python 3.12.3
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/Leenoose/FastAPI-Kafka-SQL-Example.git
   cd FastAPI-Kafka-SQL-Example/
   ```
2. Create virtual environment and switch into it for a clean environment to start
   ```sh
   python -m venv .venv
   source .venv/bin/activate
   ```
3. Install required dependencies
   ```sh
   pip install -r requirements.txt
   ```
4. Ensure you have a PostgreSQL running. If not, use Podman or Docker to run an image.
   ```sh
   podman run -d --name <db-name> -p 5432:5432 -e POSTGRES_PASSWORD=<mypassword> postgres:latest
   #The command should run interchangeably with Docker
   ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Leenoose/FastAPI-Kafka-SQL-Example.svg?style=for-the-badge
[contributors-url]: https://github.com/Leenoose/FastAPI-Kafka-SQL-Example/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Leenoose/FastAPI-Kafka-SQL-Example.svg?style=for-the-badge
[forks-url]: https://github.com/Leenoose/FastAPI-Kafka-SQL-Example/network/members
[stars-shield]: https://img.shields.io/github/stars/Leenoose/FastAPI-Kafka-SQL-Example.svg?style=for-the-badge
[stars-url]: https://github.com/Leenoose/FastAPI-Kafka-SQL-Example/stargazers
[issues-shield]: https://img.shields.io/github/issues/Leenoose/FastAPI-Kafka-SQL-Example.svg?style=for-the-badge
[issues-url]: https://github.com/Leenoose/FastAPI-Kafka-SQL-Example/issues
[license-shield]: https://img.shields.io/github/license/Leenoose/FastAPI-Kafka-SQL-Example.svg?style=for-the-badge
[license-url]: https://github.com/Leenoose/FastAPI-Kafka-SQL-Example/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/
[PostgreSQL]: https://img.shields.io/badge/postgresql-4169e1?style=for-the-badge&logo=postgresql&logoColor=white
[PostgreSQL-url]: https://www.postgresql.org
[FastAPI]: https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi
[FastAPI-url]: https://fastapi.tiangolo.com/
